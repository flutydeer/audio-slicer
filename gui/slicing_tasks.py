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
        target_dir = output_dir or os.path.dirname(os.path.abspath(source_path))
        os.makedirs(target_dir, exist_ok=True)
        ranges, sample_rate, channels = analyze_slicing_task(source_path, settings)

        base_name = os.path.basename(source_path).rsplit(".", maxsplit=1)[0]
        for index, (begin, end) in enumerate(ranges):
            output_path = os.path.join(target_dir, f"{base_name}_{index}.{output_format}")
            write_slice_range(source_path, output_path, sample_rate, channels, begin, end)
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


def analyze_slicing_task(
    source_path: str,
    settings: SlicingSettings,
) -> tuple[list[tuple[int, int]], int, int]:
    with soundfile.SoundFile(source_path) as source_file:
        sample_rate = source_file.samplerate
        channels = source_file.channels
        total_samples = len(source_file)

        slicer = Slicer(
            sr=sample_rate,
            threshold=settings.threshold,
            min_length=settings.min_length,
            min_interval=settings.min_interval,
            hop_size=settings.hop_size,
            max_sil_kept=settings.max_sil_kept,
        )

        if (total_samples + slicer.hop_size - 1) // slicer.hop_size <= slicer.min_length:
            return [(0, total_samples)], sample_rate, channels

        rms_list = build_rms_list_from_file(source_file, slicer)
        ranges = slicer.slice_ranges_from_rms(rms_list, total_samples)
        return ranges, sample_rate, channels


def build_rms_list_from_file(
    source_file: soundfile.SoundFile,
    slicer: Slicer,
    read_size: int = 131072,
) -> np.ndarray:
    source_file.seek(0)
    pad = slicer.win_size // 2
    buffer = np.zeros(pad, dtype=np.float32)
    rms_parts: list[np.ndarray] = []

    while True:
        chunk = source_file.read(read_size, dtype="float32", always_2d=True)
        if len(chunk) == 0:
            break
        mono = chunk.mean(axis=1, dtype=np.float32)
        buffer = np.concatenate((buffer, mono.astype(np.float32, copy=False)))
        values, buffer = _consume_rms_frames(buffer, slicer)
        if values.size:
            rms_parts.append(values)

    buffer = np.concatenate((buffer, np.zeros(pad, dtype=np.float32)))
    values, _ = _consume_rms_frames(buffer, slicer)
    if values.size:
        rms_parts.append(values)

    if not rms_parts:
        return np.zeros(0, dtype=np.float32)
    return np.concatenate(rms_parts)


def write_slice_range(
    source_path: str,
    output_path: str,
    sample_rate: int,
    channels: int,
    begin: int,
    end: int,
    chunk_size: int = 65536,
) -> None:
    frames_remaining = max(0, end - begin)
    with (
        soundfile.SoundFile(source_path) as source_file,
        soundfile.SoundFile(output_path, mode="w", samplerate=sample_rate, channels=channels) as output_file,
    ):
        source_file.seek(begin)
        while frames_remaining > 0:
            block = source_file.read(min(chunk_size, frames_remaining), dtype="float32", always_2d=True)
            if len(block) == 0:
                break
            output_file.write(block)
            frames_remaining -= len(block)


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


def _consume_rms_frames(buffer: np.ndarray, slicer: Slicer) -> tuple[np.ndarray, np.ndarray]:
    if buffer.shape[0] < slicer.win_size:
        return np.zeros(0, dtype=np.float32), buffer

    usable = ((buffer.shape[0] - slicer.win_size) // slicer.hop_size) + 1
    window_view = np.lib.stride_tricks.sliding_window_view(buffer, slicer.win_size)
    windows = window_view[::slicer.hop_size][:usable]
    rms_values = np.sqrt(np.mean(np.abs(windows) ** 2, axis=1, dtype=np.float64)).astype(np.float32)
    remaining = buffer[usable * slicer.hop_size:]
    return rms_values, remaining
