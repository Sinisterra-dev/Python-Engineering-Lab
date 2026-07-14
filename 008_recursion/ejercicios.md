# Ejercicios - Recursion

Total del modulo: **3 ejercicios**.

Esta version prioriza variedad real sobre cantidad. Se eliminaron bloques con entrada/salida repetidas para cumplir la regla absoluta de no repeticion.

## Ejercicio #0001 (Modulo 008_recursion - #001)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** recursion, diccionarios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** contar_archivos (variante base). Cuenta archivos en carpetas anidadas representadas con diccionarios. Resuelve exactamente el caso indicado.
- **Entrada:** `contar({"a.txt": None, "src": {"b.py": None}})`
- **Salida esperada:** `2`
- **Reglas:** Archivo tiene valor None. Carpeta tiene dict. Resuelve exactamente el caso indicado.
- **Pista opcional:** Caso base: None.

## Ejercicio #0002 (Modulo 008_recursion - #002)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** recursion, listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** aplanar_categorias (variante base). Aplana listas anidadas conservando orden. Resuelve exactamente el caso indicado.
- **Entrada:** `aplanar(["A", ["B", ["C"]]])`
- **Salida esperada:** `["A", "B", "C"]`
- **Reglas:** Si un elemento es lista, procesalo recursivamente. Resuelve exactamente el caso indicado.
- **Pista opcional:** Concatena resultados.

## Ejercicio #0003 (Modulo 008_recursion - #003)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** recursion, arboles
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** sumar_puntajes (variante base). Suma puntos de un arbol de partidas. Resuelve exactamente el caso indicado.
- **Entrada:** `sumar({"puntos":5,"sub":[{"puntos":3,"sub":[]}]})`
- **Salida esperada:** `8`
- **Reglas:** Cada nodo tiene puntos y sub. Resuelve exactamente el caso indicado.
- **Pista opcional:** Suma nodo e hijos.
