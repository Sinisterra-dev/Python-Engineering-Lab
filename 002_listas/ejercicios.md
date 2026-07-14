# Ejercicios - Listas

Total del modulo: **5 ejercicios**.

Esta version prioriza variedad real sobre cantidad. Se eliminaron bloques con entrada/salida repetidas para cumplir la regla absoluta de no repeticion.

## Ejercicio #0001 (Modulo 002_listas - #001)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** listas, filtros
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Compactar lecturas validas (variante base). Recibes lecturas con None. Devuelve validas y posiciones descartadas. Resuelve exactamente el caso indicado.
- **Entrada:** `lecturas = [20, None, 22, None, 19]`
- **Salida esperada:** `{"validas": [20, 22, 19], "descartadas": [1, 3]}`
- **Reglas:** No modifiques la lista original. Resuelve exactamente el caso indicado.
- **Pista opcional:** Usa enumerate.

## Ejercicio #0002 (Modulo 002_listas - #002)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** listas, rachas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Mayor racha de ventas bajas (variante base). Recibes ventas diarias. Devuelve la longitud de la mayor racha menor a 10. Resuelve exactamente el caso indicado.
- **Entrada:** `ventas = [12, 4, 3, 15, 2, 1, 0]`
- **Salida esperada:** `3`
- **Reglas:** Reinicia el contador cuando la venta sea suficiente. Resuelve exactamente el caso indicado.
- **Pista opcional:** Compara racha actual contra mejor.

## Ejercicio #0003 (Modulo 002_listas - #003)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** listas, orden estable
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Priorizar cola de atencion (variante base). Recibes cola y clientes urgentes. Devuelve urgentes primero sin duplicar. Resuelve exactamente el caso indicado.
- **Entrada:** `cola = ["Ana", "Luis", "Eva", "Juan"]; urgentes = ["Eva", "Ana"]`
- **Salida esperada:** `["Ana", "Eva", "Luis", "Juan"]`
- **Reglas:** Conserva orden relativo. Resuelve exactamente el caso indicado.
- **Pista opcional:** Haz dos pasadas.

## Ejercicio #0004 (Modulo 002_listas - #004)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** listas, simulacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Historial de stock (variante base). Recibes stock inicial y movimientos. Devuelve stock despues de cada movimiento, sin negativos. Resuelve exactamente el caso indicado.
- **Entrada:** `stock = 10; movimientos = [-2, 5, -20, 4]`
- **Salida esperada:** `[8, 13, 0, 4]`
- **Reglas:** El stock minimo es cero. Resuelve exactamente el caso indicado.
- **Pista opcional:** Ajusta despues de cada movimiento.

## Ejercicio #0005 (Modulo 002_listas - #005)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** listas paralelas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Mejoras de calificaciones (variante base). Recibes notas antes y despues. Devuelve indices donde hubo mejora. Resuelve exactamente el caso indicado.
- **Entrada:** `antes = [5, 8, 6]; despues = [7, 7, 9]`
- **Salida esperada:** `[0, 2]`
- **Reglas:** Ambas listas tienen igual longitud. Resuelve exactamente el caso indicado.
- **Pista opcional:** Compara por indice.
