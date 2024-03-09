# Tarea 2: DCCruz vs Zombies :zombie::seedling::sunflower:

* Nombre: Tomás Tapia Pavez.
* Sección: 4.
* Usuario GitHub: tom4stapia.

## Consideraciones generales :octocat:

Antes de iniciar el codigo se deben agregar a la carpeta frontend la carpeta de sprites, y a la carpeta de backend el archivo aparicion_zombies.py.
Hay que tener cuidado con el archivo de puntajes.txt, este debe terminar con una linea sin texto, dado al mecanismo de agregación a este archivo.
Para facilitar la revisión, recomiendo aumentar el intervalo de aparición de zombies y aumentar la velocidad sobre el eje x.

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Ventanas: 39 pts (40%)
##### ✅ Ventana de Inicio
##### ✅ Ventana de Ranking	
##### ✅ Ventana principal
##### ✅ Ventana de juego	
##### ✅ Ventana post-ronda
#### Mecánicas de juego: 46 pts (47%)			
##### ✅ Plantas
##### ✅ Zombies
##### ✅ Escenarios		
##### ✅ Fin de ronda	
##### ✅ Fin de juego	
#### Interacción con el usuario: 22 pts (23%)
##### ✅ Clicks	
##### ✅ Animaciones
#### Cheatcodes: 8 pts (8%)
##### ✅ Pausa
##### ✅ S + U + N
##### ✅ K + I + L
#### Archivos: 4 pts (4%)
##### ✅ Sprites
##### ✅ Parametros.py
#### Bonus: 9 décimas máximo
##### ❌ Crazy Cruz Dinámico
##### ❌ Pala
##### ❌ Drag and Drop Tienda
##### ❌ Música juego

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```puntajes.txt``` en ```Tareas\T2\```
2. ```aparicion_zombies.py``` en ```Tareas\T2\backend\```
3. carpeta ```sprites``` en ```Tareas\T2\frontend\```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5```: ```pyqtSignal() / QtCore```, ```QTimer() / QtCore```, ```Qt() / QtCore```, ```QLabel() / QtWidgets```, ```QPixmap() / QtGui```, ```uic```, ```QObject() / QtCore```
2. ```os```: ```path.join()``` 
3. ```sys```: ```exit()```
4. ```random```: ```randint()```  

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```dccruzvszombies.py```: Contiene a todas las clases creadas, con las señales respectivas.


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Al salir en medio de la partida pierde, guardando su puntaje.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. De la actividad sumativa 3, realizada este año. En base a ese codigo realice esta tarea, desconocía bastante el como llevarla a cabo, por lo tanto seguí la estructura de esta, teniendo por ejemplo el archivo main.py literalmente a la as3, pero luego, en los demas archivos, la estructura puede ser similar, pero no es textualmente.



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/master/Tareas/Descuentos.md).
