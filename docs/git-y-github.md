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

**Descargar ZIP** crea una carpeta sin historial. Es un fallback útil si Git falla, pero no es el flujo que queremos practicar. Si usas ZIP, crea después tu repo propio y sube los archivos desde GitHub web o GitHub Desktop.

## 3. GitHub Desktop

En macOS o Windows puedes usar GitHub Desktop si la terminal todavía te resulta nueva:

1. Inicia sesión.
2. Clona tu repo propio.
3. Ábrelo en el explorador o en una terminal.
4. Revisa los cambios.
5. Escribe un mensaje de commit.
6. Pulsa **Commit** y luego **Push origin**.

GitHub Desktop no elimina la idea de Git: solo hace visibles las mismas operaciones.

## 4. Tu primer registro

Ejecuta el preflight, revisa `evidence/preflight-report.md` y crea `notes/intent.md`. En esa nota escribe qué proceso o problema te gustaría explorar, sin datos sensibles.

```bash
mkdir -p notes evidence
git add .
git commit -m "chore: complete environment preflight"
git push
```

En Windows PowerShell puedes crear las carpetas así:

```powershell
New-Item -ItemType Directory -Force notes,evidence
```

## 5. Evidencia de llegada

Llegas listo(a) para la siguiente indicación cuando puedes mostrar:

- la URL de tu propio repo;
- un primer commit visible;
- `evidence/preflight-report.md`;
- una nota de intención en `notes/intent.md`;
- qué herramienta usarás y qué fallback tienes.
