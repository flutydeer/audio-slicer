import math
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import numpy as np
import soundfile

from gui.slicing_tasks import SlicingSettings, run_slicing_task


class RunSlicingTaskTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)

        self.source_path = Path(self.temp_dir.name) / "input.wav"
        self.output_dir = Path(self.temp_dir.name) / "out"
        self.settings = SlicingSettings(
            threshold=-40.0,
            min_length=500,
            min_interval=300,
            hop_size=10,
            max_sil_kept=100,
        )

        sample_rate = 16000
        duration = sample_rate
        sine = np.array(
            [0.25 * math.sin(2 * math.pi * 440 * i / sample_rate) for i in range(duration)],
            dtype=np.float32,
        )
        silence = np.zeros(sample_rate // 2, dtype=np.float32)
        audio = np.concatenate([sine, silence, sine])
        soundfile.write(self.source_path, audio, sample_rate)

    def test_run_slicing_task_writes_output_files(self):
        result = run_slicing_task(
            str(self.source_path),
            str(self.output_dir),
            "wav",
            self.settings,
        )

        self.assertTrue(result.success)
        self.assertGreaterEqual(result.output_count, 1)
        self.assertEqual(result.output_count, len(result.output_paths))
        for path in result.output_paths:
            self.assertTrue(Path(path).exists())

    def test_run_slicing_task_returns_failure_when_write_raises(self):
        with mock.patch("gui.slicing_tasks.soundfile.write", side_effect=RuntimeError("disk full")):
            result = run_slicing_task(
                str(self.source_path),
                str(self.output_dir),
                "wav",
                self.settings,
            )

        self.assertFalse(result.success)
        self.assertEqual(result.output_count, 0)
        self.assertIn("disk full", result.error)


if __name__ == "__main__":
    unittest.main()
