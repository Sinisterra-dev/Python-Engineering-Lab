# Ejercicios - Busqueda y ordenamiento

Total del modulo: **3 ejercicios**.

Esta version prioriza variedad real sobre cantidad. Se eliminaron bloques con entrada/salida repetidas para cumplir la regla absoluta de no repeticion.

## Ejercicio #0001 (Modulo 010_busqueda_y_ordenamiento - #001)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** busqueda lineal
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** primer_disponible (variante base). Devuelve indice del primer producto con stock > 0. Resuelve exactamente el caso indicado.
- **Entrada:** `buscar([{ "stock":0 }, { "stock":3 }])`
- **Salida esperada:** `1`
- **Reglas:** Devuelve -1 si no existe. Resuelve exactamente el caso indicado.
- **Pista opcional:** Corta al encontrar.

## Ejercicio #0002 (Modulo 010_busqueda_y_ordenamiento - #002)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** sorted, key
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** ordenar_estudiantes (variante base). Ordena por nota descendente y nombre ascendente. Resuelve exactamente el caso indicado.
- **Entrada:** `ordenar([{ "nombre":"Luis", "nota":9 }, {"nombre":"Ana", "nota":9}])`
- **Salida esperada:** `[{"nombre":"Ana","nota":9},{"nombre":"Luis","nota":9}]`
- **Reglas:** No modifiques original. Resuelve exactamente el caso indicado.
- **Pista opcional:** Usa key con tupla.

## Ejercicio #0003 (Modulo 010_busqueda_y_ordenamiento - #003)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** busqueda binaria
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** existe_codigo (variante base). Implementa busqueda binaria sobre codigos ordenados. Resuelve exactamente el caso indicado.
- **Entrada:** `existe([100, 200, 350], 200)`
- **Salida esperada:** `True`
- **Reglas:** Entrada ordenada. Resuelve exactamente el caso indicado.
- **Pista opcional:** Ajusta inicio y fin.
