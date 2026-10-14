# QA del preflight

## Validaciones realizadas

- El script corre sin red ni API key.
- El dataset sintético se valida con Python estándar.
- Python, Git, raíz del workspace, identidad del commit, repo GitHub propio y Claude Code tienen estados explícitos.
- Node.js/npm, GitHub CLI y base de datos aparecen como `DEFERRED`, no como bloqueos universales.
- El script escribe `evidence/preflight-report.md` sin incluir secretos.
- El README enseña cuenta de GitHub, Use this template, clonación, ZIP como fallback, diagnóstico, Terminal Lab, commit de cierre y push.
- La portada centra el título y muestra etiquetas de Python, Git/GitHub, Claude Code, Cowork, Node.js y API key.
- Las instrucciones distinguen macOS, Windows PowerShell y GitHub Desktop.
- La Terminal Lab tiene un núcleo obligatorio de 35–45 minutos, una fast lane de 15–20 minutos, extensiones opcionales y Claude Code al final en modo de solo lectura.
- El orden visible es diagnóstico → Terminal Lab o fast lane → intención → staging explícito → commit de cierre.
- Los checkpoints cubren carpeta actual, archivos, Git status/diff, commit, error seguro y verificación posterior.
- H8 cubre una edición temporal de `prueba.txt`, `git diff`, `git restore` y la diferencia entre recuperar antes y después de un commit.
- Las pruebas de endurecimiento cubren repo padre, remoto mal formado, dataset no UTF-8, identidad Git ausente y siguientes pasos por estado.
- Las fuentes de instalación de Claude Code apuntan a documentación oficial verificada el 14 de octubre de 2026.

## Comandos de prueba

```bash
PYTHONDONTWRITEBYTECODE=1 python3 preflight/preflight.py
python3 -m json.tool preflight/casos-minimos.json
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s preflight -p 'test_*.py'
```

En Windows PowerShell:

```powershell
py preflight/preflight.py
py -m unittest discover -s preflight -p "test_*.py"
```

## Limitaciones

La cuenta de GitHub y la propiedad del repo se comprueban de forma indirecta mediante el remoto `origin`; el script no inicia sesión ni usa la API de GitHub. La autenticación de Claude Code tampoco se ejecuta automáticamente. La disponibilidad de una base de datos se reporta como información, pero su necesidad depende del proyecto que la persona defina después.
