# Ejercicios - Diccionarios

Total del modulo: **5 ejercicios**.

Esta version prioriza variedad real sobre cantidad. Se eliminaron bloques con entrada/salida repetidas para cumplir la regla absoluta de no repeticion.

## Ejercicio #0001 (Modulo 003_diccionarios - #001)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** diccionarios, acumuladores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Ventas por producto (variante base). Agrupa cantidad vendida por producto. Resuelve exactamente el caso indicado.
- **Entrada:** `ventas = [{"producto":"pan","cantidad":2},{"producto":"pan","cantidad":3},{"producto":"leche","cantidad":1}]`
- **Salida esperada:** `{"pan": 5, "leche": 1}`
- **Reglas:** Inicializa claves al aparecer. Resuelve exactamente el caso indicado.
- **Pista opcional:** get ayuda.

## Ejercicio #0002 (Modulo 003_diccionarios - #002)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** diccionarios, porcentajes
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Asistencia por curso (variante base). Calcula porcentaje de asistencia por curso. Resuelve exactamente el caso indicado.
- **Entrada:** `registros = [{"curso":"A","presente":True},{"curso":"A","presente":False},{"curso":"B","presente":True}]`
- **Salida esperada:** `{"A": 50.0, "B": 100.0}`
- **Reglas:** Cuenta presentes y totales. Resuelve exactamente el caso indicado.
- **Pista opcional:** Usa dos diccionarios.

## Ejercicio #0003 (Modulo 003_diccionarios - #003)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** diccionarios, validaciones
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Productos sin precio valido (variante base). Devuelve nombres con precio faltante o no positivo. Resuelve exactamente el caso indicado.
- **Entrada:** `productos = [{"nombre":"A","precio":10},{"nombre":"B","precio":None},{"nombre":"C","precio":0}]`
- **Salida esperada:** `["B", "C"]`
- **Reglas:** Precio valido es mayor que cero. Resuelve exactamente el caso indicado.
- **Pista opcional:** Revisa cada registro.

## Ejercicio #0004 (Modulo 003_diccionarios - #004)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** diccionarios, logs
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Errores por servicio (variante base). Cuenta logs de severidad error por servicio. Resuelve exactamente el caso indicado.
- **Entrada:** `logs = [{"servicio":"api","sev":"error"},{"servicio":"web","sev":"info"},{"servicio":"api","sev":"error"}]`
- **Salida esperada:** `{"api": 2}`
- **Reglas:** Ignora severidades distintas. Resuelve exactamente el caso indicado.
- **Pista opcional:** Filtra antes de contar.

## Ejercicio #0005 (Modulo 003_diccionarios - #005)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** diccionarios, mezcla
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Fusionar inventarios (variante base). Suma dos inventarios sin modificar originales. Resuelve exactamente el caso indicado.
- **Entrada:** `a = {"pan": 2}; b = {"pan": 3, "leche": 4}`
- **Salida esperada:** `{"pan": 5, "leche": 4}`
- **Reglas:** Devuelve un diccionario nuevo. Resuelve exactamente el caso indicado.
- **Pista opcional:** Copia y suma.
