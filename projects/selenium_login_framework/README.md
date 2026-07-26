# Selenium Login Framework

## Descripción

Este proyecto implementa un framework básico de automatización de pruebas para una página de inicio de sesión utilizando **Python**, **Selenium WebDriver**, **Pytest** y el patrón **Page Object Model (POM)**.

El objetivo es demostrar una estructura escalable y mantenible para automatizar pruebas funcionales de aplicaciones web.

---

## Objetivo

Automatizar las validaciones principales de una página de Login aplicando buenas prácticas de automatización mediante Page Object Model.

---

## Tecnologías

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Git
- GitHub

---

## Estructura del proyecto

```
selenium_login_framework
│
├── config
│   ├── __init__.py
│   └── config.py
│
├── pages
│   ├── __init__.py
│   ├── base_page.py
│   └── login_page.py
│
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_base.py
│   └── test_login.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Casos de prueba automatizados

Actualmente el proyecto valida:

- Verificación del título de la página.
- Visibilidad del enlace **Sign Up**.
- Inicio de sesión utilizando Page Object Model.

---

## Patrón utilizado

Se implementó el patrón **Page Object Model (POM)** para separar la lógica de las páginas de los casos de prueba, facilitando el mantenimiento y la reutilización del código.

---

## Instalación

Clonar el repositorio

```bash
git clone git@github.com:Daironmp/qa-portfolio-DaironMP.git
```

Entrar al proyecto

```bash
cd selenium-login-framework
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecutar las pruebas

```bash
pytest -v
```

---

## Aprendizajes

Durante este proyecto reforcé conocimientos sobre:

- Automatización con Selenium.
- Uso de Pytest.
- Organización mediante Page Object Model.
- Configuración reutilizable mediante archivos de configuración.
- Buenas prácticas de automatización.

## Video demostración

En este video explico la estructura del proyecto, la implementación del patrón **Page Object Model (POM)** y la ejecución de las pruebas automatizadas.

**Ver video:** https://drive.google.com/file/d/12FPLQ2NAy8lmi8ZxNbQirmxDs4nqGzsZ/view?usp=sharing **Ver video:**  


## Autor

**Dairon Manzo**

QA Engineer Jr.

LinkedIn:
https://www.linkedin.com/in/daironmp/

GitHub:
https://github.com/Daironmp
