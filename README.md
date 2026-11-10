# TPF-AlgoritmoCRUD-ALANROMERO
Aplicación web CRUD desarrollada para la gestión de bases de datos. El proyecto implementara el patrón de arquitectura **MVC (Modelo-Vista-Controlador)**.

**Alumno:** Alan Joel Romero 

**Materia / Curso:** Técnicas Avanzadas de Programación

## Consigna
- Realizar un CRUD en una base de datos

## CRITERIOS DE APROBACION
- CRUD simple con una tabla de Base de Datos.

## CRITERIOS DE PROMOCION
Cualquiera de estas opciones es válida
- Utilizar una API 
- Utilizar patrón MVC
- Utilizar minimamente 2 tablas relacionadas para hacer el CRUD
- Tema a elección
- El tema, el lenguaje y la base de datos son a elección 

## TECNOLOGIAS UTILIZADAS

* **Python**: Lenguaje de programacion principal utilizado para el desarrollo del backend.
* **Flask**: Microframework web utilizado para estructurar la API REST y aplicar el patrón **MVC** mediante el uso de Blueprints.
* **SQLite**: Sistema de gestion de bases de datos relacional embebido para el manejo de las tablas conectadas (`categorias` y `productos`).
* **Git / GitHub**: Herramientas de control de versiones y repositorio remoto para la entrega del trabajo final.

## COMO USAR
Sigue los siguientes pasos para poner en marcha el proyecto en tu entorno local:

### 1. Clonar el repositorio

Abre tu terminal y ejecuta el siguiente comando:
```bash
git clone [https://github.com/Alan2Romero/TPF-AlgoritmoCRUD-ALANROMERO.git](https://github.com/Alan2Romero/TPF-AlgoritmoCRUD-ALANROMERO.git)
cd TPF-AlgoritmoCRUD-ALANROMERO
```

### 2. Crear y activar un entorno virtual
* En Windows (Powershell/CMD):
```bash
python -m venv venv
venv\Scripts\activate
```
* En Mac / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicacion
Entra a la carpeta del código fuente (src) y arranca el servidor:
```bash
cd src
python app.py
```

### 5. Probar los Endpoints (CRUD)
Puedes utilizar herramientas como Postman, Insomnia o Thunder Client para interactuar con la API:
* Listar productos (GET):
GET http://127.0.0.1:5000/api/productos

* Crear un producto (POST):
POST http://127.0.0.1:5000/api/productos
(Enviar en el Body un JSON con: nombre, precio y categoria_id)

* Actualizar un producto (PUT):
PUT http://127.0.0.1:5000/api/productos/{id}
(Enviar en el Body un JSON con los nuevos datos)

* Eliminar un producto (DELETE):
DELETE http://127.0.0.1:5000/api/productos/{id}