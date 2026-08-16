# ============================================================
# EJERCICIOS DE SETS Y TUPLAS - PYTHON
# Total: 22 ejercicios
#
# Objetivo:
# Practicar sets y tuplas combinándolos con listas, diccionarios,
# strings, filtros, búsquedas y lógica.
#
# Todos los ejercicios están preparados para trabajar
# directamente en un archivo .py.
# ============================================================


# ============================================================
# EJERCICIO #0001
# Nivel: Nivel 2 - Básico
# Conceptos: sets, diferencia
#
# Problema:
# Devuelve los usuarios que aparecen hoy pero no ayer.
# La salida debe ser una lista ordenada alfabéticamente.
#
# Entrada:
ayer = ["ana", "luis"]
hoy = ["ana", "eva", "zoe"]
#
# Salida esperada:
# ["eva", "zoe"]
#
# Pista:
# Convierte las listas a sets y usa diferencia.
# ============================================================
set_ayer = set(ayer)
set_hoy = set(hoy)

salida = set_hoy - set_ayer
resultado = sorted(salida)
print(resultado)


# ============================================================
# EJERCICIO #0002
# Nivel: Nivel 1 - Inicial
# Conceptos: sets, unicidad
#
# Problema:
# Devuelve los elementos únicos de una lista como un set.
#
# Entrada:
lista = [1, 2, 2, 3, 4, 4]
#
# Salida esperada:
# {1, 2, 3, 4}
#
# Regla:
# El resultado debe ser realmente un objeto set.
# ============================================================
unicos = set(lista)
print(unicos)

# ============================================================
# EJERCICIO #0003
# Nivel: Nivel 2 - Básico
# Conceptos: sets, intersección
#
# Problema:
# Devuelve las etiquetas que aparecen en ambos productos.
# La salida debe ser una lista ordenada alfabéticamente.
#
# Entrada:
a = ["frio", "bebida"]
b = ["bebida", "promo", "frio"]
#
# Salida esperada:
# ["bebida", "frio"]
#
# Pista:
# Usa la intersección de sets y luego sorted().
# ============================================================
salida = sorted(set(a) & set(b))
print(salida)

# ============================================================
# EJERCICIO #0004
# Nivel: Nivel 2 - Básico
# Conceptos: sets, diferencia simétrica
#
# Problema:
# Devuelve los usuarios que pertenecen a A o a B, pero no a ambos.
#
# Entrada:
grupo_a = {"admin", "editor"}
grupo_b = {"editor", "viewer"}
#
# Salida esperada:
# {"admin", "viewer"}
#
# Regla:
# El resultado debe ser un set.
#
# Pista:
# Puedes usar ^ o symmetric_difference().
# ============================================================
salida = grupo_a ^ grupo_b
print(salida)

# ============================================================
# EJERCICIO #0005
# Nivel: Nivel 2 - Básico
# Conceptos: sets, subconjuntos
#
# Problema:
# Comprueba si todas las herramientas requeridas para un trabajo
# están disponibles en la caja de herramientas.
#
# Entrada:
requeridas = {"martillo", "destornillador"}
caja = {"martillo", "destornillador", "pinza"}
#
# Salida esperada:
# True
#
# Pista:
# issubset() o <=.
# ============================================================

print(requeridas.issubset(caja))
print(requeridas <= caja)


# ============================================================
# EJERCICIO #0006
# Nivel: Nivel 2 - Básico
# Conceptos: sets, unión
#
# Problema:
# Combina las categorías de productos de dos departamentos
# en una sola colección sin duplicados.
#
# Entrada:
dep_a = {"hogar", "cocina"}
dep_b = {"cocina", "jardin"}
#
# Salida esperada:
# {"hogar", "cocina", "jardin"}
#
# Regla:
# Devuelve un set.
# ============================================================
departamenos = dep_a | dep_b
print(departamenos)

# ============================================================
# EJERCICIO #0007
# Nivel: Nivel 2 - Básico
# Conceptos: sets, intersección múltiple
#
# Problema:
# Encuentra los elementos que son comunes a tres conjuntos.
#
# Entrada:
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}
#
# Salida esperada:
# {3}
#
# Pista:
# Puedes encadenar & o intersection().
# ============================================================
comunes = set1 & set2 & set3
print(comunes)

