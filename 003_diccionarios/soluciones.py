# ============================================================
# EJERCICIOS DE DICCIONARIOS - PYTHON
# Total: 40 ejercicios
#
# INSTRUCCIONES:
# - Cada ejercicio está preparado como código Python válido.
# - No hay soluciones.
# - Lee el problema, modifica/prueba los datos y resuelve debajo.
# - Los ejercicios aumentan progresivamente de dificultad.
# - Se mezclan diccionarios con listas, strings, tuplas y lógica.
# ============================================================


# ============================================================
# EJERCICIO #0001
# Nivel: Nivel 1 - Inicial
# Conceptos: diccionarios, acceso, actualización
#
# Problema:
# Dado un diccionario de producto, cambia el precio y agrega
# una nueva clave "stock".
#
# Entrada:
producto = {"nombre": "Laptop", "precio": 2500}
#
# Salida esperada:
# {"nombre": "Laptop", "precio": 2300, "stock": 5}
#
# ============================================================
producto = {"nombre": "Laptop", "precio": 2500}
producto["stock"] = 5
print(producto)

# ============================================================
# EJERCICIO #0002
# Nivel: Nivel 1 - Inicial
# Conceptos: diccionarios, búsqueda, in
#
# Problema:
# Determina si un usuario existe en el diccionario.
#
# Entrada:
usuarios = {"ana": "admin", "luis": "editor", "eva": "usuario"}
usuario_buscado = "luis"
#
# Salida esperada:
# True
#
# ============================================================


# ============================================================
# EJERCICIO #0003
# Nivel: Nivel 1 - Inicial
# Conceptos: diccionarios, recorrido, items
#
# Problema:
# Recorre un diccionario de productos e imprime cada producto
# junto con su precio.
#
# Entrada:
precios = {"pan": 3000, "leche": 4500, "arroz": 6000}
#
# Salida esperada:
# pan -> 3000
# leche -> 4500
# arroz -> 6000
#
# ============================================================


# ============================================================
# EJERCICIO #0004
# Nivel: Nivel 1 - Inicial
# Conceptos: diccionarios, filtros
#
# Problema:
# Devuelve una lista con los productos cuyo stock sea menor
# que 5.
#
# Entrada:
stock = {"pan": 8, "leche": 3, "arroz": 10, "cafe": 2}
#
# Salida esperada:
# ["leche", "cafe"]
#
# ============================================================


# ============================================================
# EJERCICIO #0005
# Nivel: Nivel 1 - Inicial
# Conceptos: diccionarios, acumuladores
#
# Problema:
# Suma todos los valores de un diccionario de ventas.
#
# Entrada:
ventas = {"lunes": 20, "martes": 15, "miercoles": 30}
#
# Salida esperada:
# 65
#
# ============================================================


# ============================================================
# EJERCICIO #0006
# Nivel: Nivel 1 - Inicial
# Conceptos: diccionarios, conteo, strings
#
# Problema:
# Cuenta cuántas veces aparece cada carácter de un texto.
# Ignora los espacios.
#
# Entrada:
texto = "banana"
#
# Salida esperada:
# {"b": 1, "a": 3, "n": 2}
#
# ============================================================


# ============================================================
# EJERCICIO #0007
# Nivel: Nivel 2 - Básico
# Conceptos: diccionarios, listas, acumuladores
#
# Problema:
# Tienes una lista de ventas. Agrupa la cantidad vendida
# por producto.
#
# Entrada:
ventas = [
    {"producto": "pan", "cantidad": 2},
    {"producto": "pan", "cantidad": 3},
    {"producto": "leche", "cantidad": 4}
]
#
# Salida esperada:
# {"pan": 5, "leche": 4}
#
# ============================================================


# ============================================================
# EJERCICIO #0008
# Nivel: Nivel 2 - Básico
# Conceptos: diccionarios, filtros, listas
#
# Problema:
# Devuelve los nombres de los estudiantes con nota >= 6.
#
# Entrada:
notas = {"Ana": 8, "Luis": 4, "Eva": 6, "Juan": 3}
#
# Salida esperada:
# ["Ana", "Eva"]
#
# ============================================================


# ============================================================
# EJERCICIO #0009
# Nivel: Nivel 2 - Básico
# Conceptos: diccionarios, maximo, min
#
# Problema:
# Encuentra el nombre del producto con mayor precio.
#
# Entrada:
precios = {"pan": 3000, "leche": 4500, "cafe": 12000}
#
# Salida esperada:
# "cafe"
#
# Pista:
# Puedes resolverlo recorriendo el diccionario sin usar max().
#
# ============================================================


