from datetime import date, timedelta

import pytest

from prometheus_core import (Brand, ContentEngine, DevelopmentSystem,
                             build_manifest, verify_manifest, write_manifest)


def test_content_generation_and_helpers():
    e = ContentEngine()
    out = e.generate("social", "T", "Hook", ["a", "b"], "Join now", ["ai tools", "PCI"])
    assert "- a\n- b" in out and "#AiTools #Pci" in out
    assert out.endswith("Positive Change Institute: Build systems. Create opportunity.")
    assert e.generate("article", "T", "H", ["x"], "Go").startswith("# T")
    assert e.slug("Hello, World! 2026") == "hello-world-2026"
    assert e.reading_time_minutes("word " * 450) == 3
    with pytest.raises(ValueError):
        e.generate("nope", "T", "H", ["x"], "Go")
    with pytest.raises(ValueError):
        e.generate("social", "T", "H", [], "Go")
    with pytest.raises(ValueError):
        ContentEngine(Brand(banned_words=("guaranteed",))).generate(
            "social", "T", "Guaranteed wins", ["x"], "Go")


def test_legacy_manifest_detects_changes(tmp_path):
    (tmp_path / "a.txt").write_text("one")
    (tmp_path / "sub").mkdir()
    (tmp_path / "sub" / "b.txt").write_text("two")
    m = write_manifest(tmp_path, tmp_path.parent / "manifest.json")
    assert m["file_count"] == 2 and verify_manifest(tmp_path, m).ok
    (tmp_path / "a.txt").write_text("changed")
    (tmp_path / "sub" / "b.txt").unlink()
    (tmp_path / "c.txt").write_text("new")
    v = verify_manifest(tmp_path, m)
    assert not v.ok and v.modified == ("a.txt",)
    assert v.missing == ("sub/b.txt",) and v.added == ("c.txt",)
    with pytest.raises(NotADirectoryError):
        build_manifest(tmp_path / "nope")


def test_development_streaks_and_persistence(tmp_path):
    p = tmp_path / "d.json"
    s = DevelopmentSystem(p)
    today = date(2026, 10, 4)
    for i in (0, 1, 2, 5):
        s.check_in("study", today - timedelta(days=i))
    h = s.habit("study")
    assert h.current_streak(today) == 3 and h.longest_streak() == 3
    assert h.current_streak(today + timedelta(days=2)) == 0
    s.add_goal("ship", 10)
    s.advance("ship", 25)
    assert s.summary(today)["goals"]["ship"] == 100.0
    assert DevelopmentSystem(p).habit("study").current_streak(today) == 3
    with pytest.raises(ValueError):
        s.add_goal("bad", 0)
