# Ejercicios - Funciones

Total del modulo: **26 ejercicios**.

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

## Ejercicio #0005 (Modulo 007_funciones - #005)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** funciones, algoritmos, primos
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** es_primo. Determina si un número entero positivo es primo.
- **Entrada:** `es_primo(11)`
- **Salida esperada:** `True`
- **Reglas:** Retorna True o False. Los números menores o iguales a 1 no son primos.
- **Pista opcional:** Itera desde 2 hasta la raíz cuadrada de N para buscar divisores.

## Ejercicio #0006 (Modulo 007_funciones - #006)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** funciones, acumuladores, factorial
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** calcular_factorial. Calcula el factorial de un número entero no negativo de forma iterativa.
- **Entrada:** `calcular_factorial(5)`
- **Salida esperada:** `120`
- **Reglas:** El factorial de 0 es 1.
- **Pista opcional:** Usa un acumulador multiplicativo y un bucle.

## Ejercicio #0007 (Modulo 007_funciones - #007)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** funciones, filtros, listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** filtrar_pares. Filtra los números pares de una lista dada y devuélvelos en una lista nueva.
- **Entrada:** `filtrar_pares([1, 2, 3, 4, 5])`
- **Salida esperada:** `[2, 4]`
- **Reglas:** No utilices comprensiones en este ejercicio para practicar lógica explícita.
- **Pista opcional:** Usa un bucle for tradicional y append().

## Ejercicio #0008 (Modulo 007_funciones - #008)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** funciones, strings, matematicas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** convertir_tiempo. Recibe una cantidad total de segundos y la convierte a una cadena formateada en formato "HH:MM:SS".
- **Entrada:** `convertir_tiempo(3665)`
- **Salida esperada:** `"01:01:05"`
- **Reglas:** Rellena con ceros a la izquierda para garantizar dos dígitos por sección.
- **Pista opcional:** Usa división entera y residuo con 3600 y 60, y formatea con f-strings `:02d`.

## Ejercicio #0009 (Modulo 007_funciones - #009)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** funciones, strings, diccionarios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** contar_letras_digitos. Cuenta el número de caracteres alfabéticos y numéricos en un string.
- **Entrada:** `contar_letras_digitos("Python 3.9")`
- **Salida esperada:** `{"letras": 6, "digitos": 2}`
- **Reglas:** Ignora espacios y signos de puntuación como el punto.
- **Pista opcional:** Usa los métodos isalpha() e isdigit() de los caracteres.

## Ejercicio #0010 (Modulo 007_funciones - #010)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** funciones, argumentos opcionales
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** crear_perfil. Crea un diccionario que represente un perfil de usuario utilizando argumentos con valores por defecto.
- **Entrada:** `crear_perfil("Ana", edad=25)`
- **Salida esperada:** `{"nombre": "Ana", "edad": 25, "rol": "usuario"}`
- **Reglas:** El rol por defecto debe ser "usuario".
- **Pista opcional:** Define en la firma de la función `rol="usuario"`.

## Ejercicio #0011 (Modulo 007_funciones - #011)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** funciones, validaciones, strings
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** validar_contraseña. Comprueba si una contraseña es segura: tiene al menos 8 caracteres, al menos una letra mayúscula, una minúscula y al menos un dígito.
- **Entrada:** `validar_contraseña("Pass1234")`
- **Salida esperada:** `True`
- **Reglas:** Retorna únicamente True o False.
- **Pista opcional:** Itera sobre el string evaluando condiciones con banderas booleanas.

## Ejercicio #0012 (Modulo 007_funciones - #012)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** funciones, impuestos, condicionales
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** calcular_impuestos. Calcula el impuesto progresivo: 0% por los primeros 1000, 10% por el excedente entre 1001 y 5000, y 20% por cualquier excedente sobre 5000.
- **Entrada:** `calcular_impuestos(6000)`
- **Salida esperada:** `600.0`
- **Reglas:** Retorna un float. (10% de 4000 = 400; 20% de 1000 = 200; total = 600).
- **Pista opcional:** Evalúa los tramos en orden restando los umbrales.

## Ejercicio #0013 (Modulo 007_funciones - #013)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** funciones, strings, contadores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** frecuencia_caracter. Cuenta cuántas veces aparece un carácter específico en un texto.
- **Entrada:** `frecuencia_caracter("ingenieria", "i")`
- **Salida esperada:** `2`
- **Reglas:** La búsqueda debe ser sensible a mayúsculas y minúsculas.
- **Pista opcional:** Usa un bucle for o count().

## Ejercicio #0014 (Modulo 007_funciones - #014)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** funciones, listas, alternancia
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** combinar_listas. Combina dos listas alternando sus elementos en una sola.
- **Entrada:** `combinar_listas([1, 2], ["A", "B"])`
- **Salida esperada:** `[1, "A", 2, "B"]`
- **Reglas:** Asume que las listas tienen la misma longitud.
- **Pista opcional:** Usa un bucle por índice.

## Ejercicio #0015 (Modulo 007_funciones - #015)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** funciones, condicionales
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** calcular_bmi. Calcula el Índice de Masa Corporal (peso en kg / altura^2 en metros) y devuelve su clasificación ("bajo", "normal", "sobrepeso").
- **Entrada:** `calcular_bmi(70, 1.75)`
- **Salida esperada:** `"normal"`
- **Reglas:** Clasificaciones: menor a 18.5 ("bajo"), entre 18.5 y 24.9 inclusive ("normal"), mayor a 24.9 ("sobrepeso").
- **Pista opcional:** Realiza la operación aritmética y luego aplica la estructura de control.