# ============================================================
# EJERCICIO #0008
# Nivel: Nivel 2 - Básico
# Conceptos: sets, diferencia
#
# Problema:
# Quita los usuarios bloqueados del conjunto de usuarios autorizados.
#
# Entrada:
autorizados = {"ana", "luis", "eva"}
bloqueados = {"luis", "pedro"}
#
# Salida esperada:
# {"ana", "eva"}
#
# Pista:
# El operador - representa diferencia.
# ============================================================
aut = autorizados - bloqueados
print(aut)

# ============================================================
# EJERCICIO #0009
# Nivel: Nivel 2 - Básico
# Conceptos: sets, disjuntos
#
# Problema:
# Verifica si dos listas de IDs no comparten ningún elemento.
#
# Entrada:
cat1 = [101, 102, 103]
cat2 = [201, 202]
#
# Salida esperada:
# True
#
# Pista:
# isdisjoint() devuelve True cuando no hay elementos en común.
# ============================================================
salida = set(cat1).isdisjoint(set(cat2))
print(salida)

# ============================================================
# EJERCICIO #0010
# Nivel: Nivel 2 - Básico
# Conceptos: sets, strings, filtros
#
# Problema:
# Comprueba si un texto contiene únicamente caracteres permitidos.
#
# Entrada:
texto = "10010"
permitidos = {"0", "1"}
#
# Salida esperada:
# True
#
# Pista:
# El set de caracteres del texto debe ser subconjunto del set
# de caracteres permitidos.
# ============================================================


# ============================================================
# EJERCICIO #0011
# Nivel: Nivel 2 - Básico
# Conceptos: sets, strings, conteo
#
# Problema:
# Cuenta cuántas palabras únicas tiene una frase.
# Ignora puntos y comas.
#
# Entrada:
frase = "hola, mundo. hola de nuevo."
#
# Salida esperada:
# 4
#
# Regla:
# Las palabras únicas son:
# "hola", "mundo", "de", "nuevo"
#
# Pista:
# Limpia la puntuación y luego usa set().
# ============================================================


# ============================================================
# EJERCICIO #0012
# Nivel: Nivel 2 - Básico
# Conceptos: sets, strings, búsqueda
#
# Problema:
# Encuentra la única letra minúscula que falta para completar
# una secuencia consecutiva desde la primera hasta la última.
#
# Entrada:
secuencia = "abce"
#
# Salida esperada:
# "d"
#
# Regla:
# La secuencia original está ordenada y solo falta una letra.
#
# Pista:
# Crea el set completo del rango y calcula la diferencia.
# ============================================================


# ============================================================
# EJERCICIO #0013
# Nivel: Nivel 2 - Básico
# Conceptos: sets, partición, filtros
#
# Problema:
# Divide un conjunto de enteros en dos sets:
# uno con pares y otro con impares.
#
# Entrada:
numeros = {1, 2, 3, 4, 5}
#
# Salida esperada:
# ({2, 4}, {1, 3, 5})
#
# Regla:
# Debes retornar una tupla que contenga los dos sets.
#
# Pista:
# Usa un for y dos conjuntos vacíos.
# ============================================================


# ============================================================
# EJERCICIO #0014
# Nivel: Nivel 2 - Básico
# Conceptos: tuplas, zip
#
# Problema:
# Combina dos listas paralelas de coordenadas X e Y en una lista
# de tuplas (x, y).
#
# Entrada:
x = [1, 2, 3]
y = [10, 20, 30]
#
# Salida esperada:
# [(1, 10), (2, 20), (3, 30)]
#
# Nota:
# zip() ya lo has trabajado bastante; aquí el objetivo nuevo
# es observar que cada par generado es una tupla.
# ============================================================


# ============================================================
# EJERCICIO #0015
# Nivel: Nivel 2 - Básico
# Conceptos: tuplas, índices, desempaquetado
#
# Problema:
# Recibe una tupla con nombre, edad y ciudad.
# Devuelve un texto con esos datos.
#
# Entrada:
persona = ("Ana", 28, "Palmira")
#
# Salida esperada:
# "Ana tiene 28 años y vive en Palmira"
#
# Pista:
# nombre, edad, ciudad = persona
# ============================================================


# ============================================================
# EJERCICIO #0016
# Nivel: Nivel 2 - Básico
# Conceptos: tuplas, matemáticas
#
# Problema:
# Calcula la distancia Manhattan entre dos puntos 2D.
#
# Entrada:
p1 = (1, 5)
p2 = (4, 1)
#
# Salida esperada:
# 7
#
# Fórmula:
# |x1 - x2| + |y1 - y2|
#
# Pista:
# Usa abs().
# ============================================================


