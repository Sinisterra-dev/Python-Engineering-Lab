# Ejercicios - Fundamentos y logica

Total del modulo: **93 ejercicios**.

Esta version prioriza variedad real sobre cantidad. Se eliminaron bloques con entrada/salida repetidas para cumplir la regla absoluta de no repeticion.

## Ejercicio #0001 (Modulo 001_fundamentos_y_logica - #001)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** variables, operadores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Total de caja diaria. Recibes billetes de 100, 50 y 20. Devuelve el dinero total.
- **Entrada:** `b100 = 3; b50 = 4; b20 = 2`
- **Salida esperada:** `540`
- **Reglas:** Usa operaciones aritmeticas simples.
- **Pista opcional:** Multiplica cada cantidad por su valor.

## Ejercicio #0002 (Modulo 001_fundamentos_y_logica - #002)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** if, else
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Estado de bateria de sensor. Recibes porcentaje de bateria. Devuelve "critica" si es menor a 15, si no "normal".
- **Entrada:** `bateria = 12`
- **Salida esperada:** `"critica"`
- **Reglas:** Usa una condicion directa.
- **Pista opcional:** Compara contra el umbral.

## Ejercicio #0003 (Modulo 001_fundamentos_y_logica - #003)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** for, acumuladores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Minutos atendidos por soporte. Recibes duraciones de llamadas. Devuelve el total de minutos.
- **Entrada:** `llamadas = [4, 12, 8]`
- **Salida esperada:** `24`
- **Reglas:** Recorre la lista con for.
- **Pista opcional:** Acumula cada duracion.

## Ejercicio #0004 (Modulo 001_fundamentos_y_logica - #004)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** for, contadores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Productos agotados en estanteria. Recibes stocks. Cuenta cuantos son exactamente cero.
- **Entrada:** `stocks = [3, 0, 8, 0, 1]`
- **Salida esperada:** `2`
- **Reglas:** Usa un contador.
- **Pista opcional:** Incrementa cuando el stock sea 0.

## Ejercicio #0005 (Modulo 001_fundamentos_y_logica - #005)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** while, simulacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Consumir creditos de juego. Recibes creditos y costo por partida. Devuelve cuantas partidas se pueden jugar.
- **Entrada:** `creditos = 17; costo = 5`
- **Salida esperada:** `3`
- **Reglas:** Usa while restando el costo hasta que no alcance.
- **Pista opcional:** Cuenta cada partida jugada.

## Ejercicio #0006 (Modulo 001_fundamentos_y_logica - #006)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** busqueda basica
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Encontrar turno libre. Recibes estados de turnos. Devuelve el primer indice con "libre" o -1.
- **Entrada:** `turnos = ["ocupado", "ocupado", "libre"]`
- **Salida esperada:** `2`
- **Reglas:** Deten la busqueda al encontrar el primer libre.
- **Pista opcional:** Guarda el indice encontrado.

## Ejercicio #0007 (Modulo 001_fundamentos_y_logica - #007)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** validaciones simples
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Validar temperatura de heladera. Recibes temperatura. Devuelve True si esta entre 2 y 8 inclusive.
- **Entrada:** `temperatura = 9`
- **Salida esperada:** `False`
- **Reglas:** Combina dos comparaciones.
- **Pista opcional:** Usa and.

## Ejercicio #0008 (Modulo 001_fundamentos_y_logica - #008)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** strings, contadores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Contar codigos con prefijo. Recibes codigos y un prefijo. Cuenta cuantos empiezan con ese prefijo.
- **Entrada:** `codigos = ["A-1", "B-2", "A-3"]; prefijo = "A"`
- **Salida esperada:** `2`
- **Reglas:** Revisa cada string.
- **Pista opcional:** startswith puede ayudar.

## Ejercicio #0009 (Modulo 001_fundamentos_y_logica - #009)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** listas, filtros
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Pedidos mayores al minimo. Recibes importes y un minimo. Devuelve importes que superan el minimo.
- **Entrada:** `importes = [80, 120, 40, 200]; minimo = 100`
- **Salida esperada:** `[120, 200]`
- **Reglas:** Construye una lista nueva.
- **Pista opcional:** Agrega solo los que cumplen.

## Ejercicio #0010 (Modulo 001_fundamentos_y_logica - #010)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** maximos
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Mayor puntaje de partida. Recibes puntajes. Devuelve el mayor sin usar max.
- **Entrada:** `puntajes = [12, 40, 25, 39]`
- **Salida esperada:** `40`
- **Reglas:** Inicializa con el primer puntaje.
- **Pista opcional:** Actualiza cuando encuentres uno mayor.

## Ejercicio #0011 (Modulo 001_fundamentos_y_logica - #011)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** minimos
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Menor tiempo de entrega. Recibes tiempos. Devuelve el menor sin usar min.
- **Entrada:** `tiempos = [45, 30, 55, 28]`
- **Salida esperada:** `28`
- **Reglas:** La lista no esta vacia.
- **Pista opcional:** Compara contra el menor actual.

## Ejercicio #0012 (Modulo 001_fundamentos_y_logica - #012)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** promedios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Promedio de calificaciones validas. Recibes notas donde -1 significa ausente. Promedia solo notas validas.
- **Entrada:** `notas = [8, -1, 6, 10]`
- **Salida esperada:** `8.0`
- **Reglas:** Ignora los -1. Si no hay validas, devuelve 0.
- **Pista opcional:** Cuenta y suma a la vez.

## Ejercicio #0013 (Modulo 001_fundamentos_y_logica - #013)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** conteos multiples
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Resumen de tickets. Recibes estados de tickets. Devuelve cantidad de abiertos, cerrados y pausados.
- **Entrada:** `tickets = ["abierto", "cerrado", "abierto", "pausado"]`
- **Salida esperada:** `{"abierto": 2, "cerrado": 1, "pausado": 1}`
- **Reglas:** Usa contadores separados.
- **Pista opcional:** Cada ticket pertenece a un estado.

## Ejercicio #0014 (Modulo 001_fundamentos_y_logica - #014)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** listas auxiliares
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Separar sensores fuera de rango. Recibes lecturas y rango minimo/maximo. Devuelve lecturas bajas, normales y altas.
- **Entrada:** `lecturas = [1, 5, 9, 12]; minimo = 4; maximo = 10`
- **Salida esperada:** `{"bajas": [1], "normales": [5, 9], "altas": [12]}`
- **Reglas:** Usa tres listas.
- **Pista opcional:** Evalua en orden: bajo, alto, normal.

