#!/usr/bin/env python3
"""Render an original, procedural Prometheus concept cinematic.

Narration uses Google Text-to-Speech and therefore needs internet access.
Visuals, captions, and the synthesized score are generated locally.
"""

from __future__ import annotations

import argparse
import math
import struct
import tempfile
import wave
from pathlib import Path

try:
    import numpy as np
    from gtts import gTTS
    from moviepy import AudioFileClip, CompositeAudioClip, VideoClip, concatenate_videoclips
    from PIL import Image, ImageDraw, ImageFont
except ImportError as error:
    raise SystemExit(
        "Missing cinematic dependencies. Install them with "
        "`python -m pip install -r cinematic_requirements.txt`."
    ) from error


VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
FPS = 30
OUTPUT_VIDEO = "Prometheus_2026_Cinematic.mp4"
CAPTIONS_FILE = "prometheus_captions.srt"
DISCLAIMER = "Concept visualization • performance figures are unverified design claims"

SCENES = [
    {
        "key": "intro",
        "title": "PROMETHEUS SUPERINTELLIGENCE",
        "narration": (
            "Prometheus Superintelligence represents Positive Change Institute's vision "
            "for a connected, human-directed systems architecture."
        ),
        "duration": 10,
        "visual": "core",
        "domain": "A systems concept by Positive Change Institute",
    },
    {
        "key": "node_network",
        "title": "A NETWORK OF SPECIALIZED IDEAS",
        "narration": (
            "The concept brings together analytics, robotics, blockchain, creative tools, "
            "and autonomous devices as distinct parts of one evolving network."
        ),
        "duration": 15,
        "visual": "network",
        "domain": "Analytics • Robotics • Blockchain • Creative",
    },
    {
        "key": "drone_orchestration",
        "title": "COORDINATION AT THE EDGE",
        "narration": (
            "In the envisioned architecture, coordinated devices share signals and status "
            "through monitored workflows, with human oversight at every critical step."
        ),
        "duration": 20,
        "visual": "drones",
        "domain": "Illustrative device coordination",
    },
    {
        "key": "data_centers",
        "title": "COMPUTE • ENERGY • OPERATIONS",
        "narration": (
            "Data center and mining facility operations are represented as connected "
            "systems, where energy, cooling, and compute can be observed together."
        ),
        "duration": 20,
        "visual": "facility",
        "domain": "Conceptual infrastructure visualization",
    },
    {
        "key": "blockchain_creative",
        "title": "DIGITAL RAILS, CREATIVE OUTPUT",
        "narration": (
            "Blockchain infrastructure and creative production form another layer of the "
            "vision, linking digital assets with repeatable enterprise workflows."
        ),
        "duration": 20,
        "visual": "blocks",
        "domain": "Blockchain • Creative systems",
    },
    {
        "key": "transformers_layer",
        "title": "ADAPTIVE SYSTEMS",
        "narration": (
            "An adaptive intelligence layer is imagined to organize skills, tools, and "
            "knowledge while keeping decisions transparent and accountable."
        ),
        "duration": 15,
        "visual": "layers",
        "domain": "Illustrative model layers",
    },
    {
        "key": "predictive_engines",
        "title": "PREDICTION • SIMULATION • REVIEW",
        "narration": (
            "Predictive and simulation engines can help teams explore possible outcomes. "
            "Their results remain estimates to review, not guarantees."
        ),
        "duration": 15,
        "visual": "analytics",
        "domain": "Illustrative analytics",
    },
    {
        "key": "truth_core",
        "title": "INTEGRITY BY DESIGN",
        "narration": (
            "A truth-seeking system begins with traceable sources, explicit rules, and "
            "validation. Claims about security and accuracy require independent evidence."
        ),
        "duration": 15,
        "visual": "core",
        "domain": "Verification • Auditability • Human review",
    },
    {
        "key": "full_network_close",
        "title": "BUILD WITH PURPOSE",
        "narration": (
            "From connected devices to data systems and creative work, Prometheus is a "
            "vision for thoughtful integration, built to be tested one real capability "
            "at a time."
        ),
        "duration": 10,
        "visual": "network",
        "domain": "Positive Change Institute LLC",
    },
]


