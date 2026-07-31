"""## Ejercicio #0031 (Modulo 001_fundamentos_y_logica - #031)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** simulaciones, listas, limites
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Simulacion con limite para inventario de farmacia. Recibes nivel inicial y cambios. Devuelve historial sin bajar de 0 ni subir de 100.
- **Entrada:** `nivel = 14; cambios = [-1, 3, -4, 7]`
- **Salida esperada:** `[13, 16, 12, 19]`
- **Reglas:** Despues de cada cambio guarda el nivel ajustado.
- **Pista opcional:** Aplica limites luego de sumar."""

nivel = 14; cambios = [-1, 3, -4, 7]
actual = nivel
acumulado = []

for cambio in cambios:
    actual += cambio
    if actual <= 0:
        actual = 0
    if actual > 100:
        actual = 100
    acumulado.append(actual)
print (acumulado)
    
    

"""## Ejercicio #0032 (Modulo 001_fundamentos_y_logica - #032)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** metricas, filtros, promedios
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Metricas de aprobacion para pedidos de cafeteria. Recibes valores y minimo aprobado. Devuelve aprobados, rechazados y promedio de aprobados.
- **Entrada:** `valores = [15, 29, 9, 0]; minimo = 6`
- **Salida esperada:** `{"aprobados": 3, "rechazados": 1, "promedio_aprobados": 17.67}`
- **Reglas:** Si no hay aprobados, promedio_aprobados es 0.
- **Pista opcional:** Filtra antes de promediar."""

"""## Ejercicio #0033 (Modulo 001_fundamentos_y_logica - #033)
- **Nivel de dificultad:** Nivel 2 - Basico
- **Conceptos involucrados:** listas, rachas, contadores
- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
- **Problema:** Deteccion de racha para notas de estudiantes. Recibes estados. Devuelve la racha mas larga de estados de alerta.
- **Entrada:** `estados = ["alerta", "alerta", "ok", "alerta", "alerta", "ok"]`
- **Salida esperada:** `2`
- **Reglas:** Una racha se corta cuando el estado no es alerta.
- **Pista opcional:** Compara racha actual contra mejor."""

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
- **Pista opcional:** Puedes usar listas paralelas."""
