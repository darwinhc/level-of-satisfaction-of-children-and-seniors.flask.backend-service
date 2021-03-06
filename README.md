
# API para el uso de modelo de inteligencia artificial para predecir el nivel de satisfacción en la vida de niños y personas de la tercera edad

Se hace uso de dos modelos de inteligencia artifical (niños y adultos mayores) escogidos previamente bajo determinados criterios de aceptación para predecir todas las peticiones que lleguen a esta ruta.

## Uso
Use la API realizando peticiones POST a la siguiente ruta 

~~~
https://modelo-satisfaccion-vida.herokuapp.com/
~~~

### Niños

~~~
RUTA + /child
~~~

Se le deben enviar las siguientes características todas en número

* tiene_servicios_basicos
* calidad_sector
* calidad_vivienda
* años_cumplidos
* sexo_n
* padre_vive
* madre_vive
* estado_de_salud

En caso de que no se envie uno de estos datos, la API responderá con un error con codigo 400


### Adultos mayores
~~~
RUTA + /senior
~~~
Se le deben enviar las siguientes características todas en número

* tiene_servicios_basicos 
* calidad_sector
* calidad_vivienda 
* años_cumplidos 
* sexo_n
* padre_vive
* madre_vive
* estado_de_salud
* estado_civil_n
* campesino
* estado_de_salud
* actualmente_trabaja
* satisfaccion_tiempo_libre

En caso de que no se envie uno de estos datos, la API responderá con un error con codigo 400


## Acerca de la creación

Este componente backend de la aplicación está creado con el framework minimalista de flask. Para saber más a cerca de Flask

- [Documentación de Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Inicio rapido](https://flask.palletsprojects.com/en/2.1.x/quickstart/)

