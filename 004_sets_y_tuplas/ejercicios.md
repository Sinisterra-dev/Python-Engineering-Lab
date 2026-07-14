# Ejercicios - Sets y tuplas

Total del modulo: **22 ejercicios**.

Esta version prioriza variedad real sobre cantidad. Se eliminaron bloques con entrada/salida repetidas para cumplir la regla absoluta de no repeticion.

## Ejercicio #0001 (Modulo 004_sets_y_tuplas - #001)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** sets, diferencia
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Usuarios nuevos (variante base). Devuelve usuarios que aparecen hoy pero no ayer. Resuelve exactamente el caso indicado.
- **Entrada:** `ayer = ["ana", "luis"]; hoy = ["ana", "eva", "zoe"]`
- **Salida esperada:** `["eva", "zoe"]`
- **Reglas:** Ordena la salida. Resuelve exactamente el caso indicado.
- **Pista opcional:** Usa diferencia de sets.

## Ejercicio #0002 (Modulo 004_sets_y_tuplas - #002)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** tuplas, duplicados
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Coordenadas repetidas (variante base). Devuelve coordenadas repetidas una sola vez. Resuelve exactamente el caso indicado.
- **Entrada:** `puntos = [(1,2), (3,4), (1,2), (5,5), (3,4)]`
- **Salida esperada:** `[(1, 2), (3, 4)]`
- **Reglas:** Conserva orden de primera repeticion. Resuelve exactamente el caso indicado.
- **Pista opcional:** Usa vistos y repetidos.

## Ejercicio #0003 (Modulo 004_sets_y_tuplas - #003)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** sets, interseccion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Etiquetas compartidas (variante base). Devuelve etiquetas comunes entre dos productos. Resuelve exactamente el caso indicado.
- **Entrada:** `a = ["frio", "bebida"]; b = ["bebida", "promo", "frio"]`
- **Salida esperada:** `["bebida", "frio"]`
- **Reglas:** Ordena alfabeticamente. Resuelve exactamente el caso indicado.
- **Pista opcional:** Intersecciona sets.

## Ejercicio #0004 (Modulo 004_sets_y_tuplas - #004)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** sets, unicidad
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Elementos unicos. Devuelve los elementos únicos de una lista desordenada como un set de Python.
- **Entrada:** `lista = [1, 2, 2, 3, 4, 4]`
- **Salida esperada:** `{1, 2, 3, 4}`
- **Reglas:** Retorna un tipo de datos set.
- **Pista opcional:** El constructor set() elimina duplicados de una lista.

## Ejercicio #0005 (Modulo 004_sets_y_tuplas - #005)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** sets, diferencia simetrica
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Diferencia simetrica de usuarios. Devuelve los elementos que pertenecen al grupo A o al grupo B, pero no a ambos.
- **Entrada:** `grupo_a = {"admin", "editor"}; grupo_b = {"editor", "viewer"}`
- **Salida esperada:** `{"admin", "viewer"}`
- **Reglas:** Retorna un set.
- **Pista opcional:** Usa el operador ^ o symmetric_difference().

## Ejercicio #0006 (Modulo 004_sets_y_tuplas - #006)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** sets, subconjuntos
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Requisitos de herramientas. Comprueba si todas las herramientas requeridas para un trabajo están disponibles en la caja de herramientas.
- **Entrada:** `requeridas = {"martillo", "destornillador"}; caja = {"martillo", "destornillador", "pinza"}`
- **Salida esperada:** `True`
- **Reglas:** Usa operadores de comparación de sets.
- **Pista opcional:** issubset() o <= ayuda.

## Ejercicio #0007 (Modulo 004_sets_y_tuplas - #007)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** tuplas, zip
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Emparejar coordenadas. Combina dos listas paralelas de coordenadas X e Y en una lista de tuplas (X, Y).
- **Entrada:** `x = [1, 2, 3]; y = [10, 20, 30]`
- **Salida esperada:** `[(1, 10), (2, 20), (3, 30)]`
- **Reglas:** Deben combinarse en orden posicional.
- **Pista opcional:** La función zip() genera tuplas combinadas.

