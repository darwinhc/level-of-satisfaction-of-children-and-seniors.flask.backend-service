
# API para el uso de modelo de inteligencia artificial para predecir el nivel de satisfacción en la vida de niños y personas de la tercera edad

Se hace uso de dos modelos de inteligencia artifical (niños y adultos mayores) escogidos previamente bajo determinados criterios de aceptación para predecir todas las peticiones que lleguen a esta ruta.

## Uso
Use la API realizando peticiones POST a la siguiente ruta 

~~~
RUTA
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