# ============================================================
# EJERCICIO #0017
# Nivel: Nivel 2 - Básico
# Conceptos: tuplas, estadísticas
#
# Problema:
# Recibe una lista de números y devuelve una tupla con:
# (mínimo, máximo, promedio).
#
# Entrada:
numeros = [10, 20, 30, 40]
#
# Salida esperada:
# (10, 40, 25.0)
#
# Regla:
# La salida debe ser exactamente una tupla de tres elementos.
# ============================================================


# ============================================================
# EJERCICIO #0018
# Nivel: Nivel 2 - Básico
# Conceptos: tuplas, diccionarios, claves
#
# Problema:
# Crea un diccionario de distancias entre ciudades usando
# (origen, destino) como clave.
#
# Entrada:
rutas = [
    ("Madrid", "Barcelona", 620),
    ("Barcelona", "Valencia", 350)
]
#
# Salida esperada:
# {
#     ("Madrid", "Barcelona"): 620,
#     ("Barcelona", "Valencia"): 350
# }
#
# Pista:
# Desempaqueta cada tupla y construye la clave con otra tupla.
# ============================================================


# ============================================================
# EJERCICIO #0019
# Nivel: Nivel 3 - Práctico
# Conceptos: tuplas, sets, duplicados
#
# Problema:
# Elimina tuplas duplicadas considerando que (1, 2) y (2, 1)
# representan la misma pareja.
#
# Entrada:
tuplas = [(1, 2), (3, 4), (2, 1), (1, 2)]
#
# Salida esperada:
# [(1, 2), (3, 4)]
#
# Regla:
# Conserva la primera aparición.
#
# Pista:
# Para comparar la pareja sin importar el orden, puedes usar
# frozenset() y un set de elementos vistos.
# ============================================================


# ============================================================
# EJERCICIO #0020
# Nivel: Nivel 3 - Práctico
# Conceptos: tuplas, listas, acumuladores
#
# Problema:
# Calcula el valor total del inventario.
# Cada tupla tiene:
# (nombre_item, cantidad, precio_unitario)
#
# Entrada:
inventario = [
    ("tornillo", 100, 0.5),
    ("tuerca", 50, 0.8)
]
#
# Salida esperada:
# 90.0
#
# Regla:
# Suma cantidad * precio_unitario por cada elemento.
#
# Pista:
# Desempaqueta la tupla dentro del for.
# ============================================================


# ============================================================
# EJERCICIO #0021
# Nivel: Nivel 3 - Práctico
# Conceptos: sets, intersección, listas
#
# Problema:
# Encuentra los usuarios que estuvieron activos los tres días.
# Devuelve una lista ordenada alfabéticamente.
#
# Entrada:
lunes = {"ana", "luis"}
martes = {"luis", "eva"}
miercoles = {"luis", "pedro"}
#
# Salida esperada:
# ["luis"]
#
# Pista:
# Intersecta los tres sets y después usa sorted().
# ============================================================


# ============================================================
# EJERCICIO #0022
# Nivel: Nivel 4 - Intermedio
# Conceptos: sets, tuplas, listas, clasificación
#
# Problema:
# Recibes una lista de ventas representadas como tuplas:
# (producto, categoria)
#
# Devuelve una tupla con:
# 1. categorías utilizadas
# 2. productos que pertenecen a una categoría determinada
#
# Entrada:
ventas = [
    ("pan", "alimentos"),
    ("leche", "alimentos"),
    ("jabon", "hogar"),
    ("cafe", "alimentos")
]
categoria_objetivo = "alimentos"
#
# Salida esperada:
# (
#     {"alimentos", "hogar"},
#     {"pan", "leche", "cafe"}
# )
#
# Reglas:
# - El primer elemento de la salida debe ser un set.
# - El segundo elemento de la salida debe ser un set.
# - No debe haber duplicados.
#
# Pista:
# Recorre las tuplas y clasifica cada elemento.
# ============================================================


# ============================================================
# FIN DEL MODULO
#
# SETS:
# - unicidad
# - unión
# - intersección
# - diferencia
# - diferencia simétrica
# - subconjuntos
# - disjuntos
#
# TUPLAS:
# - creación
# - índices
# - desempaquetado
# - listas de tuplas
# - tuplas como claves
# - tuplas como resultados
#
# COMBINACIONES:
# - listas + sets
# - listas + tuplas
# - diccionarios + tuplas
# - strings + sets
# - filtros + sets
# - sorted() + sets
#
# No busques memorizar los 22 ejercicios.
# Busca reconocer qué estructura necesitas para cada problema.
# ============================================================