## Ejercicio #0015 (Modulo 001_fundamentos_y_logica - #015)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** busquedas complejas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Primer usuario bloqueado con intentos. Recibes estados e intentos paralelos. Devuelve indice del primer bloqueado con mas de 3 intentos.
- **Entrada:** `estados = ["ok", "bloqueado", "bloqueado"]; intentos = [1, 2, 5]`
- **Salida esperada:** `2`
- **Reglas:** Recorre por indice.
- **Pista opcional:** Ambas listas comparten posicion.

## Ejercicio #0016 (Modulo 001_fundamentos_y_logica - #016)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** duplicados
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Codigos unicos conservando orden. Recibes codigos con repetidos. Devuelve codigos sin repetidos en orden original.
- **Entrada:** `codigos = [7, 3, 7, 9, 3, 2]`
- **Salida esperada:** `[7, 3, 9, 2]`
- **Reglas:** No uses una salida desordenada.
- **Pista opcional:** Agrega si todavia no esta.

## Ejercicio #0017 (Modulo 001_fundamentos_y_logica - #017)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** ranking
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Top 3 productos por venta. Recibes productos y ventas paralelas. Devuelve nombres de los tres mas vendidos.
- **Entrada:** `productos = ["pan", "leche", "cafe", "te"]; ventas = [30, 12, 45, 20]`
- **Salida esperada:** `["cafe", "pan", "te"]`
- **Reglas:** Conserva la relacion producto-venta.
- **Pista opcional:** Ordena pares por venta descendente.

## Ejercicio #0018 (Modulo 001_fundamentos_y_logica - #018)
- **Nivel de dificultad:** Nivel 1 - Inicial
- **Conceptos involucrados:** porcentajes
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Porcentaje de entregas tardias. Recibes minutos de retraso. Devuelve porcentaje de entregas con retraso mayor a cero.
- **Entrada:** `retrasos = [0, 5, 0, 12, 3]`
- **Salida esperada:** `60.0`
- **Reglas:** Si no hay entregas, devuelve 0.
- **Pista opcional:** tardias * 100 / total.

## Ejercicio #0019 (Modulo 001_fundamentos_y_logica - #019)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** agregacion simple
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Ventas totales por categoria sin diccionario. Recibes categorias y montos. Devuelve listas de categorias unicas y totales paralelos.
- **Entrada:** `categorias = ["A", "B", "A"]; montos = [10, 5, 7]`
- **Salida esperada:** `{"categorias": ["A", "B"], "totales": [17, 5]}`
- **Reglas:** Usa listas auxiliares.
- **Pista opcional:** Busca si la categoria ya existe.

## Ejercicio #0020 (Modulo 001_fundamentos_y_logica - #020)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** validaciones encadenadas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Validar alta de producto. Recibes nombre, precio, stock y categoria. Devuelve True si todos los campos son validos.
- **Entrada:** `nombre = "Mouse"; precio = 25; stock = 4; categoria = "tec"`
- **Salida esperada:** `True`
- **Reglas:** Nombre no vacio, precio > 0, stock >= 0 y categoria no vacia.
- **Pista opcional:** Combina condiciones.

## Ejercicio #0021 (Modulo 001_fundamentos_y_logica - #021)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** listas paralelas, reportes, acumuladores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Reporte critico para inventario de farmacia. Recibes nombres, valores actuales y limites. Devuelve nombres cuyo valor esta por debajo del limite y el deficit total.
- **Entrada:** `nombres = ["A", "B", "C"]; valores = [4, 7, 5]; limites = [7, 8, 6]`
- **Salida esperada:** `{"criticos": ["A", "B", "C"], "deficit_total": 5}`
- **Reglas:** Compara cada valor con su limite y suma solo deficits positivos.
- **Pista opcional:** El deficit es limite - valor.

## Ejercicio #0022 (Modulo 001_fundamentos_y_logica - #022)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** ranking, ordenamiento, empates
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Ranking con empates para pedidos de cafeteria. Recibes nombres y puntos. Devuelve ranking descendente; si empatan, ordena por nombre.
- **Entrada:** `nombres = ["Ana", "Luis", "Eva"]; puntos = [5, 9, 6]`
- **Salida esperada:** `["Luis", "Eva", "Ana"]`
- **Reglas:** Ordena por puntos descendente y nombre ascendente.
- **Pista opcional:** Usa pares nombre-punto.

## Ejercicio #0023 (Modulo 001_fundamentos_y_logica - #023)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** simulaciones, listas, limites
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Simulacion con limite para notas de estudiantes. Recibes nivel inicial y cambios. Devuelve historial sin bajar de 0 ni subir de 100.
- **Entrada:** `nivel = 6; cambios = [1, 4, -4, 5]`
- **Salida esperada:** `[7, 11, 7, 12]`
- **Reglas:** Despues de cada cambio guarda el nivel ajustado.
- **Pista opcional:** Aplica limites luego de sumar.

## Ejercicio #0024 (Modulo 001_fundamentos_y_logica - #024)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** metricas, filtros, promedios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Metricas de aprobacion para sensores de clima. Recibes valores y minimo aprobado. Devuelve aprobados, rechazados y promedio de aprobados.
- **Entrada:** `valores = [7, 13, 8, 2]; minimo = 10`
- **Salida esperada:** `{"aprobados": 1, "rechazados": 3, "promedio_aprobados": 13.0}`
- **Reglas:** Si no hay aprobados, promedio_aprobados es 0.
- **Pista opcional:** Filtra antes de promediar.

## Ejercicio #0025 (Modulo 001_fundamentos_y_logica - #025)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** listas, rachas, contadores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Deteccion de racha para logs de acceso. Recibes estados. Devuelve la racha mas larga de estados de alerta.
- **Entrada:** `estados = ["alerta", "ok", "alerta", "alerta", "ok", "alerta"]`
- **Salida esperada:** `2`
- **Reglas:** Una racha se corta cuando el estado no es alerta.
- **Pista opcional:** Compara racha actual contra mejor.

## Ejercicio #0026 (Modulo 001_fundamentos_y_logica - #026)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** busqueda, listas, clasificacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Cruce de dos listas para reservas de sala. Recibes ids solicitados e ids disponibles. Devuelve atendidos y faltantes conservando orden solicitado.
- **Entrada:** `solicitados = [6, 7, 8, 9]; disponibles = [7, 9, 11]`
- **Salida esperada:** `{"atendidos": [7, 9], "faltantes": [6, 8]}`
- **Reglas:** No dupliques resultados.
- **Pista opcional:** Revisa cada solicitado.

