#!/usr/bin/env python3
"""Diagnóstico offline y multiplataforma del entorno estudiantil."""
from __future__ import annotations

import json
import platform
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "preflight" / "casos-minimos.json"


def check_python() -> tuple[str, bool, str]:
    ok = sys.version_info >= (3, 9)
    version = platform.python_version()
    return ("Python", ok, f"{version} (se requiere 3.9+)")


def check_dataset() -> tuple[str, bool, str]:
    try:
        data = json.loads(DATASET.read_text(encoding="utf-8"))
        if not isinstance(data, list) or len(data) < 3:
            return ("Dataset mínimo", False, "debe contener al menos 3 casos")
        required = {"id", "tipo", "entrada", "salida_esperada"}
        if any(not isinstance(item, dict) or not required <= item.keys() for item in data):
            return ("Dataset mínimo", False, "faltan campos requeridos")
        return ("Dataset mínimo", True, f"{len(data)} casos legibles")
    except (OSError, json.JSONDecodeError) as exc:
        return ("Dataset mínimo", False, str(exc))


def optional_tool(name: str, candidates: tuple[str, ...]) -> tuple[str, bool, str]:
    found = next((shutil.which(candidate) for candidate in candidates if shutil.which(candidate)), None)
    if found:
        return (name, True, found)
    return (name, False, "no encontrado; puedes continuar con fallback")


def main() -> int:
    checks = [
        check_python(),
        check_dataset(),
        optional_tool("Git (opcional)", ("git",)),
        optional_tool("Claude Code (opcional)", ("claude",)),
    ]
    print("PREFLIGHT — diagnóstico offline")
    print(f"Sistema: {platform.system()} {platform.release()}")
    print(f"Carpeta: {ROOT}")
    print("-" * 72)
    blocked = False
    partial = False
    for name, ok, detail in checks:
        required = name in {"Python", "Dataset mínimo"}
        if ok:
            status = "PASS"
        elif required:
            status = "BLOCKED"
            blocked = True
        else:
            status = "PARTIAL"
            partial = True
        print(f"[{status}] {name}: {detail}")
    print("-" * 72)
    if blocked:
        print("RESULTADO: BLOCKED")
        print("Siguiente: revisa docs/fallback.md o pide apoyo al facilitador.")
        return 2
    if partial:
        print("RESULTADO: PARTIAL")
        print("Siguiente: puedes continuar; conserva la salida y usa fallback si hace falta.")
        return 0
    print("RESULTADO: PASS")
    print("Siguiente: conserva la salida y espera la indicación del facilitador.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
