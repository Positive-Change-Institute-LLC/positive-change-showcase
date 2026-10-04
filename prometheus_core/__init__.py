"""Prometheus Core: reference implementations of the Prometheus engines.

Pure-Python, standard-library only. Nothing here performs network access,
trading, or key handling.
"""

from .evolution import EvolutionEngine, Review
from .memory import MemoryRecord, MemorySystem
from .pswe import DCAResult, simulate_dca
from .synthesizer import Finding, Synthesizer

__all__ = [
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
