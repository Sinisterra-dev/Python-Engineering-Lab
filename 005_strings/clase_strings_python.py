# ============================================================
# CLASE DE STRINGS EN PYTHON
# De cero a resolver ejercicios del módulo
# ============================================================
#
# OBJETIVO:
# Entender cómo funcionan los strings y reconocer qué herramienta
# usar según el problema.
#
# Pregúntate:
# ¿Necesito limpiar, separar, unir, buscar, validar, contar
# o transformar este texto?
# ============================================================


# ============================================================
# 1. ¿QUÉ ES UN STRING?
# ============================================================
nombre = "Alexander"
correo = "alex@example.com"
codigo = "LIB-001"

print(nombre)
print(correo)
print(codigo)


# ============================================================
# 2. ÍNDICES
# ============================================================
# texto = "Hola!"
#          01234
#
# -1 es el último carácter.

texto = "Hola!"
print(texto[0])   # H
print(texto[1])   # o
print(texto[-1])  # !


# ============================================================
# 3. len()
# ============================================================
texto = "Python"
print(len(texto))


# ============================================================
# 4. RECORRER UN STRING
# ============================================================
texto = "Python"

for caracter in texto:
    print(caracter)


# ============================================================
# 5. in Y not in
# ============================================================
texto = "Python"

print("P" in texto)
print("z" in texto)
print("x" not in texto)


# ============================================================
# 6. lower(), upper() Y title()
# ============================================================
texto = "pYtHoN"

print(texto.lower())
print(texto.upper())
print(texto.title())


# ============================================================
# 7. strip()
# ============================================================
# Elimina espacios al inicio y al final.

texto = "   Ana   "
print(texto.strip())


# ============================================================
# 8. NORMALIZAR TEXTO
# ============================================================
nombre = "  lUIS  "

limpio = nombre.strip().title()

print(limpio)


# ============================================================
# 9. replace()
# ============================================================
texto = "Hola mundo"

nuevo = texto.replace("mundo", "Python")

print(nuevo)


# ============================================================
# 10. CENSURAR UNA PALABRA
# ============================================================
texto = "este es un dato secreto"
palabra = "secreto"

asteriscos = "*" * len(palabra)
resultado = texto.replace(palabra, asteriscos)

print(resultado)


# ============================================================
# 11. split()
# ============================================================
# Convierte un string en una lista.

frase = "hola mundo desde python"

palabras = frase.split()

print(palabras)


# ============================================================
# 12. split() CON SEPARADOR
# ============================================================
correo = "ana@gmail.com"

partes = correo.split("@")

print(partes)


# ============================================================
# 13. EXTRAER EL DOMINIO DE UN CORREO
# ============================================================
correo = "ana@gmail.com"

dominio = correo.split("@")[1]

print(dominio)


# ============================================================
# 14. SEPARAR UN CÓDIGO
# ============================================================
codigo = "LIB-001"

partes = codigo.split("-")
prefijo = partes[0]

print(prefijo)


# ============================================================
# 15. join()
# ============================================================
# split(): string -> lista
# join(): lista -> string

palabras = ["hola", "mundo", "python"]

frase = " ".join(palabras)

print(frase)


# ============================================================
# 16. join() CON GUIONES
# ============================================================
palabras = ["hola", "mundo", "python"]

slug = "-".join(palabras)

print(slug)


# ============================================================
# 17. SLICING
# ============================================================
# texto[inicio:fin]
#
# inicio se incluye.
# fin NO se incluye.

texto = "abcdef"

print(texto[1:4])  # bcd
print(texto[:3])   # abc
print(texto[2:])   # cdef
print(texto[-4:])  # cdef


# ============================================================
# 18. INVERTIR UN STRING
# ============================================================
# [::-1] recorre desde el final hasta el inicio.

texto = "python"

invertido = texto[::-1]

print(invertido)


# ============================================================
# 19. PALÍNDROMOS
# ============================================================
# 1. normalizar
# 2. eliminar espacios si corresponde
# 3. invertir
# 4. comparar

