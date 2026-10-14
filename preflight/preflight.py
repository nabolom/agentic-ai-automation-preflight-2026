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
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "preflight" / "casos-minimos.json"
REPORT = ROOT / "evidence" / "preflight-report.md"
TEMPLATE_REPO = "agentic-ai-automation-preflight-2026"
TEMPLATE_OWNER = "nabolom"


@dataclass
class Check:
    name: str
    status: str
    detail: str
    required: bool = False


def command_version(*command: str) -> tuple[bool, str]:
    """Run a version command using the executable resolved for this OS.

    On Windows, shutil.which("npm") and shutil.which("claude") may return
    npm.cmd and claude.cmd. Passing the resolved path avoids a false PARTIAL
    caused by subprocess not resolving the command name itself.
    """
    if not command:
        return False, "comando vacío"
    executable = shutil.which(command[0]) or command[0]
    resolved = (executable, *command[1:])
    try:
        result = subprocess.run(resolved, capture_output=True, text=True, timeout=8)
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
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return Check("Dataset mínimo", "BLOCKED", str(exc), True)


def parse_origin(url: str) -> tuple[str, str, str]:
    """Return host, owner and repo without exposing credentials in the URL."""
    raw = url.strip()
    if raw.startswith("git@"):
        host_path = raw[4:]
        host, _, path = host_path.partition(":")
    else:
        parsed = urlsplit(raw)
        host = parsed.hostname or ""
        path = parsed.path
    parts = [part for part in path.strip("/").split("/") if part]
    if parts and parts[-1].endswith(".git"):
        parts[-1] = parts[-1][:-4]
    owner = parts[0] if len(parts) >= 1 else ""
    repo = parts[1] if len(parts) >= 2 else ""
    return host, owner, repo


def check_git_workspace() -> list[Check]:
    git_path = shutil.which("git")
    if not git_path:
        return [
            Check("Git", "BLOCKED", "no se encontró git; usa GitHub Desktop como fallback visual", True),
            Check("Repo propio", "BLOCKED", "no se puede verificar sin Git", True),
        ]
    ok_version, version = command_version(git_path, "--version")
    checks = [Check("Git", "PASS" if ok_version else "BLOCKED", version, True)]
    try:
        top = subprocess.run(
            [git_path, "rev-parse", "--show-toplevel"], cwd=ROOT, capture_output=True, text=True, timeout=8
        )
        if top.returncode != 0:
            checks.append(Check("Repo propio", "BLOCKED", "ejecuta el preflight desde tu repo clonado", True))
            return checks

        top_path = Path(top.stdout.strip()).resolve()
        if top_path != ROOT.resolve():
            checks.append(
                Check(
                    "Repo propio",
                    "BLOCKED",
                    "esta carpeta está dentro de otro repo Git; ejecuta el preflight desde la raíz de tu repo propio",
                    True,
                )
            )
            return checks

        remote = subprocess.run(
            [git_path, "remote", "get-url", "origin"], cwd=ROOT, capture_output=True, text=True, timeout=8
        )
        if remote.returncode != 0 or not remote.stdout.strip():
            checks.append(Check("Repo propio", "BLOCKED", "falta origin; crea y clona tu repo de GitHub", True))
            return checks

        host, owner, repo = parse_origin(remote.stdout)
        normalized_host = host.lower().removeprefix("www.")
        if normalized_host != "github.com":
            safe_host = host or "host desconocido"
            checks.append(Check("Repo propio", "PARTIAL", f"origin host {safe_host} no parece GitHub", True))
        elif not owner or not repo:
            checks.append(Check("Repo propio", "PARTIAL", "origin de GitHub sin owner/repo reconocibles", True))
        elif owner.lower() == TEMPLATE_OWNER and repo.lower() == TEMPLATE_REPO:
            checks.append(
                Check(
                    "Repo propio",
                    "PARTIAL",
                    f"origin GitHub {owner}/{repo}; crea tu repo propio con Use this template",
                    True,
                )
            )
        else:
            head = subprocess.run(
                [git_path, "log", "-1", "--format=%h"], cwd=ROOT, capture_output=True, text=True, timeout=8
            ).stdout.strip()
            checks.append(
                Check("Repo propio", "PASS", f"origin GitHub {owner}/{repo}; commit local {head or 'pendiente'}", True)
            )
    except (OSError, ValueError, subprocess.TimeoutExpired) as exc:
        checks.append(Check("Repo propio", "BLOCKED", f"no se pudo verificar el repo: {exc}", True))
    return checks


