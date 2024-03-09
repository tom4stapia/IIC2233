# Tarea 1: DCCampeonato 🏃‍♂️🏆

* Nombre: Tomás Tapia Pavez.
* Sección: 4.
* Usuario GitHub: tom4stapia.

## Consideraciones generales :octocat:

**Los entrenadores** deben ser siempre pares, para que se logren crear duplas de manera correcta.

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Programación Orientada a Objetos (18pts) (22%%)
##### ✅ Diagrama
##### ✅ Definición de clases, atributos, métodos y properties		
##### ✅ Relaciones entre clases
#### Preparación programa: 11 pts (7%)			
##### ✅ Creación de partidas
#### Entidades: 28 pts (19%)
##### ✅ Programón
##### ✅ Entrenador		
##### ✅ Liga	
##### ✅ Objetos		
#### Interacción Usuario-Programa 57 pts (38%)
##### ✅ General	
##### ✅ Menú de Inicio
##### ✅ Menú Entrenador
##### ✅ Menu Entrenamiento
##### ✅ Simulación ronda campeonato
##### ✅ Ver estado del campeonato
##### ✅ Menú crear objeto
##### ✅ Menú utilizar objeto
##### ✅ Ver estado del entrenador
##### ✅ Robustez
#### Manejo de archivos: 12 pts (8%)
##### ✅ Archivos CSV
##### ✅ Parámetros
#### Bonus: 5 décimas
##### ❌ Mega Evolución
##### ❌ CSV dinámico

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se deben abrir los siguientes archivos para el buen funcionamiento de la tarea:
1. ```dccampeonato.py```: Contiene el campeonato en curso, junto al menu de entrenador.
2. ```liga_progra.py```: Se encarga de crear y guardar los objetos del campeonato, simula rondas y entrega el resumen del campeonato.
3. ```entrenador.py```: Contiene los programones y objetos de cada entrenador, se encarga de dar su conocer el estado, crear un objeto o entrenar alguno de sus programones.
4. ```programones.py```: Contiene a los programones según tipo, entrenan, se revisa si ganan rondas con su debida bonificación.
5. ```objetos.py```: Contiene a los objetos segun su tipo, se encarga de aplicar el debido objeto a un programon para que gane una bonificación.
6. ```parametros.py```: Contiene parametros usados en los distintos archivos.


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint()```, ```random()```
2. ```sys```: ```exit()``` 
3. ```beautifultable```: ```BeautifulTable``` (debe instalarse)
4. ```os```: ```path.join()``` 
5. ```abc```: ```ABC```, ```abstractmethod```
6. ```sys```: ```exit()``` 

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```dccampeonato```: Contiene la clase ```DCCampeonatoProgramon``` y las funciones: ```empezar()```, ```reiniciar()```, ```menu_inicio()```, ```menu_entrenador()```.
2. ```liga_progra```: Contiene la clase ```LigaProgramon``` y las funciones: ```resumen_campeonato()```, ```simular_ronda()```, ```llenar_liga()```.
3. ```entrenador```: Contiene la clase ```Entrenador``` y las funciones: ```estado_entrenador()```, ```crear_objeto()```, ```menu_entrenamiento()```, ```menu_objetos()```.
4. ```objetos```: Contiene las clases ```Objetos```, ```Baya```, ```Pocion```, ```Caramelo``` y la funcion: ```aplicar_objeto()```.
5. ```programones```: Contiene las clases ```Programon```, ```TipoPlanta```, ```TipoFuego```, ```TipoAgua``` y las funciones: ```entrenamiento()```, ```luchar()```, ```gano_ronda()```.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Como se trata de un campeonato, asumo que el total de participantes es un número par, es por eso que al formar duplas es sumamente necesario que el total de entrenadores sea par.
2. Cada vez que al elegir un entrenador y este vuelve al menu de inicio se reinician los datos.
3. Cada vez que el entrenador quiere crear un objeto, este puede tenerlo repetido. 
4. Al pedir resumen del campeonato la ronda que se muestra es la que viene. Es decir, al no haber simulado ninguna pelea y se pide ronda, deberia salir Ronda 1, ya que es donde participan los entrenadores que quedan.


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \< https://beautifultable.readthedocs.io/en/latest/quickstart.html >: este \<le da un diseño a las tablas que se van imprimiendo como menu en la consola> y está implementado en los archivos <dccampeonato.py> en las líneas <23 hasta 48, 65 hasta 86>, <liga_progra.py> en las líneas <37 hasta 44, 75 hasta 91>, <entrenador.py> en las líneas <35 hasta 61, 75 hasta 93, 154 hasta 171, 195 hasta 212, 225 hasta 243>. Siendo bastantes líneas no aportan a la funcionalidad del código, sino que sea mas agradable a la vista lo que se muestra en consola.



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/master/Tareas/Descuentos.md).
