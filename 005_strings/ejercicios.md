# Ejercicios - Strings

Total del modulo: **26 ejercicios**.

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

## Ejercicio #0005 (Modulo 005_strings - #005)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** strings, reemplazo
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Censurar palabras. Reemplaza palabras ofensivas o restringidas en un texto por asteriscos de igual longitud.
- **Entrada:** `texto = "este es un dato secreto"; censura = "secreto"`
- **Salida esperada:** `"este es un dato *******"`
- **Reglas:** El reemplazo debe coincidir exactamente en cantidad de caracteres.
- **Pista opcional:** Usa el método replace() y el operador * para repetir caracteres.

## Ejercicio #0006 (Modulo 005_strings - #006)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** strings, conteo, bucles
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Contar vocales en un nombre. Cuenta cuántas vocales tiene un nombre de usuario (mayúsculas o minúsculas).
- **Entrada:** `nombre = "Eduardo"`
- **Salida esperada:** `4`
- **Reglas:** Las vocales son a, e, i, o, u.
- **Pista opcional:** Convierte a minúsculas y verifica si cada letra está en "aeiou".

## Ejercicio #0007 (Modulo 005_strings - #007)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** strings, palindromos
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Palindromo ignorando espacios. Determina si una frase se lee igual en ambas direcciones, ignorando espacios y mayúsculas.
- **Entrada:** `frase = "Anita lava la tina"`
- **Salida esperada:** `True`
- **Reglas:** Convierte a minúsculas y elimina espacios antes de evaluar.
- **Pista opcional:** Usa replace(" ", "") y rebanado [::-1] para invertir.

## Ejercicio #0008 (Modulo 005_strings - #008)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** strings, inversion, split
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Invertir orden de palabras. Invierte el orden de las palabras de una oración sin alterar los caracteres de las palabras individuales.
- **Entrada:** `oracion = "hola mundo desde python"`
- **Salida esperada:** `"python desde mundo hola"`
- **Reglas:** Mantén un único espacio entre palabras.
- **Pista opcional:** Divide con split(), invierte la lista resultante y une con join().

## Ejercicio #0009 (Modulo 005_strings - #009)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** strings, formateo, iniciales
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Obtener iniciales. Extrae las iniciales de un nombre completo y devuélvelas en mayúsculas unidas por puntos.
- **Entrada:** `nombre = "juan carlos sinisterra"`
- **Salida esperada:** `"J.C.S"`
- **Reglas:** Elimina espacios adicionales al principio o final si existen.
- **Pista opcional:** Split por espacios y toma el primer carácter en mayúsculas de cada parte.

## Ejercicio #0010 (Modulo 005_strings - #010)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** strings, validaciones
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Verificar extension de archivo. Comprueba si un nombre de archivo termina en una extensión permitida de una lista de opciones.
- **Entrada:** `archivo = "reporte.pdf"; permitidas = ["jpg", "png", "pdf"]`
- **Salida esperada:** `True`
- **Reglas:** La comparación debe ser insensible a mayúsculas y minúsculas.
- **Pista opcional:** split(".")[-1] o endswith() pueden ayudarte.

## Ejercicio #0011 (Modulo 005_strings - #011)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** strings, formateo
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Formatear numeros con miles. Convierte un número entero en un string separado por comas cada tres dígitos sin utilizar librerías.
- **Entrada:** `numero = 1234567`
- **Salida esperada:** `"1,234,567"`
- **Reglas:** Retorna un string formateado.
- **Pista opcional:** Procesa el número de atrás hacia adelante o usa la especificación de formato de Python `f"{numero:,}"`.

## Ejercicio #0012 (Modulo 005_strings - #012)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** strings, normalizacion, transformacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** CamelCase a snake_case. Convierte un string de formato CamelCase (usado en nombres de clases) a snake_case (usado en funciones).
- **Entrada:** `texto = "MiClasePython"`
- **Salida esperada:** `"mi_clase_python"`
- **Reglas:** Inserta un guion bajo antes de cada mayúscula interna y pasa todo a minúsculas.
- **Pista opcional:** Itera caracter por caracter evaluando isupper().

## Ejercicio #0013 (Modulo 005_strings - #013)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** strings, contadores, adyacencia
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Mayor racha consecutiva de caracteres. Encuentra qué carácter se repite consecutivamente la mayor cantidad de veces y devuelve una tupla con (carácter, cantidad).
- **Entrada:** `texto = "abbcccdd"`
- **Salida esperada:** `("c", 3)`
- **Reglas:** Si hay empates, devuelve el primero en alcanzar la racha máxima.
- **Pista opcional:** Recorre el string comparando cada carácter con el anterior.

## Ejercicio #0014 (Modulo 005_strings - #014)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** strings, ocultacion, seguridad
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Ocultar numero de tarjeta. Oculta todos los dígitos de una tarjeta de crédito excepto los últimos 4 dígitos, reemplazándolos con asteriscos.
- **Entrada:** `tarjeta = "1234567812345678"`
- **Salida esperada:** `"************5678"`
- **Reglas:** La salida debe conservar la misma longitud.
- **Pista opcional:** Multiplica "*" por len(tarjeta) - 4 y concatena con tarjeta[-4:].

## Ejercicio #0015 (Modulo 005_strings - #015)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** strings, busqueda, enteros
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Extraer y sumar digitos. Encuentra todos los caracteres numéricos dentro de un string y calcula su suma total.
- **Entrada:** `texto = "abc12def3"`
- **Salida esperada:** `6`
- **Reglas:** Suma cada dígito por separado: 1 + 2 + 3 = 6.
- **Pista opcional:** Itera sobre el string y verifica con isdigit().

