# Ejercicios - Diccionarios

Total del modulo: **35 ejercicios**.

Esta version prioriza variedad real sobre cantidad. Se eliminaron bloques con entrada/salida repetidas para cumplir la regla absoluta de no repeticion.

## Ejercicio #0001 (Modulo 003_diccionarios - #001)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** diccionarios, acumuladores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Ventas por producto (variante base). Agrupa cantidad vendida por producto. Resuelve exactamente el caso indicado.
- **Entrada:** `ventas = [{"producto":"pan","cantidad":2},{"producto":"pan","cantidad":3},{"producto":"leche","cantidad":1}]`
- **Salida esperada:** `{"pan": 5, "leche": 1}`
- **Reglas:** Inicializa claves al aparecer. Resuelve exactamente el caso indicado.
- **Pista opcional:** get ayuda.

## Ejercicio #0002 (Modulo 003_diccionarios - #002)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** diccionarios, porcentajes
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Asistencia por curso (variante base). Calcula porcentaje de asistencia por curso. Resuelve exactamente el caso indicado.
- **Entrada:** `registros = [{"curso":"A","presente":True},{"curso":"A","presente":False},{"curso":"B","presente":True}]`
- **Salida esperada:** `{"A": 50.0, "B": 100.0}`
- **Reglas:** Cuenta presentes y totales. Resuelve exactamente el caso indicado.
- **Pista opcional:** Usa dos diccionarios.

## Ejercicio #0003 (Modulo 003_diccionarios - #003)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** diccionarios, validaciones
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Productos sin precio valido (variante base). Devuelve nombres con precio faltante o no positivo. Resuelve exactamente el caso indicado.
- **Entrada:** `productos = [{"nombre":"A","precio":10},{"nombre":"B","precio":None},{"nombre":"C","precio":0}]`
- **Salida esperada:** `["B", "C"]`
- **Reglas:** Precio valido es mayor que cero. Resuelve exactamente el caso indicado.
- **Pista opcional:** Revisa cada registro.

## Ejercicio #0004 (Modulo 003_diccionarios - #004)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** diccionarios, logs
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Errores por servicio (variante base). Cuenta logs de severidad error por servicio. Resuelve exactamente el caso indicado.
- **Entrada:** `logs = [{"servicio":"api","sev":"error"},{"servicio":"web","sev":"info"},{"servicio":"api","sev":"error"}]`
- **Salida esperada:** `{"api": 2}`
- **Reglas:** Ignora severidades distintas. Resuelve exactamente el caso indicado.
- **Pista opcional:** Filtra antes de contar.

## Ejercicio #0005 (Modulo 003_diccionarios - #005)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** diccionarios, mezcla
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Fusionar inventarios (variante base). Suma dos inventarios sin modificar originales. Resuelve exactamente el caso indicado.
- **Entrada:** `a = {"pan": 2}; b = {"pan": 3, "leche": 4}`
- **Salida esperada:** `{"pan": 5, "leche": 4}`
- **Reglas:** Devuelve un diccionario nuevo. Resuelve exactamente el caso indicado.
- **Pista opcional:** Copia y suma.

## Ejercicio #0006 (Modulo 003_diccionarios - #006)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** diccionarios, conteo
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Contar caracteres. Cuenta cuántas veces aparece cada carácter en una cadena.
- **Entrada:** `texto = "banana"`
- **Salida esperada:** `{"b": 1, "a": 3, "n": 2}`
- **Reglas:** Ignora espacios y distingue entre mayúsculas y minúsculas.
- **Pista opcional:** Usa un bucle y actualiza la clave en el diccionario.

## Ejercicio #0007 (Modulo 003_diccionarios - #007)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** diccionarios, promedios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Precio promedio por categoria. Calcula el precio promedio de productos organizados por categoría.
- **Entrada:** `productos = [{"cat": "fruta", "precio": 10}, {"cat": "fruta", "precio": 20}, {"cat": "verdura", "precio": 15}]`
- **Salida esperada:** `{"fruta": 15.0, "verdura": 15.0}`
- **Reglas:** Calcula la media aritmética exacta.
- **Pista opcional:** Suma los precios y divide entre la cantidad de elementos.

