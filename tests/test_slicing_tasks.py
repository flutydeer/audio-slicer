import math
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import numpy as np
import soundfile

from gui.slicing_tasks import SlicingSettings, build_rms_list_from_file, parse_slicing_settings, run_slicing_task
from slicer2 import Slicer, get_rms


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
        with mock.patch("gui.slicing_tasks.write_slice_range", side_effect=RuntimeError("disk full")):
            result = run_slicing_task(
                str(self.source_path),
                str(self.output_dir),
                "wav",
                self.settings,
            )

        self.assertFalse(result.success)
        self.assertEqual(result.output_count, 0)
        self.assertIn("disk full", result.error)

    def test_run_slicing_task_streams_without_soundfile_read(self):
        with mock.patch("gui.slicing_tasks.soundfile.read", side_effect=AssertionError("whole-file read should not be used")):
            result = run_slicing_task(
                str(self.source_path),
                str(self.output_dir),
                "wav",
                self.settings,
            )

        self.assertTrue(result.success)
        self.assertGreaterEqual(result.output_count, 1)


class ParseSlicingSettingsTests(unittest.TestCase):
    def test_parse_slicing_settings_rejects_zero_or_negative_values(self):
        settings, error = parse_slicing_settings("-40", "500", "300", "0", "100")

        self.assertIsNone(settings)
        self.assertEqual(error, "Hop Size must be greater than 0.")

        settings, error = parse_slicing_settings("-40", "-1", "300", "10", "100")

        self.assertIsNone(settings)
        self.assertEqual(error, "Minimum Length must be greater than 0.")

    def test_parse_slicing_settings_rejects_invalid_interval_order(self):
        settings, error = parse_slicing_settings("-40", "100", "300", "10", "100")

        self.assertIsNone(settings)
        self.assertEqual(
            error,
            "Minimum Length must be greater than or equal to Minimum Interval.",
        )

    def test_parse_slicing_settings_returns_settings_for_valid_input(self):
        settings, error = parse_slicing_settings("-40", "500", "300", "10", "100")

        self.assertEqual(error, "")
        self.assertEqual(
            settings,
            SlicingSettings(
                threshold=-40.0,
                min_length=500,
                min_interval=300,
                hop_size=10,
                max_sil_kept=100,
            ),
        )


class BuildRmsListFromFileTests(unittest.TestCase):
    def test_build_rms_list_from_file_matches_existing_rms_calculation(self):
        sample_rate = 16000
        tone = np.array(
            [0.25 * math.sin(2 * math.pi * 440 * i / sample_rate) for i in range(sample_rate)],
            dtype=np.float32,
        )
        silence = np.zeros(sample_rate // 2, dtype=np.float32)
        waveform = np.concatenate([tone, silence, tone])
        slicer = Slicer(
            sr=sample_rate,
            threshold=-40.0,
            min_length=500,
            min_interval=300,
            hop_size=10,
            max_sil_kept=100,
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            source_path = Path(temp_dir) / "rms.wav"
            soundfile.write(source_path, waveform, sample_rate)

            with soundfile.SoundFile(source_path) as audio_file:
                rms_list = build_rms_list_from_file(audio_file, slicer)

        expected = get_rms(
            y=waveform,
            frame_length=slicer.win_size,
            hop_length=slicer.hop_size,
        ).squeeze(0)
        self.assertTrue(np.allclose(rms_list, expected, atol=2e-6))


if __name__ == "__main__":
    unittest.main()
