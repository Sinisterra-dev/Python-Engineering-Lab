# Ejercicios - POO avanzada

Total del modulo: **3 ejercicios**.

Esta version prioriza variedad real sobre cantidad. Se eliminaron bloques con entrada/salida repetidas para cumplir la regla absoluta de no repeticion.

## Ejercicio #0001 (Modulo 014_poo_avanzada - #001)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** POO, composicion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Validador de reglas (variante base). Clase Validador aplica funciones de validacion sobre un dato. Resuelve exactamente el caso indicado.
- **Entrada:** `validador.validar({"edad":20})`
- **Salida esperada:** `True o lista de errores`
- **Reglas:** Cada regla devuelve True o mensaje. Resuelve exactamente el caso indicado.
- **Pista opcional:** Acumula errores.

## Ejercicio #0002 (Modulo 014_poo_avanzada - #002)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** POO, repositorio
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Repositorio con ids (variante base). Asigna ids incrementales al agregar objetos. Resuelve exactamente el caso indicado.
- **Entrada:** `repo.agregar({"nombre":"Ana"})`
- **Salida esperada:** `1`
- **Reglas:** No reutilices ids eliminados. Resuelve exactamente el caso indicado.
- **Pista opcional:** Guarda en dict interno.

## Ejercicio #0003 (Modulo 014_poo_avanzada - #003)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** POO, comportamiento
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Reporte ordenable (variante base). Reporte acepta una funcion key para ordenar registros. Resuelve exactamente el caso indicado.
- **Entrada:** `Reporte(registros).ordenar_por(lambda r: r["total"])`
- **Salida esperada:** `registros ordenados`
- **Reglas:** No hardcodees el campo. Resuelve exactamente el caso indicado.
- **Pista opcional:** Recibe key externa.