def load_font(size: int) -> ImageFont.ImageFont:
    for font_path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/Library/Fonts/Arial.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ):
        if Path(font_path).is_file():
            return ImageFont.truetype(font_path, size)
    return ImageFont.load_default()


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for word in text.split():
        candidate = f"{current} {word}".strip()
        if current and draw.textbbox((0, 0), candidate, font=font)[2] > max_width:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def draw_visual(draw: ImageDraw.ImageDraw, scene: dict[str, object], t: float, width: int, height: int) -> None:
    visual = scene["visual"]
    center = (width // 2, int(height * 0.48))
    scale = min(width, height) / 1080
    cyan = (0, 218, 255)
    purple = (131, 83, 255)
    gold = (255, 204, 71)

    if visual in {"network", "drones", "core"}:
        count = 18 if visual == "network" else 12
        radius = int(min(width, height) * (0.29 if visual != "core" else 0.20))
        points = []
        for index in range(count):
            angle = 2 * math.pi * index / count + t * 0.12
            orbit = radius * (1 + 0.08 * math.sin(t + index))
            point = (
                center[0] + int(orbit * math.cos(angle)),
                center[1] + int(orbit * 0.58 * math.sin(angle)),
            )
            points.append(point)
            draw.line((center, point), fill=(67, 69, 137), width=max(1, int(2 * scale)))
        for index, point in enumerate(points):
            radius_px = max(4, int((14 if visual != "drones" else 9) * scale))
            color = cyan if index % 3 else purple
            draw.ellipse(
                (point[0] - radius_px, point[1] - radius_px, point[0] + radius_px, point[1] + radius_px),
                fill=color,
            )
        if visual == "core":
            for ring in range(1, 5):
                r = int(radius * ring / 5)
                draw.ellipse((center[0] - r, center[1] - r, center[0] + r, center[1] + r), outline=purple, width=2)
            draw.ellipse((center[0] - 28 * scale, center[1] - 28 * scale, center[0] + 28 * scale, center[1] + 28 * scale), fill=gold)

    elif visual == "facility":
        base_y = int(height * 0.72)
        for index in range(9):
            x = int(width * 0.12 + index * width * 0.095)
            building_height = int((height * 0.16) + (index % 3) * height * 0.045)
            draw.rectangle((x, base_y - building_height, x + width * 0.065, base_y), outline=cyan, width=3)
            for row in range(3):
                wy = base_y - building_height + int((row + 1) * building_height / 4)
                draw.line((x + 8, wy, x + width * 0.06, wy), fill=(67, 69, 137), width=2)
        draw.line((int(width * 0.08), base_y, int(width * 0.92), base_y), fill=purple, width=4)

    elif visual == "blocks":
        size = int(82 * scale)
        spacing = int(27 * scale)
        start_x = int(width * 0.22)
        start_y = int(height * 0.36)
        for row in range(3):
            for col in range(5):
                x = start_x + col * (size + spacing)
                y = start_y + row * (size + spacing)
                color = cyan if (row + col) % 2 else purple
                draw.rounded_rectangle((x, y, x + size, y + size), radius=8, outline=color, width=3)
                draw.line((x + 15, y + size // 2, x + size - 15, y + size // 2), fill=color, width=2)

    elif visual == "layers":
        start_x = int(width * 0.25)
        for index in range(6):
            y = int(height * 0.31 + index * height * 0.07)
            offset = int(math.sin(t * 0.7 + index) * 18 * scale)
            x = start_x + offset
            draw.rounded_rectangle(
                (x, y, width - x, y + int(height * 0.045)),
                radius=12,
                outline=cyan if index % 2 else purple,
                width=3,
            )

    elif visual == "analytics":
        left, right = int(width * 0.16), int(width * 0.84)
        top, bottom = int(height * 0.30), int(height * 0.72)
        for index in range(1, 5):
            y = top + index * (bottom - top) // 5
            draw.line((left, y, right, y), fill=(45, 49, 84), width=1)
        samples = 60
        coords = []
        for index in range(samples):
            x = left + index * (right - left) // (samples - 1)
            wave = math.sin(index * 0.22 + t) * 0.22 + math.sin(index * 0.07 - t * 0.4) * 0.16
            y = int((top + bottom) / 2 - wave * (bottom - top))
            coords.append((x, y))
        draw.line(coords, fill=cyan, width=max(3, int(4 * scale)))
        for index in range(0, samples, 8):
            x, y = coords[index]
            draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=gold)


def render_frame(scene: dict[str, object], t: float, width: int, height: int, caption: str | None) -> np.ndarray:
    image = Image.new("RGB", (width, height), (3, 7, 22))
    draw = ImageDraw.Draw(image)
    scale = min(width, height) / 1080

    # Subtle moving grid and radial accents create a consistent visual system.
    grid_step = max(36, int(72 * scale))
    drift = int((t * 8 * scale) % grid_step)
    for x in range(-grid_step, width + grid_step, grid_step):
        draw.line((x + drift, 0, x + drift, height), fill=(10, 17, 42), width=1)
    for y in range(-grid_step, height + grid_step, grid_step):
        draw.line((0, y + drift, width, y + drift), fill=(10, 17, 42), width=1)

    draw_visual(draw, scene, t, width, height)

    title_font = load_font(max(22, int(34 * scale)))
    small_font = load_font(max(14, int(19 * scale)))
    draw.text((int(width * 0.07), int(height * 0.075)), str(scene["title"]), font=title_font, fill=(238, 242, 255))
    draw.text((int(width * 0.07), int(height * 0.14)), str(scene["domain"]), font=small_font, fill=(0, 218, 255))

    if caption:
        caption_font = load_font(max(16, int(25 * scale)))
        lines = wrap_text(draw, caption, caption_font, int(width * 0.82))
        line_height = int(36 * scale)
        box_height = (len(lines) + 1) * line_height + int(24 * scale)
        top = height - box_height - int(height * 0.085)
        draw.rounded_rectangle(
            (int(width * 0.07), top, int(width * 0.93), top + box_height),
            radius=max(10, int(18 * scale)),
            fill=(3, 7, 22),
            outline=(0, 160, 210),
            width=2,
        )
        for index, line in enumerate(lines):
            draw.text(
                (int(width * 0.09), top + int(12 * scale) + index * line_height),
                line,
                font=caption_font,
                fill=(255, 255, 255),
            )

    draw.text((int(width * 0.07), height - int(28 * scale)), DISCLAIMER, font=load_font(max(12, int(15 * scale))), fill=(180, 188, 211))
    return np.asarray(image)


def format_srt_time(seconds: float) -> str:
    milliseconds = max(0, round(seconds * 1000))
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    secs, millis = divmod(remainder, 1_000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"


def write_srt(entries: list[tuple[float, float, str]], destination: Path) -> None:
    with destination.open("w", encoding="utf-8", newline="\n") as captions:
        for index, (start, end, text) in enumerate(entries, 1):
            captions.write(f"{index}\n{format_srt_time(start)} --> {format_srt_time(end)}\n{text}\n\n")


def write_original_score(destination: Path, duration: float, sample_rate: int = 44100) -> None:
    """Create a simple, original synthesized ambient score; no third-party music."""
    chords = [
        (110.00, 164.81, 220.00),
        (98.00, 146.83, 196.00),
        (130.81, 196.00, 261.63),
        (87.31, 130.81, 174.61),
    ]
    total_frames = int(duration * sample_rate)
    chunk_size = 4096
    with wave.open(str(destination), "wb") as output:
        output.setnchannels(2)
        output.setsampwidth(2)
        output.setframerate(sample_rate)
        for chunk_start in range(0, total_frames, chunk_size):
            frames = min(chunk_size, total_frames - chunk_start)
            samples = bytearray()
            for offset in range(frames):
                frame = chunk_start + offset
                t = frame / sample_rate
                chord = chords[int(t // 12) % len(chords)]
                fade = min(1.0, t / 2.0, max(0.0, (duration - t) / 3.0))
                value = sum(
                    math.sin(2 * math.pi * frequency * t + index * 0.13) / (index + 1)
                    for index, frequency in enumerate(chord)
                )
                value += 0.18 * math.sin(2 * math.pi * 55 * t)
                sample = int(max(-1.0, min(1.0, value * 0.11 * fade)) * 32767)
                samples.extend(struct.pack("<hh", sample, sample))
            output.writeframesraw(samples)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(OUTPUT_VIDEO))
    parser.add_argument("--captions", type=Path, default=Path(CAPTIONS_FILE))
    parser.add_argument("--width", type=int, default=VIDEO_WIDTH)
    parser.add_argument("--height", type=int, default=VIDEO_HEIGHT)
    parser.add_argument("--fps", type=int, default=FPS)
    parser.add_argument("--offline", action="store_true", help="Render with captions and score, but no spoken narration.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.width < 320 or args.height < 180 or args.fps < 1:
        raise SystemExit("Video dimensions must be at least 320x180 and FPS must be positive.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.captions.parent.mkdir(parents=True, exist_ok=True)

    video_clips = []
    audio_clips = []
    caption_entries = []
    cursor = 0.0
    with tempfile.TemporaryDirectory(prefix="prometheus-cinematic-") as temp_dir:
        temp_path = Path(temp_dir)
        for scene in SCENES:
            narration_clip = None
            if not args.offline:
                voice_file = temp_path / f"{scene['key']}.mp3"
                try:
                    gTTS(text=str(scene["narration"]), lang="en").save(str(voice_file))
                    narration_clip = AudioFileClip(str(voice_file))
                except Exception as error:
                    raise RuntimeError(
                        "Narration generation failed. Check internet access or rerun with --offline."
                    ) from error

            duration = max(float(scene["duration"]), narration_clip.duration + 1.0 if narration_clip else 8.0)
            caption_end = min(duration, narration_clip.duration if narration_clip else duration)
            caption_entries.append((cursor, cursor + caption_end, str(scene["narration"])))
            frame_function = lambda t, scene=scene, width=args.width, height=args.height, voice=narration_clip: render_frame(
                scene,
                t,
                width,
                height,
                str(scene["narration"]) if voice is None or t <= voice.duration else None,
            )
            clip = VideoClip(frame_function, duration=duration).with_fps(args.fps)
            if narration_clip:
                audio_clips.append(narration_clip.with_start(cursor))
            video_clips.append(clip)
            cursor += duration

        score_file = temp_path / "original_score.wav"
        write_original_score(score_file, cursor)
        score_clip = AudioFileClip(str(score_file)).with_volume_scaled(0.20)
        audio_clips.append(score_clip)
        final_video = concatenate_videoclips(video_clips, method="compose")
        final_video = final_video.with_audio(CompositeAudioClip(audio_clips))
        write_srt(caption_entries, args.captions)
        final_video.write_videofile(
            str(args.output),
            fps=args.fps,
            codec="libx264",
            audio_codec="aac",
            preset="medium",
        )

        final_video.close()
        score_clip.close()
        for clip in video_clips:
            clip.close()
        for clip in audio_clips:
            clip.close()

    print(f"Rendered concept cinematic: {args.output}")
    print(f"Closed captions: {args.captions}")
    print("Narration uses a generic synthetic voice; the synthesized score is original.")


if __name__ == "__main__":
    main()
