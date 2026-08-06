# ============================================================
# CLASE DE DICCIONARIOS EN PYTHON
# De cero a resolver los ejercicios del modulo
# ============================================================

# 1. ¿QUE ES UN DICCIONARIO?
# Guarda pares CLAVE -> VALOR.

persona = {"nombre": "Ana", "edad": 28, "ciudad": "Palmira"}
print(persona)

# 2. ACCEDER A VALORES
print(persona["nombre"])
print(persona["edad"])

# 3. MODIFICAR Y AGREGAR
persona["edad"] = 29
persona["profesion"] = "Programador"
print(persona)

# 4. ELIMINAR
del persona["ciudad"]
print(persona)

# 5. COMPROBAR SI EXISTE UNA CLAVE
print("nombre" in persona)
print("telefono" in persona)

# 6. .get()
print(persona.get("telefono"))
print(persona.get("telefono", "No registrado")) #No modifica el diccionario
print(persona)

# 7. RECORRER CLAVES
for clave in persona:
    print(clave)

# 8. RECORRER VALORES
for valor in persona.values():
    print(valor)

# 9. RECORRER CLAVE Y VALOR
for clave, valor in persona.items():
    print(clave, "->", valor)

# 10. LEN
print(len(persona))

# 11. UPDATE
persona.update({"edad": 30, "pais": "Colombia"})
print(persona)

# 12. COPY
original = {"a": 10, "b": 20}
copia = original.copy()
copia["a"] = 999
print(original)
print(copia)

# 13. VALORES DE DIFERENTES TIPOS
usuario = {
    "nombre": "Luis",
    "edad": 25,
    "habilidades": ["Python", "SQL"],
    "activo": True
}
print(usuario)

# 14. LISTAS DENTRO DE DICCIONARIOS
usuario["habilidades"].append("Docker")
print(usuario["habilidades"])
print(usuario["habilidades"][0])

# 15. DICCIONARIOS ANIDADOS
empresa = {
    "nombre": "Tech SAS",
    "direccion": {"ciudad": "Palmira", "pais": "Colombia"}
}
print(empresa["direccion"]["ciudad"])

# 16. DICCIONARIOS DENTRO DE LISTAS
usuarios = [
    {"nombre": "Ana", "edad": 28},
    {"nombre": "Luis", "edad": 31},
    {"nombre": "Eva", "edad": 22}
]
print(usuarios[0]["nombre"])

# 17. RECORRER LISTA DE DICCIONARIOS
for usuario in usuarios:
    print(usuario["nombre"], usuario["edad"])

# 18. FILTRAR
mayores = []
for usuario in usuarios:
    if usuario["edad"] >= 25:
        mayores.append(usuario["nombre"])
print(mayores)

# 19. ACUMULAR VALORES
ventas = {"lunes": 100, "martes": 250, "miercoles": 150}
total = 0
for venta in ventas.values():
    total += venta
print(total)

# 20. CONTAR CON DICCIONARIOS
frutas = ["manzana", "pera", "manzana", "uva", "pera", "manzana"]
frecuencias = {}
for fruta in frutas:
    if fruta in frecuencias:
        frecuencias[fruta] += 1
    else:
        frecuencias[fruta] = 1
print(frecuencias)

# 21. EL MISMO PATRON CON .get()
frecuencias = {}
for fruta in frutas:
    frecuencias[fruta] = frecuencias.get(fruta, 0) + 1
print(frecuencias)

# 22. AGRUPAR ELEMENTOS
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

# 23. ACUMULAR POR CATEGORIA
ventas = [
    {"producto": "pan", "cantidad": 2},
    {"producto": "pan", "cantidad": 3},
    {"producto": "leche", "cantidad": 4}
]
totales = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    if producto in totales:
        totales[producto] += cantidad
    else:
        totales[producto] = cantidad
print(totales)

# 24. DICCIONARIO + ZIP
nombres = ["Ana", "Luis", "Eva"]
edades = [28, 31, 22]
personas = {}
for nombre, edad in zip(nombres, edades):
    personas[nombre] = edad
print(personas)

# 25. ZIP + CALCULOS
productos = ["pan", "leche", "cafe"]
cantidades = [3, 2, 4]
precios = [2000, 3000, 5000]
totales = {}
for producto, cantidad, precio in zip(productos, cantidades, precios):
    totales[producto] = cantidad * precio
print(totales)

# 26. MAXIMO Y MINIMO MANUAL
precios = {"pan": 3000, "leche": 4500, "cafe": 12000}
producto_mayor = None
precio_mayor = None

for producto, precio in precios.items():
    if precio_mayor is None or precio > precio_mayor:
        precio_mayor = precio
        producto_mayor = producto

print(producto_mayor, precio_mayor)

# 27. ORDENAR CON sorted() + items()
precios = {"reloj": 250, "auriculares": 80, "telefono": 600}
ordenados = sorted(precios.items(), key=lambda x: x[1])
print(ordenados)

# 28. ORDENAR DE MAYOR A MENOR
ordenados = sorted(precios.items(), key=lambda x: x[1], reverse=True)
print(ordenados)

