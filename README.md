# PortafolioAlejandro

Proyecto hoja de vida en linea o portafolia para un dev junior

## Tecnologías

- **Frontend:** HTML, css
- **Backend:** Django (6.0.4), Python 3.14.4
- **Estado:** Español

### Requisitos Previos

- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/download/win)
- Un editor de código como [VS Code](https://code.visualstudio.com/)

## Instalación

Sigue estos pasos para configurar el proyecto en tu máquina local:


### 1. Clonar el repositorio
``` bash
git clone https://github.com/ratortor/projecto12.git
cd projecto12
```

### 2. Crear entorno virtual 

Windows:

```bash

python -m venv venv
venv\Scripts\activate

Mac/Linux:

python3 -m venv venv
source venv/bin/activate
Sabrás que está activado cuando veas (venv) al inicio de tu terminal.
```

### 3. Instalar dependencias

```bash

pip install -r requirements.txt

cd functions && bun install && cd ..
```
### 4. Crear la base de datos
```bash


python manage.py migrate
```
### 5. Ejecutar el servidor
```bash

python manage.py runserver
Abre tu navegador y ve a: http://127.0.0.1:8000/
```


## Estructura del proyecto

projecto12/
├── mi_hoja_de_vida/ # App de hoja de vida
├── portfolio/ # App de portafolio
├── static/ # Archivos estáticos (CSS, JS, imágenes)
├── templates/ # Plantillas HTML
├── .gitignore # Archivos excluidos de Git
├── manage.py # Archivo principal de Django
├── requirements.txt # Dependencias del proyecto
└── README.md # Este archivo


### Módulos


### Dónde colocar cada archivo


## Flujo de trabajo con Git


### 1. Crear una rama para tu tarea




### 2. Trabajar y hacer commits



### 3. Crear un Pull Request en GitHub



### 4. Revisión y merge



### 5. Después del merge

```

## Despliegue

