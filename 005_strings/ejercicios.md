# Ejercicios - Strings

Total del modulo: **4 ejercicios**.

Esta version prioriza variedad real sobre cantidad. Se eliminaron bloques con entrada/salida repetidas para cumplir la regla absoluta de no repeticion.

## Ejercicio #0001 (Modulo 005_strings - #001)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** strings, normalizacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Nombres importados limpios (variante base). Normaliza nombres con espacios y mayusculas mezcladas. Resuelve exactamente el caso indicado.
- **Entrada:** `nombres = [" ana ", "LUIS", " marta"]`
- **Salida esperada:** `["Ana", "Luis", "Marta"]`
- **Reglas:** Aplica strip y title. Resuelve exactamente el caso indicado.
- **Pista opcional:** Procesa cada nombre.

## Ejercicio #0002 (Modulo 005_strings - #002)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** strings, split
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Dominios de correo (variante base). Extrae dominios sin duplicados. Resuelve exactamente el caso indicado.
- **Entrada:** `correos = ["a@mail.com", "b@test.com", "c@mail.com"]`
- **Salida esperada:** `["mail.com", "test.com"]`
- **Reglas:** Ordena la salida. Resuelve exactamente el caso indicado.
- **Pista opcional:** Divide por @.

## Ejercicio #0003 (Modulo 005_strings - #003)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** strings, diccionarios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Codigos por prefijo (variante base). Cuenta codigos por prefijo antes del guion. Resuelve exactamente el caso indicado.
- **Entrada:** `codigos = ["LIB-001", "TEC-002", "LIB-003"]`
- **Salida esperada:** `{"LIB": 2, "TEC": 1}`
- **Reglas:** Usa split. Resuelve exactamente el caso indicado.
- **Pista opcional:** El prefijo es la parte 0.

## Ejercicio #0004 (Modulo 005_strings - #004)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** strings, validaciones
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Placas validas (variante base). Filtra placas con tres letras, guion y tres digitos. Resuelve exactamente el caso indicado.
- **Entrada:** `placas = ["ABC-123", "AB-123", "XYZ-999"]`
- **Salida esperada:** `["ABC-123", "XYZ-999"]`
- **Reglas:** No uses regex. Resuelve exactamente el caso indicado.
- **Pista opcional:** Valida longitud y partes.
