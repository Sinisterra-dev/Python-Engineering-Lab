# ============================================================
# CLASE DE LISTAS Y TUPLAS EN PYTHON
# De cero a resolver los ejercicios del modulo
#
# Objetivo:
# Entender listas y tuplas, sus operaciones principales y,
# sobre todo, reconocer qué estructura usar en cada problema.
#
# Esta clase está pensada para estudiarla ANTES de resolver
# los ejercicios del módulo de listas y de sets/tuplas.
# ============================================================


# ============================================================
# 1. ¿QUE ES UNA LISTA?
# ============================================================
#
# Una lista guarda varios elementos en un mismo objeto.
# Es ordenada, indexada y mutable.
#
# "Mutable" significa que podemos cambiar sus elementos.

numeros = [10, 20, 30, 40]

print(numeros)


# ============================================================
# 2. ACCEDER A ELEMENTOS POR INDICE
# ============================================================

print(numeros[0])
print(numeros[2])


# Los índices empiezan en 0:
#
# 0 -> 10
# 1 -> 20
# 2 -> 30
# 3 -> 40


# ============================================================
# 3. INDICES NEGATIVOS
# ============================================================
#
# -1 = último
# -2 = penúltimo
# -3 = antepenúltimo

print(numeros[-1])
print(numeros[-2])


# ============================================================
# 4. MODIFICAR UN ELEMENTO
# ============================================================

numeros[0] = 999

print(numeros)


# ============================================================
# 5. AGREGAR CON append()
# ============================================================
#
# append() agrega un elemento al final.

numeros.append(50)

print(numeros)


# ============================================================
# 6. INSERTAR CON insert()
# ============================================================
#
# insert(indice, valor)

numeros.insert(1, 15)

print(numeros)


# ============================================================
# 7. EXTENDER UNA LISTA CON extend()
# ============================================================
#
# extend() agrega varios elementos.

numeros.extend([60, 70, 80])

print(numeros)


# ============================================================
# 8. ELIMINAR CON remove()
# ============================================================
#
# remove() elimina la primera aparición del valor.

numeros = [10, 20, 30, 20, 40]

numeros.remove(20)

print(numeros)


# ============================================================
# 9. ELIMINAR CON pop()
# ============================================================
#
# pop() elimina por índice y devuelve el elemento.

numeros = [10, 20, 30, 40]

eliminado = numeros.pop(1)

print(eliminado)
print(numeros)


# ============================================================
# 10. del
# ============================================================

numeros = [10, 20, 30, 40]

del numeros[2]

print(numeros)


# ============================================================
# 11. len()
# ============================================================

numeros = [10, 20, 30, 40]

print(len(numeros))


# ============================================================
# 12. COMPROBAR SI UN ELEMENTO EXISTE
# ============================================================

numeros = [10, 20, 30, 40]

print(20 in numeros)
print(99 in numeros)
print(99 not in numeros)


# ============================================================
# 13. RECORRER UNA LISTA
# ============================================================

frutas = ["manzana", "pera", "uva"]

for fruta in frutas:
    print(fruta)


# ============================================================
# 14. RECORRER CON INDICE
# ============================================================
#
# enumerate() entrega:
# indice + valor

frutas = ["manzana", "pera", "uva"]

for indice, fruta in enumerate(frutas):
    print(indice, fruta)


# ============================================================
# 15. RECORRER CON range()
# ============================================================

numeros = [10, 20, 30, 40]

for i in range(len(numeros)):
    print(numeros[i])


# ============================================================
# 16. FILTRAR UNA LISTA
# ============================================================
#
# Patrón:
#
# resultado = []
# for elemento in lista:
#     if condicion:
#         resultado.append(elemento)

numeros = [10, 3, 8, 1, 6]

mayores = []

for numero in numeros:
    if numero > 5:
        mayores.append(numero)

print(mayores)


# ============================================================
# 17. CONTAR ELEMENTOS
# ============================================================

numeros = [2, 5, 2, 7, 2]

contador = 0

