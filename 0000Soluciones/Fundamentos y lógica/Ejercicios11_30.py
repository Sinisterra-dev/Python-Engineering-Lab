## Ejercicio #0011 (Modulo 001_fundamentos_y_logica - #011)
#- **Nivel de dificultad:** Nivel 1 - Inicial
#- **Conceptos involucrados:** minimos
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Menor tiempo de entrega. Recibes tiempos. Devuelve el menor sin usar min.
#- **Entrada:** `tiempos = [45, 30, 55, 28]`
#- **Salida esperada:** `28`
#- **Reglas:** La lista no esta vacia.
#- **Pista opcional:** Compara contra el menor actual.

tiempos = [45, 30, 55, 28]
menor = tiempos[0]

for tiempo in tiempos:
    if menor > tiempo:
        menor = tiempo
print (menor)


## Ejercicio #0012 (Modulo 001_fundamentos_y_logica - #012)
#- **Nivel de dificultad:** Nivel 1 - Inicial
#- **Conceptos involucrados:** promedios
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Promedio de calificaciones validas. Recibes notas donde -1 significa ausente. Promedia solo notas validas.
#- **Entrada:** `notas = [8, -1, 6, 10]`
#- **Salida esperada:** `8.0`
#- **Reglas:** Ignora los -1. Si no hay validas, devuelve 0.
#- **Pista opcional:** Cuenta y suma a la vez.

notas = [8, -1, 6, 10]

suma = 0
cuenta = 0

for nota in notas:
    if nota != -1:
        suma += nota
        cuenta += 1

if cuenta == 0:
    promedio = 0
else: 
    promedio = suma / cuenta
print(promedio) 



## Ejercicio #0013 (Modulo 001_fundamentos_y_logica - #013)
#- **Nivel de dificultad:** Nivel 1 - Inicial
#- **Conceptos involucrados:** conteos multiples
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Resumen de tickets. Recibes estados de tickets. Devuelve cantidad de abiertos, cerrados y pausados.
#- **Entrada:** `tickets = ["abierto", "cerrado", "abierto", "pausado"]`
#- **Salida esperada:** `{"abierto": 2, "cerrado": 1, "pausado": 1}`
#- **Reglas:** Usa contadores separados.
#- **Pista opcional:** Cada ticket pertenece a un estado.

tickets = ["abierto", "cerrado", "abierto", "pausado"]

ticket_abierto = 0
ticket_pausado = 0
ticket_cerrado = 0

for ticket in tickets:
    if ticket == "abierto":
        ticket_abierto += 1
    elif ticket == "cerrado":
        ticket_cerrado += 1
    elif ticket == "pausado":
        ticket_pausado += 1
resultado = {
    "pausado": ticket_pausado,
    "cerrado": ticket_cerrado,
    "abierto": ticket_abierto}
print(resultado)
     


## Ejercicio #0014 (Modulo 001_fundamentos_y_logica - #014)
#- **Nivel de dificultad:** Nivel 1 - Inicial
#- **Conceptos involucrados:** listas auxiliares
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Separar sensores fuera de rango. Recibes lecturas y rango minimo/maximo. Devuelve lecturas bajas, normales y altas.
#- **Entrada:** `lecturas = [1, 5, 9, 12]; minimo = 4; maximo = 10`
#- **Salida esperada:** `{"bajas": [1], "normales": [5, 9], "altas": [12]}`
#- **Reglas:** Usa tres listas.
#- **Pista opcional:** Evalua en orden: bajo, alto, normal.

lecturas = [1, 5, 9, 12]; minimo = 4; maximo = 10

bajas = []
normales =[]
altas = []

for lectura in lecturas:
    if lectura < minimo:
        bajas.append(lectura)
    elif minimo <= lectura <= maximo:
        normales.append(lectura)
    elif lectura > maximo:
        altas.append(lectura)
temperaturas = {
    "bajas": bajas,
    "normales": normales,
    "altas": altas
}
print(temperaturas)






## Ejercicio #0015 (Modulo 001_fundamentos_y_logica - #015)
#- **Nivel de dificultad:** Nivel 1 - Inicial
#- **Conceptos involucrados:** busquedas complejas
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Primer usuario bloqueado con intentos. Recibes estados e intentos paralelos. Devuelve indice del primer bloqueado con mas de 3 intentos.
#- **Entrada:** `estados = ["ok", "bloqueado", "bloqueado"]; intentos = [1, 2, 5]`
#- **Salida esperada:** `2`
#- **Reglas:** Recorre por indice.
#- **Pista opcional:** Ambas listas comparten posicion.

