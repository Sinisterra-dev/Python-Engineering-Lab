# Ejercicios - Funciones

Total del modulo: **4 ejercicios**.

Esta version prioriza variedad real sobre cantidad. Se eliminaron bloques con entrada/salida repetidas para cumplir la regla absoluta de no repeticion.

## Ejercicio #0001 (Modulo 007_funciones - #001)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** funciones, acumuladores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** calcular_total_pedido (variante base). Implementa funcion que suma precio * cantidad por item. Resuelve exactamente el caso indicado.
- **Entrada:** `calcular_total_pedido([{"precio":10,"cantidad":2},{"precio":5,"cantidad":3}])`
- **Salida esperada:** `35`
- **Reglas:** Retorna numero, no imprime. Resuelve exactamente el caso indicado.
- **Pista opcional:** Multiplica cada item.

## Ejercicio #0002 (Modulo 007_funciones - #002)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** funciones, strings
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** normalizar_usuarios (variante base). Devuelve nombres limpios de al menos 3 caracteres. Resuelve exactamente el caso indicado.
- **Entrada:** `normalizar_usuarios([" Ana ", "Li", "CARLOS"])`
- **Salida esperada:** `["Ana", "Carlos"]`
- **Reglas:** Normaliza antes de filtrar. Resuelve exactamente el caso indicado.
- **Pista opcional:** strip y title.

## Ejercicio #0003 (Modulo 007_funciones - #003)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** funciones, estadisticas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** resumen_notas (variante base). Devuelve promedio, mejor y peor nota. Resuelve exactamente el caso indicado.
- **Entrada:** `resumen_notas([7, 10, 4])`
- **Salida esperada:** `{"promedio": 7.0, "mejor": 10, "peor": 4}`
- **Reglas:** Lista vacia devuelve promedio 0 y mejor/peor None. Resuelve exactamente el caso indicado.
- **Pista opcional:** Maneja vacio primero.

## Ejercicio #0004 (Modulo 007_funciones - #004)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** funciones, reglas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** aplicar_descuentos (variante base). Aplica descuentos por total e items. Resuelve exactamente el caso indicado.
- **Entrada:** `aplicar_descuentos(1200, 6)`
- **Salida esperada:** `1020.0`
- **Reglas:** 10% si total > 1000 y 5% adicional si items > 5. Resuelve exactamente el caso indicado.
- **Pista opcional:** Suma porcentajes.
