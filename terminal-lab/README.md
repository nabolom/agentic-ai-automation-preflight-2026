# Terminal Lab

## Núcleo obligatorio: 35–45 minutos

Esta práctica es parte del preflight. No es una prueba de velocidad ni busca convertirte en especialista de terminal en una tarde.

La meta es que puedas trabajar con tu repo propio y entender qué está pasando antes de pedirle a Claude Code que haga algo. Al terminar, debes poder:

- ubicarte en una carpeta y explicar dónde estás;
- crear, leer y modificar un archivo sin perderte;
- distinguir un comando, sus argumentos, su salida y su error;
- revisar cambios con Git y guardar un primer commit;
- describir qué hiciste y cómo volver a un estado anterior;
- abrir Claude Code al final con una pregunta de solo lectura.

La competencia que practicamos es **trazabilidad, control de versiones y propiedad operativa de tu espacio de trabajo**.

## Antes de empezar

Trabaja dentro de tu repo propio, creado desde la plantilla de [Agentic AI Automation Preflight](https://github.com/nabolom/agentic-ai-automation-preflight-2026). No pegues API keys, contraseñas ni información de clientes.

Elige una terminal:

- **macOS:** Terminal, Warp u otra terminal.
- **Windows:** PowerShell o Windows Terminal. GitHub Desktop es un fallback visual para Git.

Warp es una opción válida, pero no es requisito. Una terminal es el lugar donde ejecutas comandos; VS Code es un editor/IDE donde puedes abrir y editar los archivos. Puedes usar ambos juntos.

## Editores e IDEs gratuitos opcionales

Elige uno, no todos:

- [VS Code](https://code.visualstudio.com/) — recomendación principal para editar archivos y abrir una terminal integrada.
- [Zed](https://zed.dev/) — alternativa ligera para quienes prefieren un editor rápido.
- [VSCodium](https://vscodium.com/) — alternativa comunitaria basada en el ecosistema de VS Code.
- [GitHub Desktop](https://desktop.github.com/) — no es un IDE; es un fallback visual para clonar, revisar cambios, hacer commit y hacer push.
- [Warp](https://www.warp.dev/) — no es un IDE; es una terminal alternativa que puedes usar en macOS o Windows.

Para la cohorte basta con **VS Code + la terminal del sistema**. Las demás opciones son válidas, pero no cambian los conceptos que estamos aprendiendo.

> **Regla de seguridad:** ejecuta un comando a la vez, lee la salida y no uses `sudo`, `rm -rf`, comandos destructivos ni pegues secretos solo porque alguien los incluyó en una instrucción.

## 1. Entiende tu prompt y tu carpeta actual

El prompt es la línea que espera tu siguiente comando. La carpeta actual importa porque los comandos que leen o escriben archivos normalmente trabajan ahí.

### macOS — Terminal o Warp

```bash
pwd
ls
```

`pwd` muestra la ruta actual. `ls` muestra su contenido.

### Windows — PowerShell

```powershell
Get-Location
Get-ChildItem
```

`Get-Location` muestra la ruta actual. `Get-ChildItem` muestra su contenido.

**Checkpoint 1:** explica en una frase en qué carpeta estás y cómo sabes que es tu repo propio.

## 2. Muévete, crea y lee un archivo

### macOS

```bash
mkdir -p notes/terminal-lab
cd notes/terminal-lab
printf 'Primer archivo de la Terminal Lab\n' > prueba.txt
cat prueba.txt
cd ../..
pwd
```

### Windows PowerShell

```powershell
New-Item -ItemType Directory -Force notes/terminal-lab
Set-Location notes/terminal-lab
Set-Content -Path prueba.txt -Value 'Primer archivo de la Terminal Lab'
Get-Content prueba.txt
Set-Location ../..
Get-Location
```

Observa que `>` redirige una salida hacia un archivo. Si vuelves a usar `>`, reemplazas su contenido. `>>` agrega al final en shells compatibles.

**Checkpoint 2:** abre `notes/terminal-lab/prueba.txt` en VS Code o en el editor que prefieras y confirma que contiene una sola línea.

## 3. Comprueba las herramientas sin instalar todo

### macOS

```bash
python3 --version
git --version
```

### Windows PowerShell

```powershell
py --version
git --version
```

No ejecutes todavía `claude` como parte del núcleo. Claude Code llega al final, después de entender la terminal y el repo.

**Checkpoint 3:** registra en una nota qué herramientas encontraste y cuál quedó pendiente. La falta de Node.js o de una base de datos no bloquea esta práctica.

## 4. Observa Git antes de cambiar nada

Git permite ver el estado de tu espacio y conservar decisiones.

```bash
git status
git diff -- notes/terminal-lab/prueba.txt
```

En PowerShell los comandos de Git son los mismos:

```powershell
git status
git diff -- notes/terminal-lab/prueba.txt
```

`git status` responde qué archivos cambiaron. `git diff` muestra la diferencia. No hagas `git add` todavía sin mirar la salida.

**Checkpoint 4:** identifica el archivo que creaste y explica si Git lo muestra como no rastreado o modificado.

## 5. Guarda un commit pequeño

```bash
git add notes/terminal-lab/prueba.txt
git diff --cached
git commit -m "docs: practice terminal basics"
git status
```

El orden importa:

1. `git add` prepara un cambio.
2. `git diff --cached` te deja revisarlo.
3. `git commit` lo guarda en el historial local.
4. `git status` confirma qué queda pendiente.

Si tu repo propio ya tenía cambios que no son de esta práctica, no uses `git add .` sin revisar. Añade únicamente el archivo que entiendes.

Si tienes permiso y tu remoto ya está configurado:

```bash
git push
```

**Checkpoint 5:** abre tu repo en GitHub y localiza el commit. Esa URL y ese historial son parte de tu evidencia.

## 6. Provoca un error pequeño y léelo

Los errores son información. Ejecuta una orden segura con un nombre que no existe:

```bash
git show archivo-que-no-existe.txt
```

Observa que Git escribe un mensaje de error y devuelve un código de salida distinto de cero. No intentes “arreglar” un error copiando comandos al azar.

En macOS puedes consultar el código de la última orden así:

```bash
echo $?
```

En PowerShell puedes consultar el resultado de la última orden nativa así:

```powershell
$LASTEXITCODE
```

**Checkpoint 6:** escribe qué comando falló, qué mensaje devolvió y qué harías antes de pedir ayuda.

## 7. Claude Code entra al final

Esta es la primera interacción controlada. Primero comprueba la instalación:

```bash
claude --version
```

Si responde, puedes hacer un diagnóstico de solo lectura:

```bash
claude doctor
```

Después abre Claude Code desde la raíz de tu repo:

```bash
claude
```

En Windows PowerShell se usan los mismos comandos. Dentro de Claude Code, escribe primero:

```text
Explica en lenguaje sencillo dónde estoy, qué archivos relevantes ves y cuál es el estado de Git. No modifiques ningún archivo ni ejecutes comandos destructivos.
```

Luego prueba:

```text
Propón una forma segura de revisar mi cambio en notes/terminal-lab/prueba.txt. No edites nada todavía.
```

Lee la propuesta. No aceptes cambios solo porque los propuso un modelo.

Para salir:

```text
/exit
```

Si Claude Code no está instalado, marca `PARTIAL`, conserva el mensaje y usa Cowork como fallback. No instales Node.js únicamente para intentar una ruta npm deprecada.

**Checkpoint 7:** puedes explicar qué observó Claude Code, qué no le permitiste modificar y cómo verificaste el estado de Git después.

## Extensión intermedia — opcional

Hazla solo después de completar el núcleo.

### Buscar archivos y texto

macOS:

```bash
find . -maxdepth 2 -type f
grep -RIn "terminal" .
```

Windows PowerShell:

```powershell
Get-ChildItem -Recurse -File
Select-String -Path .\* -Pattern 'terminal' -Recurse
```

`grep` busca texto dentro de archivos y muestra la línea donde aparece.

### Pipes y primeras líneas

macOS:

```bash
find . -maxdepth 2 -type f | head -10
```

Windows PowerShell:

```powershell
Get-ChildItem -Recurse -File | Select-Object -First 10
```

Una pipe `|` pasa la salida de un comando a otro. Esto será importante cuando Claude Code inspeccione muchos archivos o logs.

### Historial y ramas

```bash
git log --oneline -5
git show --stat HEAD
git switch -c experiment/terminal-lab
git status
git switch main
```

Una rama permite experimentar sin mover inmediatamente la línea principal. Si no entiendes qué hizo un comando, detente y pide una explicación.

## Extensión avanzada — opcional

### Variables de entorno sin secretos

macOS:

```bash
export LAB_MODE=practice
echo "$LAB_MODE"
```

Windows PowerShell:

```powershell
$env:LAB_MODE = 'practice'
$env:LAB_MODE
```

No guardes API keys en archivos ni las pegues en la terminal compartida. Las variables de entorno son útiles, pero también pueden exponer secretos si no sabes dónde terminan.

### Diagnóstico reproducible

Pide a Claude Code que explique, sin modificar:

```text
Revisa únicamente el estado de Git y los archivos de notes/terminal-lab. Devuélveme: comandos que usarías, riesgos, archivos que tocarías y cómo verificarías el resultado. No ejecutes nada.
```

Después compara su propuesta con lo que ya aprendiste. El objetivo no es delegar el entendimiento, sino usar el agente como copiloto verificable.

## Entregable de la Terminal Lab

En tu repo propio deben quedar:

- `evidence/preflight-report.md`;
- `notes/intent.md`;
- `notes/terminal-lab/prueba.txt`;
- un commit visible en GitHub;
- una breve nota de qué herramienta tienes, cuál falta y qué fallback usarías.

No necesitas Node.js, npm, una base de datos ni una API key para terminar el núcleo obligatorio.
