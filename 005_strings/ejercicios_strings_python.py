# ============================================================
# EJERCICIOS DE STRINGS - PYTHON
# Total: 30 ejercicios
#
# Todos los ejercicios están preparados para trabajar
# directamente en un archivo .py.
# ============================================================


# ============================================================
# EJERCICIO #0001
# Nivel: Nivel 1 - Inicial
# Conceptos: strings, lower, upper
#
# Problema:
# Convierte un nombre a minúsculas y después a mayúsculas.
#
# Entrada:
nombre = "Alexander"
#
# Salida esperada:
# "alexander"
# "ALEXANDER"
# ============================================================
salida = (nombre.upper()) + (nombre.lower())
print(salida)

# ============================================================
# EJERCICIO #0002
# Nivel: Nivel 1 - Inicial
# Conceptos: strings, strip, title
#
# Problema:
# Normaliza nombres eliminando espacios externos y poniendo
# cada palabra con la primera letra en mayúscula.
#
# Entrada:
nombres = [" ana ", "LUIS", " marta"]
#
# Salida esperada:
# ["Ana", "Luis", "Marta"]
#
# Pista:
# strip() y title()
# ============================================================


# ============================================================
# EJERCICIO #0003
# Nivel: Nivel 1 - Inicial
# Conceptos: strings, conteo, bucles
#
# Problema:
# Cuenta cuántas vocales tiene un nombre.
#
# Entrada:
nombre = "Eduardo"
#
# Salida esperada:
# 4
# ============================================================


# ============================================================
# EJERCICIO #0004
# Nivel: Nivel 1 - Inicial
# Conceptos: strings, búsqueda
#
# Problema:
# Cuenta cuántas veces aparece una letra determinada.
#
# Entrada:
texto = "banana"
objetivo = "a"
#
# Salida esperada:
# 3
# ============================================================


# ============================================================
# EJERCICIO #0005
# Nivel: Nivel 1 - Inicial
# Conceptos: strings, split, join
#
# Problema:
# Invierte el orden de las palabras de una oración.
#
# Entrada:
oracion = "hola mundo desde python"
#
# Salida esperada:
# "python desde mundo hola"
#
# Regla:
# Mantén un único espacio entre palabras.
# ============================================================


# ============================================================
# EJERCICIO #0006
# Nivel: Nivel 1 - Inicial
# Conceptos: strings, iniciales
#
# Problema:
# Extrae las iniciales de un nombre completo en mayúsculas,
# separadas por puntos.
#
# Entrada:
nombre = "juan carlos sinisterra"
#
# Salida esperada:
# "J.C.S"
# ============================================================


# ============================================================
# EJERCICIO #0007
# Nivel: Nivel 2 - Básico
# Conceptos: strings, replace, slicing
#
# Problema:
# Determina si una frase es palíndroma ignorando espacios
# y mayúsculas.
#
# Entrada:
frase = "Anita lava la tina"
#
# Salida esperada:
# True
# ============================================================


# ============================================================
# EJERCICIO #0008
# Nivel: Nivel 2 - Básico
# Conceptos: strings, replace
#
# Problema:
# Reemplaza una palabra indicada por asteriscos de igual longitud.
#
# Entrada:
texto = "este es un dato secreto"
censura = "secreto"
#
# Salida esperada:
# "este es un dato *******"
# ============================================================


# ============================================================
# EJERCICIO #0009
# Nivel: Nivel 2 - Básico
# Conceptos: strings, split, sets
#
# Problema:
# Extrae los dominios de una lista de correos, elimina duplicados
# y devuelve una lista ordenada.
#
# Entrada:
correos = ["a@mail.com", "b@test.com", "c@mail.com"]
#
# Salida esperada:
# ["mail.com", "test.com"]
# ============================================================


# ============================================================
# EJERCICIO #0010
# Nivel: Nivel 2 - Básico
# Conceptos: strings, validación, endswith
#
# Problema:
# Comprueba si el archivo tiene una extensión permitida,
# ignorando mayúsculas y minúsculas.
#
# Entrada:
archivo = "reporte.PDF"
permitidas = ["jpg", "png", "pdf"]
#
# Salida esperada:
# True
# ============================================================


# ============================================================
# EJERCICIO #0011
# Nivel: Nivel 2 - Básico
# Conceptos: strings, isdigit
#
# Problema:
# Extrae todos los dígitos de un texto y calcula su suma.
#
# Entrada:
texto = "abc12def3"
#
# Salida esperada:
# 6
# ============================================================


