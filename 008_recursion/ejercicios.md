# Ejercicios - Recursion

Total del modulo: **16 ejercicios**.

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

## Ejercicio #0004 (Modulo 008_recursion - #004)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** recursion, matematicas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** factorial_recursivo. Calcula el factorial de un número de forma recursiva.
- **Entrada:** `factorial(4)`
- **Salida esperada:** `24`
- **Reglas:** Caso base: factorial(0) = 1.
- **Pista opcional:** N * factorial(N-1).

## Ejercicio #0005 (Modulo 008_recursion - #005)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** recursion, secuencias
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** fibonacci_recursivo. Devuelve el N-ésimo término de la sucesión de Fibonacci de forma recursiva.
- **Entrada:** `fibonacci(6)`
- **Salida esperada:** `8`
- **Reglas:** Considera fibonacci(0) = 0 y fibonacci(1) = 1.
- **Pista opcional:** F(N) = F(N-1) + F(N-2).

## Ejercicio #0006 (Modulo 008_recursion - #006)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** recursion, listas, acumuladores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** suma_lista_recursiva. Calcula la suma de todos los números de una lista sin utilizar bucles.
- **Entrada:** `suma([1, 2, 3, 4])`
- **Salida esperada:** `10`
- **Reglas:** Si la lista está vacía, la suma es 0.
- **Pista opcional:** Toma el primer elemento y súmalo al resultado de llamar a la función con el resto de la lista.

## Ejercicio #0007 (Modulo 008_recursion - #007)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** recursion, strings
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** invertir_cadena. Invierte un string de forma recursiva.
- **Entrada:** `invertir("hola")`
- **Salida esperada:** `"aloh"`
- **Reglas:** Caso base: cadena vacía o de longitud 1.
- **Pista opcional:** Retorna el último carácter sumado a la inversión del resto de la cadena.

## Ejercicio #0008 (Modulo 008_recursion - #008)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** recursion, enteros
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** contar_digitos. Cuenta la cantidad de dígitos de un número entero positivo de forma recursiva.
- **Entrada:** `contar_digitos(12345)`
- **Salida esperada:** `5`
- **Reglas:** Caso base: el número es menor a 10.
- **Pista opcional:** 1 + contar_digitos(N // 10).

## Ejercicio #0009 (Modulo 008_recursion - #009)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** recursion, matematicas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** potencia_recursiva. Calcula la potencia A^B (A elevado a B) de forma recursiva, asumiendo B >= 0.
- **Entrada:** `potencia(2, 3)`
- **Salida esperada:** `8`
- **Reglas:** Caso base: potencia(A, 0) = 1.
- **Pista opcional:** A * potencia(A, B-1).

## Ejercicio #0010 (Modulo 008_recursion - #010)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** recursion, matematicas, algoritmo Euclides
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** maximo_comun_divisor. Encuentra el MCD de dos números usando el algoritmo de Euclides de forma recursiva.
- **Entrada:** `mcd(48, 18)`
- **Salida esperada:** `6`
- **Reglas:** MCD(a, b) = MCD(b, a % b). Caso base: b = 0.
- **Pista opcional:** Si b es cero, la respuesta es a.

## Ejercicio #0011 (Modulo 008_recursion - #011)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** recursion, listas, busqueda
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** buscar_recursivo. Comprueba si un valor objetivo se encuentra dentro de una lista usando recursión.
- **Entrada:** `buscar([10, 20, 30, 40], 30)`
- **Salida esperada:** `True`
- **Reglas:** No utilices el operador in directamente en el cuerpo principal del código.
- **Pista opcional:** Si la lista está vacía, devuelve False. Si el primer elemento es el objetivo, devuelve True. Si no, busca en el resto.

## Ejercicio #0012 (Modulo 008_recursion - #012)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** recursion, strings, palindromos
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** es_palindromo_recursivo. Determina si una palabra es palíndroma usando lógica recursiva.
- **Entrada:** `es_palindromo("radar")`
- **Salida esperada:** `True`
- **Reglas:** Caso base: longitud menor o igual a 1.
- **Pista opcional:** Compara el primer y último carácter. Si coinciden, llama recursivamente con la subcadena central.

## Ejercicio #0013 (Modulo 008_recursion - #013)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** recursion, arboles, conteo
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** contar_hojas. Cuenta la cantidad de nodos hoja (nodos que no tienen hijos o cuya lista "sub" está vacía) en un árbol de partidas.
- **Entrada:** `contar_hojas({"puntos":5,"sub":[{"puntos":3,"sub":[]},{"puntos":2,"sub":[]}]})`
- **Salida esperada:** `2`
- **Reglas:** Si el nodo no tiene subnodos, es una hoja y cuenta como 1.
- **Pista opcional:** Suma los resultados de llamar recursivamente a cada subnodo si existen.

## Ejercicio #0014 (Modulo 008_recursion - #014)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** recursion, strings, permutaciones
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** generar_permutaciones. Genera una lista con todas las permutaciones posibles de las letras de un string (sin duplicar si las letras son únicas).
- **Entrada:** `permutaciones("abc")`
- **Salida esperada:** `["abc", "acb", "bac", "bca", "cab", "cba"]`
- **Reglas:** La lista de salida debe estar ordenada alfabéticamente.
- **Pista opcional:** Extrae un carácter y genera las permutaciones del resto, luego inserta el carácter en cada posición.

## Ejercicio #0015 (Modulo 008_recursion - #015)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** recursion, enteros, acumuladores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** suma_digitos. Calcula la suma de todos los dígitos de un número entero positivo de forma recursiva.
- **Entrada:** `suma_digitos(456)`
- **Salida esperada:** `15`
- **Reglas:** Caso base: número menor a 10.
- **Pista opcional:** N % 10 + suma_digitos(N // 10).

## Ejercicio #0016 (Modulo 008_recursion - #016)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** recursion, diccionarios, anidamiento
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** profundidad_maxima. Encuentra el nivel máximo de anidamiento de un diccionario.
- **Entrada:** `profundidad({"a": 1, "b": {"c": {"d": 2}}})`
- **Salida esperada:** `3`
- **Reglas:** Un diccionario plano sin subdiccionarios tiene profundidad 1.
- **Pista opcional:** Si el valor de una llave es un diccionario, calcula su profundidad de manera recursiva sumando 1, y quédate con el máximo.
