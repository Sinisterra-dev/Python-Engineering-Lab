# ============================================================
# EJERCICIOS DE LISTAS
# Total: 40 ejercicios
# ============================================================


# ============================================================
# EJERCICIO #0001
# Nivel: Nivel 1 - Inicial
# Conceptos: listas, filtros, None
#
# Problema:
# Compactar lecturas válidas eliminando valores None y
# devolviendo además los índices descartados.
#
# Entrada:
# [20, None, 22, None, 19]
#
# Salida esperada:
# {"validas": [20, 22, 19], "descartadas": [1, 3]}
#
# ============================================================
lista_entrada = [20, None, 22, None, 19]
validas = []
descartadas = []

for indice, entrada in enumerate(lista_entrada):
    if entrada is None:
        descartadas.append(indice)
    if isinstance(entrada, int):
        validas.append(entrada)
print( {"validas": validas, "descartadas": descartadas})
# ============================================================
# EJERCICIO #0002
# Nivel: Nivel 1 - Inicial
# Conceptos: listas, filtros
#
# Problema:
# Devolver únicamente temperaturas bajo cero.
#
# Entrada:
# [12, -3, 5, -1, 0]
#
# Salida esperada:
# [-3, -1]
#
# ============================================================
temperaturas = [12, -3, 5, -1, 0]
bajo_cero = []

for temperatura in temperaturas:
    if temperatura < 0:
        bajo_cero.append(temperatura)
print(bajo_cero)


# ============================================================
# EJERCICIO #0003
# Nivel: Nivel 1 - Inicial
# Conceptos: listas, índices
#
# Problema:
# Intercambiar primer y último elemento.
#
# Entrada:
# [5, 2, 8, 9]
#
# Salida esperada:
# [9, 2, 8, 5]
#
# ============================================================

valores = [5, 2, 8, 9]
primer_valor = valores[0]
ultimo_valor = valores[-1]
valores[0] = ultimo_valor
valores[-1] = primer_valor
print(valores)


# ============================================================
# EJERCICIO #0004
# Nivel: Nivel 1 - Inicial
# Conceptos: listas, búsqueda
#
# Problema:
# Contar manualmente cuántas veces aparece un valor.
#
# Entrada:
# [3, 5, 3, 2, 3], objetivo=3
#
# Salida esperada:
# 3
#
# ============================================================
lista = [3, 5, 3, 2, 3]
objetivo = 3
contador = 0
for valor in lista:
    if valor == objetivo:
        contador +=1
print(contador)
# ============================================================
# EJERCICIO #0005
# Nivel: Nivel 1 - Inicial
# Conceptos: listas, transformaciones
#
# Problema:
# Reemplazar todos los negativos por cero.
#
# Entrada:
# [10, -5, 20, -3]
#
# Salida esperada:
# [10, 0, 20, 0]
#
# ============================================================
lista = [10, -5, 20, -3]
salida = []
for valor in lista:
    if valor< 0:
        valor = 0
        salida.append(valor)
    else:
        salida.append(valor)
print(salida)

# ============================================================
# EJERCICIO #0006
# Nivel: Nivel 1 - Inicial
# Conceptos: listas, orden inverso
#
# Problema:
# Invertir una lista sin modificar la original.
#
# Entrada:
# ["sol", "luna", "estrella"]
#
# Salida esperada:
# ["estrella", "luna", "sol"]
#
# ============================================================
lista = ["sol", "luna", "estrella"]
lista_inversa = reversed(lista)
lista_lista = list(lista_inversa)
print(lista_lista)

##Slicing
lista = ["sol", "luna", "estrella"]
lista_inversa = lista[::-1]
print("Inversa:", lista_inversa)
print("Original:", lista)

# Salida:
# Inversa: ['estrella', 'luna', 'sol']
# Original: ['sol', 'luna', 'estrella']

# ============================================================
# EJERCICIO #0007
# Nivel: Nivel 2 - Básico
# Conceptos: listas, promedios
#
# Problema:
# Calcular promedio de aprobados.
#
# Entrada:
# [4, 7, 8, 2, 9]
#
# Salida esperada:
# 8.0
#
# ============================================================
lista = [4, 7, 8, 2, 9]
sumadetodas = 0
aprobados = 0
for valor in lista:
    if valor > 5:
        sumadetodas += valor
        aprobados += 1
print(sumadetodas)
promedio = sumadetodas / aprobados
print(promedio)