## Ejercicio #0008 (Modulo 004_sets_y_tuplas - #008)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** sets, interseccion multiple
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Interseccion de multiples sets. Encuentra los elementos que son comunes a tres conjuntos de datos.
- **Entrada:** `set1 = {1, 2, 3}; set2 = {2, 3, 4}; set3 = {3, 4, 5}`
- **Salida esperada:** `{3}`
- **Reglas:** Debe retornar un set.
- **Pista opcional:** Encadena intersection() o el operador &.

## Ejercicio #0009 (Modulo 004_sets_y_tuplas - #009)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** tuplas, duplicados, sets
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Duplicados sin importar orden. Elimina tuplas duplicadas de una lista sin importar el orden de sus elementos (es decir, (1, 2) y (2, 1) se consideran iguales).
- **Entrada:** `tuplas = [(1, 2), (3, 4), (2, 1)]`
- **Salida esperada:** `[(1, 2), (3, 4)]`
- **Reglas:** Conserva el primer elemento que apareció.
- **Pista opcional:** Convierte temporalmente cada tupla a un set congelado (frozenset) para revisar si ya lo has visto.

## Ejercicio #0010 (Modulo 004_sets_y_tuplas - #010)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** sets, strings, pangramas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Comprobar si es pangrama. Verifica si un string contiene todas las letras del abecedario inglés (a-z).
- **Entrada:** `texto = "the quick brown fox jumps over the lazy dog"`
- **Salida esperada:** `True`
- **Reglas:** Ignora espacios y mayúsculas.
- **Pista opcional:** Compara el set del texto (filtrando sólo letras) con el set del abecedario.

## Ejercicio #0011 (Modulo 004_sets_y_tuplas - #011)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** tuplas, matematicas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Distancia Manhattan. Dadas dos tuplas de coordenadas 2D (x, y), calcula su distancia Manhattan.
- **Entrada:** `p1 = (1, 5); p2 = (4, 1)`
- **Salida esperada:** `7`
- **Reglas:** La distancia es |x1 - x2| + |y1 - y2|.
- **Pista opcional:** Usa la función abs().

## Ejercicio #0012 (Modulo 004_sets_y_tuplas - #012)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** sets, eliminacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Remover bloqueados. Quita un conjunto de usuarios bloqueados de un conjunto de usuarios autorizados.
- **Entrada:** `autorizados = {"ana", "luis", "eva"}; bloqueados = {"luis", "pedro"}`
- **Salida esperada:** `{"ana", "eva"}`
- **Reglas:** Usa diferencia de sets.
- **Pista opcional:** El operador - realiza la diferencia de conjuntos.

## Ejercicio #0013 (Modulo 004_sets_y_tuplas - #013)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** sets, strings, conteo
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Palabras unicas en parrafo. Cuenta cuántas palabras únicas tiene una frase sin importar signos de puntuación como puntos o comas.
- **Entrada:** `frase = "hola, mundo. hola de nuevo."`
- **Salida esperada:** `4`
- **Reglas:** Limpia los caracteres de puntuación antes de separar. Las palabras únicas en este caso son "hola", "mundo", "de", "nuevo".
- **Pista opcional:** Reemplaza los signos por strings vacíos y luego aplica set().

## Ejercicio #0014 (Modulo 004_sets_y_tuplas - #014)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** tuplas, diccionarios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Tuplas como llaves. Crea un diccionario de distancias entre ciudades a partir de una lista de tuplas con el formato (origen, destino, distancia), usando (origen, destino) como llave.
- **Entrada:** `rutas = [("Madrid", "Barcelona", 620), ("Barcelona", "Valencia", 350)]`
- **Salida esperada:** `{("Madrid", "Barcelona"): 620, ("Barcelona", "Valencia"): 350}`
- **Reglas:** Las tuplas son inmutables y por tanto hashables, válidas como claves.
- **Pista opcional:** Itera desempaquetando cada ruta.