## Ejercicio #0027 (Modulo 001_fundamentos_y_logica - #027)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** ventanas, bucles, listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Resumen por ventanas para ventas de tienda. Recibes valores y tamano de ventana 3. Devuelve suma de cada ventana consecutiva.
- **Entrada:** `valores = [10, 19, 4, 0, 8]`
- **Salida esperada:** `[33, 31, 15]`
- **Reglas:** Genera ventanas completas solamente.
- **Pista opcional:** Recorre hasta len(valores)-2.

## Ejercicio #0028 (Modulo 001_fundamentos_y_logica - #028)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** agregaciones, multiples listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Categorias con umbral para partidas de juego. Recibes categorias y cantidades. Devuelve categorias cuyo total supera el umbral.
- **Entrada:** `categorias = ["A", "B", "A", "C"]; cantidades = [11, 21, 5, 1]; umbral = 8`
- **Salida esperada:** `["A", "B"]`
- **Reglas:** Acumula por categoria y filtra al final.
- **Pista opcional:** Puedes usar listas paralelas.

## Ejercicio #0029 (Modulo 001_fundamentos_y_logica - #029)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** listas paralelas, reportes, acumuladores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Reporte critico para prestamos de biblioteca. Recibes nombres, valores actuales y limites. Devuelve nombres cuyo valor esta por debajo del limite y el deficit total.
- **Entrada:** `nombres = ["A", "B", "C"]; valores = [12, 23, 6]; limites = [9, 11, 6]`
- **Salida esperada:** `{"criticos": [], "deficit_total": 0}`
- **Reglas:** Compara cada valor con su limite y suma solo deficits positivos.
- **Pista opcional:** El deficit es limite - valor.

## Ejercicio #0030 (Modulo 001_fundamentos_y_logica - #030)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** ranking, ordenamiento, empates
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Ranking con empates para envios urbanos. Recibes nombres y puntos. Devuelve ranking descendente; si empatan, ordena por nombre.
- **Entrada:** `nombres = ["Ana", "Luis", "Eva"]; puntos = [13, 25, 7]`
- **Salida esperada:** `["Luis", "Ana", "Eva"]`
- **Reglas:** Ordena por puntos descendente y nombre ascendente.
- **Pista opcional:** Usa pares nombre-punto.

## Ejercicio #0031 (Modulo 001_fundamentos_y_logica - #031)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** simulaciones, listas, limites
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Simulacion con limite para inventario de farmacia. Recibes nivel inicial y cambios. Devuelve historial sin bajar de 0 ni subir de 100.
- **Entrada:** `nivel = 14; cambios = [-1, 3, -4, 7]`
- **Salida esperada:** `[13, 16, 12, 19]`
- **Reglas:** Despues de cada cambio guarda el nivel ajustado.
- **Pista opcional:** Aplica limites luego de sumar.

## Ejercicio #0032 (Modulo 001_fundamentos_y_logica - #032)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** metricas, filtros, promedios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Metricas de aprobacion para pedidos de cafeteria. Recibes valores y minimo aprobado. Devuelve aprobados, rechazados y promedio de aprobados.
- **Entrada:** `valores = [15, 29, 9, 0]; minimo = 6`
- **Salida esperada:** `{"aprobados": 3, "rechazados": 1, "promedio_aprobados": 17.67}`
- **Reglas:** Si no hay aprobados, promedio_aprobados es 0.
- **Pista opcional:** Filtra antes de promediar.

## Ejercicio #0033 (Modulo 001_fundamentos_y_logica - #033)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** listas, rachas, contadores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Deteccion de racha para notas de estudiantes. Recibes estados. Devuelve la racha mas larga de estados de alerta.
- **Entrada:** `estados = ["alerta", "alerta", "ok", "alerta", "alerta", "ok"]`
- **Salida esperada:** `2`
- **Reglas:** Una racha se corta cuando el estado no es alerta.
- **Pista opcional:** Compara racha actual contra mejor.

## Ejercicio #0034 (Modulo 001_fundamentos_y_logica - #034)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** busqueda, listas, clasificacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Cruce de dos listas para sensores de clima. Recibes ids solicitados e ids disponibles. Devuelve atendidos y faltantes conservando orden solicitado.
- **Entrada:** `solicitados = [14, 15, 16, 17]; disponibles = [15, 17, 19]`
- **Salida esperada:** `{"atendidos": [15, 17], "faltantes": [14, 16]}`
- **Reglas:** No dupliques resultados.
- **Pista opcional:** Revisa cada solicitado.

## Ejercicio #0035 (Modulo 001_fundamentos_y_logica - #035)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** ventanas, bucles, listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Resumen por ventanas para logs de acceso. Recibes valores y tamano de ventana 3. Devuelve suma de cada ventana consecutiva.
- **Entrada:** `valores = [18, 35, 5, -2, 7]`
- **Salida esperada:** `[58, 47, 17]`
- **Reglas:** Genera ventanas completas solamente.
- **Pista opcional:** Recorre hasta len(valores)-2.

## Ejercicio #0036 (Modulo 001_fundamentos_y_logica - #036)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** agregaciones, multiples listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Categorias con umbral para reservas de sala. Recibes categorias y cantidades. Devuelve categorias cuyo total supera el umbral.
- **Entrada:** `categorias = ["A", "B", "A", "C"]; cantidades = [19, 37, 6, -1]; umbral = 10`
- **Salida esperada:** `["A", "B"]`
- **Reglas:** Acumula por categoria y filtra al final.
- **Pista opcional:** Puedes usar listas paralelas.

## Ejercicio #0037 (Modulo 001_fundamentos_y_logica - #037)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** listas paralelas, reportes, acumuladores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Reporte critico para ventas de tienda. Recibes nombres, valores actuales y limites. Devuelve nombres cuyo valor esta por debajo del limite y el deficit total.
- **Entrada:** `nombres = ["A", "B", "C"]; valores = [20, 39, 7]; limites = [11, 9, 6]`
- **Salida esperada:** `{"criticos": [], "deficit_total": 0}`
- **Reglas:** Compara cada valor con su limite y suma solo deficits positivos.
- **Pista opcional:** El deficit es limite - valor.

