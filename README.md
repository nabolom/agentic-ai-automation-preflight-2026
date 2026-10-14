# Preflight — prepara tu entorno

Este repositorio comprueba si tu computadora está lista para participar en la siguiente sesión. **No es la sesión, no es un agente y no mide la calidad de un modelo.**

## Haz esto primero

1. Descarga o clona esta carpeta.
2. Abre una terminal dentro de ella.
3. Ejecuta:

```bash
python3 preflight/preflight.py
```

En Windows, si `python3` no existe, prueba:

```powershell
py preflight/preflight.py
```

4. Lee el resultado:

- **PASS:** el preflight básico está listo.
- **PARTIAL:** puedes continuar, pero falta una herramienta opcional o conviene usar un fallback.
- **BLOCKED:** hay que resolver el bloqueo o trabajar con el fallback.

## Qué comprueba

- versión disponible de Python;
- lectura del dataset mínimo incluido;
- disponibilidad de Git como herramienta opcional;
- disponibilidad de Claude Code como herramienta opcional;
- que no necesites una API key ni conexión a internet para hacer este diagnóstico.

## Qué no comprueba

- que Claude Code esté autenticado;
- que una API real funcione;
- que tengas acceso a una cuenta o plataforma externa;
- que hayas completado la Sesión 2;
- que estés listo(a) para producción.

## Si algo falla

No te quedes detenido(a) instalando herramientas. Consulta [`docs/fallback.md`](docs/fallback.md) y registra qué paso sí pudiste completar.

No uses datos personales, confidenciales o de clientes en este preflight. Consulta [`docs/seguridad-basica.md`](docs/seguridad-basica.md).

## Siguiente acción

Conserva la salida del comando o una captura. Tu facilitador indicará cuándo abrir el siguiente material del curso. Este repo **no contiene S2, comandos del Mentor, rúbricas ni la solución completa del camino dorado**.
