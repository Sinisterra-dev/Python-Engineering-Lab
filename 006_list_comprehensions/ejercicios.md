# Ejercicios - List comprehensions

Total del modulo: **3 ejercicios**.

Esta version prioriza variedad real sobre cantidad. Se eliminaron bloques con entrada/salida repetidas para cumplir la regla absoluta de no repeticion.

## Ejercicio #0001 (Modulo 006_list_comprehensions - #001)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** comprehensions, filtros
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Precios con IVA (variante base). Devuelve precios positivos con IVA del 21%. Resuelve exactamente el caso indicado.
- **Entrada:** `precios = [100, 0, 50, -4]`
- **Salida esperada:** `[121.0, 60.5]`
- **Reglas:** Usa list comprehension. Resuelve exactamente el caso indicado.
- **Pista opcional:** Filtra positivos.

## Ejercicio #0002 (Modulo 006_list_comprehensions - #002)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** comprehensions, strings
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Iniciales validas (variante base). Devuelve iniciales de nombres no vacios. Resuelve exactamente el caso indicado.
- **Entrada:** `nombres = ["ana", "", "Luis"]`
- **Salida esperada:** `["A", "L"]`
- **Reglas:** Usa comprehension. Resuelve exactamente el caso indicado.
- **Pista opcional:** Verifica string no vacio.

## Ejercicio #0003 (Modulo 006_list_comprehensions - #003)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** comprehensions anidadas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Disponibilidad habitacion-dia (variante base). Genera pares habitacion-dia. Resuelve exactamente el caso indicado.
- **Entrada:** `habitaciones = [101, 102]; dias = ["lun", "mar"]`
- **Salida esperada:** `[(101, "lun"), (101, "mar"), (102, "lun"), (102, "mar")]`
- **Reglas:** Mantiene orden. Resuelve exactamente el caso indicado.
- **Pista opcional:** Usa dos for.
