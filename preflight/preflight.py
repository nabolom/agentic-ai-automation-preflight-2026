#!/usr/bin/env python3
"""Preflight offline y multiplataforma del espacio de trabajo estudiantil."""
from __future__ import annotations

import json
import platform
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "preflight" / "casos-minimos.json"
REPORT = ROOT / "evidence" / "preflight-report.md"
TEMPLATE_REPO = "agentic-ai-automation-preflight-2026"


@dataclass
class Check:
    name: str
    status: str
    detail: str
    required: bool = False


def command_version(*command: str) -> tuple[bool, str]:
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=8)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, str(exc)
    output = (result.stdout or result.stderr).strip().splitlines()
    return result.returncode == 0, output[0] if output else "sin salida"


def check_python() -> Check:
    version = platform.python_version()
    ok = sys.version_info >= (3, 9)
    return Check("Python", "PASS" if ok else "BLOCKED", f"{version} (se requiere 3.9+)", True)


def check_dataset() -> Check:
    try:
        data = json.loads(DATASET.read_text(encoding="utf-8"))
        required = {"id", "tipo", "entrada", "salida_esperada"}
        valid = isinstance(data, list) and len(data) >= 3 and all(
            isinstance(item, dict) and required <= item.keys() for item in data
        )
        if not valid:
            return Check("Dataset mínimo", "BLOCKED", "faltan casos o campos requeridos", True)
        return Check("Dataset mínimo", "PASS", f"{len(data)} casos sintéticos legibles", True)
    except (OSError, json.JSONDecodeError) as exc:
        return Check("Dataset mínimo", "BLOCKED", str(exc), True)


def check_git_workspace() -> list[Check]:
    git_path = shutil.which("git")
    if not git_path:
        return [
            Check("Git", "BLOCKED", "no se encontró git; usa GitHub Desktop como fallback visual", True),
            Check("Repo propio", "BLOCKED", "no se puede verificar sin Git", True),
        ]
    ok_version, version = command_version("git", "--version")
    checks = [Check("Git", "PASS" if ok_version else "BLOCKED", version, True)]
    try:
        top = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"], cwd=ROOT, capture_output=True, text=True, timeout=8
        )
        remote = subprocess.run(
            ["git", "remote", "get-url", "origin"], cwd=ROOT, capture_output=True, text=True, timeout=8
        )
        if top.returncode != 0:
            checks.append(Check("Repo propio", "BLOCKED", "ejecuta el preflight desde tu repo clonado", True))
        elif remote.returncode != 0 or not remote.stdout.strip():
            checks.append(Check("Repo propio", "BLOCKED", "falta origin; crea y clona tu repo de GitHub", True))
        else:
            url = remote.stdout.strip()
            if "github.com" not in url.lower():
                checks.append(Check("Repo propio", "PARTIAL", f"origin no parece GitHub: {url}", True))
            elif TEMPLATE_REPO in url:
                checks.append(Check("Repo propio", "PARTIAL", "sigues en la plantilla; crea tu repo propio con Use this template", True))
            else:
                head = subprocess.run(
                    ["git", "log", "-1", "--format=%h"], cwd=ROOT, capture_output=True, text=True, timeout=8
                ).stdout.strip()
                checks.append(Check("Repo propio", "PASS", f"origin GitHub detectado; commit local {head or 'pendiente'}", True))
    except (OSError, subprocess.TimeoutExpired) as exc:
        checks.append(Check("Repo propio", "BLOCKED", str(exc), True))
    return checks


def check_claude() -> Check:
    if not shutil.which("claude"):
        return Check("Claude Code", "PARTIAL", "no encontrado; usa Cowork como fallback y revisa docs/claude-code.md")
    ok, version = command_version("claude", "--version")
    return Check("Claude Code", "PASS" if ok else "PARTIAL", version if ok else "encontrado pero no respondió correctamente")


def check_conditional_tools() -> list[Check]:
    node = shutil.which("node")
    npm = shutil.which("npm")
    gh = shutil.which("gh")
    db_names = ("psql", "sqlite3", "mysql", "mongosh")
    db = next((name for name in db_names if shutil.which(name)), None)
    node_version = command_version("node", "--version")[1] if node else None
    npm_version = command_version("npm", "--version")[1] if npm else None
    gh_version = command_version("gh", "--version")[1] if gh else None
    db_version = command_version(db, "--version")[1] if db else None
    return [
        Check("Node.js / npm", "DEFERRED", f"node {node_version}; npm {npm_version}" if node and npm else "no necesario para el instalador nativo de Claude Code"),
        Check("GitHub CLI", "DEFERRED", f"{gh_version} en {gh}" if gh else "no instalado; GitHub web o GitHub Desktop son suficientes"),
        Check("Base de datos", "DEFERRED", f"{db}: {db_version}; se decide según tu proyecto" if db else "se decide después de definir qué quieres agentizar"),
    ]


def all_checks() -> list[Check]:
    return [check_python(), check_dataset(), *check_git_workspace(), check_claude(), *check_conditional_tools()]


def write_report(checks: list[Check], result: str) -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Reporte de preflight",
        "",
        f"Fecha UTC: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        f"Sistema: {platform.system()} {platform.release()}",
        "",
        "Este reporte comprueba el entorno local. No autentica cuentas, no llama a APIs y no prueba una integración real.",
        "",
        "| Comprobación | Estado | Detalle |",
        "|---|---|---|",
    ]
    lines.extend(f"| {c.name} | {c.status} | {c.detail.replace('|', '/')} |" for c in checks)
    lines.extend(["", f"**Resultado:** `{result}`", "", "Siguiente: conserva este archivo en tu repo propio y haz un commit."])
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    checks = all_checks()
    blocked = any(c.status == "BLOCKED" for c in checks)
    partial = any(c.status == "PARTIAL" for c in checks)
    result = "BLOCKED" if blocked else "PARTIAL" if partial else "PASS"
    print("PREFLIGHT — trazabilidad, control de versiones y propiedad del espacio de trabajo")
    print(f"Sistema: {platform.system()} {platform.release()}")
    print("-" * 88)
    for check in checks:
        print(f"[{check.status}] {check.name}: {check.detail}")
    print("-" * 88)
    print(f"RESULTADO: {result}")
    write_report(checks, result)
    print(f"Reporte escrito en: {REPORT.relative_to(ROOT)}")
    if result == "BLOCKED":
        print("Siguiente: revisa docs/fallback.md y resuelve el bloqueo antes de avanzar.")
        return 2
    if result == "PARTIAL":
        print("Siguiente: puedes avanzar con el fallback; registra qué quedó pendiente.")
    else:
        print("Siguiente: crea notes/intent.md, haz commit y push en tu repo propio.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
