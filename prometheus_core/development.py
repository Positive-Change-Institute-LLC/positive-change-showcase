"""Prometheus Personal Development System: goals, habits and streaks."""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path
from typing import Optional


@dataclass
class Habit:
    name: str
    log: set[str] = field(default_factory=set)  # ISO dates completed

    def check_in(self, day: date) -> None:
        self.log.add(day.isoformat())

    def current_streak(self, today: date) -> int:
        """Consecutive days ending today (or yesterday, so the streak survives until today ends)."""
        day = today if today.isoformat() in self.log else today - timedelta(days=1)
        n = 0
        while day.isoformat() in self.log:
            n += 1
            day -= timedelta(days=1)
        return n

    def longest_streak(self) -> int:
        days = sorted(date.fromisoformat(d) for d in self.log)
        best = run = 0
        prev = None
        for d in days:
            run = run + 1 if prev and d - prev == timedelta(days=1) else 1
            best = max(best, run)
            prev = d
        return best


@dataclass
class Goal:
    name: str
    target: float
    progress: float = 0.0

    def advance(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("amount must be non-negative")
        self.progress += amount

    @property
    def percent(self) -> float:
        return min(100.0, self.progress / self.target * 100)


class DevelopmentSystem:
    """Tracks habits and goals; optionally persists to a JSON file."""

    def __init__(self, path: Optional[str | Path] = None) -> None:
        self.path = Path(path) if path else None
        self.habits: dict[str, Habit] = {}
        self.goals: dict[str, Goal] = {}
        if self.path and self.path.exists():
            data = json.loads(self.path.read_text(encoding="utf-8"))
            self.habits = {h["name"]: Habit(h["name"], set(h["log"])) for h in data["habits"]}
            self.goals = {g["name"]: Goal(**g) for g in data["goals"]}

    def habit(self, name: str) -> Habit:
        return self.habits.setdefault(name, Habit(name))

    def add_goal(self, name: str, target: float) -> Goal:
        if target <= 0:
            raise ValueError("target must be positive")
        return self.goals.setdefault(name, Goal(name, target))

    def check_in(self, name: str, day: date) -> None:
        self.habit(name).check_in(day)
        self.save()

    def advance(self, name: str, amount: float) -> None:
        self.goals[name].advance(amount)
        self.save()

    def summary(self, today: date) -> dict:
        return {
            "habits": {n: {"current": h.current_streak(today), "longest": h.longest_streak()}
                       for n, h in sorted(self.habits.items())},
            "goals": {n: round(g.percent, 1) for n, g in sorted(self.goals.items())},
        }

    def save(self) -> None:
        if self.path:
            self.path.write_text(json.dumps({
                "habits": [{"name": h.name, "log": sorted(h.log)} for h in self.habits.values()],
                "goals": [{"name": g.name, "target": g.target, "progress": g.progress}
                          for g in self.goals.values()],
            }, indent=2), encoding="utf-8")