## Ejercicio #0038 (Modulo 001_fundamentos_y_logica - #038)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** ranking, ordenamiento, empates
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Ranking con empates para partidas de juego. Recibes nombres y puntos. Devuelve ranking descendente; si empatan, ordena por nombre.
- **Entrada:** `nombres = ["Ana", "Luis", "Eva"]; puntos = [21, 41, 8]`
- **Salida esperada:** `["Luis", "Ana", "Eva"]`
- **Reglas:** Ordena por puntos descendente y nombre ascendente.
- **Pista opcional:** Usa pares nombre-punto.

## Ejercicio #0039 (Modulo 001_fundamentos_y_logica - #039)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** simulaciones, listas, limites
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Simulacion con limite para prestamos de biblioteca. Recibes nivel inicial y cambios. Devuelve historial sin bajar de 0 ni subir de 100.
- **Entrada:** `nivel = 22; cambios = [2, 2, -4, 3]`
- **Salida esperada:** `[24, 26, 22, 25]`
- **Reglas:** Despues de cada cambio guarda el nivel ajustado.
- **Pista opcional:** Aplica limites luego de sumar.

## Ejercicio #0040 (Modulo 001_fundamentos_y_logica - #040)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** metricas, filtros, promedios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Metricas de aprobacion para envios urbanos. Recibes valores y minimo aprobado. Devuelve aprobados, rechazados y promedio de aprobados.
- **Entrada:** `valores = [23, 45, 10, -2]; minimo = 8`
- **Salida esperada:** `{"aprobados": 3, "rechazados": 1, "promedio_aprobados": 26.0}`
- **Reglas:** Si no hay aprobados, promedio_aprobados es 0.
- **Pista opcional:** Filtra antes de promediar.

## Ejercicio #0041 (Modulo 001_fundamentos_y_logica - #041)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** listas, rachas, contadores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Deteccion de racha para inventario de farmacia. Recibes estados. Devuelve la racha mas larga de estados de alerta.
- **Entrada:** `estados = ["ok", "alerta", "alerta", "ok", "alerta", "alerta"]`
- **Salida esperada:** `2`
- **Reglas:** Una racha se corta cuando el estado no es alerta.
- **Pista opcional:** Compara racha actual contra mejor.

## Ejercicio #0042 (Modulo 001_fundamentos_y_logica - #042)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** busqueda, listas, clasificacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Cruce de dos listas para pedidos de cafeteria. Recibes ids solicitados e ids disponibles. Devuelve atendidos y faltantes conservando orden solicitado.
- **Entrada:** `solicitados = [22, 23, 24, 25]; disponibles = [23, 25, 27]`
- **Salida esperada:** `{"atendidos": [23, 25], "faltantes": [22, 24]}`
- **Reglas:** No dupliques resultados.
- **Pista opcional:** Revisa cada solicitado.

## Ejercicio #0043 (Modulo 001_fundamentos_y_logica - #043)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** ventanas, bucles, listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Resumen por ventanas para notas de estudiantes. Recibes valores y tamano de ventana 3. Devuelve suma de cada ventana consecutiva.
- **Entrada:** `valores = [26, 51, 6, 1, 6]`
- **Salida esperada:** `[83, 63, 19]`
- **Reglas:** Genera ventanas completas solamente.
- **Pista opcional:** Recorre hasta len(valores)-2.

## Ejercicio #0044 (Modulo 001_fundamentos_y_logica - #044)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** agregaciones, multiples listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Categorias con umbral para sensores de clima. Recibes categorias y cantidades. Devuelve categorias cuyo total supera el umbral.
- **Entrada:** `categorias = ["A", "B", "A", "C"]; cantidades = [27, 53, 7, 2]; umbral = 6`
- **Salida esperada:** `["A", "B"]`
- **Reglas:** Acumula por categoria y filtra al final.
- **Pista opcional:** Puedes usar listas paralelas.

## Ejercicio #0045 (Modulo 001_fundamentos_y_logica - #045)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** listas paralelas, reportes, acumuladores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Reporte critico para logs de acceso. Recibes nombres, valores actuales y limites. Devuelve nombres cuyo valor esta por debajo del limite y el deficit total.
- **Entrada:** `nombres = ["A", "B", "C"]; valores = [28, 55, 8]; limites = [7, 7, 6]`
- **Salida esperada:** `{"criticos": [], "deficit_total": 0}`
- **Reglas:** Compara cada valor con su limite y suma solo deficits positivos.
- **Pista opcional:** El deficit es limite - valor.

## Ejercicio #0046 (Modulo 001_fundamentos_y_logica - #046)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** ranking, ordenamiento, empates
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Ranking con empates para reservas de sala. Recibes nombres y puntos. Devuelve ranking descendente; si empatan, ordena por nombre.
- **Entrada:** `nombres = ["Ana", "Luis", "Eva"]; puntos = [29, 57, 9]`
- **Salida esperada:** `["Luis", "Ana", "Eva"]`
- **Reglas:** Ordena por puntos descendente y nombre ascendente.
- **Pista opcional:** Usa pares nombre-punto.

## Ejercicio #0047 (Modulo 001_fundamentos_y_logica - #047)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** simulaciones, listas, limites
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Simulacion con limite para ventas de tienda. Recibes nivel inicial y cambios. Devuelve historial sin bajar de 0 ni subir de 100.
- **Entrada:** `nivel = 30; cambios = [0, 1, -4, 5]`
- **Salida esperada:** `[30, 31, 27, 32]`
- **Reglas:** Despues de cada cambio guarda el nivel ajustado.
- **Pista opcional:** Aplica limites luego de sumar.

## Ejercicio #0048 (Modulo 001_fundamentos_y_logica - #048)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** metricas, filtros, promedios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Metricas de aprobacion para partidas de juego. Recibes valores y minimo aprobado. Devuelve aprobados, rechazados y promedio de aprobados.
- **Entrada:** `valores = [31, 61, 4, 1]; minimo = 10`
- **Salida esperada:** `{"aprobados": 2, "rechazados": 2, "promedio_aprobados": 46.0}`
- **Reglas:** Si no hay aprobados, promedio_aprobados es 0.
- **Pista opcional:** Filtra antes de promediar.

