import io
import unittest
from types import SimpleNamespace
from unittest import mock

from gui.startup import apply_optional_theme, get_missing_display_error


class ApplyOptionalThemeTests(unittest.TestCase):
    def test_apply_optional_theme_skips_missing_theme_module(self):
        log_stream = io.StringIO()

        with mock.patch("gui.startup.importlib.import_module", side_effect=ModuleNotFoundError("no module named qdarktheme")):
            applied = apply_optional_theme(log_stream)

        self.assertFalse(applied)
        self.assertIn("Optional theme module is unavailable", log_stream.getvalue())

    def test_apply_optional_theme_configures_theme_when_module_exists(self):
        log_stream = io.StringIO()
        theme_module = SimpleNamespace(setup_theme=mock.Mock())

        with mock.patch("gui.startup.importlib.import_module", return_value=theme_module):
            applied = apply_optional_theme(log_stream)

        self.assertTrue(applied)
        theme_module.setup_theme.assert_called_once_with(theme="auto")


class GetMissingDisplayErrorTests(unittest.TestCase):
    def test_get_missing_display_error_returns_message_on_headless_linux(self):
        error = get_missing_display_error(
            platform="linux",
            environ={},
        )

        self.assertIn("No graphical display session was detected", error)

    def test_get_missing_display_error_allows_linux_with_display(self):
        error = get_missing_display_error(
            platform="linux",
            environ={"DISPLAY": ":0"},
        )

        self.assertEqual(error, "")

    def test_get_missing_display_error_ignores_non_linux_platforms(self):
        error = get_missing_display_error(
            platform="win32",
            environ={},
        )

        self.assertEqual(error, "")


if __name__ == "__main__":
    unittest.main()
