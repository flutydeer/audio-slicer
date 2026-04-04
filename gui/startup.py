import importlib
import os
import sys
from collections.abc import Mapping
from typing import TextIO


def apply_optional_theme(log_stream: TextIO | None = None) -> bool:
    stream = log_stream or sys.stderr

    try:
        theme_module = importlib.import_module("qdarktheme")
    except ModuleNotFoundError as exc:
        if exc.name == "qdarktheme":
            print(
                f"Optional theme module is unavailable; continuing without it. ({exc})",
                file=stream,
            )
        else:
            print(
                f"Optional theme import failed; continuing without it. ({type(exc).__name__}: {exc})",
                file=stream,
            )
        return False
    except Exception as exc:
        print(
            f"Optional theme import failed; continuing without it. ({type(exc).__name__}: {exc})",
            file=stream,
        )
        return False

    try:
        theme_module.setup_theme(theme="auto")
    except Exception as exc:
        print(
            f"Optional theme setup failed; continuing without it. ({type(exc).__name__}: {exc})",
            file=stream,
        )
        return False

    return True


def get_missing_display_error(
    platform: str | None = None,
    environ: Mapping[str, str] | None = None,
) -> str:
    current_platform = platform or sys.platform
    env = environ or os.environ

    if not current_platform.startswith("linux"):
        return ""

    if env.get("DISPLAY") or env.get("WAYLAND_DISPLAY"):
        return ""

    return (
        "No graphical display session was detected. "
        "Audio Slicer requires an X11 or Wayland desktop session to launch the GUI on Linux."
    )
