import os

import soundfile
import numpy as np
import urllib

from typing import List
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from slicer2 import Slicer

from gui.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonAddFiles.clicked.connect(self._q_add_audio_files)
        self.ui.pushButtonBrowse.clicked.connect(self._q_browse_output_dir)
        self.ui.pushButtonClearList.clicked.connect(self._q_clear_audio_list)
        self.ui.pushButtonAbout.clicked.connect(self._q_about)
        self.ui.pushButtonStart.clicked.connect(self._q_start)

        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setValue(0)
        self.ui.pushButtonStart.setDefault(True)

        validator = QRegularExpressionValidator(QRegularExpression(r"\d+"))
        self.ui.lineEditThreshold.setValidator(QDoubleValidator())
        self.ui.lineEditMinLen.setValidator(validator)
        self.ui.lineEditMinInterval.setValidator(validator)
        self.ui.lineEditHopSize.setValidator(validator)
        self.ui.lineEditMaxSilence.setValidator(validator)

        self.ui.listWidgetTaskList.setAlternatingRowColors(True)

        # State variables
        self.workers: list[QThread] = []
        self.workCount = 0
        self.workFinished = 0
        self.processing = False

        self.setWindowTitle(QApplication.applicationName())

        # Must set to accept drag and drop events
        self.setAcceptDrops(True)

    def _q_browse_output_dir(self):
        path = QFileDialog.getExistingDirectory(
            self, "Browse Output Directory", ".")
        if path != "":
            self.ui.lineEditOutputDir.setText(QDir.toNativeSeparators(path))

    def _q_add_audio_files(self):
        if self.processing:
            self.warningProcessNotFinished()
            return

        paths, _ = QFileDialog.getOpenFileNames(
            self, 'Select Audio Files', ".", 'Wave Files(*.wav)')
        for path in paths:
            item = QListWidgetItem()
            item.setSizeHint(QSize(200, 24))
            item.setText(QFileInfo(path).fileName())
            # Save full path at custom role
            item.setData(Qt.ItemDataRole.UserRole + 1, path)
            self.ui.listWidgetTaskList.addItem(item)

    def _q_clear_audio_list(self):
        if self.processing:
            self.warningProcessNotFinished()
            return

        self.ui.listWidgetTaskList.clear()

    def _q_about(self):
        QMessageBox.information(
            self, "About", "Audio Slicer v1.2.1\nCopyright 2020-2023 OpenVPI Team")

    def _q_start(self):
        if self.processing:
            self.warningProcessNotFinished()
            return

        item_count = self.ui.listWidgetTaskList.count()
        if item_count == 0:
            return

        class WorkThread(QThread):
            oneFinished = Signal()

            def __init__(self, filenames: List[str], window: MainWindow):
                super().__init__()

                self.filenames = filenames
                self.win = window

            def run(self):
                for filename in self.filenames:
                    audio, sr = soundfile.read(filename, dtype=np.float32)
                    is_mono = True
                    if len(audio.shape) > 1:
                        is_mono = False
                        audio = audio.T
                    slicer = Slicer(
                        sr=sr,
                        threshold=float(self.win.ui.lineEditThreshold.text()),
                        min_length=int(self.win.ui.lineEditMinLen.text()),
                        min_interval=int(
                            self.win.ui.lineEditMinInterval.text()),
                        hop_size=int(self.win.ui.lineEditHopSize.text()),
                        max_sil_kept=int(self.win.ui.lineEditMaxSilence.text())
                    )
                    chunks = slicer.slice(audio)
                    out_dir = self.win.ui.lineEditOutputDir.text()
                    if out_dir == '':
                        out_dir = os.path.dirname(os.path.abspath(filename))
                    else:
                        # Make dir if not exists
                        info = QDir(out_dir)
                        if not info.exists():
                            info.mkpath(out_dir)

                    for i, chunk in enumerate(chunks):
                        path = os.path.join(out_dir, f'%s_%d.wav' % (os.path.basename(filename)
                                                                     .rsplit('.', maxsplit=1)[0], i))
                        if not is_mono:
                            chunk = chunk.T
                        soundfile.write(path, chunk, sr)

                    self.oneFinished.emit()

        # Collect paths
        paths: list[str] = []
        for i in range(0, item_count):
            item = self.ui.listWidgetTaskList.item(i)
            path = item.data(Qt.ItemDataRole.UserRole + 1)  # Get full path
            paths.append(path)

        self.ui.progressBar.setMaximum(item_count)
        self.ui.progressBar.setValue(0)

        self.workCount = item_count
        self.workFinished = 0
        self.setProcessing(True)

        # Start work thread
        worker = WorkThread(paths, self)
        worker.oneFinished.connect(self._q_oneFinished)
        worker.finished.connect(self._q_threadFinished)
        worker.start()

        self.workers.append(worker)  # Collect in case of auto deletion

    def _q_oneFinished(self):
        self.workFinished += 1
        self.ui.progressBar.setValue(self.workFinished)

    def _q_threadFinished(self):
        # Join all workers
        for worker in self.workers:
            worker.wait()
        self.workers.clear()
        self.setProcessing(False)

        QMessageBox.information(
            self, QApplication.applicationName(), "Slicing complete!")

    def warningProcessNotFinished(self):
        QMessageBox.warning(self, QApplication.applicationName(),
                            "Please wait for slicing to complete!")

    def setProcessing(self, processing: bool):
        enabled = not processing
        self.ui.pushButtonStart.setText(
            "Slicing..." if processing else "Start")
        self.ui.pushButtonStart.setEnabled(enabled)
        self.ui.pushButtonAddFiles.setEnabled(enabled)
        self.ui.listWidgetTaskList.setEnabled(enabled)
        self.ui.pushButtonClearList.setEnabled(enabled)
        self.ui.lineEditThreshold.setEnabled(enabled)
        self.ui.lineEditMinLen.setEnabled(enabled)
        self.ui.lineEditMinInterval.setEnabled(enabled)
        self.ui.lineEditHopSize.setEnabled(enabled)
        self.ui.lineEditMaxSilence.setEnabled(enabled)
        self.ui.lineEditOutputDir.setEnabled(enabled)
        self.ui.pushButtonBrowse.setEnabled(enabled)
        self.processing = processing

    # Event Handlers
    def closeEvent(self, event):
        if self.processing:
            self.warningProcessNotFinished()
            event.ignore()

    def dragEnterEvent(self, event):
        urls = event.mimeData().urls()
        has_wav = False
        for url in urls:
            if not url.isLocalFile():
                continue
            path = url.toLocalFile()
            ext = os.path.splitext(path)[1]
            if ext.lower() == '.wav':
                has_wav = True
                break
        if has_wav:
            event.accept()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        for url in urls:
            if not url.isLocalFile():
                continue
            path = url.toLocalFile()
            ext = os.path.splitext(path)[1]
            if ext.lower() != '.wav':
                continue
            item = QListWidgetItem()
            item.setSizeHint(QSize(200, 24))
            item.setText(QFileInfo(path).fileName())
            item.setData(Qt.ItemDataRole.UserRole + 1,
                         path)
            self.ui.listWidgetTaskList.addItem(item)