## Ejercicio #0016 (Modulo 001_fundamentos_y_logica - #016)
#- **Nivel de dificultad:** Nivel 1 - Inicial
#- **Conceptos involucrados:** duplicados
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Codigos unicos conservando orden. Recibes codigos con repetidos. Devuelve codigos sin repetidos en orden original.
#- **Entrada:** `codigos = [7, 3, 7, 9, 3, 2]`
#- **Salida esperada:** `[7, 3, 9, 2]`
#- **Reglas:** No uses una salida desordenada.
#- **Pista opcional:** Agrega si todavia no esta.

## Ejercicio #0017 (Modulo 001_fundamentos_y_logica - #017)
#- **Nivel de dificultad:** Nivel 1 - Inicial
#- **Conceptos involucrados:** ranking
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Top 3 productos por venta. Recibes productos y ventas paralelas. Devuelve nombres de los tres mas vendidos.
#- **Entrada:** `productos = ["pan", "leche", "cafe", "te"]; ventas = [30, 12, 45, 20]`
#- **Salida esperada:** `["cafe", "pan", "te"]`
#- **Reglas:** Conserva la relacion producto-venta.
#- **Pista opcional:** Ordena pares por venta descendente.

## Ejercicio #0018 (Modulo 001_fundamentos_y_logica - #018)
#- **Nivel de dificultad:** Nivel 1 - Inicial
#- **Conceptos involucrados:** porcentajes
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Porcentaje de entregas tardias. Recibes minutos de retraso. Devuelve porcentaje de entregas con retraso mayor a cero.
#- **Entrada:** `retrasos = [0, 5, 0, 12, 3]`
#- **Salida esperada:** `60.0`
#- **Reglas:** Si no hay entregas, devuelve 0.
#- **Pista opcional:** tardias * 100 / total.

## Ejercicio #0019 (Modulo 001_fundamentos_y_logica - #019)
#- **Nivel de dificultad:** Nivel 2 - Basico
#- **Conceptos involucrados:** agregacion simple
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Ventas totales por categoria sin diccionario. Recibes categorias y montos. Devuelve listas de categorias unicas y totales paralelos.
#- **Entrada:** `categorias = ["A", "B", "A"]; montos = [10, 5, 7]`
#- **Salida esperada:** `{"categorias": ["A", "B"], "totales": [17, 5]}`
#- **Reglas:** Usa listas auxiliares.
#- **Pista opcional:** Busca si la categoria ya existe.

## Ejercicio #0020 (Modulo 001_fundamentos_y_logica - #020)
#- **Nivel de dificultad:** Nivel 2 - Basico
#- **Conceptos involucrados:** validaciones encadenadas
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Validar alta de producto. Recibes nombre, precio, stock y categoria. Devuelve True si todos los campos son validos.
#- **Entrada:** `nombre = "Mouse"; precio = 25; stock = 4; categoria = "tec"`
#- **Salida esperada:** `True`
#- **Reglas:** Nombre no vacio, precio > 0, stock >= 0 y categoria no vacia.
#- **Pista opcional:** Combina condiciones.

## Ejercicio #0021 (Modulo 001_fundamentos_y_logica - #021)
#- **Nivel de dificultad:** Nivel 2 - Basico
#- **Conceptos involucrados:** listas paralelas, reportes, acumuladores
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Reporte critico para inventario de farmacia. Recibes nombres, valores actuales y limites. Devuelve nombres cuyo valor esta por debajo del limite y el deficit total.
#- **Entrada:** `nombres = ["A", "B", "C"]; valores = [4, 7, 5]; limites = [7, 8, 6]`
#- **Salida esperada:** `{"criticos": ["A", "B", "C"], "deficit_total": 5}`
#- **Reglas:** Compara cada valor con su limite y suma solo deficits positivos.
#- **Pista opcional:** El deficit es limite - valor.

## Ejercicio #0022 (Modulo 001_fundamentos_y_logica - #022)
#- **Nivel de dificultad:** Nivel 2 - Basico
#- **Conceptos involucrados:** ranking, ordenamiento, empates
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Ranking con empates para pedidos de cafeteria. Recibes nombres y puntos. Devuelve ranking descendente; si empatan, ordena por nombre.
#- **Entrada:** `nombres = ["Ana", "Luis", "Eva"]; puntos = [5, 9, 6]`
#- **Salida esperada:** `["Luis", "Eva", "Ana"]`
#- **Reglas:** Ordena por puntos descendente y nombre ascendente.
#- **Pista opcional:** Usa pares nombre-punto.

## Ejercicio #0023 (Modulo 001_fundamentos_y_logica - #023)
#- **Nivel de dificultad:** Nivel 2 - Basico
#- **Conceptos involucrados:** simulaciones, listas, limites
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Simulacion con limite para notas de estudiantes. Recibes nivel inicial y cambios. Devuelve historial sin bajar de 0 ni subir de 100.
#- **Entrada:** `nivel = 6; cambios = [1, 4, -4, 5]`
#- **Salida esperada:** `[7, 11, 7, 12]`
#- **Reglas:** Despues de cada cambio guarda el nivel ajustado.
#- **Pista opcional:** Aplica limites luego de sumar.