# ============================================================
# EJERCICIO #0008
# Nivel: Nivel 2 - Básico
# Conceptos: listas, índices
#
# Problema:
# Sumar elementos ubicados en posiciones pares.
#
# Entrada:
# [10, 20, 30, 40, 50]
#
# Salida esperada:
# 90
#
# ============================================================
lista =  [10, 20, 30, 40, 50]
pares = []


for i,valor in enumerate(lista):
    if i % 2 == 0:
        pares.append(valor)
resultado = sum(pares)
print(pares)
print(resultado)






# ============================================================
# EJERCICIO #0009
# Nivel: Nivel 2 - Básico
# Conceptos: listas, duplicados
#
# Problema:
# Eliminar duplicados manteniendo el orden original.
#
# Entrada:
# [1, 2, 1, 3, 2]
#
# Salida esperada:
# [1, 2, 3]
#
# ============================================================

lista = [1, 2, 1, 3, 2]
sin_duplicar = []

for valor in lista:
    if valor not in sin_duplicar:
        sin_duplicar.append(valor)
print(sin_duplicar)

# ============================================================
# EJERCICIO #0010
# Nivel: Nivel 2 - Básico
# Conceptos: listas, extremos
#
# Problema:
# Obtener el segundo valor más grande ignorando duplicados.
#
# Entrada:
# [10, 40, 30, 40, 20]
#
# Salida esperada:
# 30
#
# ============================================================


# ============================================================
# EJERCICIO #0011
# Nivel: Nivel 2 - Básico
# Conceptos: listas, validación
#
# Problema:
# Determinar si la lista está ordenada ascendentemente.
#
# Entrada:
# [1, 3, 5, 4]
#
# Salida esperada:
# False
#
# ============================================================
# Entrada del ejercicio
lista = [1, 3, 5, 4]

# Variable para guardar el resultado final
ordenada = True

# Comparamos cada elemento con el siguiente usando un bucle
for i in range(len(lista) - 1):
    if lista[i] > lista[i + 1]:
        ordenada = False
        break  # Rompemos el bucle porque ya sabemos que es False

# Salida esperada
print(ordenada)


# ============================================================
# EJERCICIO #0012
# Nivel: Nivel 2 - Básico
# Conceptos: listas, palíndromos
#
# Problema:
# Determinar si una lista es palíndroma.
#
# Entrada:
# [1, 2, 3, 2, 1]
#
# Salida esperada:
# True
#
# ============================================================
lista = [1, 2, 3, 2, 1]
lista_revertida = reversed(lista)
lista_realmente_invertida = list(lista_revertida)
print(lista_realmente_invertida)

polindormo = False
if lista == lista_realmente_invertida:
    polindormo = True
print(polindormo)



# ============================================================
# EJERCICIO #0013
# Nivel: Nivel 2 - Básico
# Conceptos: listas, intersecciones
#
# Problema:
# Obtener elementos comunes sin duplicados.
#
# Entrada:
# [1, 2, 3] y [2, 3, 4]
#
# Salida esperada:
# [2, 3]
#
# ============================================================


# ============================================================
# EJERCICIO #0014
# Nivel: Nivel 2 - Básico
# Conceptos: listas, frecuencias
#
# Problema:
# Contar frecuencia de aparición de cada elemento.
#
# Entrada:
# [1, 2, 1, 3, 2, 1]
#
# Salida esperada:
# {1: 3, 2: 2, 3: 1}
#
# ============================================================


# ============================================================
# EJERCICIO #0015
# Nivel: Nivel 2 - Básico
# Conceptos: listas, agrupaciones
#
# Problema:
# Agrupar números en pares e impares.
#
# Entrada:
# [1, 2, 3, 4, 5]
#
# Salida esperada:
# {"pares": [2, 4], "impares": [1, 3, 5]}
#
# ============================================================


# ============================================================
# EJERCICIO #0016
# Nivel: Nivel 3 - Práctico
# Conceptos: listas, rotaciones
#
# Problema:
# Rotar una posición a la derecha.
#
# Entrada:
# [1, 2, 3, 4]
#
# Salida esperada:
# [4, 1, 2, 3]
#
# ============================================================


# ============================================================
# EJERCICIO #0017
# Nivel: Nivel 3 - Práctico
# Conceptos: listas, inserción ordenada
#
# Problema:
# Insertar un valor manteniendo el orden ascendente.
#
# Entrada:
# [1, 3, 5, 7], valor=4
#
# Salida esperada:
# [1, 3, 4, 5, 7]
#
# ============================================================


# ============================================================
# EJERCICIO #0018
# Nivel: Nivel 3 - Práctico
# Conceptos: listas, mezcla
#
# Problema:
# Intercalar dos listas del mismo tamaño.
#
# Entrada:
# [1, 3, 5] y [2, 4, 6]
#
# Salida:
# [1, 2, 3, 4, 5, 6]
#
# ============================================================