## Ejercicio #0008 (Modulo 003_diccionarios - #008)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** diccionarios, inversion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Invertir llaves y valores. Intercambia las llaves por sus valores correspondientes. Asume que todos los valores son únicos.
- **Entrada:** `colores = {"rojo": "#FF0000", "verde": "#00FF00"}`
- **Salida esperada:** `{"#FF0000": "rojo", "#00FF00": "verde"}`
- **Reglas:** El diccionario resultante debe tener los valores como llaves.
- **Pista opcional:** Recorre con items() y reconstruye.

## Ejercicio #0009 (Modulo 003_diccionarios - #009)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** diccionarios, filtros
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Filtrar por valor minimo. Devuelve las claves cuyo valor sea estrictamente mayor que un umbral.
- **Entrada:** `edades = {"Ana": 18, "Luis": 15, "Pedro": 23}; umbral = 17`
- **Salida esperada:** `["Ana", "Pedro"]`
- **Reglas:** Retorna la lista de llaves ordenada alfabéticamente.
- **Pista opcional:** Filtra las llaves e itera sobre ellas.

## Ejercicio #0010 (Modulo 003_diccionarios - #010)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** diccionarios, extremos
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Clave con maximo valor. Encuentra el elemento con el valor numérico más alto y devuelve su clave.
- **Entrada:** `ventas = {"enero": 1200, "febrero": 1500, "marzo": 900}`
- **Salida esperada:** `"febrero"`
- **Reglas:** En caso de empate, devuelve cualquiera de los máximos.
- **Pista opcional:** Usa la función max pasándole la clave key.

## Ejercicio #0011 (Modulo 003_diccionarios - #011)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** diccionarios, agrupacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Agrupar por longitud. Clasifica palabras en listas según su número de caracteres.
- **Entrada:** `palabras = ["sol", "luna", "mar", "cielo"]`
- **Salida esperada:** `{3: ["sol", "mar"], 4: ["luna"], 5: ["cielo"]}`
- **Reglas:** Mantén el orden original de las palabras.
- **Pista opcional:** La clave será la longitud.

## Ejercicio #0012 (Modulo 003_diccionarios - #012)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** diccionarios, transformacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Aplicar recargo a precios. Incrementa en un 15% los precios del inventario.
- **Entrada:** `precios = {"leche": 100, "pan": 50}`
- **Salida esperada:** `{"leche": 115.0, "pan": 57.5}`
- **Reglas:** Crea un nuevo diccionario con los precios actualizados.
- **Pista opcional:** Multiplica cada valor por 1.15.

## Ejercicio #0013 (Modulo 003_diccionarios - #013)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** diccionarios, strings, listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Frecuencia de palabras en parrafo. Cuenta cuántas veces se repite cada palabra en una frase.
- **Entrada:** `frase = "hola mundo hola"`
- **Salida esperada:** `{"hola": 2, "mundo": 1}`
- **Reglas:** Divide por espacios.
- **Pista opcional:** Usa split() para separar las palabras.

## Ejercicio #0014 (Modulo 003_diccionarios - #014)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** diccionarios, union
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Fusionar sumando cantidades. Une dos diccionarios sumando los valores de las claves que coincidan.
- **Entrada:** `a = {"pan": 5, "leche": 2}; b = {"leche": 3, "agua": 10}`
- **Salida esperada:** `{"pan": 5, "leche": 5, "agua": 10}`
- **Reglas:** No modifiques las entradas originales.
- **Pista opcional:** Copia un diccionario y luego recorre el segundo agregando.

## Ejercicio #0015 (Modulo 003_diccionarios - #015)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** diccionarios, generacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Diccionario de cuadrados. Genera un diccionario cuyas claves sean números del 1 al N y los valores sean sus respectivos cuadrados.
- **Entrada:** `n = 4`
- **Salida esperada:** `{1: 1, 2: 4, 3: 9, 4: 16}`
- **Reglas:** N es inclusivo.
- **Pista opcional:** Usa un rango de 1 a N+1.

