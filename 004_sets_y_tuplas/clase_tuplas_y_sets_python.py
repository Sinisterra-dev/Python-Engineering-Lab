# ============================================================
# CLASE DE TUPLAS Y SETS EN PYTHON
# De cero a resolver los ejercicios del modulo
#
# Objetivo:
# Entender TUPLAS y SETS de forma práctica y tener las
# herramientas necesarias para resolver los 22 ejercicios
# del módulo de Sets y Tuplas.
#
# Esta clase NO está centrada en listas.
# Las listas aparecen únicamente cuando necesitamos
# combinarlas con sets o tuplas en los ejercicios.
# ============================================================


# ============================================================
# PARTE 1 - TUPLAS
# ============================================================


# ============================================================
# 1. ¿QUE ES UNA TUPLA?
# ============================================================
#
# Una tupla es una colección ordenada de elementos.
#
# Se parece a una lista:
#
# lista = [10, 20, 30]
#
# Pero se crea normalmente con paréntesis:
#
# tupla = (10, 20, 30)
#
# La diferencia principal es que una tupla es INMUTABLE:
# una vez creada, no puedes cambiar sus elementos.


persona = ("Ana", 28, "Palmira")

print(persona)


# ============================================================
# 2. ACCEDER A ELEMENTOS DE UNA TUPLA
# ============================================================

print(persona[0])
print(persona[1])
print(persona[-1])


# ============================================================
# 3. RECORRER UNA TUPLA
# ============================================================

colores = ("rojo", "verde", "azul")

for color in colores:
    print(color)


# ============================================================
# 4. LEN() EN TUPLAS
# ============================================================

persona = ("Ana", 28, "Palmira")

print(len(persona))


# ============================================================
# 5. IN / NOT IN EN TUPLAS
# ============================================================

numeros = (10, 20, 30, 40)

print(20 in numeros)
print(99 not in numeros)


# ============================================================
# 6. SLICING EN TUPLAS
# ============================================================
#
# Las tuplas también permiten slicing.
#
# tupla[inicio:fin]

numeros = (10, 20, 30, 40, 50)

print(numeros[1:4])
print(numeros[:3])
print(numeros[2:])


# ============================================================
# 7. INMUTABILIDAD
# ============================================================
#
# Esto produciría un error:
#
# persona[0] = "Luis"
#
# Porque las tuplas NO se pueden modificar después de creadas.
#
# Esa es una diferencia fundamental respecto a las listas.


# ============================================================
# 8. DESEMPAQUETADO
# ============================================================
#
# Puedes sacar los valores de una tupla directamente:

persona = ("Ana", 28, "Palmira")

nombre, edad, ciudad = persona

print(nombre)
print(edad)
print(ciudad)


# ============================================================
# 9. DESEMPAQUETADO DENTRO DE UN FOR
# ============================================================
#
# Esto aparece mucho en los ejercicios.

rutas = [
    ("Madrid", "Barcelona", 620),
    ("Barcelona", "Valencia", 350)
]

for origen, destino, distancia in rutas:
    print(origen, destino, distancia)


# ============================================================
# 10. TUPLAS COMO RESULTADO
# ============================================================
#
# Una tupla sirve para devolver varios datos relacionados.

numeros = [10, 20, 30, 40]

resultado = (
    min(numeros),
    max(numeros),
    sum(numeros) / len(numeros)
)

print(resultado)


# ============================================================
# 11. TUPLAS DENTRO DE LISTAS
# ============================================================
#
# Esta estructura aparece en varios ejercicios:
#
# [
#     (valor1, valor2),
#     (valor1, valor2)
# ]

puntos = [
    (1, 2),
    (3, 4),
    (5, 6)
]

print(puntos[0])


# ============================================================
# 12. TUPLAS COMO CLAVES DE DICCIONARIO
# ============================================================
#
# Como una tupla es inmutable y hashable, puede ser una clave.

distancias = {
    ("Palmira", "Cali"): 30,
    ("Cali", "Buga"): 70
}

print(distancias[("Palmira", "Cali")])


# ============================================================
# 13. zip() GENERA TUPLAS
# ============================================================
#
# zip() ya lo conoces.
# Aquí interesa observar que cada pareja generada es una tupla.

