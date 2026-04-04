import os
import unittest
from unittest import mock

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication, QMessageBox

from gui.mainwindow import MainWindow
from gui.slicing_tasks import SlicingResult


class MainWindowCompletionMessageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def setUp(self):
        self.window = MainWindow()

    def tearDown(self):
        self.window.close()

    def test_show_completion_message_uses_warning_when_some_tasks_fail(self):
        results = [
            SlicingResult(
                source_path="ok.wav",
                success=True,
                output_paths=("ok_0.wav", "ok_1.wav"),
            ),
            SlicingResult(
                source_path="bad.wav",
                success=False,
                error="RuntimeError: disk full",
            ),
        ]

        with (
            mock.patch.object(QMessageBox, "information") as information,
            mock.patch.object(QMessageBox, "warning") as warning,
            mock.patch.object(QMessageBox, "critical") as critical,
        ):
            self.window._show_completion_message(results)

        information.assert_not_called()
        critical.assert_not_called()
        warning.assert_called_once()
        self.assertIn("bad.wav", warning.call_args.args[2])


if __name__ == "__main__":
    unittest.main()
