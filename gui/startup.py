import importlib
import sys
from typing import TextIO


def apply_optional_theme(log_stream: TextIO | None = None) -> bool:
    stream = log_stream or sys.stderr

    try:
        theme_module = importlib.import_module("qdarktheme")
    except ModuleNotFoundError as exc:
        print(
            f"Optional theme module is unavailable; continuing without it. ({exc})",
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
