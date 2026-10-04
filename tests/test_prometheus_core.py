import pytest

from prometheus_core import EvolutionEngine, MemorySystem, Synthesizer, simulate_dca


def test_memory_add_search_persist(tmp_path):
    p = tmp_path / "m.json"
    m = MemorySystem(p)
    m.add("lesson", "Use cold storage", tags=["Crypto", "security"])
    m.add("project", "Ship PCI site")
    assert [r.text for r in m.search("cold")] == ["Use cold storage"]
    assert len(m.search(tag="crypto")) == 1
    assert len(MemorySystem(p)) == 2
    assert m.delete(1) and not m.delete(99)
    with pytest.raises(ValueError):
        m.add("", "x")


def test_synthesizer_noisy_or():
    s = Synthesizer()
    s.observe("a", "Demand is rising", 0.5)
    s.observe("b", "demand  is rising", 0.5)
    s.observe("a", "demand is rising", 0.9)  # duplicate source ignored
    s.observe("c", "Weak claim", 0.2)
    top = s.synthesize()[0]
    assert top.confidence == 0.75 and top.sources == ("a", "b")
    assert len(s.synthesize(min_confidence=0.5)) == 1
    with pytest.raises(ValueError):
        s.observe("a", "x", 1.5)


def test_evolution_review_and_level():
    e = EvolutionEngine({"uptime": 99.0, "tests": 10})
    reviews = e.review({"uptime": 99.5, "tests": 4})
    assert reviews[0].metric == "tests" and reviews[0].status == "weak"
    assert e.level({"uptime": 99.5, "tests": 4}) == 1
    with pytest.raises(KeyError):
        e.review({"uptime": 1})


def test_dca():
    r = simulate_dca([10, 20], 100)
    assert r.total_invested == 200
    assert r.units == pytest.approx(15)
    assert r.average_cost == pytest.approx(200 / 15)
    assert r.return_pct == pytest.approx((300 / 200 - 1) * 100)
    with pytest.raises(ValueError):
        simulate_dca([], 10)
    with pytest.raises(ValueError):
        simulate_dca([1], 0)
