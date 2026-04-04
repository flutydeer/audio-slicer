import math
import unittest

import numpy as np

from slicer2 import Slicer


class SliceRangesTests(unittest.TestCase):
    def test_slice_ranges_match_slice_output(self):
        sample_rate = 16000
        tone = np.array(
            [0.25 * math.sin(2 * math.pi * 440 * i / sample_rate) for i in range(sample_rate)],
            dtype=np.float32,
        )
        silence = np.zeros(sample_rate // 2, dtype=np.float32)
        waveform = np.concatenate([tone, silence, tone, silence, tone])
        slicer = Slicer(
            sr=sample_rate,
            threshold=-40.0,
            min_length=500,
            min_interval=300,
            hop_size=10,
            max_sil_kept=100,
        )

        ranges = slicer.slice_ranges(waveform)
        chunks = slicer.slice(waveform)

        self.assertEqual(len(ranges), len(chunks))
        rebuilt = [waveform[start:end] for start, end in ranges]
        for rebuilt_chunk, chunk in zip(rebuilt, chunks):
            self.assertTrue(np.allclose(rebuilt_chunk, chunk))


if __name__ == "__main__":
    unittest.main()