# ============================================================
# EJERCICIO #0010
# Nivel: Nivel 2 - Básico
# Conceptos: diccionarios, transformación
#
# Problema:
# Crea un nuevo diccionario donde cada precio tenga un descuento
# del 10%. No modifiques el diccionario original.
#
# Entrada:
precios = {"pan": 100, "leche": 200, "cafe": 500}
#
# Salida esperada:
# {"pan": 90.0, "leche": 180.0, "cafe": 450.0}
#
# ============================================================


# ============================================================
# EJERCICIO #0011
# Nivel: Nivel 2 - Básico
# Conceptos: diccionarios, inversión
#
# Problema:
# Invierte las claves y valores de un diccionario.
# Supón que todos los valores son únicos.
#
# Entrada:
colores = {"rojo": "#F00", "verde": "#0F0", "azul": "#00F"}
#
# Salida esperada:
# {"#F00": "rojo", "#0F0": "verde", "#00F": "azul"}
#
# ============================================================


# ============================================================
# EJERCICIO #0012
# Nivel: Nivel 2 - Básico
# Conceptos: diccionarios, agrupación
#
# Problema:
# Agrupa palabras según su longitud.
#
# Entrada:
palabras = ["sol", "luna", "mar", "cielo", "rio"]
#
# Salida esperada:
# {3: ["sol", "mar", "rio"], 4: ["luna", "cielo"]}
#
# Regla:
# Mantén el orden original.
#
# ============================================================


# ============================================================
# EJERCICIO #0013
# Nivel: Nivel 2 - Básico
# Conceptos: diccionarios, frecuencias, strings
#
# Problema:
# Cuenta la frecuencia de cada palabra de una frase.
#
# Entrada:
frase = "python es bueno y python es util"
#
# Salida esperada:
# {"python": 2, "es": 2, "bueno": 1, "y": 1, "util": 1}
#
# Pista:
# split()
#
# ============================================================


# ============================================================
# EJERCICIO #0014
# Nivel: Nivel 2 - Básico
# Conceptos: diccionarios, valores, promedio
#
# Problema:
# Calcula el promedio de las notas almacenadas en el diccionario.
#
# Entrada:
notas = {"Ana": 8, "Luis": 5, "Eva": 9}
#
# Salida esperada:
# 7.333333333333333
#
# ============================================================


# ============================================================
# EJERCICIO #0015
# Nivel: Nivel 2 - Básico
# Conceptos: diccionarios, clasificación, listas
#
# Problema:
# Clasifica estudiantes en aprobados y reprobados.
# Se aprueba con nota >= 6.
#
# Entrada:
notas = {"Ana": 8, "Luis": 5, "Eva": 6, "Juan": 3}
#
# Salida esperada:
# {"aprobados": ["Ana", "Eva"], "reprobados": ["Luis", "Juan"]}
#
# ============================================================


# ============================================================
# EJERCICIO #0016
# Nivel: Nivel 2 - Básico
# Conceptos: diccionarios, None, limpieza
#
# Problema:
# Crea un nuevo diccionario eliminando las claves cuyo valor
# sea None.
#
# Entrada:
datos = {"id": 10, "nombre": "Ana", "telefono": None, "edad": 28}
#
# Salida esperada:
# {"id": 10, "nombre": "Ana", "edad": 28}
#
# ============================================================


# ============================================================
# EJERCICIO #0017
# Nivel: Nivel 2 - Básico
# Conceptos: diccionarios, get, validación
#
# Problema:
# Valida si un usuario y contraseña coinciden.
# Si el usuario no existe, debe devolver False.
#
# Entrada:
usuarios = {"ana": "1234", "luis": "abcd"}
usuario = "ana"
contrasena = "1234"
#
# Salida esperada:
# True
#
# ============================================================


# ============================================================
# EJERCICIO #0018
# Nivel: Nivel 2 - Básico
# Conceptos: diccionarios, listas, conteo
#
# Problema:
# Cuenta cuántas veces aparece cada ciudad en una lista.
#
# Entrada:
ciudades = ["Palmira", "Cali", "Palmira", "Buga", "Cali", "Palmira"]
#
# Salida esperada:
# {"Palmira": 3, "Cali": 2, "Buga": 1}
#
# ============================================================


