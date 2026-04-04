import os

import soundfile

from typing import List
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from gui.Ui_MainWindow import Ui_MainWindow
from gui.slicing_tasks import SlicingResult, SlicingSettings, run_slicing_task


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
        self.workSucceeded = 0
        self.workFailed = 0
        self.workResults: list[SlicingResult] = []
        self.processing = False

        self.setWindowTitle(QApplication.applicationName())

        # Must set to accept drag and drop events
        self.setAcceptDrops(True)

        # Get available formats/extensions supported
        self.availableFormats = [str(formatExt).lower(
        ) for formatExt in soundfile.available_formats().keys()]
        # libsndfile supports Opus in Ogg container
        # .opus is a valid extension and recommended for Ogg Opus (see RFC 7845, Section 9)
        # append opus for convenience as tools like youtube-dl(p) extract to .opus by default
        self.availableFormats.append("opus")

        self.formatAllFilter = " ".join(
            [f"*.{formatExt}" for formatExt in self.availableFormats])
        self.formatIndividualFilter = ";;".join(
            [f"{formatExt} (*.{formatExt})" for formatExt in sorted(self.availableFormats)])

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
            self, 'Select Audio Files', ".", f'Audio ({self.formatAllFilter});;{self.formatIndividualFilter}')
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
            self, "About", "Audio Slicer v1.3.0\nCopyright 2020-2024 OpenVPI Team")

    def _q_start(self):
        if self.processing:
            self.warningProcessNotFinished()
            return

        item_count = self.ui.listWidgetTaskList.count()
        if item_count == 0:
            return

        output_format = self.ui.buttonGroup.checkedButton().text()
        if output_format == "mp3":
            ret = QMessageBox.warning(self, "Warning",
                                      "MP3 is not recommended for saving vocals as it is lossy. "
                                      "If you want to save disk space, consider using FLAC instead. "
                                      "Do you want to continue?",
                                      QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
            if ret == QMessageBox.Cancel:
                return

        settings = SlicingSettings(
            threshold=float(self.ui.lineEditThreshold.text()),
            min_length=int(self.ui.lineEditMinLen.text()),
            min_interval=int(self.ui.lineEditMinInterval.text()),
            hop_size=int(self.ui.lineEditHopSize.text()),
            max_sil_kept=int(self.ui.lineEditMaxSilence.text()),
        )

        output_dir = self.ui.lineEditOutputDir.text()

        class WorkThread(QThread):
            oneFinished = Signal(object)

            def __init__(self, filenames: List[str], output_dir: str, output_format: str, settings: SlicingSettings):
                super().__init__()

                self.filenames = filenames
                self.output_dir = output_dir
                self.output_format = output_format
                self.settings = settings

            def run(self):
                for filename in self.filenames:
                    result = run_slicing_task(
                        filename,
                        self.output_dir,
                        self.output_format,
                        self.settings,
                    )
                    self.oneFinished.emit(result)

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
        self.workSucceeded = 0
        self.workFailed = 0
        self.workResults = []
        self.setProcessing(True)

        # Start work thread
        worker = WorkThread(paths, output_dir, output_format, settings)
        worker.oneFinished.connect(self._q_oneFinished)
        worker.finished.connect(self._q_threadFinished)
        worker.start()

        self.workers.append(worker)  # Collect in case of auto deletion

    def _q_oneFinished(self, result: SlicingResult):
        self.workResults.append(result)
        self.workFinished += 1
        if result.success:
            self.workSucceeded += 1
        else:
            self.workFailed += 1
        self.ui.progressBar.setValue(self.workFinished)

    def _q_threadFinished(self):
        # Join all workers
        for worker in self.workers:
            worker.wait()
        self.workers.clear()
        self.setProcessing(False)
        self._show_completion_message(self.workResults)

    def _show_completion_message(self, results: list[SlicingResult]):
        processed_count = len(results)
        success_count = sum(1 for result in results if result.success)
        failed_count = processed_count - success_count
        total_outputs = sum(result.output_count for result in results)
        if failed_count == 0:
            QMessageBox.information(
                self,
                QApplication.applicationName(),
                f"Slicing complete!\nProcessed {processed_count} file(s).\nGenerated {total_outputs} output file(s).",
            )
            return

        first_failure = next(result for result in results if not result.success)
        failure_name = QFileInfo(first_failure.source_path).fileName() or first_failure.source_path
        failure_message = (
            f"Failed: {failure_name}\n{first_failure.error}"
            if first_failure.error
            else f"Failed: {failure_name}"
        )

        if success_count == 0:
            QMessageBox.critical(
                self,
                QApplication.applicationName(),
                f"Slicing failed for all {processed_count} file(s).\n{failure_message}",
            )
            return

        QMessageBox.warning(
            self,
            QApplication.applicationName(),
            "Slicing finished with errors.\n"
            f"Succeeded: {success_count}\n"
            f"Failed: {failed_count}\n"
            f"Generated {total_outputs} output file(s).\n"
            f"{failure_message}",
        )

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
        valid = False
        for url in urls:
            if not url.isLocalFile():
                continue
            path = url.toLocalFile()
            ext = os.path.splitext(path)[1]
            if ext[1:].lower() in self.availableFormats:
                valid = True
                break
        if valid:
            event.accept()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        for url in urls:
            if not url.isLocalFile():
                continue
            path = url.toLocalFile()
            ext = os.path.splitext(path)[1]
            if ext[1:].lower() not in self.availableFormats:
                continue
            item = QListWidgetItem()
            item.setSizeHint(QSize(200, 24))
            item.setText(QFileInfo(path).fileName())
            item.setData(Qt.ItemDataRole.UserRole + 1,
                         path)
            self.ui.listWidgetTaskList.addItem(item)
