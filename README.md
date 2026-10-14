<p align="center">
  <img src="docs/visuales/preflight-banner.svg" alt="Preflight: trazabilidad, control de versiones y propiedad del espacio de trabajo" width="900">
</p>

<h1 align="center">Preflight</h1>
<p align="center"><strong>Prepara tu entorno en macOS o Windows</strong></p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white">
  <img alt="Git y GitHub" src="https://img.shields.io/badge/Git%20%2F%20GitHub-control%20de%20versiones-F05032?logo=git&logoColor=white">
  <img alt="Claude Code" src="https://img.shields.io/badge/Claude%20Code-ruta%20principal-D97757?logo=anthropic&logoColor=white">
  <img alt="Cowork fallback" src="https://img.shields.io/badge/Cowork-fallback-6E56CF">
  <img alt="Node.js condicional" src="https://img.shields.io/badge/Node.js-condicional-5FA04E?logo=node.js&logoColor=white">
  <img alt="Sin API key" src="https://img.shields.io/badge/API%20key-no%20requerida-2E8B57">
</p>

<p align="center"><em>Antes de agentizar, aprende a cuidar tu propio espacio de trabajo.</em></p>

Este repositorio no es la sesión técnica ni un agente completo. Es tu **primer checkpoint de trazabilidad, control de versiones y propiedad de tu espacio de trabajo**.

Al terminar, debes poder responder tres preguntas:

1. ¿Dónde está mi propio repositorio?
2. ¿Qué hice, cuándo lo hice y cómo puedo volver atrás?
3. ¿Qué herramientas tengo, cuál me falta y qué fallback usaré?

## Empieza por tu propio repositorio

No trabajes permanentemente dentro del repositorio de la clase. Primero crea tu cuenta de GitHub y luego usa este repositorio como plantilla:

1. En GitHub, pulsa **Use this template → Create a new repository**.
2. Crea un repo propio, por ejemplo `mi-proyecto-agentico`.
3. Elige una visibilidad compatible con la información que manejarás. Para datos reales o de clientes, usa un repositorio privado.
4. Clona **tu propio repo**, no el repo de la clase.
5. Ejecuta el preflight desde esa copia.

### Opción A — Terminal con Git

```bash
git clone https://github.com/TU-USUARIO/TU-REPO.git
cd TU-REPO
python3 preflight/preflight.py
```

En Windows PowerShell:

```powershell
git clone https://github.com/TU-USUARIO/TU-REPO.git
cd TU-REPO
py preflight/preflight.py
```

### Opción B — GitHub Desktop

Abre GitHub Desktop, inicia sesión, clona tu repo propio y selecciona **Open in terminal**. Después ejecuta el comando de Python indicado arriba.

### Descargar ZIP: solo como fallback

Descargar ZIP sirve para no quedarse bloqueado, pero **no conserva el historial ni enseña el flujo de clonación, commit y push**. Si usas ZIP, crea después tu repo propio y sube el resultado desde GitHub Desktop o desde la web.

## Guarda evidencia y haz tu primer commit

Después del preflight, conserva la salida en `evidence/preflight-report.md`. Escribe también en `notes/intent.md` qué proceso o problema te gustaría explorar, sin usar datos sensibles.

```bash
mkdir -p notes evidence
git add .
git commit -m "chore: complete environment preflight"
git push
```

En Windows, puedes crear las carpetas desde el Explorador de archivos o usar:

```powershell
New-Item -ItemType Directory -Force notes,evidence
```

Tu primer resultado no es un agente. Es una URL propia, un primer commit, un reporte y una decisión explícita sobre el siguiente paso.

## Terminal Lab — paso obligatorio

Antes de pasar a Claude Code, completa el [Terminal Lab](terminal-lab/README.md). El núcleo toma aproximadamente 35–45 minutos y enseña a ubicarte, navegar, crear y leer archivos, revisar Git, hacer un commit pequeño y leer un error seguro.

La extensión intermedia trabaja búsqueda, pipes, historial y ramas. La extensión avanzada conecta variables de entorno, códigos de salida y una primera interacción de solo lectura con Claude Code. Las extensiones son opcionales; el núcleo es común para toda la cohorte.

La secuencia didáctica es:

> observar → explicar → proponer → revisar → ejecutar → verificar → versionar

## Ejecuta el diagnóstico

```bash
python3 preflight/preflight.py
```

En Windows:

```powershell
py preflight/preflight.py
```

El script no instala nada, no llama a una API y no necesita una API key. Escribe un reporte local sin secretos.

### Cómo leer el resultado

- **PASS:** lo necesario para este checkpoint está disponible.
- **PARTIAL:** puedes avanzar, pero falta una herramienta de la ruta principal o debes usar un fallback.
- **DEFERRED:** la comprobación depende de tu proyecto y todavía no corresponde instalarla.
- **BLOCKED:** primero resuelve el bloqueo o usa el fallback documentado.

## Qué revisa y qué no

### Revisión base

El preflight comprueba Python, Git, que estés trabajando dentro de un repositorio GitHub propio, el dataset sintético y la disponibilidad de Claude Code.

Claude Code es la ruta principal del curso. Si no está disponible, el resultado será `PARTIAL` y podrás continuar con Cowork como fallback mientras resuelves la instalación.

### Dependencias condicionales

Node.js y npm se detectan como información, pero **no se marcan como bloqueo**. El instalador nativo recomendado de Claude Code no necesita Node.js; Node.js solo entra si eliges una herramienta o proyecto que lo requiera. La base de datos tampoco se instala aquí: se decide después de definir qué quieres agentizar y qué arquitectura necesita.

GitHub CLI (`gh`) es útil, pero no es requisito. Git o GitHub Desktop sí forman parte del aprendizaje porque permiten conservar historial, revisar cambios y recuperar decisiones.

## Qué significa “ser dueño(a) de tu espacio”

Tu repo propio será el lugar donde guardarás decisiones, notas, evidencias, prompts y cambios revisables. La meta no es llenar carpetas: es que otra persona pueda entender qué intentaste, qué cambió y cómo volver a un estado anterior.

No subas API keys, contraseñas, transcripts con datos personales ni información de clientes. Revisa [`docs/seguridad-basica.md`](docs/seguridad-basica.md) antes de guardar evidencia.

## Si algo falla

Consulta [`docs/fallback.md`](docs/fallback.md). Si Claude Code falla, no conviertas la clase en una instalación interminable: conserva el mensaje, usa Cowork o el fallback de papel y registra qué quedó pendiente.

Para aprender la diferencia entre descargar, clonar, hacer commit y hacer push, abre [`docs/git-y-github.md`](docs/git-y-github.md).

## Fuentes oficiales de instalación

- [Claude Code — instalación y requisitos](https://code.claude.com/docs/en/setup)
- [Claude Code — quickstart](https://code.claude.com/docs/en/quickstart)

Este repo **no contiene S2, comandos internos del Mentor, rúbricas del facilitador ni la solución completa del camino dorado**.