# ============================================================
# EJERCICIO #0019
# Nivel: Nivel 3 - Práctico
# Conceptos: diccionarios, listas, acumuladores
#
# Problema:
# Tienes ventas con producto y cantidad. Devuelve el producto
# más vendido y la cantidad total vendida.
#
# Entrada:
ventas = [
    {"producto": "pan", "cantidad": 5},
    {"producto": "leche", "cantidad": 3},
    {"producto": "pan", "cantidad": 7},
    {"producto": "cafe", "cantidad": 4}
]
#
# Salida esperada:
# {"producto": "pan", "cantidad": 12}
#
# ============================================================


# ============================================================
# EJERCICIO #0020
# Nivel: Nivel 3 - Práctico
# Conceptos: diccionarios, listas, agrupación
#
# Problema:
# Agrupa nombres de empleados por departamento.
#
# Entrada:
empleados = [
    {"nombre": "Ana", "departamento": "TI"},
    {"nombre": "Luis", "departamento": "Ventas"},
    {"nombre": "Eva", "departamento": "TI"},
    {"nombre": "Juan", "departamento": "Ventas"}
]
#
# Salida esperada:
# {
#     "TI": ["Ana", "Eva"],
#     "Ventas": ["Luis", "Juan"]
# }
#
# ============================================================


# ============================================================
# EJERCICIO #0021
# Nivel: Nivel 3 - Práctico
# Conceptos: diccionarios, listas, filtros
#
# Problema:
# De una lista de productos, crea un diccionario que tenga como
# clave la categoría y como valor la suma de los precios.
#
# Entrada:
productos = [
    {"categoria": "fruta", "precio": 10},
    {"categoria": "fruta", "precio": 20},
    {"categoria": "verdura", "precio": 15},
    {"categoria": "verdura", "precio": 5}
]
#
# Salida esperada:
# {"fruta": 30, "verdura": 20}
#
# ============================================================


# ============================================================
# EJERCICIO #0022
# Nivel: Nivel 3 - Práctico
# Conceptos: diccionarios, listas, porcentajes
#
# Problema:
# Calcula el porcentaje de asistencia por curso.
#
# Entrada:
registros = [
    {"curso": "A", "presente": True},
    {"curso": "A", "presente": False},
    {"curso": "A", "presente": True},
    {"curso": "B", "presente": True},
    {"curso": "B", "presente": True}
]
#
# Salida esperada:
# {"A": 66.67, "B": 100.0}
#
# ============================================================


# ============================================================
# EJERCICIO #0023
# Nivel: Nivel 3 - Práctico
# Conceptos: diccionarios, ordenamiento, sorted, lambda
#
# Problema:
# Ordena un diccionario por sus valores de menor a mayor.
# Devuelve una lista de tuplas.
#
# Entrada:
precios = {"reloj": 250, "auriculares": 80, "telefono": 600}
#
# Salida esperada:
# [("auriculares", 80), ("reloj", 250), ("telefono", 600)]
#
# ============================================================


# ============================================================
# EJERCICIO #0024
# Nivel: Nivel 3 - Práctico
# Conceptos: diccionarios, listas, diferencia
#
# Problema:
# Compara dos inventarios. Devuelve los productos que necesitan
# reposición y cuántas unidades faltan.
#
# Entrada:
minimos = {"pan": 10, "leche": 8, "cafe": 5}
stock = {"pan": 7, "leche": 10, "cafe": 2}
#
# Salida esperada:
# {"pan": 3, "cafe": 3}
#
# ============================================================


# ============================================================
# EJERCICIO #0025
# Nivel: Nivel 3 - Práctico
# Conceptos: diccionarios, listas, duplicados
#
# Problema:
# Encuentra los elementos que aparecen dos o más veces.
# Devuelve una lista ordenada alfabéticamente.
#
# Entrada:
elementos = ["A", "B", "A", "C", "B", "A", "D"]
#
# Salida esperada:
# ["A", "B"]
#
# ============================================================


# ============================================================
# EJERCICIO #0026
# Nivel: Nivel 3 - Práctico
# Conceptos: diccionarios, listas anidadas, intersección
#
# Problema:
# Encuentra los gustos que comparten TODOS los usuarios.
#
# Entrada:
usuarios = {
    "Ana": ["cine", "musica", "viajes"],
    "Luis": ["musica", "cine", "libros"],
    "Eva": ["cine", "musica"]
}
#
# Salida esperada:
# ["cine", "musica"]
#
# Regla:
# Puedes usar sets, pero intenta primero entender la lógica.
#
# ============================================================