# ============================================================
# EJERCICIO #0019
# Nivel: Nivel 3 - Práctico
# Conceptos: listas, filtros, strings
#
# Problema:
# Filtrar palabras largas y ordenarlas alfabéticamente.
#
# Entrada:
# ["sol", "estrella", "luz", "nube"], min=4
#
# Salida esperada:
# ["estrella", "nube"]
#
# ============================================================


# ============================================================
# EJERCICIO #0020
# Nivel: Nivel 3 - Práctico
# Conceptos: listas, ventanas deslizantes
#
# Problema:
# Obtener la suma de cada ventana de tamaño k.
#
# Entrada:
# [1, 2, 3, 4, 5], k=3
#
# Salida esperada:
# [6, 9, 12]
#
# ============================================================


# ============================================================
# EJERCICIO #0021
# Nivel: Nivel 3 - Práctico
# Conceptos: listas, colas
#
# Problema:
# Priorizar clientes urgentes manteniendo orden relativo.
#
# Entrada:
# cola=["Ana", "Luis", "Eva", "Juan"]
#
# Salida esperada:
# ["Ana", "Eva", "Luis", "Juan"]
#
# ============================================================


# ============================================================
# EJERCICIO #0022
# Nivel: Nivel 3 - Práctico
# Conceptos: listas, rachas
#
# Problema:
# Calcular la mayor racha consecutiva de ventas menores a 10.
#
# Entrada:
# [12, 4, 3, 15, 2, 1, 0]
#
# Salida esperada:
# 3
#
# ============================================================


# ============================================================
# EJERCICIO #0023
# Nivel: Nivel 4 - Intermedio
# Conceptos: listas, chunks
#
# Problema:
# Dividir una lista en bloques de tamaño fijo.
#
# Entrada:
# [1, 2, 3, 4, 5], tamaño=2
#
# Salida esperada:
# [[1, 2], [3, 4], [5]]
#
# ============================================================


# ============================================================
# EJERCICIO #0024
# Nivel: Nivel 4 - Intermedio
# Conceptos: listas, compresión
#
# Problema:
# Eliminar repeticiones consecutivas.
#
# Entrada:
# ["a", "a", "b", "a", "a"]
#
# Salida esperada:
# ["a", "b", "a"]
#
# ============================================================


# ============================================================
# EJERCICIO #0025
# Nivel: Nivel 4 - Intermedio
# Conceptos: listas, merge
#
# Problema:
# Mezclar dos listas ordenadas conservando el orden final.
#
# Entrada:
# [1, 5, 8] y [2, 6, 7]
#
# Salida esperada:
# [1, 2, 5, 6, 7, 8]
#
# ============================================================


# ============================================================
# EJERCICIO #0026
# Nivel: Nivel 4 - Intermedio
# Conceptos: listas, estabilidad
#
# Problema:
# Mover todos los ceros al final conservando el orden relativo.
#
# Entrada:
# [0, 1, 0, 3, 12]
#
# Salida esperada:
# [1, 3, 12, 0, 0]
#
# ============================================================


# ============================================================
# EJERCICIO #0027
# Nivel: Nivel 4 - Intermedio
# Conceptos: matrices
#
# Problema:
# Transponer una matriz 2D.
#
# Entrada:
# [[1, 2], [3, 4], [5, 6]]
#
# Salida esperada:
# [[1, 3, 5], [2, 4, 6]]
#
# ============================================================


# ============================================================
# EJERCICIO #0028
# Nivel: Nivel 4 - Intermedio
# Conceptos: listas, sublistas
#
# Problema:
# Determinar si una lista aparece consecutivamente dentro de otra.
#
# Entrada:
# [1, 2, 3, 4, 5], sub=[2, 3, 4]
#
# Salida esperada:
# True
#
# ============================================================


# ============================================================
# EJERCICIO #0029
# Nivel: Nivel 5 - Integrador
# Conceptos: simulación
#
# Problema:
# Mantener historial de stock evitando valores negativos.
#
# Entrada:
# stock=10, movimientos=[-2, 5, -20, 4]
#
# Salida esperada:
# [8, 13, 0, 4]
#
# ============================================================


# ============================================================
# EJERCICIO #0030
# Nivel: Nivel 5 - Integrador
# Conceptos: algoritmos, subarreglos
#
# Problema:
# Encontrar la suma máxima de un subarreglo contiguo (Kadane).
#
# Entrada:
# [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#
# Salida esperada:
# 6
#
# ============================================================


