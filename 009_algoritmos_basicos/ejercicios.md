# Ejercicios - Algoritmos basicos

Total del modulo: **22 ejercicios**.

Esta version prioriza variedad real sobre cantidad. Se eliminaron bloques con entrada/salida repetidas para cumplir la regla absoluta de no repeticion.

## Ejercicio #0001 (Modulo 009_algoritmos_basicos - #001)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** algoritmos, rachas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** comprimir_estados (variante base). Convierte estados consecutivos en pares estado-cantidad. Resuelve exactamente el caso indicado.
- **Entrada:** `comprimir(["ok", "ok", "error", "ok"])`
- **Salida esperada:** `[("ok", 2), ("error", 1), ("ok", 1)]`
- **Reglas:** No ordenes. Resuelve exactamente el caso indicado.
- **Pista opcional:** Compara con anterior.

## Ejercicio #0002 (Modulo 009_algoritmos_basicos - #002)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** ventana deslizante
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** mejor_ventana_ventas (variante base). Devuelve suma maxima de ventana consecutiva. Resuelve exactamente el caso indicado.
- **Entrada:** `mejor_ventana([3, 5, 2, 8], 2)`
- **Salida esperada:** `10`
- **Reglas:** Solo ventanas completas. Resuelve exactamente el caso indicado.
- **Pista opcional:** Suma segmentos.

## Ejercicio #0003 (Modulo 009_algoritmos_basicos - #003)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** algoritmos, pares
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** emparejar_entregas (variante base). Forma pares consecutivos con diferencia menor o igual a 5. Resuelve exactamente el caso indicado.
- **Entrada:** `emparejar([10, 12, 30, 34])`
- **Salida esperada:** `[(10, 12), (30, 34)]`
- **Reglas:** La lista viene ordenada. Resuelve exactamente el caso indicado.
- **Pista opcional:** Avanza al siguiente par.

## Ejercicio #0004 (Modulo 009_algoritmos_basicos - #004)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** algoritmos, divisibilidad, fizzbuzz
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** fizz_buzz. Genera una lista de strings del 1 al N reemplazando múltiplos de 3 por "Fizz", de 5 por "Buzz" y de ambos por "FizzBuzz".
- **Entrada:** `n = 15`
- **Salida esperada:** `["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]`
- **Reglas:** Retorna una lista de strings.
- **Pista opcional:** Usa if/elif/else con el operador de módulo %.

## Ejercicio #0005 (Modulo 009_algoritmos_basicos - #005)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** algoritmos, operations a nivel de bits (XOR)
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** encontrar_unico. En una lista donde todos los números se repiten exactamente dos veces excepto uno, encuentra el único que aparece una sola vez.
- **Entrada:** `numeros = [4, 1, 2, 1, 2]`
- **Salida esperada:** `4`
- **Reglas:** Resuelve en tiempo O(N) y espacio O(1).
- **Pista opcional:** La operación XOR (^) de un número consigo mismo es cero.

## Ejercicio #0006 (Modulo 009_algoritmos_basicos - #006)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** algoritmos, primos, criba Eratostenes
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** criba_de_eratostenes. Genera todos los números primos estrictamente menores a N.
- **Entrada:** `n = 20`
- **Salida esperada:** `[2, 3, 5, 7, 11, 13, 17, 19]`
- **Reglas:** Devuelve una lista ordenada ascendentemente.
- **Pista opcional:** Crea un arreglo booleano de tamaño N e inicialízalo en True, marcando progresivamente los múltiplos de los primos encontrados como False.

## Ejercicio #0007 (Modulo 009_algoritmos_basicos - #007)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** algoritmos, pilas, balanceo
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** parentesis_balanceados. Comprueba si un string que contiene paréntesis `()`, corchetes `[]` y llaves `{}` está correctamente balanceado.
- **Entrada:** `cadena = "{[()]}"`
- **Salida esperada:** `True`
- **Reglas:** Los caracteres de apertura deben cerrarse en el orden inverso.
- **Pista opcional:** Usa una lista como pila (stack) agregando aperturas y desapilando al encontrar cierres compatibles.

