"""Run all Prometheus Core engines end to end: python -m prometheus_core"""
import tempfile
from datetime import date, timedelta
from pathlib import Path

from . import (ContentEngine, DevelopmentSystem, EvolutionEngine, MemorySystem,
               Synthesizer, simulate_dca, verify_manifest, write_manifest)


def main() -> None:
    today = date.today()
    mem = MemorySystem()
    mem.add("lesson", "Keep long-term holdings in cold storage", tags=["security"])
    print("Memory:", [r.text for r in mem.search(tag="security")])

    syn = Synthesizer()
    syn.observe("report-a", "Demand is rising", 0.5)
    syn.observe("report-b", "Demand is rising", 0.5)
    print("Synthesizer:", syn.synthesize()[0])

    evo = EvolutionEngine({"tests": 10, "uptime": 99.0})
    print("Evolution:", evo.review({"tests": 4, "uptime": 99.5})[0].recommendation)

    r = simulate_dca([10, 12, 9, 11, 14], 100)
    print(f"PSWE (simulation): invested {r.total_invested:.0f}, return {r.return_pct:.1f}%")

    print("Content:\n" + ContentEngine().generate(
        "social", "Launch", "Systems beat willpower.", ["Automate the repeatable"],
        "Explore PCI.", ["Prometheus", "AI"]))

    with tempfile.TemporaryDirectory() as d:
        (Path(d) / "asset.txt").write_text("knowledge")
        m = write_manifest(d, Path(d).parent / "pcimanifest.json")
        print("Legacy: verified =", verify_manifest(d, m).ok)
        Path(d).parent.joinpath("pcimanifest.json").unlink()

    dev = DevelopmentSystem()
    for i in range(3):
        dev.check_in("study", today - timedelta(days=i))
    dev.add_goal("ship v1", 10)
    dev.advance("ship v1", 4)
    print("Development:", dev.summary(today))


if __name__ == "__main__":
    main()