frase = "Anita lava la tina"

limpia = frase.lower().replace(" ", "")

es_palindromo = limpia == limpia[::-1]

print(es_palindromo)


# ============================================================
# 20. ÚLTIMOS 4 CARACTERES
# ============================================================
tarjeta = "1234567812345678"

ultimos = tarjeta[-4:]

print(ultimos)


# ============================================================
# 21. OCULTAR DATOS
# ============================================================
tarjeta = "1234567812345678"

resultado = "*" * (len(tarjeta) - 4) + tarjeta[-4:]

print(resultado)


# ============================================================
# 22. startswith() Y endswith()
# ============================================================
archivo = "reporte.PDF"

print(archivo.lower().endswith(".pdf"))
print(archivo.lower().startswith("rep"))


# ============================================================
# 23. find()
# ============================================================
# Si no encuentra devuelve -1.

texto = "hola mundo"

posicion = texto.find("mundo")

print(posicion)


# ============================================================
# 24. BUSCAR TODAS LAS APARICIONES
# ============================================================
# while permite seguir buscando hasta obtener -1.

texto = "hola hola hola"
sub = "hola"

indices = []
inicio = 0

while True:
    posicion = texto.find(sub, inicio)

    if posicion == -1:
        break

    indices.append(posicion)
    inicio = posicion + len(sub)

print(indices)


# ============================================================
# 25. isalpha()
# ============================================================
print("Hola".isalpha())
print("Hola123".isalpha())


# ============================================================
# 26. isdigit()
# ============================================================
print("12345".isdigit())
print("123a".isdigit())


# ============================================================
# 27. isalnum()
# ============================================================
print("Python2026".isalnum())
print("Python 2026".isalnum())


# ============================================================
# 28. isupper() E islower()
# ============================================================
print("PYTHON".isupper())
print("python".islower())


# ============================================================
# 29. CONTAR VOCALES
# ============================================================
nombre = "Eduardo"

vocales = "aeiou"
contador = 0

for caracter in nombre.lower():
    if caracter in vocales:
        contador += 1

print(contador)


# ============================================================
# 30. EXTRAER Y SUMAR DÍGITOS
# ============================================================
texto = "abc12def3"

suma = 0

for caracter in texto:
    if caracter.isdigit():
        suma += int(caracter)

print(suma)


# ============================================================
# 31. FRECUENCIA DE CARACTERES
# ============================================================
# Combina strings + diccionarios.

texto = "banana"

frecuencia = {}

for caracter in texto:
    if caracter not in frecuencia:
        frecuencia[caracter] = 1
    else:
        frecuencia[caracter] += 1

print(frecuencia)


# ============================================================
# 32. FRECUENCIA CON get()
# ============================================================
texto = "banana"

frecuencia = {}

for caracter in texto:
    frecuencia[caracter] = frecuencia.get(caracter, 0) + 1

print(frecuencia)


# ============================================================
# 33. FRECUENCIA DE PALABRAS
# ============================================================
frase = "python es bueno y python es util"

palabras = frase.split()
frecuencia = {}

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print(frecuencia)


# ============================================================
# 34. STRINGS + SETS
# ============================================================
# set() elimina elementos repetidos.

texto = "banana"

letras_unicas = set(texto)

print(letras_unicas)


# ============================================================
# 35. NORMALIZAR ANTES DE CONTAR
# ============================================================
frase = "Python python PYTHON"

palabras = frase.lower().split()
frecuencia = {}

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print(frecuencia)


# ============================================================
# 36. CONTAR CÓDIGOS POR PREFIJO
# ============================================================
codigos = ["LIB-001", "TEC-002", "LIB-003"]

conteo = {}

for codigo in codigos:
    prefijo = codigo.split("-")[0]
    conteo[prefijo] = conteo.get(prefijo, 0) + 1

print(conteo)


