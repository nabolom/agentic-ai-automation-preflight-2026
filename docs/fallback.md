# Fallbacks

## No tengo cuenta de GitHub

Crea una cuenta antes de avanzar. Si la creación se bloquea, conserva una captura y trabaja temporalmente en una carpeta local; el objetivo de trazabilidad quedará pendiente hasta tener un repo propio.

## No tengo Git

Usa GitHub Desktop en macOS o Windows. Si tampoco puedes instalarlo, descarga ZIP como último recurso y registra que esa ruta no conserva historial. El facilitador puede ayudarte a crear el repo y hacer el primer upload.

## No sé clonar

Abre [`docs/git-y-github.md`](git-y-github.md). La secuencia mínima es: crear tu repo con la plantilla, copiar la URL, ejecutar `git clone URL`, entrar a la carpeta y comprobar `git status`.

## No tengo Claude Code

Marca `PARTIAL`, conserva el mensaje y usa Cowork como fallback. No instales Node.js solo para probar una ruta npm deprecada. Revisa [`docs/claude-code.md`](claude-code.md) cuando tengas tiempo.

## No tengo Python

Pide ayuda para instalar Python 3.9 o superior, o usa el fallback de leer `preflight/casos-minimos.json` y registrar manualmente tu sistema, repo, herramienta disponible y bloqueo. El reporte automático quedará pendiente.

## No tengo Node.js

No es un bloqueo del preflight ni del instalador nativo recomendado de Claude Code. Instálalo solo si el proyecto que elijas lo requiere.

## No tengo base de datos

No instales una todavía. Primero define qué proceso quieres agentizar, qué datos usa, qué volumen tiene y qué salida necesita. La decisión de almacenamiento pertenece al diseño del proyecto.

## Algo pide una clave

Detente. Este preflight no necesita API keys ni debe enviar datos. Guarda el mensaje sin copiar secretos y avisa al facilitador.