## Ejercicio #0049 (Modulo 001_fundamentos_y_logica - #049)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** busqueda, listas, clasificacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Cruce de dos listas para envios urbanos. Recibes ids solicitados e ids disponibles. Devuelve atendidos y faltantes conservando orden solicitado.
- **Entrada:** `solicitados = [30, 31, 32, 33]; disponibles = [31, 33, 35]`
- **Salida esperada:** `{"atendidos": [31, 33], "faltantes": [30, 32]}`
- **Reglas:** No dupliques resultados.
- **Pista opcional:** Revisa cada solicitado.

## Ejercicio #0050 (Modulo 001_fundamentos_y_logica - #050)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** ventanas, bucles, listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Resumen por ventanas para inventario de farmacia. Recibes valores y tamano de ventana 3. Devuelve suma de cada ventana consecutiva.
- **Entrada:** `valores = [34, 67, 7, -1, 5]`
- **Salida esperada:** `[108, 79, 15]`
- **Reglas:** Genera ventanas completas solamente.
- **Pista opcional:** Recorre hasta len(valores)-2.

## Ejercicio #0051 (Modulo 001_fundamentos_y_logica - #051)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** agregaciones, multiples listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Categorias con umbral para pedidos de cafeteria. Recibes categorias y cantidades. Devuelve categorias cuyo total supera el umbral.
- **Entrada:** `categorias = ["A", "B", "A", "C"]; cantidades = [35, 69, 8, 0]; umbral = 8`
- **Salida esperada:** `["A", "B"]`
- **Reglas:** Acumula por categoria y filtra al final.
- **Pista opcional:** Puedes usar listas paralelas.

## Ejercicio #0052 (Modulo 001_fundamentos_y_logica - #052)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** listas paralelas, reportes, acumuladores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Reporte critico para notas de estudiantes. Recibes nombres, valores actuales y limites. Devuelve nombres cuyo valor esta por debajo del limite y el deficit total.
- **Entrada:** `nombres = ["A", "B", "C"]; valores = [36, 71, 9]; limites = [9, 10, 6]`
- **Salida esperada:** `{"criticos": [], "deficit_total": 0}`
- **Reglas:** Compara cada valor con su limite y suma solo deficits positivos.
- **Pista opcional:** El deficit es limite - valor.

## Ejercicio #0053 (Modulo 001_fundamentos_y_logica - #053)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** ranking, ordenamiento, empates
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Ranking con empates para sensores de clima. Recibes nombres y puntos. Devuelve ranking descendente; si empatan, ordena por nombre.
- **Entrada:** `nombres = ["Ana", "Luis", "Eva"]; puntos = [37, 73, 10]`
- **Salida esperada:** `["Luis", "Ana", "Eva"]`
- **Reglas:** Ordena por puntos descendente y nombre ascendente.
- **Pista opcional:** Usa pares nombre-punto.

## Ejercicio #0054 (Modulo 001_fundamentos_y_logica - #054)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** simulaciones, listas, limites
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Simulacion con limite para logs de acceso. Recibes nivel inicial y cambios. Devuelve historial sin bajar de 0 ni subir de 100.
- **Entrada:** `nivel = 38; cambios = [-2, 9, -4, 7]`
- **Salida esperada:** `[36, 45, 41, 48]`
- **Reglas:** Despues de cada cambio guarda el nivel ajustado.
- **Pista opcional:** Aplica limites luego de sumar.

## Ejercicio #0055 (Modulo 001_fundamentos_y_logica - #055)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** metricas, filtros, promedios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Metricas de aprobacion para reservas de sala. Recibes valores y minimo aprobado. Devuelve aprobados, rechazados y promedio de aprobados.
- **Entrada:** `valores = [39, 77, 5, -1]; minimo = 6`
- **Salida esperada:** `{"aprobados": 2, "rechazados": 2, "promedio_aprobados": 58.0}`
- **Reglas:** Si no hay aprobados, promedio_aprobados es 0.
- **Pista opcional:** Filtra antes de promediar.

## Ejercicio #0056 (Modulo 001_fundamentos_y_logica - #056)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** busqueda, listas, clasificacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Cruce de dos listas para partidas de juego. Recibes ids solicitados e ids disponibles. Devuelve atendidos y faltantes conservando orden solicitado.
- **Entrada:** `solicitados = [38, 39, 40, 41]; disponibles = [39, 41, 43]`
- **Salida esperada:** `{"atendidos": [39, 41], "faltantes": [38, 40]}`
- **Reglas:** No dupliques resultados.
- **Pista opcional:** Revisa cada solicitado.

## Ejercicio #0057 (Modulo 001_fundamentos_y_logica - #057)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** ventanas, bucles, listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Resumen por ventanas para prestamos de biblioteca. Recibes valores y tamano de ventana 3. Devuelve suma de cada ventana consecutiva.
- **Entrada:** `valores = [42, 83, 8, 2, 4]`
- **Salida esperada:** `[133, 95, 17]`
- **Reglas:** Genera ventanas completas solamente.
- **Pista opcional:** Recorre hasta len(valores)-2.

## Ejercicio #0058 (Modulo 001_fundamentos_y_logica - #058)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** agregaciones, multiples listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Categorias con umbral para envios urbanos. Recibes categorias y cantidades. Devuelve categorias cuyo total supera el umbral.
- **Entrada:** `categorias = ["A", "B", "A", "C"]; cantidades = [43, 85, 9, -2]; umbral = 10`
- **Salida esperada:** `["A", "B"]`
- **Reglas:** Acumula por categoria y filtra al final.
- **Pista opcional:** Puedes usar listas paralelas.

## Ejercicio #0059 (Modulo 001_fundamentos_y_logica - #059)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** listas paralelas, reportes, acumuladores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Reporte critico para inventario de farmacia. Recibes nombres, valores actuales y limites. Devuelve nombres cuyo valor esta por debajo del limite y el deficit total.
- **Entrada:** `nombres = ["A", "B", "C"]; valores = [44, 87, 10]; limites = [11, 8, 6]`
- **Salida esperada:** `{"criticos": [], "deficit_total": 0}`
- **Reglas:** Compara cada valor con su limite y suma solo deficits positivos.
- **Pista opcional:** El deficit es limite - valor.

## Ejercicio #0060 (Modulo 001_fundamentos_y_logica - #060)
- **Nivel de dificultad:** Nivel 3 - Practico
- **Conceptos involucrados:** ranking, ordenamiento, empates
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Ranking con empates para pedidos de cafeteria. Recibes nombres y puntos. Devuelve ranking descendente; si empatan, ordena por nombre.
- **Entrada:** `nombres = ["Ana", "Luis", "Eva"]; puntos = [45, 89, 4]`
- **Salida esperada:** `["Luis", "Ana", "Eva"]`
- **Reglas:** Ordena por puntos descendente y nombre ascendente.
- **Pista opcional:** Usa pares nombre-punto.

