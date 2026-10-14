# Git y GitHub: tu espacio de trabajo

El objetivo de esta actividad no es memorizar comandos. Es aprender a dejar un rastro revisable de tu trabajo: qué hiciste, cuándo lo hiciste, qué cambió y cómo volver atrás. Eso es **trazabilidad, control de versiones y propiedad de tu espacio de trabajo**.

## 1. Crea tu cuenta y tu repo propio

Necesitas una cuenta de GitHub. Después, desde la página de este repositorio, usa **Use this template → Create a new repository** y crea un repo propio, por ejemplo `mi-proyecto-agentico`.

Si vas a manejar datos reales o de clientes, elige un repositorio privado. No subas secretos ni información sensible.

## 2. Clonar no es descargar

**Clonar** crea una copia conectada a un repositorio remoto y conserva el historial. Es la ruta recomendada.

```bash
git clone https://github.com/TU-USUARIO/TU-REPO.git
cd TU-REPO
git status
```

**Descargar ZIP** crea una carpeta sin historial. Es un fallback útil si Git falla, pero no es el flujo que queremos practicar. Si usas ZIP, registra el bloqueo y crea después tu repo propio desde GitHub web o GitHub Desktop.

## 3. GitHub Desktop

En macOS o Windows puedes usar GitHub Desktop si la terminal todavía te resulta nueva:

1. Inicia sesión.
2. Clona tu repo propio.
3. Ábrelo en el explorador o en una terminal.
4. Sigue el [Terminal Lab](../terminal-lab/README.md) o su fast lane.
5. Revisa los cambios.
6. Escribe un mensaje de commit.
7. Pulsa **Commit** y luego **Push origin**.

GitHub Desktop no elimina la idea de Git: solo hace visibles las mismas operaciones.

## 4. Ejecuta el diagnóstico antes de versionar la evidencia

Desde la raíz de tu repo propio:

```bash
python3 preflight/preflight.py
```

En Windows PowerShell:

```powershell
py preflight/preflight.py
```

Lee `evidence/preflight-report.md`. Si aparece `PARTIAL`, conserva el mensaje y sigue el fallback. No hagas todavía el commit de cierre: el commit pequeño de práctica ocurre en la Terminal Lab.

## 5. Completa la Terminal Lab o la fast lane

- **Ruta normal:** completa [`terminal-lab/README.md`](../terminal-lab/README.md), incluidos sus checkpoints del núcleo.
- **Fast lane:** úsala solo si puedes mostrar un repo propio, un commit reciente, comprensión de `git status`/`git diff` y una falla o decisión documentada.

La Terminal Lab enseña a revisar antes de confirmar. Por eso el commit de cierre de evidencia viene después de esta práctica.

## 6. Escribe tu intención y crea el commit de cierre

Completa `notes/intent.md` con el proceso, problema o automatización que quieres explorar. No uses datos sensibles.

Para la Ruta normal, revisa y añade únicamente los tres archivos esperados:

```bash
git add evidence/preflight-report.md notes/intent.md notes/terminal-lab/prueba.txt
git diff --cached
git commit -m "chore: complete environment preflight"
git push
```

Para la fast lane, añade solo los archivos que realmente existan:

```bash
git add evidence/preflight-report.md notes/intent.md
git diff --cached
git commit -m "chore: complete environment preflight"
git push
```

No uses `git add .` sin revisar. El staging explícito te ayuda a no subir archivos accidentales, configuraciones o secretos.

## 7. Evidencia de llegada

Llegas listo(a) para la siguiente indicación cuando puedes mostrar:

- la URL de tu propio repo;
- `evidence/preflight-report.md`;
- una nota de intención en `notes/intent.md`;
- un commit de práctica o de cierre visible;
- qué herramienta usarás y qué fallback tienes;
- una decisión o siguiente paso que quieras explorar.
