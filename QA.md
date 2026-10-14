# QA del preflight

## Validaciones realizadas

- El script corre sin red ni API key.
- El dataset sintético se valida con Python estándar.
- Python, Git, repo GitHub propio y Claude Code tienen estados explícitos.
- Node.js/npm, GitHub CLI y base de datos aparecen como `DEFERRED`, no como bloqueos universales.
- El script escribe `evidence/preflight-report.md` sin incluir secretos.
- El README enseña cuenta de GitHub, Use this template, clonación, ZIP como fallback, commit y push.
- La portada centra el título y muestra etiquetas de Python, Git/GitHub, Claude Code, Cowork, Node.js y API key.
- Las instrucciones distinguen macOS, Windows PowerShell y GitHub Desktop.
- Las fuentes de instalación de Claude Code apuntan a documentación oficial verificada el 14 de octubre de 2026.

## Comandos de prueba

```bash
PYTHONDONTWRITEBYTECODE=1 python3 preflight/preflight.py
python3 -m json.tool preflight/casos-minimos.json
```

En Windows PowerShell:

```powershell
py preflight/preflight.py
```

## Limitaciones

La cuenta de GitHub y la propiedad del repo se comprueban de forma indirecta mediante el remoto `origin`; el script no inicia sesión ni usa la API de GitHub. La autenticación de Claude Code tampoco se ejecuta automáticamente. La disponibilidad de una base de datos se reporta como información, pero su necesidad depende del proyecto que la persona defina después.