# ============================================================
# 37. VALIDAR PLACA SIN REGEX
# ============================================================
# Formato esperado: ABC-123

placa = "ABC-123"

partes = placa.split("-")

valida = (
    len(partes) == 2
    and len(partes[0]) == 3
    and len(partes[1]) == 3
    and partes[0].isalpha()
    and partes[1].isdigit()
)

print(valida)


# ============================================================
# 38. VALIDAR CORREO BÁSICO SIN REGEX
# ============================================================
correo = "hola@dominio.com"

partes = correo.split("@")

valido = (
    len(partes) == 2
    and partes[0] != ""
    and partes[1] != ""
    and "." in partes[1]
)

print(valido)


# ============================================================
# 39. CamelCase -> snake_case
# ============================================================
# MiClasePython -> mi_clase_python

texto = "MiClasePython"

resultado = ""

for caracter in texto:
    if caracter.isupper() and resultado:
        resultado += "_"

    resultado += caracter.lower()

print(resultado)


# ============================================================
# 40. REDUCIR DUPLICADOS CONSECUTIVOS
# ============================================================
# aaabbbccc -> abc

texto = "aaabbbccc"

resultado = ""

for caracter in texto:
    if not resultado or caracter != resultado[-1]:
        resultado += caracter

print(resultado)


# ============================================================
# 41. MAYOR RACHA DE UN CARÁCTER
# ============================================================
# abbcccdd -> ("c", 3)

texto = "abbcccdd"

racha_actual = 1
max_racha = 1
mejor_caracter = texto[0]

for i in range(1, len(texto)):
    if texto[i] == texto[i - 1]:
        racha_actual += 1
    else:
        racha_actual = 1

    if racha_actual > max_racha:
        max_racha = racha_actual
        mejor_caracter = texto[i]

resultado = (mejor_caracter, max_racha)

print(resultado)


# ============================================================
# 42. FORMATEAR NÚMEROS
# ============================================================
numero = 1234567

print(f"{numero:,}")


# ============================================================
# 43. ALINEAR TEXTO
# ============================================================
palabra = "sol"

print(palabra.rjust(10, "."))
print(palabra.ljust(10, "."))
print(palabra.center(10, "."))


# ============================================================
# 44. RECORTAR SIN CORTAR UNA PALABRA
# ============================================================
texto = "Python es un gran lenguaje"
limite = 15

if len(texto) <= limite:
    resultado = texto
else:
    corte = texto[:limite]
    ultimo_espacio = corte.rfind(" ")

    if ultimo_espacio == -1:
        resultado = "..."
    else:
        resultado = corte[:ultimo_espacio] + "..."

print(resultado)


# ============================================================
# 45. GENERAR UN SLUG PARA URL
# ============================================================
# Hola Mundo! Como Estan?
# -> hola-mundo-como-estan

titulo = "Hola Mundo! Como Estan?"

titulo = titulo.lower()
caracteres = []

for caracter in titulo:
    if caracter.isalnum():
        caracteres.append(caracter)
    elif caracter.isspace():
        caracteres.append("-")

slug = "".join(caracteres)

while "--" in slug:
    slug = slug.replace("--", "-")

slug = slug.strip("-")

print(slug)


# ============================================================
# 46. CIFRADO CÉSAR SIMPLE
# ============================================================
# xyz -> yza
#
# ord(): carácter -> número
# chr(): número -> carácter

texto = "xyz"

resultado = ""

for caracter in texto:
    if "a" <= caracter <= "z":
        posicion = ord(caracter) - ord("a")
        nueva_posicion = (posicion + 1) % 26
        resultado += chr(ord("a") + nueva_posicion)
    else:
        resultado += caracter

print(resultado)


# ============================================================
# 47. VALIDAR IPv4 SIN REGEX
# ============================================================
ip = "192.168.1.1"

partes = ip.split(".")

valida = len(partes) == 4