# 29. DICCIONARIOS ANIDADOS
datos = {
    "usuarios": {
        "ana": {"edad": 28, "ciudad": "Palmira"},
        "luis": {"edad": 31, "ciudad": "Cali"}
    }
}
print(datos["usuarios"]["ana"]["edad"])

# 30. RECORRER DICCIONARIO ANIDADO
for nombre, datos_usuario in datos["usuarios"].items():
    print(nombre, datos_usuario["edad"])

# 31. BUSCAR EN ESTRUCTURA ANIDADA
catalogo = {
    "frutas": {"manzana": 3000, "pera": 2500},
    "bebidas": {"agua": 2000, "jugo": 4000}
}
buscado = "jugo"
encontrado = None

for categoria, productos in catalogo.items():
    if buscado in productos:
        encontrado = productos[buscado]
        break

print(encontrado)

# 32. COMPARAR DOS DICCIONARIOS
stock = {"pan": 7, "leche": 10, "cafe": 2}
minimos = {"pan": 10, "leche": 8, "cafe": 5}
faltantes = {}

for producto, minimo in minimos.items():
    actual = stock.get(producto, 0)
    if actual < minimo:
        faltantes[producto] = minimo - actual

print(faltantes)

# 33. FUSIONAR DICCIONARIOS SUMANDO VALORES
a = {"pan": 5, "leche": 2}
b = {"leche": 3, "agua": 10}
fusionado = {}

for producto, cantidad in a.items():
    fusionado[producto] = cantidad

for producto, cantidad in b.items():
    if producto in fusionado:
        fusionado[producto] += cantidad
    else:
        fusionado[producto] = cantidad

print(fusionado)

# 34. PROMEDIO POR GRUPO
ventas = [
    {"vendedor": "Ana", "total": 100},
    {"vendedor": "Luis", "total": 200},
    {"vendedor": "Ana", "total": 300},
    {"vendedor": "Luis", "total": 100}
]

totales = {}
cantidades = {}

for venta in ventas:
    vendedor = venta["vendedor"]
    total = venta["total"]

    if vendedor not in totales:
        totales[vendedor] = 0
        cantidades[vendedor] = 0

    totales[vendedor] += total
    cantidades[vendedor] += 1

promedios = {}
for vendedor in totales:
    promedios[vendedor] = totales[vendedor] / cantidades[vendedor]

print(promedios)

# 35. DICCIONARIOS COMO CONTADORES DE ESTADOS
estados = ["ok", "error", "ok", "pendiente", "error", "ok"]
conteo = {}

for estado in estados:
    conteo[estado] = conteo.get(estado, 0) + 1

print(conteo)

# 36. DICCIONARIO COMO INDICE
usuarios = [
    {"id": 101, "nombre": "Ana"},
    {"id": 102, "nombre": "Luis"},
    {"id": 103, "nombre": "Eva"}
]
por_id = {}

for usuario in usuarios:
    por_id[usuario["id"]] = usuario

print(por_id[102])

# 37. COMPRENSION DE DICCIONARIOS
precios = {"pan": 100, "leche": 200, "cafe": 500}
descuentos = {
    producto: precio * 0.9
    for producto, precio in precios.items()
}
print(descuentos)

# 38. LISTA DE DICCIONARIOS + sorted + lambda
jugadores = [
    {"nombre": "Ana", "puntos": 30},
    {"nombre": "Luis", "puntos": 50},
    {"nombre": "Eva", "puntos": 40}
]
ranking = sorted(
    jugadores,
    key=lambda jugador: jugador["puntos"],
    reverse=True
)
print(ranking)

# 39. PATRONES PARA IDENTIFICAR EN EJERCICIOS
#
# BUSCAR      -> in / get()
# CONTAR      -> diccionario de frecuencias
# ACUMULAR    -> diccionario de totales
# AGRUPAR     -> diccionario con listas
# FILTRAR     -> for + if + lista resultado
# MAX/MIN     -> variable de mejor valor + comparación
# ORDENAR     -> sorted() + key
# ZIP         -> combinar listas paralelas
# ANIDAR      -> listas/diccionarios dentro de otros
# TRANSFORMAR -> crear un nuevo diccionario

# ============================================================
# RETO FINAL
# ============================================================
#
# Resuelve SIN copiar los ejemplos anteriores.
#
# Tienes ventas:
#
ventas = [
    {"vendedor": "Ana", "producto": "pan", "cantidad": 3, "precio": 2000},
    {"vendedor": "Luis", "producto": "leche", "cantidad": 2, "precio": 3000},
    {"vendedor": "Ana", "producto": "cafe", "cantidad": 4, "precio": 5000},
    {"vendedor": "Luis", "producto": "pan", "cantidad": 5, "precio": 2000},
    {"vendedor": "Ana", "producto": "pan", "cantidad": 2, "precio": 2000}
]
#
# Construye:
#
# {
#     "ventas_por_vendedor": ...,
#     "unidades_por_producto": ...,
#     "producto_mas_vendido": ...
# }
#
# Debes:
# 1. Calcular total de cada venta.
# 2. Acumular ventas por vendedor.
# 3. Acumular unidades por producto.
# 4. Encontrar manualmente el producto con más unidades.
#
# ============================================================
# FIN DE LA CLASE
# ============================================================
