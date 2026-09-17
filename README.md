# 🗳️ Sistema de Votación

## Descripción

Este proyecto consiste en un sistema de votación desarrollado en Python. Permite registrar votos, evitar que una misma persona vote más de una vez, consultar los resultados y reiniciar la votación.

El proyecto fue desarrollado en equipo utilizando Git y GitHub para trabajar con ramas e integrar las diferentes funcionalidades.

## Funcionalidades

### 1. Registrar votos

Permite registrar el voto de una persona utilizando su documento de identidad y valida que una misma persona no pueda votar dos veces.

**Responsable:** Evelin Pérez

### 2. Ver resultados

Muestra el total de votos registrados, la cantidad de votos de cada opción y el porcentaje correspondiente.

**Responsable:** Evelin Pérez

### 3. Reiniciar votación y guardar historial

Permite reiniciar la votación y guardar el historial de los resultados anteriores en un archivo de texto.

**Responsable:** Ximena Acevedo

## Mejora adicional

Como mejora realizada en equipo, se agregó la función para mostrar automáticamente quién obtuvo la mayor cantidad de votos al consultar los resultados.

🏆 El sistema muestra el ganador de la votación al finalizar la consulta de resultados.

## Tecnologías utilizadas

* Python
* Git
* GitHub

## Integrantes

| Integrante     | Funcionalidades                                      |
| -------------- | ---------------------------------------------------- |
| Ximena Acevedo | Reiniciar votación y guardar historial               |
| Evelin Pérez   | Registrar votos y mostrar resultados con porcentajes |

## Archivos principales

* `votacionRama1.py` → Contiene el sistema principal de votación, registro y resultados.
* `reiniciar.py` → Contiene la función para reiniciar la votación y guardar el historial.
* `historial.txt` → Guarda el historial de la votación.