# ============================================================
# EJERCICIO #0027
# Nivel: Nivel 4 - Intermedio
# Conceptos: diccionarios, fusion, acumuladores
#
# Problema:
# Fusiona dos inventarios. Si un producto existe en ambos,
# suma sus cantidades. No modifiques los originales.
#
# Entrada:
a = {"pan": 5, "leche": 2}
b = {"leche": 3, "agua": 10}
#
# Salida esperada:
# {"pan": 5, "leche": 5, "agua": 10}
#
# ============================================================


# ============================================================
# EJERCICIO #0028
# Nivel: Nivel 4 - Intermedio
# Conceptos: diccionarios, fechas, agrupación, maximo
#
# Problema:
# Agrupa ventas por mes y devuelve el mes con mayor facturación.
#
# Entrada:
ventas = [
    {"mes": "Ene", "total": 300},
    {"mes": "Feb", "total": 500},
    {"mes": "Ene", "total": 250},
    {"mes": "Mar", "total": 700},
    {"mes": "Feb", "total": 300}
]
#
# Salida esperada:
# "Mar"
#
# ============================================================


# ============================================================
# EJERCICIO #0029
# Nivel: Nivel 4 - Intermedio
# Conceptos: diccionarios, strings, reemplazo, listas
#
# Problema:
# Reemplaza palabras de un texto utilizando un diccionario.
#
# Entrada:
texto = "el perro muerde al perro"
reemplazos = {"perro": "gato", "muerde": "juega"}
#
# Salida esperada:
# "el gato juega al gato"
#
# ============================================================


# ============================================================
# EJERCICIO #0030
# Nivel: Nivel 4 - Intermedio
# Conceptos: diccionarios anidados, recorridos anidados
#
# Problema:
# Convierte:
# {"usuario": {"mes": total}}
# en:
# {"mes": {"usuario": total}}
#
# Entrada:
datos = {
    "Ana": {"Ene": 100, "Feb": 200},
    "Luis": {"Ene": 150}
}
#
# Salida esperada:
# {
#     "Ene": {"Ana": 100, "Luis": 150},
#     "Feb": {"Ana": 200}
# }
#
# ============================================================


# ============================================================
# EJERCICIO #0031
# Nivel: Nivel 4 - Intermedio
# Conceptos: diccionarios, listas, transiciones
#
# Problema:
# Cuenta cuántas veces ocurre cada transición entre estados
# consecutivos.
#
# Entrada:
secuencia = ["iniciado", "corriendo", "pausado", "corriendo", "pausado"]
#
# Salida esperada:
# {
#     "iniciado->corriendo": 1,
#     "corriendo->pausado": 2,
#     "pausado->corriendo": 1
# }
#
# ============================================================


# ============================================================
# EJERCICIO #0032
# Nivel: Nivel 4 - Intermedio
# Conceptos: diccionarios, listas, zip, agregación
#
# Problema:
# Recibes nombres de productos, cantidades y precios.
# Calcula el valor total vendido por producto.
#
# Entrada:
productos = ["pan", "leche", "cafe"]
cantidades = [3, 2, 4]
precios = [2000, 3000, 5000]
#
# Salida esperada:
# {"pan": 6000, "leche": 6000, "cafe": 20000}
#
# ============================================================


# ============================================================
# EJERCICIO #0033
# Nivel: Nivel 4 - Intermedio
# Conceptos: diccionarios, listas, maximo, filtros
#
# Problema:
# Encuentra todos los estudiantes que obtuvieron la nota máxima.
# Si hay empate, devuelve todos.
#
# Entrada:
notas = {"Ana": 9, "Luis": 7, "Eva": 9, "Juan": 5}
#
# Salida esperada:
# ["Ana", "Eva"]
#
# ============================================================


# ============================================================
# EJERCICIO #0034
# Nivel: Nivel 4 - Intermedio
# Conceptos: diccionarios anidados, listas, busqueda
#
# Problema:
# Busca el precio de un producto dentro de una estructura
# de categorías.
#
# Entrada:
catalogo = {
    "frutas": {"manzana": 3000, "pera": 2500},
    "bebidas": {"agua": 2000, "jugo": 4000}
}
producto_buscado = "jugo"
#
# Salida esperada:
# 4000
#
# Si no existe:
# None
#
# ============================================================