for numero in numeros:
    if numero == 2:
        contador += 1

print(contador)


# ============================================================
# 18. ACUMULAR ELEMENTOS
# ============================================================

numeros = [10, 20, 30]

total = 0

for numero in numeros:
    total += numero

print(total)


# ============================================================
# 19. SUM()
# ============================================================
#
# Si solamente necesitas sumar todos los elementos:

numeros = [10, 20, 30]

print(sum(numeros))


# ============================================================
# 20. MAX() Y MIN()
# ============================================================

numeros = [10, 20, 30, 5, 40]

print(max(numeros))
print(min(numeros))


# ============================================================
# 21. PROMEDIO
# ============================================================

numeros = [10, 20, 30, 40]

promedio = sum(numeros) / len(numeros)

print(promedio)


# ============================================================
# 22. SLICING
# ============================================================
#
# Una lista[ inicio : fin ]
#
# El inicio se incluye.
# El fin NO se incluye.

numeros = [10, 20, 30, 40, 50]

print(numeros[1:4])


# ============================================================
# 23. SLICING DESDE EL PRINCIPIO
# ============================================================

numeros = [10, 20, 30, 40, 50]

print(numeros[:3])


# ============================================================
# 24. SLICING HASTA EL FINAL
# ============================================================

numeros = [10, 20, 30, 40, 50]

print(numeros[2:])


# ============================================================
# 25. SLICING CON PASO
# ============================================================
#
# lista[inicio:fin:paso]

numeros = [10, 20, 30, 40, 50, 60]

print(numeros[::2])


# ============================================================
# 26. INVERTIR CON SLICING
# ============================================================

numeros = [1, 2, 3, 4, 5]

invertida = numeros[::-1]

print(invertida)
print(numeros)


# ============================================================
# 27. reversed()
# ============================================================
#
# reversed() devuelve un iterador.
# Si necesitas una lista:

numeros = [1, 2, 3, 4, 5]

invertida = list(reversed(numeros))

print(invertida)


# ============================================================
# 28. sorted()
# ============================================================
#
# sorted() crea una NUEVA lista ordenada.
# No modifica la original.

numeros = [5, 2, 8, 1, 4]

ordenados = sorted(numeros)

print(ordenados)
print(numeros)


# ============================================================
# 29. sort()
# ============================================================
#
# sort() modifica la lista original.

numeros = [5, 2, 8, 1, 4]

numeros.sort()

print(numeros)


# ============================================================
# 30. ORDENAR DE MAYOR A MENOR
# ============================================================

numeros = [5, 2, 8, 1, 4]

numeros.sort(reverse=True)

print(numeros)


# ============================================================
# 31. ELIMINAR DUPLICADOS MANTENIENDO EL ORDEN
# ============================================================
#
# Patrón:
# resultado vacío + búsqueda + append

numeros = [1, 2, 1, 3, 2, 4]

sin_duplicados = []

for numero in numeros:
    if numero not in sin_duplicados:
        sin_duplicados.append(numero)

print(sin_duplicados)


# ============================================================
# 32. LISTAS PARALELAS + zip()
# ============================================================
#
# zip() combina elementos por posición.

nombres = ["Ana", "Luis", "Eva"]
edades = [28, 31, 22]

for nombre, edad in zip(nombres, edades):
    print(nombre, edad)


# ============================================================
# 33. zip() PARA CREAR TUPLAS
# ============================================================

x = [1, 2, 3]
y = [10, 20, 30]

puntos = list(zip(x, y))

print(puntos)


# ============================================================
# 34. LISTAS DE LISTAS
# ============================================================
#
# Una lista puede contener otras listas.

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matriz[0])
print(matriz[0][1])


# ============================================================
# 35. RECORRER UNA LISTA DE LISTAS
# ============================================================

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

for fila in matriz:
    for valor in fila:
        print(valor)


# ============================================================
# 36. LISTAS DE DICCIONARIOS
# ============================================================
#
# Esto aparece muchísimo en datos, APIs y backend.

