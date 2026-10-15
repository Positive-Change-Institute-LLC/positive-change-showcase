#!/usr/bin/env python3
"""Build a non-destructive local portfolio from existing turnkey folders."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

TURNKEYS_DIR = Path("preexisting_turnkeys")
PORTFOLIO_DIR = Path("PCI_Python_Portfolio_Full")
PDF_DIR = Path("pdf_readmes")
RENDERS_DIR = Path("renders")
CINEMATICS_DIR = Path("cinematics")
NARRATION_DIR_NAME = "narrations"
AUDIO_DIR_NAME = "audio_narration_ultra"
PYTHON_SUFFIXES = {".py"}
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}
VIDEO_SUFFIXES = {".mp4", ".webm", ".mov"}
AUDIO_SUFFIXES = {".mp3", ".wav", ".ogg", ".m4a"}


class PortfolioBuilderV2:
    def __init__(
        self,
        turnkey_dir: Path | str = TURNKEYS_DIR,
        output_dir: Path | str = PORTFOLIO_DIR,
        pdf_dir: Path | str = PDF_DIR,
        renders_dir: Path | str = RENDERS_DIR,
        cinematics_dir: Path | str = CINEMATICS_DIR,
    ) -> None:
        self.turnkey_dir_input = Path(turnkey_dir).expanduser().absolute()
        self.output_dir_input = Path(output_dir).expanduser().absolute()
        self.turnkey_dir = self.turnkey_dir_input.resolve()
        self.output_dir = self.output_dir_input.resolve()
        self.pdf_dir = Path(pdf_dir).resolve()
        self.renders_dir = Path(renders_dir).resolve()
        self.cinematics_dir = Path(cinematics_dir).resolve()

    def _validate_roots(self) -> None:
        if (
            not self.turnkey_dir.is_dir()
            or self._has_symlink_component(self.turnkey_dir_input)
        ):
            raise ValueError(f"Turnkey source directory does not exist: {self.turnkey_dir}")
        if (
            self.output_dir == self.turnkey_dir
            or self.output_dir in self.turnkey_dir.parents
            or self.turnkey_dir in self.output_dir.parents
        ):
            raise ValueError("Source and output directories must not overlap.")
        if self._has_symlink_component(self.output_dir_input):
            raise ValueError("Output path must not pass through a symbolic link.")

    def discover_turnkeys(self) -> list[Path]:
        self._validate_roots()
        return sorted(
            (
                entry
                for entry in self.turnkey_dir.iterdir()
                if entry.is_dir() and not entry.is_symlink()
            ),
            key=lambda entry: entry.name.casefold(),
        )

    def build_portfolio(self, execute: bool = False, overwrite: bool = False) -> dict[str, Any]:
        projects = self.discover_turnkeys()
        if not execute:
            print(
                f"[PortfolioBuilderV2] Dry run: would process {len(projects)} "
                f"project(s) into {self.output_dir}."
            )
            return {"project_count": len(projects), "projects": [p.name for p in projects]}

        self.output_dir.mkdir(parents=True, exist_ok=True)
        self._ensure_output_root()
        discovered_categories = {
            project.name: self._source_category(project) for project in projects
        }
        index = [
            self._process_turnkey(project, discovered_categories, overwrite)
            for project in projects
        ]
        index_path = self.output_dir / "portfolio_index.json"
        self._write_json(index_path, index, overwrite)
        self._write_index_markdown(index, overwrite)
        self._copy_dashboard(overwrite)
        print(
            f"[PortfolioBuilderV2] Built {len(index)} project record(s) in "
            f"{self.output_dir}."
        )
        return {"project_count": len(index), "projects": index}

    def _ensure_output_root(self) -> None:
        resolved = self.output_dir.resolve()
        if resolved != self.output_dir:
            raise ValueError("Output path resolves through a symbolic link.")
        if self._has_symlink_component(self.output_dir):
            raise ValueError("Output path must not pass through a symbolic link.")

    def _project_destination(self, project: Path) -> Path:
        if project.name in {"", ".", ".."} or Path(project.name).name != project.name:
            raise ValueError(f"Unsafe project folder name: {project.name!r}")
        destination = self.output_dir / project.name
        if destination.is_symlink():
            raise ValueError(f"Refusing symbolic-link project destination: {destination}")
        resolved = destination.resolve()
        if self.output_dir not in resolved.parents:
            raise ValueError("Project destination escapes the portfolio output directory.")
        return destination

    def _source_category(self, project: Path) -> str | None:
        metadata_path = project / "turnkey.json"
        if metadata_path.is_symlink() or not metadata_path.is_file():
            return None
        try:
            content = json.loads(metadata_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return None
        category = content.get("category") if isinstance(content, dict) else None
        return category.strip()[:80] if isinstance(category, str) and category.strip() else None

    def _process_turnkey(
        self,
        project: Path,
        categories: dict[str, str | None],
        overwrite: bool,
    ) -> dict[str, Any]:
        destination = self._project_destination(project)
        destination.mkdir(parents=True, exist_ok=True)

        scripts: list[str] = []
        for item in sorted(project.iterdir(), key=lambda path: path.name.casefold()):
            if item.suffix.lower() in PYTHON_SUFFIXES and self._is_safe_file(item, project):
                if self._copy_file(item, destination / item.name, overwrite):
                    scripts.append(item.name)

        renders = self._copy_tree(
            self.renders_dir / project.name,
            destination / "renders",
            IMAGE_SUFFIXES,
            overwrite,
        )
        cinematics = self._copy_tree(
            self.cinematics_dir / project.name,
            destination / "cinematics",
            VIDEO_SUFFIXES | IMAGE_SUFFIXES,
            overwrite,
        )
        audio = self._copy_tree(
            project / AUDIO_DIR_NAME,
            destination / AUDIO_DIR_NAME,
            AUDIO_SUFFIXES,
            overwrite,
        )

        pdf_source = self.pdf_dir / f"{project.name}.pdf"
        pdf_name = f"{project.name}_readme.pdf"
        readme_pdf = (
            pdf_name
            if self._is_safe_file(pdf_source, self.pdf_dir)
            and self._copy_file(pdf_source, destination / pdf_name, overwrite)
            else None
        )

        narration_name = f"{project.name}_narration.txt"
        narration_path = destination / narration_name
        narration = self._generate_narration(project.name, scripts, renders, cinematics, audio, readme_pdf)
        if self._write_text(narration_path, narration, overwrite):
            narration_script: str | None = narration_name
        else:
            narration_script = narration_name if narration_path.is_file() else None

        category = categories.get(project.name)
        cross_packaging = [
            other
            for other in sorted(
                (item for item in categories if item != project.name and categories[item] == category),
                key=str.casefold,
            )[:3]
        ] if category else []

        record: dict[str, Any] = {
            "turnkey_name": project.name,
            "category": category,
            "artifacts_verified": False,
            "python_scripts": scripts,
            "renders": renders,
            "cinematics": cinematics,
            "audio_narration": audio,
            "readme_pdf": readme_pdf,
            "narration_script": narration_script,
            "cross_packaging": cross_packaging,
            "cross_packaging_basis": "matching source category" if category else "not configured",
            "generated_at": datetime.now(timezone.utc).isoformat(),
        }
        self._write_json(destination / "metadata.json", record, overwrite)
        return record

    @staticmethod
    def _is_safe_file(path: Path, root: Path) -> bool:
        if path.is_symlink() or not path.is_file():
            return False
        try:
            path.resolve().relative_to(root.resolve())
        except (OSError, ValueError):
            return False
        return True

    def _safe_destination(self, destination: Path) -> bool:
        try:
            destination.absolute().relative_to(self.output_dir)
        except ValueError:
            return False
        if self._has_symlink_component(destination):
            return False
        try:
            destination.parent.resolve().relative_to(self.output_dir)
        except (OSError, ValueError):
            return False
        return True

    def _copy_file(self, source: Path, destination: Path, overwrite: bool) -> bool:
        if not self._safe_destination(destination):
            return False
        if destination.exists() and not overwrite:
            return destination.is_file() and not destination.is_symlink()
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.is_symlink():
            return False
        shutil.copy2(source, destination)
        return True

    def _copy_tree(
        self,
        source: Path,
        destination: Path,
        extensions: set[str],
        overwrite: bool,
    ) -> list[str]:
        if source.is_symlink() or not source.is_dir():
            return []
        copied: list[str] = []
        for current, dirs, files in os.walk(source, followlinks=False):
            current_path = Path(current)
            dirs[:] = sorted(
                (
                    name for name in dirs
                    if not (current_path / name).is_symlink()
                ),
                key=str.casefold,
            )
            for filename in sorted(files, key=str.casefold):
                source_file = current_path / filename
                if source_file.suffix.lower() not in extensions:
                    continue
                if not self._is_safe_file(source_file, source):
                    continue
                relative = source_file.relative_to(source)
                target = destination / relative
                if self._copy_file(source_file, target, overwrite):
                    copied.append(relative.as_posix())
        return copied

    @staticmethod
    def _generate_narration(
        name: str,
        scripts: list[str],
        renders: list[str],
        cinematics: list[str],
        audio: list[str],
        pdf: str | None,
    ) -> str:
        present = [
            label for label, values in (
                ("Python scripts", scripts),
                ("render images", renders),
                ("cinematic files", cinematics),
                ("audio files", audio),
            ) if values
        ]
        inventory = ", ".join(present) if present else "no supported media or Python artifacts found"
        pdf_status = "A PDF readme is included." if pdf else "No PDF readme was supplied."
        return (
            f"{name} — Positive Change Institute LLC portfolio inventory.\n\n"
            f"Files present: {inventory}. {pdf_status}\n"
            "This narration is generated from the local file inventory only. "
            "It does not verify functionality, deployment readiness, licensing, "
            "performance, or commercial claims. No external AI or voice service was used.\n"
        )

    def _write_text(self, path: Path, content: str, overwrite: bool) -> bool:
        if not self._safe_destination(path) or (path.exists() and not overwrite):
            return False
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.is_symlink():
            return False
        path.write_text(content, encoding="utf-8")
        return True

    @staticmethod
    def _has_symlink_component(path: Path) -> bool:
        absolute = path.absolute()
        current = Path(absolute.anchor)
        for part in absolute.parts[1:]:
            current /= part
            if current.is_symlink():
                return True
        return False

    def _write_json(self, path: Path, content: Any, overwrite: bool) -> bool:
        return self._write_text(
            path,
            json.dumps(content, ensure_ascii=False, indent=2) + "\n",
            overwrite,
        )

    def _write_index_markdown(self, index: list[dict[str, Any]], overwrite: bool) -> None:
        lines = [
            "# PCI Portfolio Inventory",
            "",
            f"Projects discovered: {len(index)}.",
            "",
            "This index reports files found and copied locally. It does not certify product readiness,",
            "deployment, performance, security, licensing, or sales.",
            "",
            "| Project | Category | Python | Renders | Cinematics | Audio |",
            "|---|---|---:|---:|---:|---:|",
        ]
        lines.extend(
            f"| {record['turnkey_name']} | {record.get('category') or 'Uncategorized'} "
            f"| {len(record['python_scripts'])} | {len(record['renders'])} "
            f"| {len(record['cinematics'])} | {len(record['audio_narration'])} |"
            for record in index
        )
        self._write_text(self.output_dir / "portfolio_index.md", "\n".join(lines) + "\n", overwrite)

    def _copy_dashboard(self, overwrite: bool) -> None:
        template = Path(__file__).with_name("PCI_INVESTOR_SUITE_PORTAL.html")
        if self._is_safe_file(template, template.parent):
            self._copy_file(template, self.output_dir / "investor_dashboard.html", overwrite)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--turnkeys-dir", type=Path, default=TURNKEYS_DIR)
    parser.add_argument("--output-dir", type=Path, default=PORTFOLIO_DIR)
    parser.add_argument("--pdf-dir", type=Path, default=PDF_DIR)
    parser.add_argument("--renders-dir", type=Path, default=RENDERS_DIR)
    parser.add_argument("--cinematics-dir", type=Path, default=CINEMATICS_DIR)
    parser.add_argument("--build", action="store_true", help="Write the portfolio; default is a dry run.")
    parser.add_argument("--overwrite", action="store_true", help="Replace matching generated files.")
    args = parser.parse_args(argv)

    builder = PortfolioBuilderV2(
        args.turnkeys_dir,
        args.output_dir,
        args.pdf_dir,
        args.renders_dir,
        args.cinematics_dir,
    )
    try:
        builder.build_portfolio(execute=args.build, overwrite=args.overwrite)
    except (OSError, ValueError) as exc:
        print(f"[PortfolioBuilderV2] Stopped: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
