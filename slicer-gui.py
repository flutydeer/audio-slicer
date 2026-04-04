import os
import sys
import datetime
from PySide6.QtWidgets import QApplication, QStyleFactory
from PySide6.QtGui import QFont

import gui.mainwindow
from gui.startup import apply_optional_theme

if __name__ == '__main__':
    # Write console outputs to log file.
    __stderr__ = sys.stderr
    date_time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    folder = os.path.exists('log')
    if not folder: 
        os.makedirs('log')
    sys.stderr = open(f'log/log {date_time}.txt', 'w')
    
    app = QApplication(sys.argv)
    app.setApplicationName("Audio Slicer")
    app.setApplicationDisplayName("Audio Slicer")
    
    # Apply optional theme when a compatible qdarktheme module is installed.
    apply_optional_theme(sys.stderr)

    # Auto dark title bar on Windows 10/11
    style = QStyleFactory.create("fusion")
    app.setStyle(style)

    font = QFont()
    # font.setPixelSize(12)
    font.setHintingPreference(QFont.PreferNoHinting)
    app.setFont(font)

    window = gui.mainwindow.MainWindow()
    window.show()

    sys.exit(app.exec())
