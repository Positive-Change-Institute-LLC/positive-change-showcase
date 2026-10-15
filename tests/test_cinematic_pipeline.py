import tempfile
import unittest
import wave
from pathlib import Path

import numpy as np

from PROMETHEUS_2026_CINEMATIC_PIPELINE import (
    SCENES,
    format_srt_time,
    render_frame,
    write_original_score,
    write_srt,
)


class CinematicPipelineTests(unittest.TestCase):
    def test_scene_durations_match_intended_base_runtime(self):
        self.assertEqual(sum(scene["duration"] for scene in SCENES), 140)
        self.assertEqual(len({scene["key"] for scene in SCENES}), len(SCENES))

    def test_srt_time_format_handles_minute_boundary(self):
        self.assertEqual(format_srt_time(61.234), "00:01:01,234")
        self.assertEqual(format_srt_time(-1), "00:00:00,000")

    def test_srt_and_original_score_are_written(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            captions = Path(temp_dir) / "captions.srt"
            score = Path(temp_dir) / "score.wav"
            write_srt([(0, 2.5, "Caption text")], captions)
            write_original_score(score, 0.1, sample_rate=8000)

            self.assertIn("00:00:00,000 --> 00:00:02,500", captions.read_text())
            with wave.open(str(score), "rb") as audio:
                self.assertEqual(audio.getnchannels(), 2)
                self.assertEqual(audio.getframerate(), 8000)
                self.assertEqual(audio.getnframes(), 800)

    def test_scene_frame_has_requested_dimensions(self):
        frame = render_frame(SCENES[0], 1.0, 320, 180, "Test caption")
        self.assertEqual(frame.shape, (180, 320, 3))
        self.assertEqual(frame.dtype, np.uint8)


if __name__ == "__main__":
    unittest.main()