# ============================================================
# EJERCICIO #0031
# Nivel: Nivel 2 - Básico
# Conceptos: listas, filtros, strings
#
# Problema:
# Filtrar strings por longitud y devolver una tupla con la lista
# de filtrados (longitud >= 4) y la lista de descartados.
#
# Entrada:
# ["ana", "pedro", "luis", "ir"]
#
# Salida esperada:
# (["pedro", "luis"], ["ana", "ir"])
#
# ============================================================


# ============================================================
# EJERCICIO #0032
# Nivel: Nivel 2 - Básico
# Conceptos: listas, índices, eliminación
#
# Problema:
# Eliminar elementos en índices impares de una lista y devolver
# la lista resultante.
#
# Entrada:
# [10, 20, 30, 40, 50]
#
# Salida esperada:
# [10, 30, 50]
#
# ============================================================


# ============================================================
# EJERCICIO #0033
# Nivel: Nivel 3 - Práctico
# Conceptos: listas, flotantes, normalización
#
# Problema:
# Normalizar una lista de flotantes dividiendo cada elemento por
# el máximo valor de la lista.
#
# Devuelve lista vacía si la lista original está vacía o si el
# máximo es cero.
#
# Entrada:
# [2.0, 5.0, 10.0]
#
# Salida esperada:
# [0.2, 0.5, 1.0]
#
# ============================================================


# ============================================================
# EJERCICIO #0034
# Nivel: Nivel 4 - Intermedio
# Conceptos: listas, agrupación
#
# Problema:
# Agrupar elementos contiguos iguales en sublistas.
#
# Entrada:
# [1, 1, 2, 3, 3, 3, 2]
#
# Salida esperada:
# [[1, 1], [2], [3, 3, 3], [2]]
#
# ============================================================


# ============================================================
# EJERCICIO #0035
# Nivel: Nivel 3 - Práctico
# Conceptos: listas, búsqueda, parejas
#
# Problema:
# Encontrar todos los pares únicos de números en una lista que
# sumen un valor objetivo.
#
# Devolver una lista de tuplas ordenadas por el primer elemento.
#
# Entrada:
# [2, 4, 3, 5, 7, 8, 9], objetivo=11
#
# Salida esperada:
# [(2, 9), (3, 8), (4, 7)]
#
# ============================================================


# ============================================================
# EJERCICIO #0036
# Nivel: Nivel 3 - Práctico
# Conceptos: listas, diferencias
#
# Problema:
# Operar diferencias consecutivas (de primer orden) entre
# elementos adyacentes de una lista.
#
# Entrada:
# [1, 3, 7, 12]
#
# Salida esperada:
# [2, 4, 5]
#
# ============================================================


# ============================================================
# EJERCICIO #0037
# Nivel: Nivel 4 - Intermedio
# Conceptos: listas, algoritmos
#
# Problema:
# Encontrar el primer elemento "pico".
#
# Un elemento pico es mayor que sus vecinos adyacentes inmediatos.
# Considera los extremos comparando solo con su vecino directo.
#
# Devolver el índice.
#
# Entrada:
# [1, 3, 20, 4, 1, 0]
#
# Salida esperada:
# 2
#
# ============================================================


# ============================================================
# EJERCICIO #0038
# Nivel: Nivel 3 - Práctico
# Conceptos: listas, rotación
#
# Problema:
# Rotar una lista K posiciones a la izquierda de forma circular.
#
# Entrada:
# [1, 2, 3, 4, 5], k=2
#
# Salida esperada:
# [3, 4, 5, 1, 2]
#
# ============================================================


# ============================================================
# EJERCICIO #0039
# Nivel: Nivel 4 - Intermedio
# Conceptos: listas, compresión, RLE
#
# Problema:
# Comprimir una lista por longitud de rachas consecutivas
# (Run-Length Encoding) devolviendo una lista de tuplas
# (elemento, cantidad).
#
# Entrada:
# ["A", "A", "B", "C", "C", "C"]
#
# Salida esperada:
# [("A", 2), ("B", 1), ("C", 3)]
#
# ============================================================


# ============================================================
# EJERCICIO #0040
# Nivel: Nivel 3 - Práctico
# Conceptos: listas, intersección
#
# Problema:
# Encontrar la intersección de dos listas desordenadas
# conservando el orden de aparición de la primera lista
# y sin usar conjuntos (sets).
#
# Entrada:
# [4, 2, 9, 7, 5] y [9, 5, 1, 4]
#
# Salida esperada:
# [4, 9, 5]
#
# ============================================================