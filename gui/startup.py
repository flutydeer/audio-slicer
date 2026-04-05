import os
import sys
from collections.abc import Mapping


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