## Ejercicio #0061 (Modulo 001_fundamentos_y_logica - #061)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** simulaciones, listas, limites
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Simulacion con limite para notas de estudiantes. Recibes nivel inicial y cambios. Devuelve historial sin bajar de 0 ni subir de 100.
- **Entrada:** `nivel = 46; cambios = [1, 8, -4, 3]`
- **Salida esperada:** `[47, 55, 51, 54]`
- **Reglas:** Despues de cada cambio guarda el nivel ajustado.
- **Pista opcional:** Aplica limites luego de sumar.

## Ejercicio #0062 (Modulo 001_fundamentos_y_logica - #062)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** metricas, filtros, promedios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Metricas de aprobacion para sensores de clima. Recibes valores y minimo aprobado. Devuelve aprobados, rechazados y promedio de aprobados.
- **Entrada:** `valores = [47, 93, 6, 2]; minimo = 8`
- **Salida esperada:** `{"aprobados": 2, "rechazados": 2, "promedio_aprobados": 70.0}`
- **Reglas:** Si no hay aprobados, promedio_aprobados es 0.
- **Pista opcional:** Filtra antes de promediar.

## Ejercicio #0063 (Modulo 001_fundamentos_y_logica - #063)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** busqueda, listas, clasificacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Cruce de dos listas para reservas de sala. Recibes ids solicitados e ids disponibles. Devuelve atendidos y faltantes conservando orden solicitado.
- **Entrada:** `solicitados = [46, 47, 48, 49]; disponibles = [47, 49, 51]`
- **Salida esperada:** `{"atendidos": [47, 49], "faltantes": [46, 48]}`
- **Reglas:** No dupliques resultados.
- **Pista opcional:** Revisa cada solicitado.

## Ejercicio #0064 (Modulo 001_fundamentos_y_logica - #064)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** ventanas, bucles, listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Resumen por ventanas para ventas de tienda. Recibes valores y tamano de ventana 3. Devuelve suma de cada ventana consecutiva.
- **Entrada:** `valores = [50, 99, 9, 0, 3]`
- **Salida esperada:** `[158, 111, 19]`
- **Reglas:** Genera ventanas completas solamente.
- **Pista opcional:** Recorre hasta len(valores)-2.

## Ejercicio #0065 (Modulo 001_fundamentos_y_logica - #065)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** agregaciones, multiples listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Categorias con umbral para partidas de juego. Recibes categorias y cantidades. Devuelve categorias cuyo total supera el umbral.
- **Entrada:** `categorias = ["A", "B", "A", "C"]; cantidades = [51, 101, 10, 1]; umbral = 6`
- **Salida esperada:** `["A", "B"]`
- **Reglas:** Acumula por categoria y filtra al final.
- **Pista opcional:** Puedes usar listas paralelas.

## Ejercicio #0066 (Modulo 001_fundamentos_y_logica - #066)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** listas paralelas, reportes, acumuladores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Reporte critico para prestamos de biblioteca. Recibes nombres, valores actuales y limites. Devuelve nombres cuyo valor esta por debajo del limite y el deficit total.
- **Entrada:** `nombres = ["A", "B", "C"]; valores = [52, 103, 4]; limites = [7, 11, 6]`
- **Salida esperada:** `{"criticos": ["C"], "deficit_total": 2}`
- **Reglas:** Compara cada valor con su limite y suma solo deficits positivos.
- **Pista opcional:** El deficit es limite - valor.

## Ejercicio #0067 (Modulo 001_fundamentos_y_logica - #067)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** ranking, ordenamiento, empates
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Ranking con empates para envios urbanos. Recibes nombres y puntos. Devuelve ranking descendente; si empatan, ordena por nombre.
- **Entrada:** `nombres = ["Ana", "Luis", "Eva"]; puntos = [53, 105, 5]`
- **Salida esperada:** `["Luis", "Ana", "Eva"]`
- **Reglas:** Ordena por puntos descendente y nombre ascendente.
- **Pista opcional:** Usa pares nombre-punto.

## Ejercicio #0068 (Modulo 001_fundamentos_y_logica - #068)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** simulaciones, listas, limites
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Simulacion con limite para inventario de farmacia. Recibes nivel inicial y cambios. Devuelve historial sin bajar de 0 ni subir de 100.
- **Entrada:** `nivel = 54; cambios = [-1, 7, -4, 5]`
- **Salida esperada:** `[53, 60, 56, 61]`
- **Reglas:** Despues de cada cambio guarda el nivel ajustado.
- **Pista opcional:** Aplica limites luego de sumar.

## Ejercicio #0069 (Modulo 001_fundamentos_y_logica - #069)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** metricas, filtros, promedios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Metricas de aprobacion para pedidos de cafeteria. Recibes valores y minimo aprobado. Devuelve aprobados, rechazados y promedio de aprobados.
- **Entrada:** `valores = [55, 109, 7, 0]; minimo = 10`
- **Salida esperada:** `{"aprobados": 2, "rechazados": 2, "promedio_aprobados": 82.0}`
- **Reglas:** Si no hay aprobados, promedio_aprobados es 0.
- **Pista opcional:** Filtra antes de promediar.

## Ejercicio #0070 (Modulo 001_fundamentos_y_logica - #070)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** busqueda, listas, clasificacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Cruce de dos listas para sensores de clima. Recibes ids solicitados e ids disponibles. Devuelve atendidos y faltantes conservando orden solicitado.
- **Entrada:** `solicitados = [54, 55, 56, 57]; disponibles = [55, 57, 59]`
- **Salida esperada:** `{"atendidos": [55, 57], "faltantes": [54, 56]}`
- **Reglas:** No dupliques resultados.
- **Pista opcional:** Revisa cada solicitado.

## Ejercicio #0071 (Modulo 001_fundamentos_y_logica - #071)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** ventanas, bucles, listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Resumen por ventanas para logs de acceso. Recibes valores y tamano de ventana 3. Devuelve suma de cada ventana consecutiva.
- **Entrada:** `valores = [58, 115, 10, -2, 2]`
- **Salida esperada:** `[183, 127, 15]`
- **Reglas:** Genera ventanas completas solamente.
- **Pista opcional:** Recorre hasta len(valores)-2.

