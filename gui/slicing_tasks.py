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