## Ejercicio #0010 (Modulo 009_algoritmos_basicos - #008)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** algoritmos, intervalos, ordenamiento
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** fusionar_intervalos. Combina una lista de intervalos que se traslapan.
- **Entrada:** `intervalos = [[1, 3], [2, 6], [8, 10], [15, 18]]`
- **Salida esperada:** `[[1, 6], [8, 10], [15, 18]]`
- **Reglas:** El resultado debe venir ordenado por el inicio de cada intervalo.
- **Pista opcional:** Ordena los intervalos por su inicio y luego recórrelos comparando el inicio del actual con el final del anterior fusionado.

## Ejercicio #0009 (Modulo 009_algoritmos_basicos - #009)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** algoritmos, busqueda, diccionarios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** dos_sumas. Encuentra los índices de dos números en una lista desordenada que sumen exactamente un valor objetivo.
- **Entrada:** `numeros = [2, 7, 11, 15]; objetivo = 9`
- **Salida esperada:** `[0, 1]`
- **Reglas:** Resuelve en tiempo O(N) usando almacenamiento auxiliar.
- **Pista opcional:** Guarda en un diccionario cada número visitado y su índice, y busca si su complemento (objetivo - num) ya fue guardado.

## Ejercicio #0010 (Modulo 009_algoritmos_basicos - #010)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** algoritmos, combinaciones, punteros
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** suma_tres_numeros. Determina si existen tres números en una lista que sumen exactamente cero.
- **Entrada:** `numeros = [-1, 0, 1, 2, -1, -4]`
- **Salida esperada:** `[(-1, -1, 2), (-1, 0, 1)]`
- **Reglas:** Devuelve una lista de tuplas únicas ordenadas de menor a mayor.
- **Pista opcional:** Ordena la lista y usa un bucle con dos punteros para los extremos restantes de forma que evites duplicados.

## Ejercicio #0011 (Modulo 009_algoritmos_basicos - #011)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** algoritmos, arreglos, Pascal
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** triangulo_de_pascal. Genera las primeras N filas del Triángulo de Pascal.
- **Entrada:** `filas = 5`
- **Salida esperada:** `[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]`
- **Reglas:** Cada número es la suma de los dos que están directamente encima de él.
- **Pista opcional:** Usa la fila anterior para generar la actual sumando elementos adyacentes.

## Ejercicio #0012 (Modulo 009_algoritmos_basicos - #012)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** algoritmos, conjuntos, secuencias
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** racha_consecutiva_mas_larga. Encuentra la longitud de la secuencia de números consecutivos más larga a partir de una lista desordenada de enteros.
- **Entrada:** `numeros = [100, 4, 200, 1, 3, 2]`
- **Salida esperada:** `4`
- **Reglas:** La secuencia es [1, 2, 3, 4], de longitud 4. Resuelve en tiempo O(N).
- **Pista opcional:** Introduce los números en un set y comprueba si x es el inicio de una secuencia verificando que x-1 no esté en el set.

