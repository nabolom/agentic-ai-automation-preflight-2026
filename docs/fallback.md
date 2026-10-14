# Fallbacks

## No tengo cuenta de GitHub

Crea una cuenta antes de avanzar. Si la creación se bloquea, conserva una captura y trabaja temporalmente en una carpeta local; el objetivo de trazabilidad quedará pendiente hasta tener un repo propio.

## No tengo Git en la terminal

GitHub Desktop puede servir como **ruta visual**, pero no convierte automáticamente los comandos de esta guía en comandos de terminal. Elige una sola salida:

1. **Ruta visual:** clona tu repo propio en GitHub Desktop, revisa los cambios, crea el commit y haz push desde Desktop. El preflight puede seguir mostrando `BLOCKED` para Git en la terminal; registra esa limitación en tu evidencia.
2. **Ruta terminal:** instala o habilita Git, confirma que `git --version` funciona en la terminal que vas a usar y vuelve a correr el preflight.
3. **Último recurso:** descarga ZIP, registra que no conserva historial y deja pendiente la trazabilidad hasta crear o abrir tu repo propio desde GitHub Desktop o la web.

## No sé clonar

Abre [`docs/git-y-github.md`](git-y-github.md). La secuencia mínima es: crear tu repo con la plantilla, copiar la URL, ejecutar `git clone URL`, entrar a la carpeta y comprobar `git status`.

## No tengo Claude Code

Marca `PARTIAL`, conserva el mensaje y usa Cowork **solo si tienes una modalidad compatible, conexión activa y acceso a tus archivos locales**. La autenticación de Claude Code ocurre después del preflight y requiere una modalidad de acceso compatible. Revisa [`docs/claude-code.md`](claude-code.md) cuando tengas tiempo.

## No tengo Claude Code ni Cowork

Puedes cerrar el preflight de forma manual y honesta, sin simular una inspección del modelo:

1. Lee `evidence/preflight-report.md`, `notes/README.md` y [`docs/seguridad-basica.md`](seguridad-basica.md).
2. Comprueba visualmente que el remoto que aparece en el reporte corresponde a tu repo propio.
3. Escribe en `notes/intent.md` qué proceso, problema o automatización quieres explorar.
4. Añade tres observaciones concretas sobre tu espacio de trabajo: dónde estás, qué herramienta tienes y qué quedó pendiente.
5. Registra el estado como **parcial** y lleva el mensaje de bloqueo a la siguiente sesión u office hour.

Si Git sí funciona, puedes versionar `evidence/preflight-report.md` y `notes/intent.md`. Si Git tampoco funciona, conserva esos archivos localmente y declara que el commit/push quedó pendiente. No afirmes que Claude Code inspeccionó el repo si no hubo sesión autenticada.

## No tengo Python

Pide ayuda para instalar Python 3.9 o superior, o usa el fallback de leer `preflight/casos-minimos.json` y registrar manualmente tu sistema, repo, herramienta disponible y bloqueo. El reporte automático quedará pendiente.

## No tengo Node.js

No es un bloqueo del preflight ni del instalador nativo recomendado de Claude Code. Instálalo solo si eliges la ruta npm, que requiere Node.js 22 o superior, o si el proyecto que elijas lo requiere.

## No tengo base de datos

No instales una todavía. Primero define qué proceso quieres agentizar, qué datos usa, qué volumen tiene y qué salida necesita. La decisión de almacenamiento pertenece al diseño del proyecto.

## Algo pide una clave

Detente. Este preflight no necesita API keys ni debe enviar datos. Guarda el mensaje sin copiar secretos y avisa al facilitador.
