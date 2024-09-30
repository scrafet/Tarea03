# Tarea 03

Este proyecto es una aplicación REST desarrollada con Flask que desarrolla la Tarea 03 del curso API DEVELOPER de Cybertec por parte del alumno Waldo Anthony Berrocal Garcia 

## Características

- **Publicaciones de Blog**: Crear, editar, eliminar y listar publicaciones.
- **Comentarios**: Crear y listar comentarios en publicaciones de blog.
- **Usuarios**: Asociar publicaciones a usuarios específicos.

## Tecnologías Utilizadas

- **Python 3.10**
- **Flask 2.1.0**
- **SQLAlchemy 1.4.46**
- **SQLite**: Base de datos para almacenar usuarios, publicaciones y comentarios.

## Instalación

Sigue los siguientes pasos para clonar y ejecutar el proyecto en tu máquina local.

### Inicializar la Base de Datos

Dentro del entorno virtual, abre un terminal de Python para crear la base de datos:

```sh
python
```

  ## Luego ejecuta los siguientes comandos:
```
from app import db
db.create_all()
exit()
```

 ## Ejecutar la Aplicación

Para ejecutar la aplicación en modo de desarrollo:
```
python -m flask run
```
## Uso de la API

Los siguientes son los endpoints disponibles en la aplicación:

### POSTS
#### Obtener todos los posts.
```
http://127.0.0.1:5000/posts
```
#### Obtener todos los posts de un usuario.
```
http://127.0.0.1:5000/posts-by-user/<user-id>
```
#### Crear un nuevo post asociado a un usuario.
```
http://127.0.0.1:5000/posts-by-user/<user-id>
```
#### Editar un post existente.
```
http://127.0.0.1:5000/posts/<post-id>
```
#### Eliminar un post.
```
http://127.0.0.1:5000/posts/<post-id>
```
### Comentarios
#### Obtener todos los Comentarios.
```
http://127.0.0.1:5000/comments
```
#### Crear nuevo comentario.
```
http://127.0.0.1:5000/comments
```
### Ejemplos de Peticiones con Postman
#### Crear un Nuevo Post:
#### URL:
```
http://127.0.0.1:5000/posts-by-user/1
```
###### Metodo POST  :
```
{
  "title": "Mi primer post",
  "content": "Este es el contenido de mi primer post"
}
```
#### Editar un Post:
#### URL:
```
http://127.0.0.1:5000/posts-by-user/1
```
###### Metodo PATCH  :
```
{
  "title": "Mi post actualizado",
  "content": "Contenido actualizado del post"
}
```
#### Eliminar un Post:
#### URL:
```
http://127.0.0.1:5000/posts/1
```
### Licencia

Este proyecto está bajo la Licencia MIT.

### Autor
Creado por Waldo Anthony Berrocal Garcia 