## Ejercicio #0072 (Modulo 001_fundamentos_y_logica - #072)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** agregaciones, multiples listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Categorias con umbral para reservas de sala. Recibes categorias y cantidades. Devuelve categorias cuyo total supera el umbral.
- **Entrada:** `categorias = ["A", "B", "A", "C"]; cantidades = [59, 117, 4, -1]; umbral = 8`
- **Salida esperada:** `["A", "B"]`
- **Reglas:** Acumula por categoria y filtra al final.
- **Pista opcional:** Puedes usar listas paralelas.

## Ejercicio #0073 (Modulo 001_fundamentos_y_logica - #073)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** listas paralelas, reportes, acumuladores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Reporte critico para ventas de tienda. Recibes nombres, valores actuales y limites. Devuelve nombres cuyo valor esta por debajo del limite y el deficit total.
- **Entrada:** `nombres = ["A", "B", "C"]; valores = [60, 119, 5]; limites = [9, 9, 6]`
- **Salida esperada:** `{"criticos": ["C"], "deficit_total": 1}`
- **Reglas:** Compara cada valor con su limite y suma solo deficits positivos.
- **Pista opcional:** El deficit es limite - valor.

## Ejercicio #0074 (Modulo 001_fundamentos_y_logica - #074)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** ranking, ordenamiento, empates
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Ranking con empates para partidas de juego. Recibes nombres y puntos. Devuelve ranking descendente; si empatan, ordena por nombre.
- **Entrada:** `nombres = ["Ana", "Luis", "Eva"]; puntos = [61, 121, 6]`
- **Salida esperada:** `["Luis", "Ana", "Eva"]`
- **Reglas:** Ordena por puntos descendente y nombre ascendente.
- **Pista opcional:** Usa pares nombre-punto.

## Ejercicio #0075 (Modulo 001_fundamentos_y_logica - #075)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** simulaciones, listas, limites
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Simulacion con limite para prestamos de biblioteca. Recibes nivel inicial y cambios. Devuelve historial sin bajar de 0 ni subir de 100.
- **Entrada:** `nivel = 62; cambios = [2, 6, -4, 7]`
- **Salida esperada:** `[64, 70, 66, 73]`
- **Reglas:** Despues de cada cambio guarda el nivel ajustado.
- **Pista opcional:** Aplica limites luego de sumar.

## Ejercicio #0076 (Modulo 001_fundamentos_y_logica - #076)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** metricas, filtros, promedios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Metricas de aprobacion para envios urbanos. Recibes valores y minimo aprobado. Devuelve aprobados, rechazados y promedio de aprobados.
- **Entrada:** `valores = [63, 125, 8, -2]; minimo = 6`
- **Salida esperada:** `{"aprobados": 3, "rechazados": 1, "promedio_aprobados": 65.33}`
- **Reglas:** Si no hay aprobados, promedio_aprobados es 0.
- **Pista opcional:** Filtra antes de promediar.

## Ejercicio #0077 (Modulo 001_fundamentos_y_logica - #077)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** busqueda, listas, clasificacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Cruce de dos listas para pedidos de cafeteria. Recibes ids solicitados e ids disponibles. Devuelve atendidos y faltantes conservando orden solicitado.
- **Entrada:** `solicitados = [62, 63, 64, 65]; disponibles = [63, 65, 67]`
- **Salida esperada:** `{"atendidos": [63, 65], "faltantes": [62, 64]}`
- **Reglas:** No dupliques resultados.
- **Pista opcional:** Revisa cada solicitado.

## Ejercicio #0078 (Modulo 001_fundamentos_y_logica - #078)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** ventanas, bucles, listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Resumen por ventanas para notas de estudiantes. Recibes valores y tamano de ventana 3. Devuelve suma de cada ventana consecutiva.
- **Entrada:** `valores = [66, 131, 4, 1, 1]`
- **Salida esperada:** `[201, 136, 10]`
- **Reglas:** Genera ventanas completas solamente.
- **Pista opcional:** Recorre hasta len(valores)-2.

## Ejercicio #0079 (Modulo 001_fundamentos_y_logica - #079)
- **Nivel de dificultad:** Nivel 4 - Intermedio
- **Conceptos involucrados:** agregaciones, multiples listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Categorias con umbral para sensores de clima. Recibes categorias y cantidades. Devuelve categorias cuyo total supera el umbral.
- **Entrada:** `categorias = ["A", "B", "A", "C"]; cantidades = [67, 133, 5, 2]; umbral = 10`
- **Salida esperada:** `["A", "B"]`
- **Reglas:** Acumula por categoria y filtra al final.
- **Pista opcional:** Puedes usar listas paralelas.

## Ejercicio #0080 (Modulo 001_fundamentos_y_logica - #080)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** listas paralelas, reportes, acumuladores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Reporte critico para logs de acceso. Recibes nombres, valores actuales y limites. Devuelve nombres cuyo valor esta por debajo del limite y el deficit total.
- **Entrada:** `nombres = ["A", "B", "C"]; valores = [68, 135, 6]; limites = [11, 7, 6]`
- **Salida esperada:** `{"criticos": [], "deficit_total": 0}`
- **Reglas:** Compara cada valor con su limite y suma solo deficits positivos.
- **Pista opcional:** El deficit es limite - valor.

## Ejercicio #0081 (Modulo 001_fundamentos_y_logica - #081)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** ranking, ordenamiento, empates
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Ranking con empates para reservas de sala. Recibes nombres y puntos. Devuelve ranking descendente; si empatan, ordena por nombre.
- **Entrada:** `nombres = ["Ana", "Luis", "Eva"]; puntos = [69, 137, 7]`
- **Salida esperada:** `["Luis", "Ana", "Eva"]`
- **Reglas:** Ordena por puntos descendente y nombre ascendente.
- **Pista opcional:** Usa pares nombre-punto.

## Ejercicio #0082 (Modulo 001_fundamentos_y_logica - #082)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** simulaciones, listas, limites
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Simulacion con limite para ventas de tienda. Recibes nivel inicial y cambios. Devuelve historial sin bajar de 0 ni subir de 100.
- **Entrada:** `nivel = 70; cambios = [0, 5, -4, 3]`
- **Salida esperada:** `[70, 75, 71, 74]`
- **Reglas:** Despues de cada cambio guarda el nivel ajustado.
- **Pista opcional:** Aplica limites luego de sumar.