x = [1, 2, 3]
y = [10, 20, 30]

puntos = list(zip(x, y))

print(puntos)


# ============================================================
# PARTE 2 - SETS
# ============================================================


# ============================================================
# 14. ¿QUE ES UN SET?
# ============================================================
#
# Un set es una colección de elementos ÚNICOS.
#
# No permite duplicados.

numeros = {1, 2, 3, 4}

print(numeros)


# ============================================================
# 15. CREAR UN SET DESDE UNA LISTA
# ============================================================
#
# Esta es una operación muy importante.

lista = [1, 2, 2, 3, 4, 4]

unicos = set(lista)

print(unicos)


# ============================================================
# 16. IMPORTANTE: {} NO ES UN SET VACIO
# ============================================================
#
# {} crea un diccionario vacío.
#
# Para crear un set vacío:
#
# set_vacio = set()

vacio = set()

print(vacio)


# ============================================================
# 17. ADD()
# ============================================================

usuarios = {"ana", "luis"}

usuarios.add("eva")

print(usuarios)


# ============================================================
# 18. DUPLICADOS AUTOMATICAMENTE
# ============================================================

usuarios = {"ana", "luis"}

usuarios.add("ana")
usuarios.add("ana")

print(usuarios)


# ============================================================
# 19. REMOVE() Y DISCARD()
# ============================================================

usuarios = {"ana", "luis", "eva"}

usuarios.remove("luis")

print(usuarios)

# discard() no produce error si el elemento no existe:

usuarios.discard("pedro")

print(usuarios)


# ============================================================
# 20. BUSCAR EN UN SET
# ============================================================

usuarios = {"ana", "luis", "eva"}

print("ana" in usuarios)
print("pedro" not in usuarios)


# ============================================================
# 21. UNION
# ============================================================
#
# Une elementos de ambos sets.

a = {"hogar", "cocina"}
b = {"cocina", "jardin"}

union = a | b

print(union)


# También:
# union = a.union(b)


# ============================================================
# 22. INTERSECCION
# ============================================================
#
# Elementos que están en ambos conjuntos.

a = {"pan", "leche", "cafe"}
b = {"leche", "cafe", "agua"}

comunes = a & b

print(comunes)


# También:
# comunes = a.intersection(b)


# ============================================================
# 23. DIFERENCIA
# ============================================================
#
# Elementos que están en A pero no en B.

a = {"ana", "luis", "eva"}
b = {"luis", "pedro"}

solo_a = a - b

print(solo_a)


# También:
# solo_a = a.difference(b)


# ============================================================
# 24. DIFERENCIA SIMETRICA
# ============================================================
#
# Elementos que están en A o B, pero no en ambos.

a = {"admin", "editor"}
b = {"editor", "viewer"}

resultado = a ^ b

print(resultado)


# También:
# resultado = a.symmetric_difference(b)


# ============================================================
# 25. SUBCONJUNTO
# ============================================================
#
# Pregunta:
# ¿Todos los elementos de A están dentro de B?

requeridas = {"martillo", "destornillador"}
caja = {"martillo", "destornillador", "pinza"}

print(requeridas <= caja)


# También:
# print(requeridas.issubset(caja))


# ============================================================
# 26. SUPERCONJUNTO
# ============================================================
#
# ¿B contiene todos los elementos de A?

a = {"martillo", "destornillador"}
b = {"martillo", "destornillador", "pinza"}

print(b >= a)


# También:
# print(b.issuperset(a))


# ============================================================
# 27. CONJUNTOS DISJUNTOS
# ============================================================
#
# Dos sets son disjuntos si NO comparten ningún elemento.

a = {101, 102, 103}
b = {201, 202}

print(a.isdisjoint(b))


# ============================================================
# 28. INTERSECCION DE TRES SETS
# ============================================================

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}

comunes = set1 & set2 & set3

print(comunes)


# ============================================================
# 29. DIFERENCIA ENTRE SET Y LISTA
# ============================================================
#
# LISTA:
# - mantiene orden
# - permite duplicados
# - tiene índices
#
# SET:
# - no está pensado para trabajar por posición
# - elimina duplicados
# - está pensado para pertenencia y operaciones de conjuntos
#
# Ejemplo:
#
# lista = [1, 2, 2, 3]
# set(lista) -> {1, 2, 3}