usuarios = [
    {"nombre": "Ana", "edad": 28},
    {"nombre": "Luis", "edad": 31},
    {"nombre": "Eva", "edad": 22}
]

print(usuarios[0]["nombre"])


# ============================================================
# 37. RECORRER LISTA DE DICCIONARIOS
# ============================================================

for usuario in usuarios:
    print(usuario["nombre"], usuario["edad"])


# ============================================================
# 38. LISTA + DICCIONARIO + FILTRO
# ============================================================

mayores = []

for usuario in usuarios:
    if usuario["edad"] >= 25:
        mayores.append(usuario["nombre"])

print(mayores)


# ============================================================
# 39. LISTA + DICCIONARIO + AGRUPACION
# ============================================================
#
# La lista puede contener registros y podemos agruparlos
# utilizando un diccionario.

personas = [
    {"nombre": "Ana", "ciudad": "Palmira"},
    {"nombre": "Luis", "ciudad": "Cali"},
    {"nombre": "Eva", "ciudad": "Palmira"},
    {"nombre": "Juan", "ciudad": "Cali"}
]

por_ciudad = {}

for persona in personas:
    ciudad = persona["ciudad"]

    if ciudad not in por_ciudad:
        por_ciudad[ciudad] = []

    por_ciudad[ciudad].append(persona["nombre"])

print(por_ciudad)


# ============================================================
# 40. LISTAS Y TUPLAS
# ============================================================
#
# Una tupla se crea normalmente con paréntesis.
# Es inmutable.
#
# Lista:
#     [1, 2, 3]
#
# Tupla:
#     (1, 2, 3)

lista = [1, 2, 3]
tupla = (1, 2, 3)

print(lista)
print(tupla)


# ============================================================
# 41. ACCEDER A UNA TUPLA
# ============================================================

persona = ("Ana", 28, "Palmira")

print(persona[0])
print(persona[1])
print(persona[-1])


# ============================================================
# 42. SLICING EN TUPLAS
# ============================================================

numeros = (10, 20, 30, 40, 50)

print(numeros[1:4])


# ============================================================
# 43. INMUTABILIDAD
# ============================================================
#
# Esto NO funciona:
#
# numeros = (10, 20, 30)
# numeros[0] = 99
#
# Las tuplas no permiten modificar sus elementos.
#
# Esa es una diferencia fundamental con las listas.


# ============================================================
# 44. RECORRER UNA TUPLA
# ============================================================

colores = ("rojo", "verde", "azul")

for color in colores:
    print(color)


# ============================================================
# 45. DESEMPAQUETADO
# ============================================================

persona = ("Ana", 28, "Palmira")

nombre, edad, ciudad = persona

print(nombre)
print(edad)
print(ciudad)


# ============================================================
# 46. TUPLAS COMO RESULTADO
# ============================================================
#
# Una función o algoritmo puede devolver varios valores
# agrupados en una tupla.

numeros = [10, 20, 30, 40]

resumen = (
    min(numeros),
    max(numeros),
    sum(numeros) / len(numeros)
)

print(resumen)


# ============================================================
# 47. LISTA DE TUPLAS
# ============================================================

rutas = [
    ("Palmira", "Cali", 30),
    ("Cali", "Buga", 70),
    ("Palmira", "Buga", 90)
]

print(rutas)


# ============================================================
# 48. DESEMPAQUETAR TUPLAS EN UN FOR
# ============================================================

for origen, destino, distancia in rutas:
    print(origen, destino, distancia)


# ============================================================
# 49. TUPLAS COMO CLAVES DE DICCIONARIO
# ============================================================
#
# Una tupla puede servir como clave.

distancias = {
    ("Palmira", "Cali"): 30,
    ("Cali", "Buga"): 70
}

print(distancias[("Palmira", "Cali")])


# ============================================================
# 50. TUPLAS Y zip()
# ============================================================

nombres = ["Ana", "Luis", "Eva"]
edades = [28, 31, 22]

personas = list(zip(nombres, edades))

print(personas)


