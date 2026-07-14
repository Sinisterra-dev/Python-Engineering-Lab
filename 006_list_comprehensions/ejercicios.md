# Ejercicios - List comprehensions

Total del modulo: **16 ejercicios**.

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

## Ejercicio #0004 (Modulo 006_list_comprehensions - #004)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** comprehensions, filtros, matematicas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Cuadrados de impares. A partir de una lista de números enteros, devuelve el cuadrado de cada número que sea impar.
- **Entrada:** `numeros = [1, 2, 3, 4, 5]`
- **Salida esperada:** `[1, 9, 25]`
- **Reglas:** Usa list comprehension en una sola línea.
- **Pista opcional:** Agrega una cláusula if num % 2 != 0 al final de tu comprehension.

## Ejercicio #0005 (Modulo 006_list_comprehensions - #005)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** comprehensions, strings, filtros
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Palabras largas en mayusculas. Pasa a mayúsculas únicamente las palabras de una lista que tengan 4 o más caracteres de longitud.
- **Entrada:** `palabras = ["sol", "luna", "mar", "tierra"]`
- **Salida esperada:** `["LUNA", "TIERRA"]`
- **Reglas:** Las palabras más cortas se descartan del resultado.
- **Pista opcional:** Usa len() en la condición if de la list comprehension.

## Ejercicio #0006 (Modulo 006_list_comprehensions - #006)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** comprehensions, aplanamiento, matrices
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Aplanar matriz. Convierte una matriz 2D (lista de listas de enteros) en una lista plana de una sola dimensión.
- **Entrada:** `matriz = [[1, 2], [3, 4]]`
- **Salida esperada:** `[1, 2, 3, 4]`
- **Reglas:** Usa list comprehension anidada.
- **Pista opcional:** Usa `[elemento for fila in matriz for elemento in fila]`.

## Ejercicio #0007 (Modulo 006_list_comprehensions - #007)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** comprehensions, diccionarios, filtros
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Filtrar nombres de adultos. A partir de una lista de diccionarios que representan usuarios, extrae los nombres de aquellos con 18 o más años.
- **Entrada:** `usuarios = [{"nombre": "Ana", "edad": 17}, {"nombre": "Luis", "edad": 20}, {"nombre": "Eva", "edad": 18}]`
- **Salida esperada:** `["Luis", "Eva"]`
- **Reglas:** Devuelve una lista de strings.
- **Pista opcional:** Accede a la clave "edad" en el filtro y a "nombre" en la expresión.

## Ejercicio #0008 (Modulo 006_list_comprehensions - #008)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** comprehensions, matrices, transposicion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Transponer matriz simple. Transpone una matriz 2D de dimensiones 3x2 a 2x3 usando list comprehension.
- **Entrada:** `matriz = [[1, 2], [3, 4], [5, 6]]`
- **Salida esperada:** `[[1, 3, 5], [2, 4, 6]]`
- **Reglas:** Utiliza list comprehensions anidadas.
- **Pista opcional:** Itera sobre el índice de las columnas primero.

## Ejercicio #0009 (Modulo 006_list_comprehensions - #009)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** comprehensions, tuplas, formateo
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Formatear coordenadas. Convierte una lista de tuplas (x, y) en strings legibles con el formato "X: x, Y: y".
- **Entrada:** `puntos = [(0, 5), (10, -2)]`
- **Salida esperada:** `["X: 0, Y: 5", "X: 10, Y: -2"]`
- **Reglas:** Retorna una lista de strings.
- **Pista opcional:** Usa f-strings dentro de la list comprehension.

## Ejercicio #0010 (Modulo 006_list_comprehensions - #010)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** comprehensions, condicionales
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Clasificar numeros. Genera una lista donde los números negativos son reemplazados por el string "Negativo" y los positivos o cero por "Positivo".
- **Entrada:** `numeros = [1, -2, 0, -5]`
- **Salida esperada:** `["Positivo", "Negativo", "Positivo", "Negativo"]`
- **Reglas:** Usa la sintaxis de operador ternario en list comprehension `[val_if_true if cond else val_if_false for x in ...]`.
- **Pista opcional:** La condición va antes del for.

## Ejercicio #0011 (Modulo 006_list_comprehensions - #011)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** comprehensions, strings, split
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Extraer dominios de correos. Obtén los dominios de una lista de direcciones de correo electrónico.
- **Entrada:** `correos = ["user1@gmail.com", "user2@yahoo.com"]`
- **Salida esperada:** `["gmail.com", "yahoo.com"]`
- **Reglas:** Asume correos válidos con un solo `@`.
- **Pista opcional:** Usa split("@")[-1] para extraer la segunda mitad de cada correo.

## Ejercicio #0012 (Modulo 006_list_comprehensions - #012)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** comprehensions, filtros, divisibilidad
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Multiplos de 3 y 5. Genera una lista de números del 1 al 30 que sean simultáneamente múltiplos de 3 y de 5.
- **Entrada:** `rango = range(1, 31)`
- **Salida esperada:** `[15, 30]`
- **Reglas:** Usa operadores lógicos en la condición if de la list comprehension.
- **Pista opcional:** Combina con and.

## Ejercicio #0013 (Modulo 006_list_comprehensions - #013)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** comprehensions, conjuntos, listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Interseccion de dos listas. Genera la lista de elementos en común entre dos listas dadas conservando el orden de la primera.
- **Entrada:** `a = [1, 2, 3, 4]; b = [3, 4, 5]`
- **Salida esperada:** `[3, 4]`
- **Reglas:** No utilices la librería set directamente en la salida.
- **Pista opcional:** Filtra con `if x in b`.

## Ejercicio #0014 (Modulo 006_list_comprehensions - #014)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** comprehensions, matrices, sumas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Suma de filas de matriz. A partir de una matriz 2D, calcula una lista con la suma total de cada fila.
- **Entrada:** `matriz = [[1, 2, 3], [4, 5, 6]]`
- **Salida esperada:** `[6, 15]`
- **Reglas:** Usa la función sum() sobre cada elemento fila de la matriz.
- **Pista opcional:** `[sum(fila) for fila in matriz]`.

## Ejercicio #0015 (Modulo 006_list_comprehensions - #015)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** comprehensions, conversiones
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Celsius a Fahrenheit. Convierte una lista de temperaturas de grados Celsius a grados Fahrenheit.
- **Entrada:** `celsius = [0, 10, 20]`
- **Salida esperada:** `[32.0, 50.0, 68.0]`
- **Reglas:** La fórmula es (C * 9/5) + 32.
- **Pista opcional:** Aplica la fórmula sobre cada elemento de la list comprehension.

## Ejercicio #0016 (Modulo 006_list_comprehensions - #016)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** comprehensions, diccionarios, llaves
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Claves valor alto. Genera una lista con las claves de un diccionario cuyo valor numérico sea estrictamente superior a 100.
- **Entrada:** `inventario = {"lapiz": 50, "cuaderno": 120, "goma": 80, "regla": 200}`
- **Salida esperada:** `["cuaderno", "regla"]`
- **Reglas:** La lista resultante debe estar ordenada alfabéticamente.
- **Pista opcional:** Usa sorted() sobre la list comprehension resultante de iterar items().
