# JPA Demo

Este es un primer proyecto de ejemplo sencillo para estudiar JPA (Java Persistence API)
en la asignatura de Sistemas de Información para Internet, de 3º del Grado en Ingeniería Informática
y 4º del Doble Grado en Matemáticas e Ingeniería Informática de la Universidad de Málaga.

## Crear una base de datos H2 con la consola Web

La base de datos puede crearse de la siguiente forma:
1. Se arranca el servidor y la consola Web con `java -cp h2-*.jar org.h2.tools.Server`.
2. En el perfil de conexión se escoge `Generic H2 (embedded)`.
3. Com URL de conexión se indica `jdbc:h2:./db`.
4. Se rellena el usuario y contraseña (el que se quiera, pero debe ser el mimso que luego se use en posteriores conexiones).
5. Se conecta con la base de datos. Si no existe, creará una nueva.

## Ejecutar un servidor H2

Vamos a suponer que queremos servir la base de datos creada en el punto anterior de forma remota,
es decir, queremos habilitar una conexión remota a la base de datos. Para ello basta con ejecutar el comando:
```bash
java -cp h2-*.jar org.h2.tools.Server
```
## Conectar el proyecto con la base de datos creada de forma remota

El código del presente proyecto está preparado para conectarse a una base de datos H2 embedida en memoria.
Para poder conectar a un servidor H2 escuchando en el puerto 9092 (por defecto) en la máquina local
hay que modificar el fichero `persistence.xml` de la siguiente forma:
1. En la propiedad `jakarta.persistence.jdbc.url` hay que indicar `jdbc:h2:tcp://localhost/./db`. Antes de hacer esto, la base de datos debe existir y debe
   haber un servidor escuchando. Para hacer ambas cosas se pueden seguir los pasos indicados arriba.
3. En las propiedades `jakarta.persistence.jdbc.user` y `jakarta.persistence.jdbc.user` se debe indicar el usuario y contraseña de la base de datos.