def check_git_identity(git_path: str) -> Check:
    """Ensure the first commit has an explicit local or global author identity."""
    values = {}
    try:
        for key in ("user.name", "user.email"):
            result = subprocess.run(
                [git_path, "config", "--get", key], cwd=ROOT, capture_output=True, text=True, timeout=8
            )
            values[key] = result.stdout.strip()
    except (OSError, subprocess.TimeoutExpired) as exc:
        return Check("Identidad Git", "BLOCKED", f"no se pudo comprobar user.name/user.email: {exc}", True)

    missing = [key for key in ("user.name", "user.email") if not values.get(key)]
    if missing:
        return Check(
            "Identidad Git",
            "BLOCKED",
            "configura user.name y user.email antes del primer commit; son autoría local, no credenciales",
            True,
        )
    return Check("Identidad Git", "PASS", "user.name y user.email están configurados", True)


def check_claude() -> Check:
    claude_path = shutil.which("claude")
    if not claude_path:
        return Check("Claude Code", "PARTIAL", "no encontrado; usa Cowork como fallback y revisa docs/claude-code.md")
    ok, version = command_version(claude_path, "--version")
    return Check("Claude Code", "PASS" if ok else "PARTIAL", version if ok else "encontrado pero no respondió correctamente")


def check_conditional_tools() -> list[Check]:
    node_path = shutil.which("node")
    npm_path = shutil.which("npm")
    gh_path = shutil.which("gh")
    db_names = ("psql", "sqlite3", "mysql", "mongosh")
    db_name = None
    db_path = None
    for candidate in db_names:
        resolved = shutil.which(candidate)
        if resolved:
            db_name, db_path = candidate, resolved
            break
    node_version = command_version(node_path, "--version")[1] if node_path else None
    npm_version = command_version(npm_path, "--version")[1] if npm_path else None
    gh_version = command_version(gh_path, "--version")[1] if gh_path else None
    db_version = command_version(db_path, "--version")[1] if db_path else None
    return [
        Check("Node.js / npm", "DEFERRED", f"node {node_version}; npm {npm_version}" if node_path and npm_path else "no necesario para el instalador nativo de Claude Code"),
        Check("GitHub CLI", "DEFERRED", f"{gh_version} en {gh_path}" if gh_path else "no instalado; GitHub web o GitHub Desktop son suficientes"),
        Check("Base de datos", "DEFERRED", f"{db_name}: {db_version}; se decide según tu proyecto" if db_path else "se decide después de definir qué quieres agentizar"),
    ]


def all_checks() -> list[Check]:
    checks = [check_python(), check_dataset(), *check_git_workspace()]
    git_path = shutil.which("git")
    if git_path:
        checks.append(check_git_identity(git_path))
    return [*checks, check_claude(), *check_conditional_tools()]


def next_step_for(result: str) -> str:
    if result == "BLOCKED":
        return "detente, revisa docs/fallback.md y resuelve o documenta el bloqueo antes de crear el commit de cierre"
    if result == "PARTIAL":
        return "puedes avanzar con el fallback; registra qué quedó pendiente antes del commit de cierre"
    return "completa la Terminal Lab, llena notes/intent.md y crea el commit de cierre después de revisar el staging"


def write_report(checks: list[Check], result: str) -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    next_step = next_step_for(result)
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
    lines.extend(["", f"**Resultado:** `{result}`", "", f"Siguiente: {next_step}."])
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
    print(f"DIAGNOSTICO: {result}")
    try:
        write_report(checks, result)
    except (OSError, UnicodeError) as exc:
        print("RESULTADO: ERROR_DE_EVIDENCIA")
        print(f"No se pudo guardar evidence/preflight-report.md: {exc}")
        print("Conserva esta salida en la terminal y resuelve el permiso antes de cerrar la actividad.")
        return 1
    print(f"RESULTADO: {result}")
    print(f"Reporte escrito en: {REPORT.relative_to(ROOT)}")
    print(f"Siguiente: {next_step_for(result)}.")
    if result == "BLOCKED":
        return 2
    if result == "PARTIAL":
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
