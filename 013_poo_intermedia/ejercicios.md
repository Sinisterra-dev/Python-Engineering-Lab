# Ejercicios - POO intermedia

Total del modulo: **3 ejercicios**.

Esta version prioriza variedad real sobre cantidad. Se eliminaron bloques con entrada/salida repetidas para cumplir la regla absoluta de no repeticion.

## Ejercicio #0001 (Modulo 013_poo_intermedia - #001)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** herencia, metodos
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Empleado por horas (variante base). Crea Empleado base y EmpleadoPorHoras. Resuelve exactamente el caso indicado.
- **Entrada:** `EmpleadoPorHoras("Ana", 10, 20).sueldo()`
- **Salida esperada:** `200`
- **Reglas:** La subclase calcula sueldo. Resuelve exactamente el caso indicado.
- **Pista opcional:** Reutiliza nombre.

## Ejercicio #0002 (Modulo 013_poo_intermedia - #002)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** polimorfismo
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Notificaciones polimorficas (variante base). Crea Email y SMS con metodo enviar. Resuelve exactamente el caso indicado.
- **Entrada:** `procesar([Email("a@x.com"), SMS("123")])`
- **Salida esperada:** `lista de mensajes enviados`
- **Reglas:** Procesa sin preguntar tipo concreto. Resuelve exactamente el caso indicado.
- **Pista opcional:** Todas exponen enviar.

## Ejercicio #0003 (Modulo 013_poo_intermedia - #003)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** encapsulamiento
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Inventario encapsulado (variante base). Crea Inventario con agregar, quitar y total_stock. Resuelve exactamente el caso indicado.
- **Entrada:** `inventario.total_stock()`
- **Salida esperada:** `numero total`
- **Reglas:** No expongas lista interna. Resuelve exactamente el caso indicado.
- **Pista opcional:** Usa metodos.