## Ejercicio #0016 (Modulo 007_funciones - #016)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** funciones, listas, vecinos
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** encontrar_pico. Devuelve el valor del primer elemento en una lista que es estrictamente mayor que sus vecinos adyacentes inmediatos.
- **Entrada:** `encontrar_pico([1, 2, 5, 3, 4])`
- **Salida esperada:** `5`
- **Reglas:** Si no hay pico, devuelve None. Los extremos no tienen dos vecinos, evalúalos comparando con su vecino directo.
- **Pista opcional:** Recorre por índice y compara con i-1 e i+1.

## Ejercicio #0017 (Modulo 007_funciones - #017)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** funciones, listas, ordenamiento
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** ordenar_por_longitud. Recibe una lista de palabras y las devuelve ordenadas ascendentemente por su cantidad de caracteres.
- **Entrada:** `ordenar_por_longitud(["elefante", "sol", "perro"])`
- **Salida esperada:** `["sol", "perro", "elefante"]`
- **Reglas:** Si hay longitudes iguales, conserva el orden relativo original (estable).
- **Pista opcional:** Usa sorted() pasándole len en la clave key.

## Ejercicio #0018 (Modulo 007_funciones - #018)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** funciones, listas, sublistas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** es_sublista. Determina si todos los elementos de una lista aparecen consecutivamente y en el mismo orden dentro de otra lista.
- **Entrada:** `es_sublista([2, 3], [1, 2, 3, 4])`
- **Salida esperada:** `True`
- **Reglas:** Debe ser exactamente consecutiva.
- **Pista opcional:** Compara subconjuntos de la lista grande usando rebanado (slicing).

## Ejercicio #0019 (Modulo 007_funciones - #019)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** funciones, rangos, bucles
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** generar_rango_personalizado. Simula la función range() devolviendo una lista de números enteros, admitiendo inicio, fin y paso (el cual puede ser negativo).
- **Entrada:** `generar_rango_personalizado(5, 1, -2)`
- **Salida esperada:** `[5, 3]`
- **Reglas:** El valor de fin es exclusivo.
- **Pista opcional:** Usa un bucle while actualizando el valor corriente con el paso.

## Ejercicio #0020 (Modulo 007_funciones - #020)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** funciones, filtros, tipos
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** filtrar_por_tipo. Filtra los elementos de una lista conservando únicamente aquellos que correspondan al tipo de datos especificado en el segundo parámetro.
- **Entrada:** `filtrar_por_tipo([1, "hola", 2, "mundo"], str)`
- **Salida esperada:** `["hola", "mundo"]`
- **Reglas:** Compara tipos directamente usando isinstance() o type().
- **Pista opcional:** isinstance(x, tipo) comprueba si x pertenece a ese tipo.

## Ejercicio #0021 (Modulo 007_funciones - #021)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** funciones, argumentos variables, conjuntos
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** interseccion_multiple. Acepta un número indeterminado de listas usando *args y devuelve una lista con los elementos comunes a todas.
- **Entrada:** `interseccion_multiple([1, 2, 3], [2, 3, 4], [3, 4, 5])`
- **Salida esperada:** `[3]`
- **Reglas:** La lista de salida debe estar ordenada de menor a mayor.
- **Pista opcional:** Convierte cada lista a un set e interseca.

## Ejercicio #0022 (Modulo 007_funciones - #022)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** funciones, callbacks
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** operar_lista. Recibe una lista de números y una función callback que se debe aplicar individualmente sobre cada elemento, retornando los nuevos valores.
- **Entrada:** `operar_lista([1, 2, 3], lambda x: x * 2)`
- **Salida esperada:** `[2, 4, 6]`
- **Reglas:** No modifiques la lista original.
- **Pista opcional:** Itera sobre la lista y llama al callback por cada valor.

## Ejercicio #0023 (Modulo 007_funciones - #023)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** funciones, algoritmos, divisores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** descomponer_cambio. Calcula la menor cantidad de billetes y monedas necesarias para dar el cambio exacto.
- **Entrada:** `descomponer_cambio(250, [100, 50, 20])`
- **Salida esperada:** `{100: 2, 50: 1}`
- **Reglas:** Los valores de billetes/monedas vienen ordenados de mayor a menor. No agregues claves con valor cero a la salida.
- **Pista opcional:** Divide usando la división entera // y actualiza el residuo con el operador %.

## Ejercicio #0024 (Modulo 007_funciones - #024)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** funciones, anagramas, strings
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** es_anagrama. Determina si dos cadenas de caracteres son anagramas (contienen las mismas letras con la misma frecuencia pero en diferente orden).
- **Entrada:** `es_anagrama("roma", "amor")`
- **Salida esperada:** `True`
- **Reglas:** Ignora mayúsculas y minúsculas.
- **Pista opcional:** Ordena los caracteres de cada cadena y compáralos.

## Ejercicio #0025 (Modulo 007_funciones - #025)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** funciones, diccionarios, limpieza
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** limpiar_datos. Normaliza un diccionario de datos eliminando espacios al principio y final de los strings, y descartando registros con valor None o vacíos.
- **Entrada:** `limpiar_datos({"nombre": " Ana ", "edad": None, "ciudad": ""})`
- **Salida esperada:** `{"nombre": "Ana"}`
- **Reglas:** Retorna un nuevo diccionario.
- **Pista opcional:** Usa strip() y evalúa la presencia de valores útiles antes de agregarlos.

## Ejercicio #0026 (Modulo 007_funciones - #026)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** funciones, duplicados, listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** encontrar_duplicados. Devuelve una lista con aquellos elementos que aparecen más de una vez en una lista dada.
- **Entrada:** `encontrar_duplicados([1, 2, 3, 1, 2, 1])`
- **Salida esperada:** `[1, 2]`
- **Reglas:** El orden de la salida debe ser por su primera repetición.
- **Pista opcional:** Usa un set para registrar elementos vistos y otro para duplicados.