## Ejercicio #0015 (Modulo 004_sets_y_tuplas - #015)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** sets, interseccion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Usuarios activos consecutivos. Encuentra los usuarios que estuvieron activos tanto el lunes como el martes y el miércoles.
- **Entrada:** `lunes = {"ana", "luis"}; martes = {"luis", "eva"}; miercoles = {"luis", "pedro"}`
- **Salida esperada:** `{"luis"}`
- **Reglas:** Retorna un set.
- **Pista opcional:** Intersecciona los tres conjuntos de nombres.

## Ejercicio #0016 (Modulo 004_sets_y_tuplas - #016)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** sets, disjuntos
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Comprobar catalogos independientes. Verifica si dos listas de IDs de productos no comparten absolutamente ningún elemento en común.
- **Entrada:** `cat1 = [101, 102, 103]; cat2 = [201, 202]`
- **Salida esperada:** `True`
- **Reglas:** Utiliza métodos de conjuntos.
- **Pista opcional:** isdisjoint() devuelve True si la intersección está vacía.

## Ejercicio #0017 (Modulo 004_sets_y_tuplas - #017)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** tuplas, desempaquetado
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Calcular total de inventario. Recibe una lista de tuplas con el formato (nombre_item, cantidad, precio_unitario) y calcula el valor total de todas las existencias.
- **Entrada:** `inventario = [("tornillo", 100, 0.5), ("tuerca", 50, 0.8)]`
- **Salida esperada:** `90.0`
- **Reglas:** Suma cantidad * precio_unitario por cada tupla.
- **Pista opcional:** Usa un bucle for desempaquetando cada tupla.

## Ejercicio #0018 (Modulo 004_sets_y_tuplas - #018)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** sets, strings, busqueda
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Letra faltante en secuencia. Encuentra la única letra minúscula que falta para completar una secuencia consecutiva desde la primera a la última letra presente.
- **Entrada:** `secuencia = "abce"`
- **Salida esperada:** `"d"`
- **Reglas:** La secuencia original está ordenada pero le falta un elemento.
- **Pista opcional:** Crea un set de letras completo entre el valor mínimo y máximo y calcula la diferencia con el set de la entrada.

## Ejercicio #0019 (Modulo 004_sets_y_tuplas - #019)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** sets, union
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Union de catalogos. Combina las categorías de productos de dos departamentos en una sola colección única.
- **Entrada:** `dep_a = {"hogar", "cocina"}; dep_b = {"cocina", "jardin"}`
- **Salida esperada:** `{"hogar", "cocina", "jardin"}`
- **Reglas:** Retorna un set.
- **Pista opcional:** El operador | realiza la unión de conjuntos.

## Ejercicio #0020 (Modulo 004_sets_y_tuplas - #020)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** tuplas, estadisticas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Resumen estadistico. Recibe una lista de números y devuelve una tupla con (mínimo, máximo, promedio).
- **Entrada:** `numeros = [10, 20, 30, 40]`
- **Salida esperada:** `(10, 40, 25.0)`
- **Reglas:** La salida debe ser exactamente una tupla de tres elementos.
- **Pista opcional:** Usa min(), max() y sum()/len() para construir la tupla.

## Ejercicio #0021 (Modulo 004_sets_y_tuplas - #021)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** sets, strings, filtros
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Filtro de caracteres permitidos. Comprueba si un string contiene únicamente caracteres incluidos en un set de caracteres válidos.
- **Entrada:** `texto = "10010"; validos = {"0", "1"}`
- **Salida esperada:** `True`
- **Reglas:** El string completo debe coincidir.
- **Pista opcional:** Compara si el set de caracteres del texto es un subconjunto del set de caracteres válidos.

## Ejercicio #0022 (Modulo 004_sets_y_tuplas - #022)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** sets, particion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Particionar en pares e impares. Divide un conjunto de números enteros en dos conjuntos: uno de números pares y otro de impares.
- **Entrada:** `numeros = {1, 2, 3, 4, 5}`
- **Salida esperada:** `({2, 4}, {1, 3, 5})`
- **Reglas:** Retorna una tupla conteniendo los dos sets.
- **Pista opcional:** Itera sobre el conjunto inicial y clasifica en dos conjuntos vacíos.
