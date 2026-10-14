# Dependencias y decisiones

No todo lo que puede aparecer en un proyecto debe instalarse antes de saber qué quieres agentizar. El preflight distingue lo que necesitas para aprender el flujo de lo que depende de tu arquitectura.

| Elemento | Estado | Razón |
|---|---|---|
| Cuenta de GitHub | Requerida | Es la identidad con la que crearás y cuidarás tu repo propio. |
| Repo propio en GitHub | Requerido | Es el espacio donde guardarás historial, notas y evidencia. |
| Git o GitHub Desktop | Requerido para el flujo | Permite clonar, revisar cambios, hacer commit y push. |
| Python 3.9+ | Requerido para este preflight | Ejecuta el diagnóstico sin paquetes externos. |
| Claude Code | Ruta principal | Se comprueba con `claude --version`; la autenticación ocurre después. |
| Cowork | Fallback | Permite continuar si Claude Code no está disponible. |
| Node.js/npm | Condicional | No es requisito del instalador nativo recomendado; npm requiere Node.js 22+ si eliges esa ruta. |
| GitHub CLI (`gh`) | Opcional | GitHub web, Git o GitHub Desktop cubren el flujo inicial. |
| Base de datos | Condicional | Se decide después de acotar proceso, decisión, datos y arquitectura. |
| API key | No requerida para el preflight | El diagnóstico no llama a ningún modelo ni servicio externo. Claude Code puede requerir una cuenta compatible. |

## Regla de instalación

Primero identifica la necesidad. Después instala la dependencia mínima. Si una persona instala Node.js, una base de datos, n8n y varias CLIs antes de definir su proceso, el entorno se convierte en el proyecto y se pierde el objetivo didáctico.

## Fuentes actuales de Claude Code

La documentación oficial indica que el instalador nativo es la opción recomendada para macOS, Linux, WSL y Windows. También indica que Git for Windows es recomendable en Windows para usar Git Bash, pero no es obligatorio para ejecutar Claude Code. La instalación global vía npm sigue disponible y requiere Node.js 22 o superior.

- [Claude Code — instalación y requisitos](https://code.claude.com/docs/en/setup)
- [Claude Code — quickstart](https://code.claude.com/docs/en/quickstart)
- [Claude Code — guía de terminal](https://code.claude.com/docs/en/terminal-guide)
- [Repositorio oficial de Claude Code](https://github.com/anthropics/claude-code)

**Verificado:** 14 de octubre de 2026.
