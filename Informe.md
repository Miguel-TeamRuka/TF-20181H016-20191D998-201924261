Autor(es):

Johnny Miguel Sebastian Roque Neciosup U201924261

Miguel Antonio Benavides Roque U20191D998

Sergio Martin Guanillo Gonzales U20181H016


###Introducción

Muchas locaciones alrededor del mundo que actualmente están habitadas, presentan una distribución de caminos y calles que permiten la movilización, ya sea de personas, medios de transporte, etc. Algo resaltante es que gracias a la definición y agregado a una calle ,ya sea gracias a que esta posea un nombre, una longitud y unas coordenadas en el espacio, permite generar una orientación y delimitación de caminos.

Tomando en cuenta lo antes mencionado, nos hemos dado cuenta que estas secciones e intersecciones de un mapa, funcionan y se pueden comparar con un grafo, el cual posee aristas y vértices que cumplirían con la imagen de calles e intersecciones. En el presente trabajo elaboramos un grafo para representar una ciudad o una porción. Por medio de un proceso de selección de calles, gracias a la herramienta de google maps.


###Resumen Ejecutivo

Para esta entrega se nos solicitó realizar un grafo de las intersecciones de las calles de una ciudad o sector de una ciudad. Para ello hemos utilizado las herramientas de google map para obtener la información necesaria de las calles y Google Collaboratory para realizar el código.

Se dividió el trabajo en tres partes, recoger la información de las calles horizontales, recoger la información de las calles verticales, e identificar una solución para hallar las intersecciones, solo con la información de las calles, de manera automática.

Una vez se obtuvo la información de una lista de adyacencia, se procedió a plasmarla en un archivo de texto.

Link del código: https://colab.research.google.com/drive/1t\_JWcVNHzrBLhOsYXkdF-z08gQmN3-9S?usp=sharing


### Definición del mapa

Se escogió la ciudad de Chicago debido a que posee calles largas y casi sin curvas, lo que nos facilitará el obtener las intersecciones.

Como punto inicial se seleccionó la intersección de las avenidas W Devon Ave y N Pulaski Rd.


### Descripción de las calles

Las calles, contenidas en los archivos horizontal.txt y vertical.txt, constan de su nombre obtenido con la herramienta google maps. su distancia horizontal (x) y vertical(y) con respecto al punto inicial, además de su longitud, todo esto en metros. Lo planteamos de esta manera porque no siempre las calles empiezan desde el límite del contorno, sino que pueden hacerlo un poco más a la derecha si es una calle horizontal, o más abajo si es una calle vertical.

### Descripción de las intersecciones

Las intersecciones constan de un número identificador, junto con los nombres de la calle horizontal y la calle vertical que la cruzan.

### Explicación del procedimiento para obtener el grafo

Se leen los archivos Horizontal.txt y Vertical.txt para obtener las calles con sus elementos.

Se crea una matriz llena de -1, esto simula el sector de la ciudad que hemos escogido, cada fila y columna representa las calles horizontales y verticales respectivamente.

Para hallar las intersecciones usamos el siguiente planteamiento:

xHorizontal<= xVertical<=xHorizontal + longitudHorizontal

También una calle horizontal debe estar dentro de los límites de una calle vertical:

yVertical<=yHorizontal<=yVertical + longitudVertical

Ahora cada número diferente de “-1” es una intersección, porque no todas las calles se cruzan entre sí.

Entonces solo nos faltaría hallar la lista de adyacencia, la cual representa a cuáles otros nodos se une una intersección en específico. Para lograrlo debemos usar la matriz anterior, ya que se debe preguntar a un nodo quiénes son sus vecinos en las direcciones de arriba,abajo,derecha e izquierda.

Se debe recorrer la matriz, sin embargo, con algunos condicionales, como no preguntar al nodo final de una fila si tiene alguien a la derecha, o preguntar al nodo inicial de una columna si tiene un vecino arriba de él, y por supuesto solo añadir a la lista si es que una intersección o vecino de este es diferente de “-1”.
