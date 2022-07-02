Autor(es):

Johnny Miguel Sebastian Roque Neciosup U201924261

Miguel Antonio Benavides Roque U20191D998

Sergio Martin Guanillo Gonzales U20181H016


### Introducción

Muchas locaciones alrededor del mundo que actualmente están habitadas, presentan una distribución de caminos y calles que permiten la movilización, ya sea de personas, medios de transporte, etc. Algo resaltante es que gracias a la definición y agregado a una calle ,ya sea gracias a que esta posea un nombre, una longitud y unas coordenadas en el espacio, permite generar una orientación y delimitación de caminos.

Tomando en cuenta lo antes mencionado, nos hemos dado cuenta que estas secciones e intersecciones de un mapa, funcionan y se pueden comparar con un grafo, el cual posee aristas y vértices que cumplirían con la imagen de calles e intersecciones. En el presente trabajo elaboramos un grafo para representar una ciudad o una porción. Por medio de un proceso de selección de calles, gracias a la herramienta de google maps.


### Resumen Ejecutivo
Para este trabajo final, se nos pidió agregar pesos al grafo obtenido del trabajo parcial, esta información debia representar el tráfico y la distancia o longitud de la arista. Luego, se solicitó encontrar la ruta más corta mediante el algoritmo de dijkstra y las otras dos siguientes rutas más cortas, para lo cual se uso el algoritmo de Yen, recurso: https://www.lavivienpost.com/shortest-path-and-2nd-shortest-path-using-dijkstra-code/. Por último, debimos implementar una interfaz visual en la que se observe nuestro grafo, así como las 3 rutas mas cortas y los niveles de tráfico. 


### Definición del mapa

Se escogió la ciudad de Chicago debido a que posee calles largas y casi sin curvas, lo que nos facilitará el obtener las intersecciones.

Como punto inicial se seleccionó la intersección de las avenidas W Devon Ave y N Pulaski Rd.
![img](https://raw.githubusercontent.com/Miguel-TeamRuka/TF-20181H016-20191D998-201924261/main/imagenes/mapa.png)

### Descripción de las calles

Las calles, contenidas en los archivos horizontal.txt y vertical.txt, constan de su nombre obtenido con la herramienta google maps. su distancia horizontal (x) y vertical(y) con respecto al punto inicial, además de su longitud, todo esto en metros. Lo planteamos de esta manera porque no siempre las calles empiezan desde el límite del contorno, sino que pueden hacerlo un poco más a la derecha si es una calle horizontal, o más abajo si es una calle vertical.
|calle|x|y|longitud|
|-----|-|-|--------|
|W Bertau Ave|540|3680|8000|

### Descripción de las intersecciones

Las intersecciones constan de un número identificador, junto con los nombres de la calle horizontal y la calle vertical que la cruzan, así como su latitud y longitud.
|Nodo|Calle Horizontal|Calle Vertical|latitud|longitud|
|----|----------------|--------------|-------|--------|
|26|W Rosemont Ave|N Ridgeway Ave|41.995319|-87.722704|

### Explicación del procedimiento para obtener el grafo

Se leen los archivos Horizontal.txt y Vertical.txt para obtener las calles con sus elementos.

Se crea una matriz llena de -1, esto simula el sector de la ciudad que hemos escogido, cada fila y columna representa las calles horizontales y verticales respectivamente.

Para hallar las intersecciones usamos el siguiente planteamiento:

xHorizontal<= xVertical<=xHorizontal + longitudHorizontal

También una calle horizontal debe estar dentro de los límites de una calle vertical:

yVertical<=yHorizontal<=yVertical + longitudVertical

![img](https://raw.githubusercontent.com/Miguel-TeamRuka/TF-20181H016-20191D998-201924261/main/imagenes/interseccion-forma.png)

Ahora cada número diferente de “-1” es una intersección, porque no todas las calles se cruzan entre sí.

Entonces solo nos faltaría hallar la lista de adyacencia, la cual representa a cuáles otros nodos se une una intersección en específico. Para lograrlo debemos usar la matriz anterior, ya que se debe preguntar a un nodo quiénes son sus vecinos en las direcciones de arriba,abajo,derecha e izquierda.

Se debe recorrer la matriz, sin embargo, con algunos condicionales, como no preguntar al nodo final de una fila si tiene alguien a la derecha, o preguntar al nodo inicial de una columna si tiene un vecino arriba de él, y por supuesto solo añadir a la lista si es que una intersección o vecino de este es diferente de “-1”. Sin embargo, si pasa lo antes mencionado, se debe buscar el nodo mas cercano, es decir que no sea un -1.

### Explicación del procedimiento para obtener el peso de las aristas

Como se explicó anteriormente, las calles cuentan con una distancia en "x" e "y" al nodo origen (0,0), al realizar la función para detectar todas las intersecciones se obtiene las coordenadas de estos pero en metros, así que para pasarlo a coordendas geográficas usamos las siguientes ecuaciones: 

![img](https://raw.githubusercontent.com/Miguel-TeamRuka/TF-20181H016-20191D998-201924261/main/imagenes/latlon.PNG)

Con las coordendas de cada nodo, se puede hallar la distancia entre ellos con la formula del haversine:

![img](https://raw.githubusercontent.com/Miguel-TeamRuka/TF-20181H016-20191D998-201924261/main/imagenes/haversineFormula.png)

Para el factor de tráfico decidimos trabajar con la librería perlin_noise, la cual nos genera una matriz de valores uniformes que van del -1 (negro) al 1 (blanco), por lo tanto mientras más cercano al valor -1, habrá más tráfico, mientras que por el contrario, si está más cerca al 1, habrá menos tráfico.

Estos dos valores forman el peso de una aristas.

También se nos pidió una forma de actulizar según la hora, para lograrlo empleamos la hora de nuestra computadora, según eso, se le múltiplicará cierto valor a una arista.

### Explicación del procedimiento para obtener los 3 caminos más cortos

Para obtener los tres caminos más cortos, usamos el algoritmo de yen, el cual consiste en usar dijkstra para hallar el camino más corto, luego a ese camino se le suprime cada nodo de esa ruta para hallar cual es la siguiente de menor costo.

### Resultados:
Verde: mejor ruta
Azul:  segunda mejor ruta
Rojo: tercera mejor ruta

Prueba1:

![img](https://raw.githubusercontent.com/Miguel-TeamRuka/TF-20181H016-20191D998-201924261/main/imagenes/prueba1.PNG)

Prueba2:

![img](https://raw.githubusercontent.com/Miguel-TeamRuka/TF-20181H016-20191D998-201924261/main/imagenes/prueba2.PNG)

Prueba3:

![img](https://raw.githubusercontent.com/Miguel-TeamRuka/TF-20181H016-20191D998-201924261/main/imagenes/prueba3.PNG)

### Conclusiones

Para este trabajo se utilizarón conocimientos adquiridos durante el curso y también de otros anteriores, además de investigar por nuestra cuenta y sobretodo prácticar o jugar con los algoritmos.