## Ejercicio #0016 (Modulo 005_strings - #016)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** strings, validaciones, correo
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Validar correo simple. Comprueba si un string tiene el formato básico de un correo: contiene exactamente un carácter `@`, y al menos un punto `.` después del `@`.
- **Entrada:** `correo = "hola@dominio.com"`
- **Salida esperada:** `True`
- **Reglas:** No uses expresiones regulares (regex).
- **Pista opcional:** Divide por `@` y luego evalúa la segunda mitad.

## Ejercicio #0017 (Modulo 005_strings - #017)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** strings, cifrado
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Cifrado Cesar simple. Desplaza cada letra minúscula en el string una posición adelante en el abecedario circular (la 'z' pasa a ser 'a').
- **Entrada:** `texto = "xyz"`
- **Salida esperada:** `"yza"`
- **Reglas:** Mantén caracteres no alfabéticos sin cambios.
- **Pista opcional:** Usa ord() y chr() sobre los caracteres correspondientes.

## Ejercicio #0018 (Modulo 005_strings - #018)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** strings, formateo, alineacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Alinear a la derecha. Formatea una lista de palabras para que queden alineadas a la derecha con un ancho fijo de 10 caracteres, rellenando con puntos a la izquierda.
- **Entrada:** `palabras = ["sol", "estrella"]`
- **Salida esperada:** `[".......sol", "..estrella"]`
- **Reglas:** Cada palabra resultante debe tener exactamente longitud 10.
- **Pista opcional:** El método rjust() o f-strings permiten alineación y relleno.

## Ejercicio #0019 (Modulo 005_strings - #019)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** strings, duplicados, adyacencia
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Reducir duplicados adyacentes. Reduce letras repetidas de forma consecutiva a un solo carácter.
- **Entrada:** `texto = "aaabbbccc"`
- **Salida esperada:** `"abc"`
- **Reglas:** Conserva el orden original.
- **Pista opcional:** Agrega el carácter a la salida sólo si es diferente al último agregado.

## Ejercicio #0020 (Modulo 005_strings - #020)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** strings, conjuntos, busqueda
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Subcadena sin repetir mas larga. Encuentra la longitud de la subcadena continua más larga que no contenga caracteres repetidos.
- **Entrada:** `texto = "abcabcbb"`
- **Salida esperada:** `3`
- **Reglas:** La subcadena más larga es "abc", de longitud 3.
- **Pista opcional:** Usa dos punteros (ventana deslizante) y un conjunto para realizar el seguimiento de vistos.

## Ejercicio #0021 (Modulo 005_strings - #021)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** strings, division, conteo
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Contar oraciones. Cuenta cuántas oraciones hay en un párrafo asumiendo que terminan únicamente con un punto.
- **Entrada:** `parrafo = "El sol brilla. Hace calor. El dia es hermoso."`
- **Salida esperada:** `3`
- **Reglas:** Ignora el último punto si termina en espacio o está vacío.
- **Pista opcional:** Cuenta las ocurrencias de "." limpiando espacios al final.

## Ejercicio #0022 (Modulo 005_strings - #022)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** strings, conversion, bucles
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Representacion binaria manual. Convierte un número entero positivo en su representación binaria en string sin usar bin().
- **Entrada:** `numero = 10`
- **Salida esperada:** `"1010"`
- **Reglas:** Retorna un string.
- **Pista opcional:** Divide sucesivamente entre 2 y acumula los residuos al revés.

## Ejercicio #0023 (Modulo 005_strings - #023)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** strings, recorte, formato
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Recortar por palabras. Recorta un texto a un máximo de N caracteres de manera limpia, sin cortar palabras a la mitad, agregando "..." al final.
- **Entrada:** `texto = "Python es un gran lenguaje"; limite = 15`
- **Salida esperada:** `"Python es..."`
- **Reglas:** Si el texto ya es más corto que el límite, devuélvelo intacto.
- **Pista opcional:** Corta en el límite y luego retrocede hasta el último espacio.

## Ejercicio #0024 (Modulo 005_strings - #024)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** strings, indices, busqueda
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Encontrar todos los indices. Devuelve una lista con todos los índices iniciales donde aparece una subcadena en un texto.
- **Entrada:** `texto = "hola hola hola"; sub = "hola"`
- **Salida esperada:** `[0, 5, 10]`
- **Reglas:** Busca de forma no solapada en este caso.
- **Pista opcional:** Usa find() indicando el punto de inicio para avanzar.

## Ejercicio #0025 (Modulo 005_strings - #025)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** strings, URLs, normalizacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Generar slug para URLs. Convierte un título en una cadena compatible con URLs: en minúsculas, reemplazando espacios con guiones y eliminando signos especiales.
- **Entrada:** `titulo = "Hola Mundo! Como Estan?"`
- **Salida esperada:** `"hola-mundo-como-estan"`
- **Reglas:** Elimina caracteres como !, ?, , y puntos.
- **Pista opcional:** Filtra letras/números y espacios, reemplaza espacios por guiones simples.

## Ejercicio #0026 (Modulo 005_strings - #026)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** strings, validaciones, IP
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Validar direccion IPv4. Comprueba si un string representa una dirección IPv4 válida (cuatro bloques de números de 0 a 255 separados por puntos).
- **Entrada:** `ip = "192.168.1.1"`
- **Salida esperada:** `True`
- **Reglas:** Cada bloque no debe tener ceros a la izquierda (ej. "01" es inválido) y debe ser entero. No uses regex.
- **Pista opcional:** Divide con split(".") y valida longitud y rango de cada parte.
