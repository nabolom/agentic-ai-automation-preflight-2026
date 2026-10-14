# Claude Code: ruta principal

Claude Code es la ruta principal de este curso porque trabaja dentro de tu proyecto, lee sus archivos, ejecuta tareas y puede acompañar el flujo de Git. El preflight solo comprueba que el comando exista; no inicia sesión ni consume créditos.

## Instalación recomendada

La documentación oficial recomienda el instalador nativo. En macOS o Linux:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

En Windows PowerShell:

```powershell
irm https://claude.ai/install.ps1 | iex
```

También existe WinGet:

```powershell
winget install Anthropic.ClaudeCode
```

Después de instalar, abre una terminal nueva y verifica:

```bash
claude --version
```

Para un diagnóstico de instalación de solo lectura:

```bash
claude doctor
```

La primera sesión puede pedir autenticación en el navegador. Claude Code requiere una cuenta o modalidad de acceso compatible, como Pro, Max, Team, Enterprise, Console o un proveedor cloud compatible. El plan gratuito de claude.ai no incluye Claude Code. Esa autenticación ocurre después del preflight y no debe guardarse en el repo.

Si el comando no aparece, revisa tu `PATH`:

- macOS/Linux: `command -v claude`
- Windows PowerShell: `Get-Command claude`

## ¿Necesito Node.js?

No para el instalador nativo recomendado. La instalación global vía npm sigue disponible para quien la elija deliberadamente y requiere Node.js 22 o superior:

```bash
npm install -g @anthropic-ai/claude-code
```

La ruta npm instala el mismo binario nativo. No conviertas Node.js en requisito universal del curso: instálalo solo si eliges esa ruta o si tu proyecto lo necesita. No uses `sudo npm install -g`.

## Windows y Git

Git for Windows es recomendable si quieres que Claude Code use Git Bash. Sin Git for Windows, Claude Code puede usar PowerShell. Para el aprendizaje del curso, Git sigue siendo importante por el control de versiones aunque Claude Code pueda ejecutar comandos sin él.

## Si Claude Code no está disponible

Usa Cowork como fallback operativo, conserva el reporte y registra la instalación pendiente. No conviertas la primera actividad en una sesión interminable de soporte.

## Fuentes oficiales

- [Advanced setup](https://code.claude.com/docs/en/setup)
- [Quickstart](https://code.claude.com/docs/en/quickstart)
- [Guía de terminal](https://code.claude.com/docs/en/terminal-guide)
- [Repositorio oficial](https://github.com/anthropics/claude-code)

**Verificado:** 14 de octubre de 2026.