if valida:
    for parte in partes:
        if not parte.isdigit():
            valida = False
            break

        if len(parte) > 1 and parte[0] == "0":
            valida = False
            break

        if not 0 <= int(parte) <= 255:
            valida = False
            break

print(valida)


# ============================================================
# 48. VALIDAR CONTRASEÑA
# ============================================================
# Requisitos:
# - mínimo 8 caracteres
# - una mayúscula
# - una minúscula
# - un dígito

contrasena = "Python2026"

tiene_mayuscula = False
tiene_minuscula = False
tiene_digito = False

for caracter in contrasena:
    if caracter.isupper():
        tiene_mayuscula = True
    elif caracter.islower():
        tiene_minuscula = True
    elif caracter.isdigit():
        tiene_digito = True

valida = (
    len(contrasena) >= 8
    and tiene_mayuscula
    and tiene_minuscula
    and tiene_digito
)

print(valida)


# ============================================================
# 49. PRIMERA PALABRA CON FRECUENCIA 1
# ============================================================
frase = "hola mundo hola python mundo codigo"

palabras = frase.split()
frecuencia = {}

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

primera_unica = None

for palabra in palabras:
    if frecuencia[palabra] == 1:
        primera_unica = palabra
        break

print(primera_unica)


# ============================================================
# 50. MAPA MENTAL PARA RESOLVER EJERCICIOS
# ============================================================
#
# "limpiar texto"              -> strip()
# "ignorar mayúsculas"         -> lower()
# "separar"                    -> split()
# "unir"                       -> join()
# "reemplazar"                 -> replace()
# "buscar"                     -> in / find()
# "empieza con"                -> startswith()
# "termina con"                -> endswith()
# "son letras"                 -> isalpha()
# "son números"                -> isdigit()
# "letras y números"           -> isalnum()
# "invertir"                   -> [::-1]
# "últimos N caracteres"       -> texto[-N:]
# "contar"                     -> contador o diccionario
# "eliminar duplicados"        -> set()
# "validar formato"            -> split() + condiciones
# "comparar consecutivos"      -> texto[i] y texto[i - 1]
# ============================================================


# ============================================================
# RECOMENDACIONES
# ============================================================
#
# 1. No memorices código completo.
#
# Ejemplo:
# "Necesito separar por @"
# -> pienso en split("@")
#
# 2. Divide los problemas grandes.
#
# Por ejemplo IPv4:
# - separar
# - comprobar cantidad
# - recorrer bloques
# - validar cada bloque
#
# 3. Prueba casos diferentes:
# ""
# "aaaa"
# "Python"
# "123"
#
# 4. Cuando te bloquees, escribe:
#
# # ¿Qué tengo?
# # ¿Qué necesito?
# # ¿Qué transformación necesito?
#
# ============================================================


# ============================================================
# RETO FINAL
# ============================================================
#
# Procesa estos usuarios:
#
usuarios = [
    "  Alexander ",
    "ANA_123",
    " Luis!! ",
    "marta22",
    "abc"
]
#
# Debes:
# 1. Eliminar espacios externos.
# 2. Convertir a minúsculas.
# 3. Validar que tenga entre 5 y 12 caracteres.
# 4. Sólo puede contener letras, números o "_".
#
# Construye:
#
# {
#     "validos": [...],
#     "invalidos": [...]
# }
#
# Mantén el orden original.
#
# PISTA:
#
# resultado = {
#     "validos": [],
#     "invalidos": []
# }
#
# Después:
# - recorres cada usuario
# - lo normalizas
# - validas carácter por carácter
# - agregas al grupo correspondiente
#
# ============================================================
# FIN DE LA CLASE
# ============================================================
#
# IDEA FINAL:
#
# No necesitas memorizar decenas de métodos.
#
# Necesitas reconocer patrones:
#
# STRING -> limpiar
# STRING -> separar
# STRING -> unir
# STRING -> buscar
# STRING -> validar
# STRING -> recorrer
# STRING -> transformar
# STRING -> contar
# ============================================================