## Ejercicio #0016 (Modulo 003_diccionarios - #016)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** diccionarios, autenticacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Validar credenciales de usuario. Verifica si un usuario y contraseña coinciden en la base de datos de usuarios.
- **Entrada:** `db = {"admin": "1234", "user": "abcd"}; user = "admin"; password = "123"`
- **Salida esperada:** `False`
- **Reglas:** Si el usuario no existe, devuelve False en vez de fallar.
- **Pista opcional:** Usa get() o comprueba la existencia de la llave antes de comparar.

## Ejercicio #0017 (Modulo 003_diccionarios - #017)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** diccionarios, comparacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Claves con valores identicos. Encuentra qué claves están presentes en dos diccionarios compartiendo exactamente el mismo valor.
- **Entrada:** `a = {"A": 1, "B": 2, "C": 3}; b = {"A": 1, "B": 9, "C": 3}`
- **Salida esperada:** `["A", "C"]`
- **Reglas:** Devuelve la lista ordenada alfabéticamente.
- **Pista opcional:** Compara llaves en común y evalúa si sus valores coinciden.

## Ejercicio #0018 (Modulo 003_diccionarios - #018)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** diccionarios, limpieza
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Limpiar valores nulos. Remueve del diccionario todas las entradas cuyos valores sean None.
- **Entrada:** `datos = {"id": 1, "nombre": None, "edad": 25, "ciudad": None}`
- **Salida esperada:** `{"id": 1, "edad": 25}`
- **Reglas:** No modifiques el diccionario original.
- **Pista opcional:** Crea un diccionario vacío y llénalo sólo con los valores válidos.

## Ejercicio #0019 (Modulo 003_diccionarios - #019)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** diccionarios, clasificacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Agrupar estudiantes por estado. Clasifica estudiantes en "aprobados" (nota >= 6) o "reprobados".
- **Entrada:** `notas = {"Ana": 8, "Luis": 4, "Eva": 6}`
- **Salida esperada:** `{"aprobados": ["Ana", "Eva"], "reprobados": ["Luis"]}`
- **Reglas:** Las listas internas deben estar ordenadas alfabéticamente.
- **Pista opcional:** Crea listas de aprobados y reprobados vacías y clasifica.

## Ejercicio #0020 (Modulo 003_diccionarios - #020)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** diccionarios, minimos
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Categoria de gastos menor. Encuentra la categoría de gastos con el menor monto acumulado.
- **Entrada:** `gastos = {"comida": 350, "transporte": 120, "ocio": 200}`
- **Salida esperada:** `"transporte"`
- **Reglas:** En caso de empate, devuelve cualquiera de ellos.
- **Pista opcional:** Usa la función min pasándole el diccionario.

## Ejercicio #0021 (Modulo 003_diccionarios - #021)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** diccionarios, anidamiento, busqueda
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Acceso seguro anidado. Busca un valor en una estructura de diccionarios anidada a través de una lista de claves, devolviendo None si alguna clave no existe.
- **Entrada:** `datos = {"a": {"b": {"c": 42}}}; ruta = ["a", "b", "c"]`
- **Salida esperada:** `42`
- **Reglas:** Maneja excepciones de clave faltante retornando None de manera segura.
- **Pista opcional:** Utiliza un bucle para avanzar en la estructura.

## Ejercicio #0022 (Modulo 003_diccionarios - #022)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** diccionarios, logs, unicidad
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Contador de paginas unicas. Cuenta las visitas totales por página a partir de logs donde se repiten entradas.
- **Entrada:** `logs = ["home", "login", "home", "home", "dashboard"]`
- **Salida esperada:** `{"home": 3, "login": 1, "dashboard": 1}`
- **Reglas:** Mapea directamente cada string al total de visitas.
- **Pista opcional:** Si la página no está en el diccionario, inicialízala con 0.

