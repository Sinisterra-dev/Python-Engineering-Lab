# Ejercicios — Relaciones SQL

Total del módulo: **40 ejercicios**.

Cada ejercicio incluye: número, nivel, conceptos, prerequisitos, historia de usuario, objetivo, restricciones, entrada, salida y pista opcional.

## Ejercicio #2606 (Módulo 030_relaciones_sql — #001)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** 1:1, 1:N
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Una API interna debe soportar reglas de validación más estrictas.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2607 (Módulo 030_relaciones_sql — #002)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** 1:N, N:M
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Un equipo de soporte requiere reportes confiables para tomar decisiones.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2608 (Módulo 030_relaciones_sql — #003)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** N:M, integridad referencial
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Una empresa de suscripciones necesita automatizar verificaciones críticas.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2609 (Módulo 030_relaciones_sql — #004)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** integridad referencial, cascadas
- **Prerequisitos:** 029_modelado_de_bases_de_datos, 028_sql_avanzado
- **Historia de usuario:** Una plataforma de e-commerce necesita mejorar su operación diaria.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2610 (Módulo 030_relaciones_sql — #005)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** cascadas, 1:1
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Un sistema de logística debe reducir errores de procesamiento.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2611 (Módulo 030_relaciones_sql — #006)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** 1:1, 1:N
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Una fintech requiere mayor trazabilidad de transacciones.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2612 (Módulo 030_relaciones_sql — #007)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** 1:N, N:M
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Un SaaS B2B necesita estandarizar su lógica de negocio.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2613 (Módulo 030_relaciones_sql — #008)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** N:M, integridad referencial
- **Prerequisitos:** 029_modelado_de_bases_de_datos, 028_sql_avanzado
- **Historia de usuario:** Un marketplace quiere detectar inconsistencias operativas en tiempo real.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2614 (Módulo 030_relaciones_sql — #009)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** integridad referencial, cascadas
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Una API interna debe soportar reglas de validación más estrictas.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2615 (Módulo 030_relaciones_sql — #010)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** cascadas, 1:1
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Un equipo de soporte requiere reportes confiables para tomar decisiones.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2616 (Módulo 030_relaciones_sql — #011)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** 1:1, 1:N
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Una empresa de suscripciones necesita automatizar verificaciones críticas.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2617 (Módulo 030_relaciones_sql — #012)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** 1:N, N:M
- **Prerequisitos:** 029_modelado_de_bases_de_datos, 028_sql_avanzado
- **Historia de usuario:** Una plataforma de e-commerce necesita mejorar su operación diaria.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2618 (Módulo 030_relaciones_sql — #013)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** N:M, integridad referencial
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Un sistema de logística debe reducir errores de procesamiento.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2619 (Módulo 030_relaciones_sql — #014)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** integridad referencial, cascadas
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Una fintech requiere mayor trazabilidad de transacciones.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2620 (Módulo 030_relaciones_sql — #015)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** cascadas, 1:1
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Un SaaS B2B necesita estandarizar su lógica de negocio.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2621 (Módulo 030_relaciones_sql — #016)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** 1:1, 1:N
- **Prerequisitos:** 029_modelado_de_bases_de_datos, 028_sql_avanzado
- **Historia de usuario:** Un marketplace quiere detectar inconsistencias operativas en tiempo real.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2622 (Módulo 030_relaciones_sql — #017)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** 1:N, N:M
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Una API interna debe soportar reglas de validación más estrictas.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2623 (Módulo 030_relaciones_sql — #018)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** N:M, integridad referencial
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Un equipo de soporte requiere reportes confiables para tomar decisiones.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2624 (Módulo 030_relaciones_sql — #019)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** integridad referencial, cascadas
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Una empresa de suscripciones necesita automatizar verificaciones críticas.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2625 (Módulo 030_relaciones_sql — #020)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** cascadas, 1:1
- **Prerequisitos:** 029_modelado_de_bases_de_datos, 028_sql_avanzado
- **Historia de usuario:** Una plataforma de e-commerce necesita mejorar su operación diaria.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2626 (Módulo 030_relaciones_sql — #021)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** 1:1, 1:N
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Un sistema de logística debe reducir errores de procesamiento.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2627 (Módulo 030_relaciones_sql — #022)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** 1:N, N:M
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Una fintech requiere mayor trazabilidad de transacciones.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2628 (Módulo 030_relaciones_sql — #023)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** N:M, integridad referencial
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Un SaaS B2B necesita estandarizar su lógica de negocio.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2629 (Módulo 030_relaciones_sql — #024)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** integridad referencial, cascadas
- **Prerequisitos:** 029_modelado_de_bases_de_datos, 028_sql_avanzado
- **Historia de usuario:** Un marketplace quiere detectar inconsistencias operativas en tiempo real.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2630 (Módulo 030_relaciones_sql — #025)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** cascadas, 1:1
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Una API interna debe soportar reglas de validación más estrictas.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2631 (Módulo 030_relaciones_sql — #026)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** 1:1, 1:N
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Un equipo de soporte requiere reportes confiables para tomar decisiones.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2632 (Módulo 030_relaciones_sql — #027)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** 1:N, N:M
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Una empresa de suscripciones necesita automatizar verificaciones críticas.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2633 (Módulo 030_relaciones_sql — #028)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** N:M, integridad referencial
- **Prerequisitos:** 029_modelado_de_bases_de_datos, 028_sql_avanzado
- **Historia de usuario:** Una plataforma de e-commerce necesita mejorar su operación diaria.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2634 (Módulo 030_relaciones_sql — #029)
- **Nivel de dificultad:** Nivel 5 — Avanzado
- **Conceptos involucrados:** integridad referencial, cascadas
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Un sistema de logística debe reducir errores de procesamiento.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2635 (Módulo 030_relaciones_sql — #030)
- **Nivel de dificultad:** Nivel 5 — Avanzado
- **Conceptos involucrados:** cascadas, 1:1
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Una fintech requiere mayor trazabilidad de transacciones.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2636 (Módulo 030_relaciones_sql — #031)
- **Nivel de dificultad:** Nivel 5 — Avanzado
- **Conceptos involucrados:** 1:1, 1:N
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Un SaaS B2B necesita estandarizar su lógica de negocio.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2637 (Módulo 030_relaciones_sql — #032)
- **Nivel de dificultad:** Nivel 5 — Avanzado
- **Conceptos involucrados:** 1:N, N:M
- **Prerequisitos:** 029_modelado_de_bases_de_datos, 028_sql_avanzado
- **Historia de usuario:** Un marketplace quiere detectar inconsistencias operativas en tiempo real.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2638 (Módulo 030_relaciones_sql — #033)
- **Nivel de dificultad:** Nivel 5 — Avanzado
- **Conceptos involucrados:** N:M, integridad referencial
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Una API interna debe soportar reglas de validación más estrictas.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2639 (Módulo 030_relaciones_sql — #034)
- **Nivel de dificultad:** Nivel 5 — Avanzado
- **Conceptos involucrados:** integridad referencial, cascadas
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Un equipo de soporte requiere reportes confiables para tomar decisiones.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2640 (Módulo 030_relaciones_sql — #035)
- **Nivel de dificultad:** Nivel 6 — Muy avanzado
- **Conceptos involucrados:** cascadas, 1:1
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Una empresa de suscripciones necesita automatizar verificaciones críticas.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2641 (Módulo 030_relaciones_sql — #036)
- **Nivel de dificultad:** Nivel 6 — Muy avanzado
- **Conceptos involucrados:** 1:1, 1:N
- **Prerequisitos:** 029_modelado_de_bases_de_datos, 028_sql_avanzado
- **Historia de usuario:** Una plataforma de e-commerce necesita mejorar su operación diaria.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2642 (Módulo 030_relaciones_sql — #037)
- **Nivel de dificultad:** Nivel 6 — Muy avanzado
- **Conceptos involucrados:** 1:N, N:M
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Un sistema de logística debe reducir errores de procesamiento.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2643 (Módulo 030_relaciones_sql — #038)
- **Nivel de dificultad:** Nivel 6 — Muy avanzado
- **Conceptos involucrados:** N:M, integridad referencial
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Una fintech requiere mayor trazabilidad de transacciones.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2644 (Módulo 030_relaciones_sql — #039)
- **Nivel de dificultad:** Nivel 6 — Muy avanzado
- **Conceptos involucrados:** integridad referencial, cascadas
- **Prerequisitos:** 029_modelado_de_bases_de_datos
- **Historia de usuario:** Un SaaS B2B necesita estandarizar su lógica de negocio.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2645 (Módulo 030_relaciones_sql — #040)
- **Nivel de dificultad:** Nivel 6 — Muy avanzado
- **Conceptos involucrados:** cascadas, 1:1
- **Prerequisitos:** 029_modelado_de_bases_de_datos, 028_sql_avanzado
- **Historia de usuario:** Un marketplace quiere detectar inconsistencias operativas en tiempo real.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.
