# Ejercicios — Modelado de bases de datos

Total del módulo: **50 ejercicios**.

Cada ejercicio incluye: número, nivel, conceptos, prerequisitos, historia de usuario, objetivo, restricciones, entrada, salida y pista opcional.

## Ejercicio #2556 (Módulo 029_modelado_de_bases_de_datos — #001)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** entidades, normalización
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un SaaS B2B necesita estandarizar su lógica de negocio.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2557 (Módulo 029_modelado_de_bases_de_datos — #002)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** normalización, restricciones
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un marketplace quiere detectar inconsistencias operativas en tiempo real.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2558 (Módulo 029_modelado_de_bases_de_datos — #003)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** restricciones, claves
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Una API interna debe soportar reglas de validación más estrictas.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2559 (Módulo 029_modelado_de_bases_de_datos — #004)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** claves, consistencia
- **Prerequisitos:** 028_sql_avanzado, 027_sql_intermedio
- **Historia de usuario:** Un equipo de soporte requiere reportes confiables para tomar decisiones.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2560 (Módulo 029_modelado_de_bases_de_datos — #005)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** consistencia, entidades
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Una empresa de suscripciones necesita automatizar verificaciones críticas.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2561 (Módulo 029_modelado_de_bases_de_datos — #006)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** entidades, normalización
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Una plataforma de e-commerce necesita mejorar su operación diaria.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2562 (Módulo 029_modelado_de_bases_de_datos — #007)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** normalización, restricciones
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un sistema de logística debe reducir errores de procesamiento.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2563 (Módulo 029_modelado_de_bases_de_datos — #008)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** restricciones, claves
- **Prerequisitos:** 028_sql_avanzado, 027_sql_intermedio
- **Historia de usuario:** Una fintech requiere mayor trazabilidad de transacciones.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2564 (Módulo 029_modelado_de_bases_de_datos — #009)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** claves, consistencia
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un SaaS B2B necesita estandarizar su lógica de negocio.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2565 (Módulo 029_modelado_de_bases_de_datos — #010)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** consistencia, entidades
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un marketplace quiere detectar inconsistencias operativas en tiempo real.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2566 (Módulo 029_modelado_de_bases_de_datos — #011)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** entidades, normalización
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Una API interna debe soportar reglas de validación más estrictas.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2567 (Módulo 029_modelado_de_bases_de_datos — #012)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** normalización, restricciones
- **Prerequisitos:** 028_sql_avanzado, 027_sql_intermedio
- **Historia de usuario:** Un equipo de soporte requiere reportes confiables para tomar decisiones.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2568 (Módulo 029_modelado_de_bases_de_datos — #013)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** restricciones, claves
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Una empresa de suscripciones necesita automatizar verificaciones críticas.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2569 (Módulo 029_modelado_de_bases_de_datos — #014)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** claves, consistencia
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Una plataforma de e-commerce necesita mejorar su operación diaria.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2570 (Módulo 029_modelado_de_bases_de_datos — #015)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** consistencia, entidades
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un sistema de logística debe reducir errores de procesamiento.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2571 (Módulo 029_modelado_de_bases_de_datos — #016)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** entidades, normalización
- **Prerequisitos:** 028_sql_avanzado, 027_sql_intermedio
- **Historia de usuario:** Una fintech requiere mayor trazabilidad de transacciones.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2572 (Módulo 029_modelado_de_bases_de_datos — #017)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** normalización, restricciones
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un SaaS B2B necesita estandarizar su lógica de negocio.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2573 (Módulo 029_modelado_de_bases_de_datos — #018)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** restricciones, claves
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un marketplace quiere detectar inconsistencias operativas en tiempo real.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2574 (Módulo 029_modelado_de_bases_de_datos — #019)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** claves, consistencia
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Una API interna debe soportar reglas de validación más estrictas.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2575 (Módulo 029_modelado_de_bases_de_datos — #020)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** consistencia, entidades
- **Prerequisitos:** 028_sql_avanzado, 027_sql_intermedio
- **Historia de usuario:** Un equipo de soporte requiere reportes confiables para tomar decisiones.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2576 (Módulo 029_modelado_de_bases_de_datos — #021)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** entidades, normalización
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Una empresa de suscripciones necesita automatizar verificaciones críticas.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2577 (Módulo 029_modelado_de_bases_de_datos — #022)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** normalización, restricciones
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Una plataforma de e-commerce necesita mejorar su operación diaria.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2578 (Módulo 029_modelado_de_bases_de_datos — #023)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** restricciones, claves
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un sistema de logística debe reducir errores de procesamiento.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2579 (Módulo 029_modelado_de_bases_de_datos — #024)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** claves, consistencia
- **Prerequisitos:** 028_sql_avanzado, 027_sql_intermedio
- **Historia de usuario:** Una fintech requiere mayor trazabilidad de transacciones.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2580 (Módulo 029_modelado_de_bases_de_datos — #025)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** consistencia, entidades
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un SaaS B2B necesita estandarizar su lógica de negocio.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2581 (Módulo 029_modelado_de_bases_de_datos — #026)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** entidades, normalización
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un marketplace quiere detectar inconsistencias operativas en tiempo real.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2582 (Módulo 029_modelado_de_bases_de_datos — #027)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** normalización, restricciones
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Una API interna debe soportar reglas de validación más estrictas.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2583 (Módulo 029_modelado_de_bases_de_datos — #028)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** restricciones, claves
- **Prerequisitos:** 028_sql_avanzado, 027_sql_intermedio
- **Historia de usuario:** Un equipo de soporte requiere reportes confiables para tomar decisiones.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2584 (Módulo 029_modelado_de_bases_de_datos — #029)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** claves, consistencia
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Una empresa de suscripciones necesita automatizar verificaciones críticas.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2585 (Módulo 029_modelado_de_bases_de_datos — #030)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** consistencia, entidades
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Una plataforma de e-commerce necesita mejorar su operación diaria.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2586 (Módulo 029_modelado_de_bases_de_datos — #031)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** entidades, normalización
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un sistema de logística debe reducir errores de procesamiento.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2587 (Módulo 029_modelado_de_bases_de_datos — #032)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** normalización, restricciones
- **Prerequisitos:** 028_sql_avanzado, 027_sql_intermedio
- **Historia de usuario:** Una fintech requiere mayor trazabilidad de transacciones.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2588 (Módulo 029_modelado_de_bases_de_datos — #033)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** restricciones, claves
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un SaaS B2B necesita estandarizar su lógica de negocio.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2589 (Módulo 029_modelado_de_bases_de_datos — #034)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** claves, consistencia
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un marketplace quiere detectar inconsistencias operativas en tiempo real.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2590 (Módulo 029_modelado_de_bases_de_datos — #035)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** consistencia, entidades
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Una API interna debe soportar reglas de validación más estrictas.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2591 (Módulo 029_modelado_de_bases_de_datos — #036)
- **Nivel de dificultad:** Nivel 5 — Avanzado
- **Conceptos involucrados:** entidades, normalización
- **Prerequisitos:** 028_sql_avanzado, 027_sql_intermedio
- **Historia de usuario:** Un equipo de soporte requiere reportes confiables para tomar decisiones.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2592 (Módulo 029_modelado_de_bases_de_datos — #037)
- **Nivel de dificultad:** Nivel 5 — Avanzado
- **Conceptos involucrados:** normalización, restricciones
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Una empresa de suscripciones necesita automatizar verificaciones críticas.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2593 (Módulo 029_modelado_de_bases_de_datos — #038)
- **Nivel de dificultad:** Nivel 5 — Avanzado
- **Conceptos involucrados:** restricciones, claves
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Una plataforma de e-commerce necesita mejorar su operación diaria.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2594 (Módulo 029_modelado_de_bases_de_datos — #039)
- **Nivel de dificultad:** Nivel 5 — Avanzado
- **Conceptos involucrados:** claves, consistencia
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un sistema de logística debe reducir errores de procesamiento.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2595 (Módulo 029_modelado_de_bases_de_datos — #040)
- **Nivel de dificultad:** Nivel 5 — Avanzado
- **Conceptos involucrados:** consistencia, entidades
- **Prerequisitos:** 028_sql_avanzado, 027_sql_intermedio
- **Historia de usuario:** Una fintech requiere mayor trazabilidad de transacciones.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2596 (Módulo 029_modelado_de_bases_de_datos — #041)
- **Nivel de dificultad:** Nivel 5 — Avanzado
- **Conceptos involucrados:** entidades, normalización
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un SaaS B2B necesita estandarizar su lógica de negocio.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2597 (Módulo 029_modelado_de_bases_de_datos — #042)
- **Nivel de dificultad:** Nivel 5 — Avanzado
- **Conceptos involucrados:** normalización, restricciones
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un marketplace quiere detectar inconsistencias operativas en tiempo real.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2598 (Módulo 029_modelado_de_bases_de_datos — #043)
- **Nivel de dificultad:** Nivel 5 — Avanzado
- **Conceptos involucrados:** restricciones, claves
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Una API interna debe soportar reglas de validación más estrictas.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2599 (Módulo 029_modelado_de_bases_de_datos — #044)
- **Nivel de dificultad:** Nivel 6 — Muy avanzado
- **Conceptos involucrados:** claves, consistencia
- **Prerequisitos:** 028_sql_avanzado, 027_sql_intermedio
- **Historia de usuario:** Un equipo de soporte requiere reportes confiables para tomar decisiones.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2600 (Módulo 029_modelado_de_bases_de_datos — #045)
- **Nivel de dificultad:** Nivel 6 — Muy avanzado
- **Conceptos involucrados:** consistencia, entidades
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Una empresa de suscripciones necesita automatizar verificaciones críticas.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2601 (Módulo 029_modelado_de_bases_de_datos — #046)
- **Nivel de dificultad:** Nivel 6 — Muy avanzado
- **Conceptos involucrados:** entidades, normalización
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Una plataforma de e-commerce necesita mejorar su operación diaria.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2602 (Módulo 029_modelado_de_bases_de_datos — #047)
- **Nivel de dificultad:** Nivel 6 — Muy avanzado
- **Conceptos involucrados:** normalización, restricciones
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un sistema de logística debe reducir errores de procesamiento.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2603 (Módulo 029_modelado_de_bases_de_datos — #048)
- **Nivel de dificultad:** Nivel 6 — Muy avanzado
- **Conceptos involucrados:** restricciones, claves
- **Prerequisitos:** 028_sql_avanzado, 027_sql_intermedio
- **Historia de usuario:** Una fintech requiere mayor trazabilidad de transacciones.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2604 (Módulo 029_modelado_de_bases_de_datos — #049)
- **Nivel de dificultad:** Nivel 6 — Muy avanzado
- **Conceptos involucrados:** claves, consistencia
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un SaaS B2B necesita estandarizar su lógica de negocio.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2605 (Módulo 029_modelado_de_bases_de_datos — #050)
- **Nivel de dificultad:** Nivel 6 — Muy avanzado
- **Conceptos involucrados:** consistencia, entidades
- **Prerequisitos:** 028_sql_avanzado
- **Historia de usuario:** Un marketplace quiere detectar inconsistencias operativas en tiempo real.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.
