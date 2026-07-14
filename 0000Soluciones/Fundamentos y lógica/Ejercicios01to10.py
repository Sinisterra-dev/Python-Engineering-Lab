
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
