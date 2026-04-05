import os
from dataclasses import dataclass

import numpy as np
import soundfile

from slicer2 import Slicer


@dataclass(frozen=True)
class SlicingSettings:
    threshold: float
    min_length: int
    min_interval: int
    hop_size: int
    max_sil_kept: int


@dataclass(frozen=True)
class SlicingResult:
    source_path: str
    success: bool
    output_paths: tuple[str, ...] = ()
    error: str = ""

    @property
    def output_count(self) -> int:
        return len(self.output_paths)


def parse_slicing_settings(
    threshold_text: str,
    min_length_text: str,
    min_interval_text: str,
    hop_size_text: str,
    max_sil_kept_text: str,
) -> tuple[SlicingSettings | None, str]:
    threshold, error = _parse_float(threshold_text, "Threshold")
    if error:
        return None, error

    min_length, error = _parse_int(min_length_text, "Minimum Length")
    if error:
        return None, error

    min_interval, error = _parse_int(min_interval_text, "Minimum Interval")
    if error:
        return None, error

    hop_size, error = _parse_int(hop_size_text, "Hop Size")
    if error:
        return None, error

    max_sil_kept, error = _parse_int(max_sil_kept_text, "Maximum Silence Length")
    if error:
        return None, error

    for field_name, value in (
        ("Minimum Length", min_length),
        ("Minimum Interval", min_interval),
        ("Hop Size", hop_size),
        ("Maximum Silence Length", max_sil_kept),
    ):
        if value <= 0:
            return None, f"{field_name} must be greater than 0."

    if min_length < min_interval:
        return None, "Minimum Length must be greater than or equal to Minimum Interval."
    if min_interval < hop_size:
        return None, "Minimum Interval must be greater than or equal to Hop Size."
    if max_sil_kept < hop_size:
        return None, "Maximum Silence Length must be greater than or equal to Hop Size."

    return SlicingSettings(
        threshold=threshold,
        min_length=min_length,
        min_interval=min_interval,
        hop_size=hop_size,
        max_sil_kept=max_sil_kept,
    ), ""


def run_slicing_task(
    source_path: str,
    output_dir: str,
    output_format: str,
    settings: SlicingSettings,
) -> SlicingResult:
    written_paths: list[str] = []

    try:
        audio, sample_rate = soundfile.read(source_path, dtype=np.float32)
        is_mono = True
        if len(audio.shape) > 1:
            is_mono = False
            audio = audio.T

        slicer = Slicer(
            sr=sample_rate,
            threshold=settings.threshold,
            min_length=settings.min_length,
            min_interval=settings.min_interval,
            hop_size=settings.hop_size,
            max_sil_kept=settings.max_sil_kept,
        )
        chunks = slicer.slice(audio)

        target_dir = output_dir or os.path.dirname(os.path.abspath(source_path))
        os.makedirs(target_dir, exist_ok=True)

        base_name = os.path.basename(source_path).rsplit(".", maxsplit=1)[0]
        for index, chunk in enumerate(chunks):
            chunk_to_write = chunk.T if not is_mono else chunk
            output_path = os.path.join(target_dir, f"{base_name}_{index}.{output_format}")
            soundfile.write(output_path, chunk_to_write, sample_rate)
            written_paths.append(output_path)
    except Exception as exc:
        message = f"{type(exc).__name__}: {exc}" if str(exc) else type(exc).__name__
        return SlicingResult(
            source_path=source_path,
            success=False,
            output_paths=tuple(written_paths),
            error=message,
        )

    return SlicingResult(
        source_path=source_path,
        success=True,
        output_paths=tuple(written_paths),
    )


def _parse_float(value: str, field_name: str) -> tuple[float | None, str]:
    try:
        return float(value), ""
    except ValueError:
        return None, f"{field_name} must be a number."


def _parse_int(value: str, field_name: str) -> tuple[int | None, str]:
    try:
        return int(value), ""
    except ValueError:
        return None, f"{field_name} must be an integer."