## Ejercicio #0023 (Modulo 003_diccionarios - #023)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** diccionarios, ordenamiento
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Ordenar diccionario por valor. Devuelve una lista de tuplas (clave, valor) ordenadas ascendentemente por su valor.
- **Entrada:** `precios = {"reloj": 250, "auriculares": 80, "telefono": 600}`
- **Salida esperada:** `[("auriculares", 80), ("reloj", 250), ("telefono", 600)]`
- **Reglas:** Utiliza sorted.
- **Pista opcional:** Usa el argumento key en sorted con lambda.

## Ejercicio #0024 (Modulo 003_diccionarios - #024)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** diccionarios, inventarios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Diferencia de inventarios. Compara el almacén A con el almacén B y devuelve qué artículos de A no están en B o tienen menor cantidad en B.
- **Entrada:** `almacen_a = {"tornillos": 100, "tuercas": 50}; almacen_b = {"tornillos": 90, "arandelas": 40}`
- **Salida esperada:** `{"tornillos": 10, "tuercas": 50}`
- **Reglas:** No devuelvas artículos que tienen suficiente stock en B.
- **Pista opcional:** Resta cantidades si el artículo existe en B, si no conserva la cantidad de A.

## Ejercicio #0025 (Modulo 003_diccionarios - #025)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** diccionarios, tipos
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Frecuencia de tipos de datos. Cuenta cuántos elementos hay de cada tipo de datos en una lista.
- **Entrada:** `datos = [1, "hola", 3.14, "mundo", 42]`
- **Salida esperada:** `{"int": 2, "str": 2, "float": 1}`
- **Reglas:** Mapea el nombre del tipo en string (ej. "int", "str") al total de ocurrencias.
- **Pista opcional:** Usa type(elemento).__name__ para obtener el nombre del tipo.

## Ejercicio #0026 (Modulo 003_diccionarios - #026)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** diccionarios, listas, interseccion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Gustos compartidos por usuarios. Encuentra los gustos en común compartidos por todos los usuarios del diccionario.
- **Entrada:** `usuarios = {"Ana": ["cine", "musica", "viajes"], "Luis": ["musica", "libros", "cine"], "Eva": ["cine", "musica"]}`
- **Salida esperada:** `["cine", "musica"]`
- **Reglas:** Devuelve la lista ordenada alfabéticamente.
- **Pista opcional:** Puedes usar sets para calcular la intersección.

## Ejercicio #0027 (Modulo 003_diccionarios - #027)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** diccionarios, agrupacion, finanzas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Consolidar depositos y retiros. Agrupa transacciones financieras por su tipo ("deposito" o "retiro") sumando el total de cada una.
- **Entrada:** `transacciones = [{"tipo": "deposito", "monto": 100}, {"tipo": "retiro", "monto": 20}, {"tipo": "deposito", "monto": 50}]`
- **Salida esperada:** `{"deposito": 150, "retiro": 20}`
- **Reglas:** Si un tipo no aparece, no debe estar en la salida.
- **Pista opcional:** Acumula por tipo de transacción.

## Ejercicio #0028 (Modulo 003_diccionarios - #028)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** diccionarios, fechas, maximo
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Ventas mensuales maximas. A partir de una lista de ventas con mes, encuentra el mes con el total de ingresos más alto.
- **Entrada:** `ventas = [{"mes": "Ene", "total": 300}, {"mes": "Feb", "total": 500}, {"mes": "Ene", "total": 250}]`
- **Salida esperada:** `"Ene"`
- **Reglas:** Suma primero los ingresos mensuales duplicados. Ene suma 550 y Feb suma 500.
- **Pista opcional:** Agrupa por mes primero y luego calcula el máximo.

## Ejercicio #0029 (Modulo 003_diccionarios - #029)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** diccionarios, strings, reemplazo
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Diccionario de censura. Reemplaza palabras de un texto según un diccionario de sustituciones.
- **Entrada:** `texto = "el perro muerde"; diccionario = {"perro": "gato", "muerde": "juega"}`
- **Salida esperada:** `"el gato juega"`
- **Reglas:** Reemplaza exactamente las palabras.
- **Pista opcional:** Divide la frase, reemplaza las palabras que existan en el diccionario y vuelve a unir.