## Ejercicio #0024 (Modulo 001_fundamentos_y_logica - #024)
#- **Nivel de dificultad:** Nivel 2 - Basico
#- **Conceptos involucrados:** metricas, filtros, promedios
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Metricas de aprobacion para sensores de clima. Recibes valores y minimo aprobado. Devuelve aprobados, rechazados y promedio de aprobados.
#- **Entrada:** `valores = [7, 13, 8, 2]; minimo = 10`
#- **Salida esperada:** `{"aprobados": 1, "rechazados": 3, "promedio_aprobados": 13.0}`
#- **Reglas:** Si no hay aprobados, promedio_aprobados es 0.
#- **Pista opcional:** Filtra antes de promediar.

## Ejercicio #0025 (Modulo 001_fundamentos_y_logica - #025)
#- **Nivel de dificultad:** Nivel 2 - Basico
#- **Conceptos involucrados:** listas, rachas, contadores
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Deteccion de racha para logs de acceso. Recibes estados. Devuelve la racha mas larga de estados de alerta.
#- **Entrada:** `estados = ["alerta", "ok", "alerta", "alerta", "ok", "alerta"]`
#- **Salida esperada:** `2`
#- **Reglas:** Una racha se corta cuando el estado no es alerta.
#- **Pista opcional:** Compara racha actual contra mejor.

## Ejercicio #0026 (Modulo 001_fundamentos_y_logica - #026)
#- **Nivel de dificultad:** Nivel 2 - Basico
#- **Conceptos involucrados:** busqueda, listas, clasificacion
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Cruce de dos listas para reservas de sala. Recibes ids solicitados e ids disponibles. Devuelve atendidos y faltantes conservando orden solicitado.
#- **Entrada:** `solicitados = [6, 7, 8, 9]; disponibles = [7, 9, 11]`
#- **Salida esperada:** `{"atendidos": [7, 9], "faltantes": [6, 8]}`
#- **Reglas:** No dupliques resultados.
#- **Pista opcional:** Revisa cada solicitado.

## Ejercicio #0027 (Modulo 001_fundamentos_y_logica - #027)
#- **Nivel de dificultad:** Nivel 2 - Basico
#- **Conceptos involucrados:** ventanas, bucles, listas
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Resumen por ventanas para ventas de tienda. Recibes valores y tamano de ventana 3. Devuelve suma de cada ventana consecutiva.
#- **Entrada:** `valores = [10, 19, 4, 0, 8]`
#- **Salida esperada:** `[33, 31, 15]`
#- **Reglas:** Genera ventanas completas solamente.
#- **Pista opcional:** Recorre hasta len(valores)-2.

## Ejercicio #0028 (Modulo 001_fundamentos_y_logica - #028)
#- **Nivel de dificultad:** Nivel 2 - Basico
#- **Conceptos involucrados:** agregaciones, multiples listas
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Categorias con umbral para partidas de juego. Recibes categorias y cantidades. Devuelve categorias cuyo total supera el umbral.
#- **Entrada:** `categorias = ["A", "B", "A", "C"]; cantidades = [11, 21, 5, 1]; umbral = 8`
#- **Salida esperada:** `["A", "B"]`
#- **Reglas:** Acumula por categoria y filtra al final.
#- **Pista opcional:** Puedes usar listas paralelas.

## Ejercicio #0029 (Modulo 001_fundamentos_y_logica - #029)
#- **Nivel de dificultad:** Nivel 2 - Basico
#- **Conceptos involucrados:** listas paralelas, reportes, acumuladores
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Reporte critico para prestamos de biblioteca. Recibes nombres, valores actuales y limites. Devuelve nombres cuyo valor esta por debajo del limite y el deficit total.
#- **Entrada:** `nombres = ["A", "B", "C"]; valores = [12, 23, 6]; limites = [9, 11, 6]`
#- **Salida esperada:** `{"criticos": [], "deficit_total": 0}`
#- **Reglas:** Compara cada valor con su limite y suma solo deficits positivos.
#- **Pista opcional:** El deficit es limite - valor.

## Ejercicio #0030 (Modulo 001_fundamentos_y_logica - #030)
#- **Nivel de dificultad:** Nivel 2 - Basico
#- **Conceptos involucrados:** ranking, ordenamiento, empates
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Ranking con empates para envios urbanos. Recibes nombres y puntos. Devuelve ranking descendente; si empatan, ordena por nombre.
#- **Entrada:** `nombres = ["Ana", "Luis", "Eva"]; puntos = [13, 25, 7]`
#- **Salida esperada:** `["Luis", "Ana", "Eva"]`
#- **Reglas:** Ordena por puntos descendente y nombre ascendente.
#- **Pista opcional:** Usa pares nombre-punto.