# ============================================================
# EJERCICIO #0012
# Nivel: Nivel 2 - Básico
# Conceptos: strings, validación
#
# Problema:
# Filtra placas con tres letras, un guion y tres dígitos.
#
# Entrada:
placas = ["ABC-123", "AB-123", "XYZ-999"]
#
# Salida esperada:
# ["ABC-123", "XYZ-999"]
#
# Regla:
# No uses regex.
# ============================================================


# ============================================================
# EJERCICIO #0013
# Nivel: Nivel 2 - Básico
# Conceptos: strings, find, búsqueda
#
# Problema:
# Devuelve todos los índices iniciales donde aparece una
# subcadena, sin buscar apariciones solapadas.
#
# Entrada:
texto = "hola hola hola"
sub = "hola"
#
# Salida esperada:
# [0, 5, 10]
# ============================================================


# ============================================================
# EJERCICIO #0014
# Nivel: Nivel 2 - Básico
# Conceptos: strings, formateo
#
# Problema:
# Formatea un entero separando miles con comas.
#
# Entrada:
numero = 1234567
#
# Salida esperada:
# "1,234,567"
# ============================================================


# ============================================================
# EJERCICIO #0015
# Nivel: Nivel 2 - Básico
# Conceptos: strings, alineación
#
# Problema:
# Alinea palabras a la derecha con ancho 10 y puntos a la izquierda.
#
# Entrada:
palabras = ["sol", "estrella"]
#
# Salida esperada:
# [".......sol", "..estrella"]
# ============================================================


# ============================================================
# EJERCICIO #0016
# Nivel: Nivel 2 - Básico
# Conceptos: strings, ocultación, slicing
#
# Problema:
# Oculta todos los dígitos de una tarjeta excepto los últimos 4.
#
# Entrada:
tarjeta = "1234567812345678"
#
# Salida esperada:
# "************5678"
# ============================================================


# ============================================================
# EJERCICIO #0017
# Nivel: Nivel 2 - Básico
# Conceptos: strings, validación, correo
#
# Problema:
# Comprueba un formato básico de correo:
# exactamente un @ y un punto después del @.
#
# Entrada:
correo = "hola@dominio.com"
#
# Salida esperada:
# True
#
# Regla:
# No uses regex.
# ============================================================


# ============================================================
# EJERCICIO #0018
# Nivel: Nivel 3 - Práctico
# Conceptos: strings, diccionarios, split
#
# Problema:
# Cuenta códigos por prefijo, usando la parte anterior al guion.
#
# Entrada:
codigos = ["LIB-001", "TEC-002", "LIB-003"]
#
# Salida esperada:
# {"LIB": 2, "TEC": 1}
# ============================================================


# ============================================================
# EJERCICIO #0019
# Nivel: Nivel 3 - Práctico
# Conceptos: strings, normalización, transformación
#
# Problema:
# Convierte CamelCase a snake_case.
#
# Entrada:
texto = "MiClasePython"
#
# Salida esperada:
# "mi_clase_python"
# ============================================================


# ============================================================
# EJERCICIO #0020
# Nivel: Nivel 3 - Práctico
# Conceptos: strings, adyacencia
#
# Problema:
# Reduce letras repetidas de forma consecutiva a una sola.
#
# Entrada:
texto = "aaabbbccc"
#
# Salida esperada:
# "abc"
# ============================================================


# ============================================================
# EJERCICIO #0021
# Nivel: Nivel 3 - Práctico
# Conceptos: strings, rachas, tuplas
#
# Problema:
# Encuentra la mayor racha consecutiva de un carácter.
# Devuelve (carácter, cantidad).
#
# Entrada:
texto = "abbcccdd"
#
# Salida esperada:
# ("c", 3)
# ============================================================


# ============================================================
# EJERCICIO #0022
# Nivel: Nivel 3 - Práctico
# Conceptos: strings, cifrado, ord, chr
#
# Problema:
# Aplica un desplazamiento César de una posición a cada letra
# minúscula. "z" debe convertirse en "a".
#
# Entrada:
texto = "xyz"
#
# Salida esperada:
# "yza"
# ============================================================


