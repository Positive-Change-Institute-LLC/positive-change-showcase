"""Prometheus AI Content Engine: deterministic, template-driven content generation.

Generates consistent branded copy (articles, social posts, product blurbs) from
structured input. It does not call any external AI service; output is
reproducible, which makes it suitable for testing and brand-consistency checks.
"""
from __future__ import annotations

import re
import string
from dataclasses import dataclass, field

TEMPLATES: dict[str, str] = {
    "social": "{hook}\n\n{points}\n\n{cta} {hashtags}",
    "product": "# {title}\n\n{hook}\n\n## What you get\n{points}\n\n{cta}",
    "article": "# {title}\n\n{hook}\n\n## Key points\n{points}\n\n## Next step\n{cta}",
}

_PLACEHOLDER = re.compile(r"\{(\w+)\}")


@dataclass(frozen=True)
class Brand:
    name: str = "Positive Change Institute"
    tagline: str = "Build systems. Create opportunity."
    banned_words: tuple[str, ...] = ()


@dataclass
class ContentEngine:
    brand: Brand = field(default_factory=Brand)

    def generate(self, kind: str, title: str, hook: str, points: list[str],
                 cta: str, tags: list[str] | None = None) -> str:
        if kind not in TEMPLATES:
            raise ValueError(f"unknown kind {kind!r}; choose from {sorted(TEMPLATES)}")
        if not title.strip() or not hook.strip() or not cta.strip():
            raise ValueError("title, hook and cta must be non-empty")
        if not points:
            raise ValueError("at least one point is required")
        bullets = "\n".join(f"- {p.strip()}" for p in points)
        hashtags = " ".join(self.hashtag(t) for t in (tags or []))
        text = TEMPLATES[kind].format(
            title=title.strip(), hook=hook.strip(), points=bullets,
            cta=cta.strip(), hashtags=hashtags,
        ).rstrip()
        self.check_brand(text)
        return f"{text}\n\n— {self.brand.name}: {self.brand.tagline}"

    @staticmethod
    def hashtag(tag: str) -> str:
        words = re.findall(r"[A-Za-z0-9]+", tag)
        if not words:
            raise ValueError(f"cannot make a hashtag from {tag!r}")
        return "#" + "".join(w.capitalize() for w in words)

    def check_brand(self, text: str) -> None:
        lowered = text.lower()
        hits = [w for w in self.brand.banned_words if w.lower() in lowered]
        if hits:
            raise ValueError(f"banned words present: {hits}")

    @staticmethod
    def slug(title: str) -> str:
        s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        if not s:
            raise ValueError("title produces an empty slug")
        return s

    @staticmethod
    def reading_time_minutes(text: str, wpm: int = 200) -> int:
        words = len(text.translate(str.maketrans("", "", string.punctuation)).split())
        return max(1, -(-words // wpm))
