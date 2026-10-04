"""Prometheus Core: reference implementations of the Prometheus engines.

Pure-Python, standard-library only. Nothing here performs network access,
trading, or key handling.
"""

from .content import Brand, ContentEngine
from .development import DevelopmentSystem, Goal, Habit
from .evolution import EvolutionEngine, Review
from .legacy import Verification, build_manifest, verify_manifest, write_manifest
from .memory import MemoryRecord, MemorySystem
from .pswe import DCAResult, simulate_dca
from .synthesizer import Finding, Synthesizer

__all__ = [
    "Brand",
    "ContentEngine",
    "DevelopmentSystem",
    "Goal",
    "Habit",
    "Verification",
    "build_manifest",
    "verify_manifest",
    "write_manifest",
    "DCAResult",
    "EvolutionEngine",
    "Finding",
    "MemoryRecord",
    "MemorySystem",
    "Review",
    "Synthesizer",
    "simulate_dca",
]
__version__ = "0.1.0"