## Ejercicio #0030 (Modulo 003_diccionarios - #030)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** diccionarios, anidamiento, inversion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Reestructurar diccionario anidado. Convierte un diccionario con formato `{usuario: {mes: total}}` a uno con formato `{mes: {usuario: total}}`.
- **Entrada:** `datos = {"Ana": {"Ene": 100, "Feb": 200}, "Luis": {"Ene": 150}}`
- **Salida esperada:** `{"Ene": {"Ana": 100, "Luis": 150}, "Feb": {"Ana": 200}}`
- **Reglas:** Crea las llaves dinámicamente si no existen en el diccionario de destino.
- **Pista opcional:** Usa bucles anidados para recorrer ambos niveles de llaves.

## Ejercicio #0031 (Modulo 003_diccionarios - #031)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** diccionarios, logs, contadores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Transiciones de estado. Cuenta cuántas veces un sistema pasó de un estado a otro consecutivo.
- **Entrada:** `secuencia = ["iniciado", "corriendo", "pausado", "corriendo"]`
- **Salida esperada:** `{"iniciado->corriendo": 1, "corriendo->pausado": 1, "pausado->corriendo": 1}`
- **Reglas:** Las llaves deben tener el formato "estado_anterior->estado_actual".
- **Pista opcional:** Recorre la lista de 0 a len(secuencia)-2.

## Ejercicio #0032 (Modulo 003_diccionarios - #032)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** diccionarios, duplicados, listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Filtrar elementos repetidos. Devuelve una lista con aquellos elementos que aparecen dos o más veces en la lista de entrada.
- **Entrada:** `elementos = ["A", "B", "A", "C", "B", "A"]`
- **Salida esperada:** `["A", "B"]`
- **Reglas:** La lista resultante debe estar ordenada alfabéticamente.
- **Pista opcional:** Cuenta las frecuencias primero en un diccionario y luego filtra.

## Ejercicio #0033 (Modulo 003_diccionarios - #033)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** diccionarios, envios, listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Agrupar envios por codigo postal. Agrupa nombres de destinatarios por su código postal.
- **Entrada:** `envios = [{"nombre": "Ana", "cp": "28001"}, {"nombre": "Luis", "cp": "08002"}, {"nombre": "Eva", "cp": "28001"}]`
- **Salida esperada:** `{"28001": ["Ana", "Eva"], "08002": ["Luis"]}`
- **Reglas:** Los nombres deben mantener su orden de aparición original.
- **Pista opcional:** Si el código postal no está en el diccionario, asígnale una lista vacía.

## Ejercicio #0034 (Modulo 003_diccionarios - #034)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** diccionarios, extremos, listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Mejor precio de proveedor. Dado un diccionario de productos donde cada producto tiene una lista de tuplas (proveedor, precio), encuentra el proveedor con el precio más bajo para cada producto.
- **Entrada:** `ofertas = {"pan": [("ProvA", 1.5), ("ProvB", 1.2)], "leche": [("ProvA", 2.0)]}`
- **Salida esperada:** `{"pan": "ProvB", "leche": "ProvA"}`
- **Reglas:** Si hay empate en precio, devuelve cualquiera de ellos.
- **Pista opcional:** Recorre el diccionario y aplica min() sobre la lista de ofertas usando el precio como clave.

## Ejercicio #0035 (Modulo 003_diccionarios - #035)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** diccionarios, colas, inventario FIFO
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Simular inventario FIFO. Calcula el costo total de las ventas procesadas según la lógica First-In, First-Out (primero en entrar, primero en salir) a partir de compras y ventas de un único producto.
- **Entrada:** `compras = [{"cant": 10, "precio": 2.0}, {"cant": 5, "precio": 3.0}]; cantidad_vendida = 12`
- **Salida esperada:** `26.0`
- **Reglas:** Usa las primeras compras primero. 10 unidades a 2.0 (total 20.0) y 2 unidades a 3.0 (total 6.0), sumando 26.0.
- **Pista opcional:** Mantén una cola de compras disponibles y ve restando de ella conforme vendes.