# ============================================================
# EJERCICIO #0023
# Nivel: Nivel 3 - Práctico
# Conceptos: strings, recorte, búsqueda
#
# Problema:
# Recorta un texto a un máximo de N caracteres sin cortar palabras
# y agrega "..." cuando sea necesario.
#
# Entrada:
texto = "Python es un gran lenguaje"
limite = 15
#
# Salida esperada:
# "Python es..."
# ============================================================


# ============================================================
# EJERCICIO #0024
# Nivel: Nivel 3 - Práctico
# Conceptos: strings, URLs, normalización
#
# Problema:
# Genera un slug compatible con URL.
#
# Entrada:
titulo = "Hola Mundo! Como Estan?"
#
# Salida esperada:
# "hola-mundo-como-estan"
#
# Regla:
# Elimina signos especiales y evita guiones repetidos.
# ============================================================


# ============================================================
# EJERCICIO #0025
# Nivel: Nivel 4 - Intermedio
# Conceptos: strings, sets, ventana deslizante
#
# Problema:
# Encuentra la longitud de la subcadena continua más larga
# sin caracteres repetidos.
#
# Entrada:
texto = "abcabcbb"
#
# Salida esperada:
# 3
#
# Pista:
# Puedes usar dos punteros y un set.
# ============================================================


# ============================================================
# EJERCICIO #0026
# Nivel: Nivel 4 - Intermedio
# Conceptos: strings, conversión, bucles
#
# Problema:
# Convierte un entero positivo a binario sin usar bin().
#
# Entrada:
numero = 10
#
# Salida esperada:
# "1010"
# ============================================================


# ============================================================
# EJERCICIO #0027
# Nivel: Nivel 4 - Intermedio
# Conceptos: strings, validación, IPv4
#
# Problema:
# Comprueba si un string representa una IPv4 válida.
#
# Entrada:
ip = "192.168.1.1"
#
# Salida esperada:
# True
#
# Reglas:
# - cuatro bloques
# - cada bloque entre 0 y 255
# - "01" es inválido
# - no uses regex
# ============================================================


# ============================================================
# EJERCICIO #0028
# Nivel: Nivel 4 - Intermedio
# Conceptos: strings, validación, contraseñas
#
# Problema:
# Valida una contraseña:
# - mínimo 8 caracteres
# - una mayúscula
# - una minúscula
# - un dígito
#
# Entrada:
contrasena = "Python2026"
#
# Salida esperada:
# True
# ============================================================


# ============================================================
# EJERCICIO #0029
# Nivel: Nivel 4 - Intermedio
# Conceptos: strings, frecuencia, diccionarios
#
# Problema:
# Encuentra la primera palabra que aparece exactamente una vez.
#
# Entrada:
frase = "hola mundo hola python mundo codigo"
#
# Salida esperada:
# "python"
# ============================================================


# ============================================================
# EJERCICIO #0030
# Nivel: Nivel 5 - Integrador
# Conceptos: strings, listas, diccionarios, validación
#
# Problema:
# Procesa nombres de usuario:
# - elimina espacios externos
# - pasa a minúsculas
# - válido si tiene entre 5 y 12 caracteres
# - sólo letras, números o "_"
#
# Entrada:
usuarios = [
    "  Alexander ",
    "ana_123",
    " Luis!! ",
    "marta22",
    "abc"
]
#
# Salida esperada:
# {
#     "validos": ["alexander", "ana_123", "marta22"],
#     "invalidos": ["luis!!", "abc"]
# }
#
# Regla:
# Conserva el orden original.
# ============================================================


# ============================================================
# FIN DEL MODULO
#
# PATRONES IMPORTANTES:
#
# NORMALIZAR
#     strip(), lower(), upper(), title()
#
# SEPARAR
#     split()
#
# UNIR
#     join()
#
# REEMPLAZAR
#     replace()
#
# BUSCAR
#     in, find(), startswith(), endswith()
#
# VALIDAR
#     isalpha(), isdigit(), isalnum(), isupper(), islower()
#
# RECORRER
#     for caracter in texto
#
# CONTAR / ACUMULAR
#     contador += 1
#     total += valor
#
# INVERTIR
#     [::-1]
#
# ORDENAR
#     sorted()
#
# CONJUNTOS
#     set()
#
# FORMATEAR
#     f-strings, rjust()
#
# ============================================================
#
# No busques memorizar cada método.
# Busca reconocer qué problema tienes y qué herramienta encaja.
# ============================================================
