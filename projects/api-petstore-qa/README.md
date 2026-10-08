# API Petstore QA

Proyecto de QA Automation para realizar pruebas sobre la API de Swagger Petstore utilizando Python, Pytest y Requests.

## 1. Información general

- **Nombre del proyecto:** api-petstore-qa
- **Especialidad:** QA
- **Sistema bajo prueba:** Swagger Petstore API
- **Endpoint principal:** `POST /v2/pet`
- **Tecnologías:** Python, Pytest, Requests
- **Fuente original:** https://petstore.swagger.io/

## 2. Objetivo

El objetivo del proyecto es validar el comportamiento de la API de Swagger Petstore al crear mascotas mediante el endpoint `POST /v2/pet`, verificando respuestas exitosas y diferentes escenarios de datos inválidos.

El proyecto busca identificar problemas de validación que podrían permitir datos incorrectos o provocar errores inesperados en la API.

## 3. Plan de trabajo

1. **Exploración inicial**
   - Analizar la API Swagger Petstore y el endpoint `POST /v2/pet`.
   - Revisar la estructura de la petición y los campos disponibles.

2. **Preparación**
   - Diseñar escenarios positivos y negativos.
   - Crear datos de prueba para diferentes situaciones.

3. **Automatización**
   - Implementar las pruebas utilizando Python, Pytest y Requests.
   - Validar códigos de respuesta y contenido de las respuestas.

4. **Evaluación**
   - Ejecutar las pruebas automatizadas.
   - Identificar y documentar comportamientos inesperados de la API.

5. **Documentación**
   - Registrar los bugs encontrados.
   - Preparar el proyecto para su publicación en GitHub.

## 4. Preguntas clave

- ¿Qué podría ocurrir si la API acepta datos inválidos y estos llegan a producción?
- ¿La API valida correctamente los tipos y valores de los campos recibidos?
- ¿Qué otros escenarios negativos deberían probarse para aumentar la cobertura de las validaciones?

## 5. Qué se hizo y cómo

Se realizaron pruebas sobre el endpoint `POST /v2/pet` utilizando Python, Pytest y Requests.

Se diseñaron escenarios positivos y negativos para validar diferentes comportamientos de la API, incluyendo:

- Creación de una mascota con datos válidos.
- Creación con múltiples URLs de fotografías.
- Uso de valores no válidos en `status`.
- Ausencia del campo `name`.
- Envío de un body vacío.
- Envío de una lista vacía en `photoUrls`.
- Uso de un tipo de dato inválido en `id`.
- Envío de un `status` vacío.

Las pruebas automatizadas verifican códigos de respuesta y datos específicos del JSON recibido. Los comportamientos identificados como defectos fueron documentados en `BUGS.md` y marcados en Pytest mediante `xfail` para reflejar que actualmente fallan debido a comportamientos conocidos de la API.

## 6. Resultados

Se implementaron y ejecutaron **8 casos de prueba automatizados** para el endpoint `POST /v2/pet`.

Resultados de la ejecución:

- **3 pruebas PASS:** los escenarios cumplieron con el comportamiento esperado.
- **5 pruebas XFAIL:** se identificaron comportamientos conocidos de la API que fueron documentados como bugs.

### Bugs encontrados

- **BUG-001:** La API acepta un valor no válido en `status`.
- **BUG-002:** La API acepta una mascota sin el campo `name`.
- **BUG-003:** La API acepta un body vacío.
- **BUG-004:** La API devuelve HTTP 500 ante un tipo de dato inválido en `id`.
- **BUG-005:** La API acepta un `status` vacío.

Los bugs fueron documentados en `BUGS.md`, incluyendo pasos para reproducirlos, resultado esperado, resultado actual y evidencia de automatización.

## 7. Conclusiones

Este proyecto permitió fortalecer conocimientos de pruebas de API y automatización utilizando Python, Pytest y Requests.

Uno de los principales aprendizajes fue trabajar con escenarios positivos y negativos y comprender la importancia de validar tanto los códigos de respuesta como el contenido de las respuestas.

También aprendí a manejar casos de prueba que actualmente presentan un comportamiento conocido de la API utilizando `pytest.mark.xfail`, permitiendo identificar estos fallos sin detener innecesariamente la ejecución del resto de las pruebas. Esto facilitó continuar evaluando los demás escenarios y mantener los defectos documentados.

Con más tiempo, ampliaría la cobertura incluyendo otros endpoints de la API, más escenarios negativos y una estructura de pruebas más completa.

En una entrevista destacaría la experiencia de transformar escenarios de prueba en pruebas automatizadas, analizar los resultados y documentar los bugs encontrados.