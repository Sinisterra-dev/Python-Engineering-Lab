
## Ejercicio #0001 (Modulo 001_fundamentos_y_logica - #001)
#- **Nivel de dificultad:** Nivel 1 - Inicial
#- **Conceptos involucrados:** variables, operadores
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Total de caja diaria. Recibes billetes de 100, 50 y 20. Devuelve el dinero total.
#- **Entrada:** `b100 = 3; b50 = 4; b20 = 2`
#- **Salida esperada:** `540`
#- **Reglas:** Usa operaciones aritmeticas simples.
#- **Pista opcional:** Multiplica cada cantidad por su valor.


billete1 = 100
billete2 = 50
billete3 = 20

cuenta_total = billete1 * 3 + billete2 * 4 + billete3 * 2
print(cuenta_total)

## Ejercicio #0002 (Modulo 001_fundamentos_y_logica - #002)
#- **Nivel de dificultad:** Nivel 1 - Inicial
#- **Conceptos involucrados:** if, else
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Estado de bateria de sensor. Recibes porcentaje de bateria. Devuelve "critica" si es menor a 15, si no "normal".
#- **Entrada:** `bateria = 12`
#- **Salida esperada:** `"critica"`
#- **Reglas:** Usa una condicion directa.
#- **Pista opcional:** Compara contra el umbral.

bateria = 12
nivel_bateria = bateria
umbral = 15
if nivel_bateria < umbral:
    print("Estado normal")
else:
    print("critica")

## Ejercicio #0003 (Modulo 001_fundamentos_y_logica - #003)
#- **Nivel de dificultad:** Nivel 1 - Inicial
#- **Conceptos involucrados:** for, acumuladores
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Minutos atendidos por soporte. Recibes duraciones de llamadas. Devuelve el total de minutos.
#- **Entrada:** `llamadas = [4, 12, 8]`
#- **Salida esperada:** `24`
#- **Reglas:** Recorre la lista con for.
#- **Pista opcional:** Acumula cada duracion.

llamadas = [4, 12, 8]
number_minutes = 0
for minutos in llamadas:
    number_minutes += minutos
print (number_minutes)

## Ejercicio #0004 (Modulo 001_fundamentos_y_logica - #004)
#- **Nivel de dificultad:** Nivel 1 - Inicial
#- **Conceptos involucrados:** for, contadores
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Productos agotados en estanteria. Recibes stocks. Cuenta cuantos son exactamente cero.
#- **Entrada:** `stocks = [3, 0, 8, 0, 1]`
#- **Salida esperada:** `2`
#- **Reglas:** Usa un contador.
#- **Pista opcional:** Incrementa cuando el stock sea 0.

stocks = [3, 0, 8, 0, 1]
contador = 0
for stock in stocks:
    if stock == 0:
        contador += 1
print(contador)


## Ejercicio #0005 (Modulo 001_fundamentos_y_logica - #005)
#- **Nivel de dificultad:** Nivel 1 - Inicial
#- **Conceptos involucrados:** while, simulacion
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Consumir creditos de juego. Recibes creditos y costo por partida. Devuelve cuantas partidas se pueden jugar.
#- **Entrada:** `creditos = 17; costo = 5`
#- **Salida esperada:** `3`
#- **Reglas:** Usa while restando el costo hasta que no alcance.
#- **Pista opcional:** Cuenta cada partida jugada.

creditos = 17; 
costo = 5
partidas_acumuladas = 0
while costo <= creditos:
    creditos -= costo
    partidas_acumuladas += 1
print(partidas_acumuladas)


## Ejercicio #0006 (Modulo 001_fundamentos_y_logica - #006)
#- **Nivel de dificultad:** Nivel 1 - Inicial
#- **Conceptos involucrados:** busqueda basica
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Encontrar turno libre. Recibes estados de turnos. Devuelve el primer indice con "libre" o -1.
#- **Entrada:** `turnos = ["ocupado", "ocupado", "libre"]`
#- **Salida esperada:** `2`
#- **Reglas:** Deten la busqueda al encontrar el primer libre.
#- **Pista opcional:** Guarda el indice encontrado.

## Ejercicio #0007 (Modulo 001_fundamentos_y_logica - #007)
#- **Nivel de dificultad:** Nivel 1 - Inicial
#- **Conceptos involucrados:** validaciones simples
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Validar temperatura de heladera. Recibes temperatura. Devuelve True si esta entre 2 y 8 inclusive.
#- **Entrada:** `temperatura = 9`
#- **Salida esperada:** `False`
#- **Reglas:** Combina dos comparaciones.
#- **Pista opcional:** Usa and.

## Ejercicio #0008 (Modulo 001_fundamentos_y_logica - #008)
#- **Nivel de dificultad:** Nivel 1 - Inicial
#- **Conceptos involucrados:** strings, contadores
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Contar codigos con prefijo. Recibes codigos y un prefijo. Cuenta cuantos empiezan con ese prefijo.
#- **Entrada:** `codigos = ["A-1", "B-2", "A-3"]; prefijo = "A"`
#- **Salida esperada:** `2`
#- **Reglas:** Revisa cada string.
#- **Pista opcional:** startswith puede ayudar.

## Ejercicio #0009 (Modulo 001_fundamentos_y_logica - #009)
#- **Nivel de dificultad:** Nivel 1 - Inicial
#- **Conceptos involucrados:** listas, filtros
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Pedidos mayores al minimo. Recibes importes y un minimo. Devuelve importes que superan el minimo.
#- **Entrada:** `importes = [80, 120, 40, 200]; minimo = 100`
#- **Salida esperada:** `[120, 200]`
#- **Reglas:** Construye una lista nueva.
#- **Pista opcional:** Agrega solo los que cumplen.

## Ejercicio #0010 (Modulo 001_fundamentos_y_logica - #010)
#- **Nivel de dificultad:** Nivel 1 - Inicial
#- **Conceptos involucrados:** maximos
#- **Prerequisitos:** leer el enunciado, ejecutar el codigo y probar al menos un caso adicional.
#- **Problema:** Mayor puntaje de partida. Recibes puntajes. Devuelve el mayor sin usar max.
#- **Entrada:** `puntajes = [12, 40, 25, 39]`
#- **Salida esperada:** `40`
#- **Reglas:** Inicializa con el primer puntaje.
# **Pista opcional:** Actualiza cuando encuentres uno mayor.