## Ejercicio #0013 (Modulo 009_algoritmos_basicos - #013)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** algoritmos, matrices, espiral
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** matriz_espiral. Devuelve todos los elementos de una matriz de M x N en orden espiral.
- **Entrada:** `matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
- **Salida esperada:** `[1, 2, 3, 6, 9, 8, 7, 4, 5]`
- **Reglas:** Sigue el sentido de las agujas del reloj.
- **Pista opcional:** Mantén límites para la fila superior, inferior, columna izquierda y derecha, y ve reduciéndolos.

## Ejercicio #0014 (Modulo 009_algoritmos_basicos - #014)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** algoritmos, matrices, rotacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** rotar_matriz_90. Rota una matriz 2D cuadrada (N x N) 90 grados a la derecha (en el sentido de las agujas del reloj) devolviendo una nueva matriz.
- **Entrada:** `matriz = [[1, 2], [3, 4]]`
- **Salida esperada:** `[[3, 1], [4, 2]]`
- **Reglas:** No modifiques la matriz original.
- **Pista opcional:** Transpone la matriz y luego invierte el orden de los elementos en cada fila.

## Ejercicio #0015 (Modulo 009_algoritmos_basicos - #015)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** algoritmos, extremos, multiplicacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** producto_maximo. En una lista de enteros, encuentra el producto máximo que se puede obtener multiplicando dos números de la lista.
- **Entrada:** `numeros = [-10, -3, 5, 6]`
- **Salida esperada:** `30`
- **Reglas:** Ten en cuenta que la multiplicación de dos negativos grandes puede ser el máximo.
- **Pista opcional:** Ordena la lista y compara el producto de los dos menores con el de los dos mayores.

## Ejercicio #0016 (Modulo 009_algoritmos_basicos - #016)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** algoritmos, finanzas, extremos
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** maximo_beneficio. Dado un arreglo de precios de acciones donde el índice representa el día, encuentra el beneficio máximo que se puede obtener comprando y vendiendo una sola acción.
- **Entrada:** `precios = [7, 1, 5, 3, 6, 4]`
- **Salida esperada:** `5`
- **Reglas:** Debes comprar antes de vender. (Comprar a 1 y vender a 6 da beneficio 5).
- **Pista opcional:** Registra el precio mínimo visto y calcula el beneficio potencial de vender al precio del día de hoy.

## Ejercicio #0017 (Modulo 009_algoritmos_basicos - #017)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** algoritmos, strings, distancia Hamming
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** distancia_de_hamming. Calcula la distancia de Hamming entre dos cadenas de texto de igual longitud (número de posiciones en las que los caracteres correspondientes son diferentes).
- **Entrada:** `s1 = "karolin"; s2 = "kathrin"`
- **Salida esperada:** `3`
- **Reglas:** Retorna un entero.
- **Pista opcional:** Itera sobre los caracteres y suma 1 cada vez que s1[i] != s2[i].

## Ejercicio #0018 (Modulo 009_algoritmos_basicos - #018)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** algoritmos, subarreglos, sumas, diccionarios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** subarreglos_suma_k. Cuenta cuántos subarreglos continuos de una lista de enteros suman exactamente un valor K.
- **Entrada:** `numeros = [1, 1, 1]; k = 2`
- **Salida esperada:** `2`
- **Reglas:** Resuelve usando sumas acumuladas y un diccionario para optimizar el tiempo a O(N).
- **Pista opcional:** Guarda la frecuencia de cada suma acumulada obtenida hasta el momento.

## Ejercicio #0019 (Modulo 009_algoritmos_basicos - #019)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** algoritmos, strings, RLE
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** comprimir_string_rle. Comprime un string reemplazando secuencias de caracteres repetidos por el carácter seguido de su cantidad.
- **Entrada:** `texto = "aabcccccaaa"`
- **Salida esperada:** `"a2b1c5a3"`
- **Reglas:** Si el string comprimido no es más corto que el original, devuelve el original.
- **Pista opcional:** Construye el string de salida comparando cada letra con la siguiente en un bucle.

## Ejercicio #0020 (Modulo 009_algoritmos_basicos - #020)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** algoritmos, strings, RLE
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** descompress_string_rle. Descomprime un string comprimido con el formato RLE básico ("c1n1...").
- **Entrada:** `comprimido = "a2b1c5"`
- **Salida esperada:** `"aabbccccc"`
- **Reglas:** Asume que la cantidad de repeticiones es siempre un solo dígito del 1 al 9.
- **Pista opcional:** Itera de dos en dos, multiplicando el carácter por su cantidad.

## Ejercicio #0021 (Modulo 009_algoritmos_basicos - #021)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** algoritmos, matematicas, listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** maximo_comun_divisor_lista. Calcula el Máximo Común Divisor (MCD) de una lista de números enteros.
- **Entrada:** `numeros = [12, 18, 30]`
- **Salida esperada:** `6`
- **Reglas:** La lista contiene al menos dos elementos.
- **Pista opcional:** Calcula el MCD de los dos primeros elementos, y luego el MCD del resultado con el siguiente, sucesivamente.

## Ejercicio #0022 (Modulo 009_algoritmos_basicos - #022)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** algoritmos, enteros, Armstrong
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** es_numero_armstrong. Determina si un número entero positivo es un número de Armstrong (la suma de sus dígitos elevados a la potencia del número total de dígitos es igual al propio número).
- **Entrada:** `numero = 153`
- **Salida esperada:** `True`
- **Reglas:** 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
- **Pista opcional:** Convierte el número a string para obtener el número de dígitos y realizar la suma.