# ============================================================
# 30. SETS Y STRINGS
# ============================================================
#
# Un string se puede convertir en un set de caracteres.

texto = "banana"

letras = set(texto)

print(letras)


# ============================================================
# 31. CONTAR LETRAS DISTINTAS
# ============================================================

texto = "banana"

letras_unicas = set(texto)

print(len(letras_unicas))


# ============================================================
# 32. SETS PARA PANGRAMAS
# ============================================================
#
# Un pangrama contiene todas las letras del alfabeto.
#
# La idea del ejercicio:
# 1. convertir el texto a minúsculas
# 2. quedarnos con letras
# 3. convertir a set
# 4. comparar con el set del alfabeto

texto = "the quick brown fox jumps over the lazy dog"

alfabeto = set("abcdefghijklmnopqrstuvwxyz")

letras_texto = set(
    letra
    for letra in texto.lower()
    if letra.isalpha()
)

print(letras_texto == alfabeto)


# ============================================================
# 33. SETS PARA ELEMENTOS UNICOS
# ============================================================

datos = [1, 2, 2, 3, 3, 4, 4]

unicos = set(datos)

print(unicos)


# ============================================================
# 34. SETS PARA DIFERENCIAS ENTRE LISTAS
# ============================================================

ayer = ["ana", "luis"]
hoy = ["ana", "eva", "zoe"]

usuarios_nuevos = set(hoy) - set(ayer)

print(usuarios_nuevos)


# ============================================================
# 35. SETS PARA ELEMENTOS EN COMUN
# ============================================================

a = ["frio", "bebida"]
b = ["bebida", "promo", "frio"]

comunes = set(a) & set(b)

print(comunes)


# ============================================================
# 36. CONVERTIR EL RESULTADO A LISTA ORDENADA
# ============================================================
#
# Recuerda:
# los sets NO mantienen el orden como una lista.
#
# Si el ejercicio pide una lista ordenada:

resultado = sorted(set(a) & set(b))

print(resultado)


# ============================================================
# 37. FILTRAR UN STRING CON UN SET
# ============================================================

texto = "10010"
validos = {"0", "1"}

caracteres = set(texto)

print(caracteres <= validos)


# ============================================================
# 38. PARTICIONAR EN DOS SETS
# ============================================================
#
# Creamos un set de pares y otro de impares.

numeros = {1, 2, 3, 4, 5}

pares = set()
impares = set()

for numero in numeros:
    if numero % 2 == 0:
        pares.add(numero)
    else:
        impares.add(numero)

print(pares)
print(impares)


# ============================================================
# 39. TUPLAS + SETS
# ============================================================
#
# Las tuplas pueden almacenarse en un set porque son hashable.

puntos = {(1, 2), (3, 4), (5, 6)}

print(puntos)


# ============================================================
# 40. ELIMINAR DUPLICADOS DE TUPLAS
# ============================================================

puntos = [(1, 2), (3, 4), (1, 2), (5, 5)]

sin_duplicados = list(set(puntos))

print(sin_duplicados)


# OJO:
# Esta solución elimina duplicados, pero NO conserva necesariamente
# el orden original.
#
# Si el ejercicio exige conservar el orden, necesitas otra estrategia:
#
# vistos = set()
# resultado = []
#
# y luego recorrer la lista.


# ============================================================
# 41. TUPLAS CON DUPLICADOS QUE CAMBIAN DE ORDEN
# ============================================================
#
# En este caso:
#
# (1, 2)
# (2, 1)
#
# son tuplas distintas.
#
# Si el problema dice que representan la misma pareja,
# necesitas una representación que ignore el orden.
#
# frozenset() sirve para eso.

pareja1 = (1, 2)
pareja2 = (2, 1)

print(frozenset(pareja1) == frozenset(pareja2))


# ============================================================
# 42. FROZENSET
# ============================================================
#
# frozenset es un conjunto inmutable.
#
# Su importancia para nuestros ejercicios:
# puede utilizarse como elemento de un set o como clave de
# un diccionario.

pareja = frozenset((1, 2))

vistos = {pareja}

print(vistos)