## Ejercicio #0083 (Modulo 001_fundamentos_y_logica - #083)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** metricas, filtros, promedios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Metricas de aprobacion para partidas de juego. Recibes valores y minimo aprobado. Devuelve aprobados, rechazados y promedio de aprobados.
- **Entrada:** `valores = [71, 141, 9, 1]; minimo = 8`
- **Salida esperada:** `{"aprobados": 3, "rechazados": 1, "promedio_aprobados": 73.67}`
- **Reglas:** Si no hay aprobados, promedio_aprobados es 0.
- **Pista opcional:** Filtra antes de promediar.

## Ejercicio #0084 (Modulo 001_fundamentos_y_logica - #084)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** busqueda, listas, clasificacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Cruce de dos listas para envios urbanos. Recibes ids solicitados e ids disponibles. Devuelve atendidos y faltantes conservando orden solicitado.
- **Entrada:** `solicitados = [70, 71, 72, 73]; disponibles = [71, 73, 75]`
- **Salida esperada:** `{"atendidos": [71, 73], "faltantes": [70, 72]}`
- **Reglas:** No dupliques resultados.
- **Pista opcional:** Revisa cada solicitado.

## Ejercicio #0085 (Modulo 001_fundamentos_y_logica - #085)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** ventanas, bucles, listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Resumen por ventanas para inventario de farmacia. Recibes valores y tamano de ventana 3. Devuelve suma de cada ventana consecutiva.
- **Entrada:** `valores = [74, 147, 5, -1, 9]`
- **Salida esperada:** `[226, 161, 21]`
- **Reglas:** Genera ventanas completas solamente.
- **Pista opcional:** Recorre hasta len(valores)-2.

## Ejercicio #0086 (Modulo 001_fundamentos_y_logica - #086)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** agregaciones, multiples listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Categorias con umbral para pedidos de cafeteria. Recibes categorias y cantidades. Devuelve categorias cuyo total supera el umbral.
- **Entrada:** `categorias = ["A", "B", "A", "C"]; cantidades = [75, 149, 6, 0]; umbral = 6`
- **Salida esperada:** `["A", "B"]`
- **Reglas:** Acumula por categoria y filtra al final.
- **Pista opcional:** Puedes usar listas paralelas.

## Ejercicio #0087 (Modulo 001_fundamentos_y_logica - #087)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** listas paralelas, reportes, acumuladores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Reporte critico para notas de estudiantes. Recibes nombres, valores actuales y limites. Devuelve nombres cuyo valor esta por debajo del limite y el deficit total.
- **Entrada:** `nombres = ["A", "B", "C"]; valores = [76, 151, 7]; limites = [7, 10, 6]`
- **Salida esperada:** `{"criticos": [], "deficit_total": 0}`
- **Reglas:** Compara cada valor con su limite y suma solo deficits positivos.
- **Pista opcional:** El deficit es limite - valor.

## Ejercicio #0088 (Modulo 001_fundamentos_y_logica - #088)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** ranking, ordenamiento, empates
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Ranking con empates para sensores de clima. Recibes nombres y puntos. Devuelve ranking descendente; si empatan, ordena por nombre.
- **Entrada:** `nombres = ["Ana", "Luis", "Eva"]; puntos = [77, 153, 8]`
- **Salida esperada:** `["Luis", "Ana", "Eva"]`
- **Reglas:** Ordena por puntos descendente y nombre ascendente.
- **Pista opcional:** Usa pares nombre-punto.

## Ejercicio #0089 (Modulo 001_fundamentos_y_logica - #089)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** simulaciones, listas, limites
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Simulacion con limite para logs de acceso. Recibes nivel inicial y cambios. Devuelve historial sin bajar de 0 ni subir de 100.
- **Entrada:** `nivel = 78; cambios = [-2, 4, -4, 5]`
- **Salida esperada:** `[76, 80, 76, 81]`
- **Reglas:** Despues de cada cambio guarda el nivel ajustado.
- **Pista opcional:** Aplica limites luego de sumar.

## Ejercicio #0090 (Modulo 001_fundamentos_y_logica - #090)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** metricas, filtros, promedios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Metricas de aprobacion para reservas de sala. Recibes valores y minimo aprobado. Devuelve aprobados, rechazados y promedio de aprobados.
- **Entrada:** `valores = [79, 157, 10, -1]; minimo = 10`
- **Salida esperada:** `{"aprobados": 3, "rechazados": 1, "promedio_aprobados": 82.0}`
- **Reglas:** Si no hay aprobados, promedio_aprobados es 0.
- **Pista opcional:** Filtra antes de promediar.

## Ejercicio #0091 (Modulo 001_fundamentos_y_logica - #091)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** busqueda, listas, clasificacion
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Cruce de dos listas para partidas de juego. Recibes ids solicitados e ids disponibles. Devuelve atendidos y faltantes conservando orden solicitado.
- **Entrada:** `solicitados = [78, 79, 80, 81]; disponibles = [79, 81, 83]`
- **Salida esperada:** `{"atendidos": [79, 81], "faltantes": [78, 80]}`
- **Reglas:** No dupliques resultados.
- **Pista opcional:** Revisa cada solicitado.

## Ejercicio #0092 (Modulo 001_fundamentos_y_logica - #092)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** ventanas, bucles, listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Resumen por ventanas para prestamos de biblioteca. Recibes valores y tamano de ventana 3. Devuelve suma de cada ventana consecutiva.
- **Entrada:** `valores = [82, 163, 6, 2, 8]`
- **Salida esperada:** `[251, 177, 17]`
- **Reglas:** Genera ventanas completas solamente.
- **Pista opcional:** Recorre hasta len(valores)-2.

## Ejercicio #0093 (Modulo 001_fundamentos_y_logica - #093)
- **Nivel de dificultad:** Nivel 5 - Integrador
- **Conceptos involucrados:** agregaciones, multiples listas
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Categorias con umbral para envios urbanos. Recibes categorias y cantidades. Devuelve categorias cuyo total supera el umbral.
- **Entrada:** `categorias = ["A", "B", "A", "C"]; cantidades = [83, 165, 7, -2]; umbral = 8`
- **Salida esperada:** `["A", "B"]`
- **Reglas:** Acumula por categoria y filtra al final.
- **Pista opcional:** Puedes usar listas paralelas.
