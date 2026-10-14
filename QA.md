# QA del preflight

## Validación local prevista

- Ejecutar `python3 preflight/preflight.py` en macOS/Linux.
- Ejecutar `py preflight/preflight.py` en Windows.
- Validar `preflight/casos-minimos.json` con Python estándar.
- Confirmar que no hay llamadas de red ni variables de credenciales requeridas.
- Confirmar que no hay enlaces hacia S2 ni materiales internos.

## Límite

La ejecución local de este documento no sustituye una prueba real en Windows o en la computadora de cada Aprendedor(a). Antes de compartirlo, el facilitador debe hacer al menos una prueba con `py` en Windows y decidir la visibilidad del repositorio.
