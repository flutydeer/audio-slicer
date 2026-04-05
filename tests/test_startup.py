import unittest

from gui.startup import get_missing_display_error


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
