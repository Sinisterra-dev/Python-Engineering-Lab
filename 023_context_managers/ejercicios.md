# Ejercicios — Context managers

Total del módulo: **35 ejercicios**.

Cada ejercicio incluye: número, nivel, conceptos, prerequisitos, historia de usuario, objetivo, restricciones, entrada, salida y pista opcional.

## Ejercicio #2231 (Módulo 023_context_managers — #001)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** gestión de recursos, atomicidad
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Un equipo de soporte requiere reportes confiables para tomar decisiones.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2232 (Módulo 023_context_managers — #002)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** atomicidad, rollback
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Una empresa de suscripciones necesita automatizar verificaciones críticas.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2233 (Módulo 023_context_managers — #003)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** rollback, transacciones
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Una plataforma de e-commerce necesita mejorar su operación diaria.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2234 (Módulo 023_context_managers — #004)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** transacciones, limpieza
- **Prerequisitos:** 022_decoradores, 021_generadores_y_iteradores
- **Historia de usuario:** Un sistema de logística debe reducir errores de procesamiento.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2235 (Módulo 023_context_managers — #005)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** limpieza, gestión de recursos
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Una fintech requiere mayor trazabilidad de transacciones.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2236 (Módulo 023_context_managers — #006)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** gestión de recursos, atomicidad
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Un SaaS B2B necesita estandarizar su lógica de negocio.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2237 (Módulo 023_context_managers — #007)
- **Nivel de dificultad:** Nivel 1 — Fácil
- **Conceptos involucrados:** atomicidad, rollback
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Un marketplace quiere detectar inconsistencias operativas en tiempo real.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2238 (Módulo 023_context_managers — #008)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** rollback, transacciones
- **Prerequisitos:** 022_decoradores, 021_generadores_y_iteradores
- **Historia de usuario:** Una API interna debe soportar reglas de validación más estrictas.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2239 (Módulo 023_context_managers — #009)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** transacciones, limpieza
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Un equipo de soporte requiere reportes confiables para tomar decisiones.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2240 (Módulo 023_context_managers — #010)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** limpieza, gestión de recursos
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Una empresa de suscripciones necesita automatizar verificaciones críticas.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2241 (Módulo 023_context_managers — #011)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** gestión de recursos, atomicidad
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Una plataforma de e-commerce necesita mejorar su operación diaria.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2242 (Módulo 023_context_managers — #012)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** atomicidad, rollback
- **Prerequisitos:** 022_decoradores, 021_generadores_y_iteradores
- **Historia de usuario:** Un sistema de logística debe reducir errores de procesamiento.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2243 (Módulo 023_context_managers — #013)
- **Nivel de dificultad:** Nivel 2 — Fácil-intermedio
- **Conceptos involucrados:** rollback, transacciones
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Una fintech requiere mayor trazabilidad de transacciones.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2244 (Módulo 023_context_managers — #014)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** transacciones, limpieza
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Un SaaS B2B necesita estandarizar su lógica de negocio.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2245 (Módulo 023_context_managers — #015)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** limpieza, gestión de recursos
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Un marketplace quiere detectar inconsistencias operativas en tiempo real.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2246 (Módulo 023_context_managers — #016)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** gestión de recursos, atomicidad
- **Prerequisitos:** 022_decoradores, 021_generadores_y_iteradores
- **Historia de usuario:** Una API interna debe soportar reglas de validación más estrictas.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2247 (Módulo 023_context_managers — #017)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** atomicidad, rollback
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Un equipo de soporte requiere reportes confiables para tomar decisiones.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2248 (Módulo 023_context_managers — #018)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** rollback, transacciones
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Una empresa de suscripciones necesita automatizar verificaciones críticas.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2249 (Módulo 023_context_managers — #019)
- **Nivel de dificultad:** Nivel 3 — Intermedio
- **Conceptos involucrados:** transacciones, limpieza
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Una plataforma de e-commerce necesita mejorar su operación diaria.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2250 (Módulo 023_context_managers — #020)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** limpieza, gestión de recursos
- **Prerequisitos:** 022_decoradores, 021_generadores_y_iteradores
- **Historia de usuario:** Un sistema de logística debe reducir errores de procesamiento.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2251 (Módulo 023_context_managers — #021)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** gestión de recursos, atomicidad
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Una fintech requiere mayor trazabilidad de transacciones.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2252 (Módulo 023_context_managers — #022)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** atomicidad, rollback
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Un SaaS B2B necesita estandarizar su lógica de negocio.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2253 (Módulo 023_context_managers — #023)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** rollback, transacciones
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Un marketplace quiere detectar inconsistencias operativas en tiempo real.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2254 (Módulo 023_context_managers — #024)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** transacciones, limpieza
- **Prerequisitos:** 022_decoradores, 021_generadores_y_iteradores
- **Historia de usuario:** Una API interna debe soportar reglas de validación más estrictas.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2255 (Módulo 023_context_managers — #025)
- **Nivel de dificultad:** Nivel 4 — Intermedio-avanzado
- **Conceptos involucrados:** limpieza, gestión de recursos
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Un equipo de soporte requiere reportes confiables para tomar decisiones.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2256 (Módulo 023_context_managers — #026)
- **Nivel de dificultad:** Nivel 5 — Avanzado
- **Conceptos involucrados:** gestión de recursos, atomicidad
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Una empresa de suscripciones necesita automatizar verificaciones críticas.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2257 (Módulo 023_context_managers — #027)
- **Nivel de dificultad:** Nivel 5 — Avanzado
- **Conceptos involucrados:** atomicidad, rollback
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Una plataforma de e-commerce necesita mejorar su operación diaria.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2258 (Módulo 023_context_managers — #028)
- **Nivel de dificultad:** Nivel 5 — Avanzado
- **Conceptos involucrados:** rollback, transacciones
- **Prerequisitos:** 022_decoradores, 021_generadores_y_iteradores
- **Historia de usuario:** Un sistema de logística debe reducir errores de procesamiento.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2259 (Módulo 023_context_managers — #029)
- **Nivel de dificultad:** Nivel 5 — Avanzado
- **Conceptos involucrados:** transacciones, limpieza
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Una fintech requiere mayor trazabilidad de transacciones.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2260 (Módulo 023_context_managers — #030)
- **Nivel de dificultad:** Nivel 5 — Avanzado
- **Conceptos involucrados:** limpieza, gestión de recursos
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Un SaaS B2B necesita estandarizar su lógica de negocio.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.

## Ejercicio #2261 (Módulo 023_context_managers — #031)
- **Nivel de dificultad:** Nivel 6 — Muy avanzado
- **Conceptos involucrados:** gestión de recursos, atomicidad
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Un marketplace quiere detectar inconsistencias operativas en tiempo real.
- **Objetivo:** Diseñar la especificación del comportamiento esperado sin implementar la solución.
- **Restricciones:** No se permite hardcodear resultados.
- **Ejemplo de entrada:** colección de registros de negocio + parámetros de configuración
- **Ejemplo de salida:** resultado estructurado listo para auditoría
- **Pista opcional:** Empieza separando validación, transformación y salida.

## Ejercicio #2262 (Módulo 023_context_managers — #032)
- **Nivel de dificultad:** Nivel 6 — Muy avanzado
- **Conceptos involucrados:** atomicidad, rollback
- **Prerequisitos:** 022_decoradores, 021_generadores_y_iteradores
- **Historia de usuario:** Una API interna debe soportar reglas de validación más estrictas.
- **Objetivo:** Modelar entradas, salidas y reglas para que el problema sea verificable.
- **Restricciones:** Debe manejar datos faltantes sin romper el flujo.
- **Ejemplo de entrada:** payload JSON con entidades relacionadas y filtros opcionales
- **Ejemplo de salida:** resumen agregado con métricas clave y alertas
- **Pista opcional:** Piensa qué estructura de datos reduce complejidad accidental.

## Ejercicio #2263 (Módulo 023_context_managers — #033)
- **Nivel de dificultad:** Nivel 6 — Muy avanzado
- **Conceptos involucrados:** rollback, transacciones
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Un equipo de soporte requiere reportes confiables para tomar decisiones.
- **Objetivo:** Definir una estrategia de resolución dividida en pasos coherentes.
- **Restricciones:** Debe mantenerse legible y modular para revisión por pares.
- **Ejemplo de entrada:** lista de eventos temporales ordenados por timestamp
- **Ejemplo de salida:** colección filtrada y priorizada para acción operativa
- **Pista opcional:** Define primero los invariantes que nunca deben romperse.

## Ejercicio #2264 (Módulo 023_context_managers — #034)
- **Nivel de dificultad:** Nivel 6 — Muy avanzado
- **Conceptos involucrados:** transacciones, limpieza
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Una empresa de suscripciones necesita automatizar verificaciones críticas.
- **Objetivo:** Identificar y documentar casos borde antes de programar.
- **Restricciones:** Debe contemplar al menos 3 casos borde explícitos.
- **Ejemplo de entrada:** tablas relacionales con datos históricos y operativos
- **Ejemplo de salida:** informe de validaciones con errores clasificados
- **Pista opcional:** Diseña ejemplos mínimos y ejemplos extremos antes de avanzar.

## Ejercicio #2265 (Módulo 023_context_managers — #035)
- **Nivel de dificultad:** Nivel 6 — Muy avanzado
- **Conceptos involucrados:** limpieza, gestión de recursos
- **Prerequisitos:** 022_decoradores
- **Historia de usuario:** Una plataforma de e-commerce necesita mejorar su operación diaria.
- **Objetivo:** Proponer criterios de aceptación medibles y trazables.
- **Restricciones:** Se debe justificar la estructura de datos elegida.
- **Ejemplo de entrada:** lote mixto de datos válidos e inválidos para depuración
- **Ejemplo de salida:** respuesta consistente para consumo por API
- **Pista opcional:** Busca duplicidad de lógica y plantea cómo reutilizarla.