# ============================================================
# 51. PATRONES PARA IDENTIFICAR EN EJERCICIOS DE LISTAS
# ============================================================
#
# FILTRAR
#     for + if + append
#
# CONTAR
#     contador += 1
#
# ACUMULAR
#     acumulador += valor
#
# BUSCAR
#     in / not in
#
# RECORRER CON INDICE
#     enumerate()
#
# COMBINAR LISTAS
#     zip()
#
# ORDENAR SIN MODIFICAR
#     sorted()
#
# ORDENAR MODIFICANDO
#     sort()
#
# INVERTIR
#     lista[::-1]
#
# ELIMINAR DUPLICADOS MANTENIENDO ORDEN
#     lista auxiliar + in
#
# VENTANAS
#     comparar posiciones consecutivas
#
# AGRUPAR
#     diccionario + listas
#
# ============================================================


# ============================================================
# 52. PATRONES PARA IDENTIFICAR EN EJERCICIOS DE TUPLAS
# ============================================================
#
# DATOS FIJOS Y RELACIONADOS
#     ("Ana", 28, "Palmira")
#
# DESEMPAQUETAR
#     nombre, edad, ciudad = persona
#
# LISTA DE REGISTROS FIJOS
#     [("pan", 3, 2000), ("leche", 2, 3000)]
#
# RESULTADO MULTIPLE
#     (minimo, maximo, promedio)
#
# CLAVE COMPUESTA
#     {("Palmira", "Cali"): 30}
#
# COMBINACION POSICIONAL
#     list(zip(x, y))
#
# ============================================================


# ============================================================
# 53. ¿CUANDO USAR LISTA?
# ============================================================
#
# Usa una lista cuando:
#
# - El orden importa.
# - Necesitas modificar elementos.
# - Puede haber duplicados.
# - Quieres recorrer una colección de elementos.
# - Vas a agregar o eliminar elementos.
#
# Ejemplo:
#
# compras = ["pan", "leche", "cafe"]


# ============================================================
# 54. ¿CUANDO USAR TUPLA?
# ============================================================
#
# Usa una tupla cuando:
#
# - Los datos representan una estructura fija.
# - No quieres que se modifique después de crearla.
# - Necesitas devolver varios valores juntos.
# - Quieres usar la colección como clave de diccionario.
#
# Ejemplo:
#
# coordenada = (10, 20)


# ============================================================
# 55. DIFERENCIA MENTAL: LISTA VS TUPLA
# ============================================================
#
# LISTA
# [10, 20, 30]
#
# "Tengo una colección que puede cambiar."
#
# TUPLA
# (10, 20, 30)
#
# "Tengo un conjunto fijo de valores relacionados."
#
# ============================================================


# ============================================================
# 56. RETO FINAL
# ============================================================
#
# Resuelve SIN copiar literalmente los ejemplos anteriores.
#
# Tienes una lista de ventas:
#
ventas = [
    ("pan", "Ana", 3, 2000),
    ("leche", "Luis", 2, 3000),
    ("pan", "Ana", 2, 2000),
    ("cafe", "Eva", 4, 5000),
    ("leche", "Ana", 1, 3000)
]
#
# Construye un reporte que contenga:
#
# 1. Un set con todos los productos vendidos.
#
# 2. Un set con todos los vendedores.
#
# 3. Una lista ordenada de los productos sin duplicados.
#
# 4. Una tupla con:
#       (venta_minima, venta_maxima, promedio_de_venta)
#
# 5. Un diccionario que acumule las unidades vendidas por producto.
#
# El punto 5 usa diccionarios porque ya conoces el patrón.
# El resto debe hacerte practicar listas, sets y tuplas.
#
# ============================================================
# FIN DE LA CLASE
#
# Antes de comenzar los ejercicios:
#
# - Ejecuta los ejemplos.
# - Cambia algunos datos.
# - Intenta predecir la salida antes de ejecutar.
# - Cuando algo te genere duda, detente y entiéndelo.
#
# Después:
# -> comienza los ejercicios del módulo.
# ============================================================