# ============================================================
# EJERCICIO #0035
# Nivel: Nivel 5 - Integrador
# Conceptos: diccionarios, listas, agrupación, promedio
#
# Problema:
# De una lista de ventas, calcula el promedio de venta por
# vendedor.
#
# Entrada:
ventas = [
    {"vendedor": "Ana", "total": 100},
    {"vendedor": "Luis", "total": 200},
    {"vendedor": "Ana", "total": 300},
    {"vendedor": "Luis", "total": 100},
    {"vendedor": "Eva", "total": 150}
]
#
# Salida esperada:
# {"Ana": 200.0, "Luis": 150.0, "Eva": 150.0}
#
# ============================================================


# ============================================================
# EJERCICIO #0036
# Nivel: Nivel 5 - Integrador
# Conceptos: diccionarios, listas anidadas, acumuladores
#
# Problema:
# Una empresa tiene empleados y proyectos. Cada empleado puede
# participar en varios proyectos.
# Calcula cuántas personas participan en cada proyecto.
#
# Entrada:
empleados = {
    "Ana": ["API", "Web"],
    "Luis": ["API"],
    "Eva": ["Web", "Datos"],
    "Juan": ["API", "Datos"]
}
#
# Salida esperada:
# {"API": 3, "Web": 2, "Datos": 2}
#
# ============================================================


# ============================================================
# EJERCICIO #0037
# Nivel: Nivel 5 - Integrador
# Conceptos: diccionarios, listas, ranking, sorted
#
# Problema:
# Calcula los puntos acumulados de jugadores a partir de una
# lista de partidas y devuelve el ranking de mayor a menor.
# En empate, ordena por nombre.
#
# Entrada:
partidas = [
    {"jugador": "Ana", "puntos": 10},
    {"jugador": "Luis", "puntos": 15},
    {"jugador": "Ana", "puntos": 5},
    {"jugador": "Eva", "puntos": 15}
]
#
# Salida esperada:
# ["Eva", "Luis", "Ana"]
#
# ============================================================


# ============================================================
# EJERCICIO #0038
# Nivel: Nivel 5 - Integrador
# Conceptos: diccionarios anidados, validacion, busqueda
#
# Problema:
# Tienes una estructura de usuarios con datos anidados.
# Busca un valor recorriendo una ruta de claves.
# Si alguna clave no existe, devuelve None.
#
# Entrada:
datos = {
    "usuarios": {
        "ana": {
            "perfil": {
                "edad": 28
            }
        }
    }
}
ruta = ["usuarios", "ana", "perfil", "edad"]
#
# Salida esperada:
# 28
#
# ============================================================


# ============================================================
# EJERCICIO #0039
# Nivel: Nivel 5 - Integrador
# Conceptos: diccionarios, listas, inventario, simulacion
#
# Problema:
# Simula movimientos de inventario.
# Cada movimiento contiene producto y cantidad.
# Las cantidades pueden ser positivas (entrada) o negativas
# (salida). El stock nunca puede quedar por debajo de cero.
#
# Entrada:
stock_inicial = {"pan": 10, "leche": 5}
movimientos = [
    {"producto": "pan", "cantidad": -3},
    {"producto": "leche", "cantidad": -8},
    {"producto": "pan", "cantidad": 5},
    {"producto": "cafe", "cantidad": 4}
]
#
# Salida esperada:
# {"pan": 12, "leche": 0, "cafe": 4}
#
# ============================================================


# ============================================================
# EJERCICIO #0040
# Nivel: Nivel 5 - Integrador
# Conceptos: diccionarios, listas, tuplas, FIFO, simulacion
#
# Problema:
# Simula ventas usando inventario FIFO.
# Las compras llegan como lotes (cantidad, precio unitario).
# Una venta consume primero las unidades del lote más antiguo.
# Calcula el costo total de la venta.
#
# Entrada:
compras = [
    {"cantidad": 10, "precio": 2.0},
    {"cantidad": 5, "precio": 3.0},
    {"cantidad": 8, "precio": 4.0}
]
cantidad_vendida = 17
#
# Salida esperada:
# 41.0
#
# Explicación:
# 10 unidades x 2.0 = 20.0
# 5 unidades x 3.0 = 15.0
# 2 unidades x 4.0 = 8.0
# Total = 43.0
#
# OJO:
# El resultado correcto de este caso es 43.0.
# ============================================================