# ============================================================
# 43. DISTANCIA MANHATTAN CON TUPLAS
# ============================================================

p1 = (1, 5)
p2 = (4, 1)

x1, y1 = p1
x2, y2 = p2

distancia = abs(x1 - x2) + abs(y1 - y2)

print(distancia)


# ============================================================
# 44. LISTA DE TUPLAS + ACUMULADOR
# ============================================================

inventario = [
    ("tornillo", 100, 0.5),
    ("tuerca", 50, 0.8)
]

total = 0

for nombre, cantidad, precio in inventario:
    total += cantidad * precio

print(total)


# ============================================================
# 45. TUPLAS COMO CLAVES DE DICCIONARIO
# ============================================================

rutas = [
    ("Madrid", "Barcelona", 620),
    ("Barcelona", "Valencia", 350)
]

distancias = {}

for origen, destino, distancia in rutas:
    distancias[(origen, destino)] = distancia

print(distancias)


# ============================================================
# 46. RECONOCER EL PATRON DE CADA EJERCICIO
# ============================================================
#
# ¿ME PIDEN ELIMINAR DUPLICADOS?
#     -> set()
#
# ¿ME PIDEN ELEMENTOS EN COMUN?
#     -> intersección &
#
# ¿ME PIDEN LO QUE ESTÁ EN A PERO NO EN B?
#     -> diferencia -
#
# ¿ME PIDEN LO QUE ESTÁ EN A O B PERO NO EN AMBOS?
#     -> diferencia simétrica ^
#
# ¿ME PIDEN UNIR CONJUNTOS?
#     -> unión |
#
# ¿ME PREGUNTAN SI TODOS LOS ELEMENTOS ESTÁN?
#     -> <= / issubset()
#
# ¿ME PREGUNTAN SI NO HAY ELEMENTOS EN COMUN?
#     -> isdisjoint()
#
# ¿NECESITO MANTENER ORDEN?
#     -> cuidado con set()
#
# ¿ME PIDEN UNA ESTRUCTURA FIJA DE DATOS?
#     -> tupla
#
# ¿TENGO VARIOS VALORES RELACIONADOS?
#     -> tupla
#
# ¿NECESITO DESEMPAQUETAR?
#     -> a, b, c = tupla
#
# ¿QUIERO USAR UNA PAREJA COMO CLAVE?
#     -> tupla como clave
#
# ¿(1,2) Y (2,1) DEBEN CONTAR COMO IGUALES?
#     -> frozenset()
#
# ============================================================


# ============================================================
# 47. RETO FINAL
# ============================================================
#
# Resuelve SIN copiar literalmente los ejemplos anteriores.
#
# Tienes tres listas de usuarios:
#
lunes = ["ana", "luis", "eva", "juan"]
martes = ["luis", "eva", "pedro"]
miercoles = ["eva", "luis", "maria"]
#
# Construye:
#
# 1. Un set con los usuarios que estuvieron activos los tres días.
#
# 2. Un set con los usuarios que estuvieron activos el lunes
#    pero no el martes.
#
# 3. Una lista ordenada con todos los usuarios distintos.
#
# 4. Una tupla con:
#       (cantidad_total_usuarios, cantidad_activos_tres_dias)
#
# ============================================================


# ============================================================
# SEGUNDO RETO FINAL
# ============================================================
#
# Trabaja con:
#
ventas = [
    ("pan", "alimentos", 3),
    ("leche", "alimentos", 2),
    ("jabon", "hogar", 4),
    ("pan", "alimentos", 2),
    ("cafe", "alimentos", 5)
]
#
# Construye una salida con:
#
# 1. Set de categorías únicas.
#
# 2. Set de productos únicos.
#
# 3. Lista ordenada de productos únicos.
#
# 4. Tupla:
#       (producto_primero, producto_ultimo)
#    usando el orden original de aparición.
#
# 5. Diccionario con unidades acumuladas por producto.
#
# ============================================================
# FIN DE LA CLASE
#
# Estudia esta clase antes de comenzar los 22 ejercicios.
# El objetivo no es memorizar métodos aislados.
# El objetivo es reconocer qué estructura necesitas:
#
#     TUpla -> datos relacionados y fijos
#     SET   -> unicidad y operaciones de conjuntos
#
# ============================================================
