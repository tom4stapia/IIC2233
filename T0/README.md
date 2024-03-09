# Tarea 0: Star Advanced :school_satchel:

* Nombre: Tomás Tapia Pavez.
* Sección: 4.
* Usuario GitHub: tom4stapia.

## Consideraciones generales :octocat:
**Antes de comenzar a correr el programa**, es necesario **crear una carpeta llamada partidas** (en minúscula), ya que si no se realiza, el programa no tendrá donde guardar las partidas en curso o terminadas.

Cuando al usuario se le pide **descubrir una columna**, no debe introducir una letra, debe **seguir el formato de las filas, es decir, poner un número que corresponda**. 

**Los usuarios** son distintos si no están estrictamente igual escritos, es decir, **Pedro es distinto de pedro**.

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Menú de Inicio: 
##### Partida nueva ✅
##### Cargar partida ✅
##### Ver Ranking ✅
##### Salir de la partida ✅
#### Menú de Juego:
##### Descubrir sector ✅
##### Guardar partida ✅
##### Salir, con o sin guardar ✅
#### Flujo de Juego: 
##### Funcionamiento de ambos menús ✅
##### Manejo de tableros ✅
##### Calculo de puntajes ✅
#### Archivos: 
##### Manejo de archivos ✅
#### General:
##### ✅ Menús
##### ✅ Parámetros
##### ✅ Módulos
##### ✅ PEP8
#### Bonus ❌

## Ejecución :computer:
* El módulo principal de la tarea a ejecutar es  ```menu_inicio.py```

* Adicionalmente se pueden abrir los siguientes archivos con el 
resto de la tarea:

    * ```parametros.py``` : Contiene todos los parámetros utilizados en la 
    Tarea. 
    * ```tablero.py``` : Contiene la formación del tablero. 
    * ```menu_juego.py``` : Contiene el funcionamiento para cuando el usuario 
      quiere jugar, da las opciones que contiene el menú de juego. 
    * ```funciones.py``` : Contiene las funciones utilizadas en ```menu_inicio.py```
      y ```menu_juego.py```, para que la lectura de ambos codigos sea más fácil de
      entender. 
    * ```puntajes.txt``` : Archivo que guarda los puntajes de los jugadores que han
      finalizado la partida.    
     

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fueron las siguientes:

1. ```random```: ```randit()```
2. ```os```: ```listdir()```, ```path.join()```, ```system()```
3. ```math``` : ```ceil()```
4. ```sys```: ```exit()```


### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```funciones```: contiene las funciones claves del juego, como ```gano()```, ```lista_a_archivo()```, ```completar_tablero()```, ```ranking()```, ```transformar_perder()```, ```obtener_fila()``` y ```obtener_columna()```.
2. ```menu_juego```: contiene a  ```jugar()```. 


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. El código inicia ofreciendo el menú de inicio, si se crea partida revisa que no exista el usuario introducido (revisando los archivos en la carpeta "partidas"),
   si se carga partida, busca el archivo que contenga los datos, si no existe archivo es porque el usuario no ha sido creado, en el caso de que exista, los datos estan
   separados por la palabra "FIN\n". Para ver ranking, revisa que ya hayan oartidas finalizadas. Cuando se crea o carga partida con exito se utiliza la función del        menu de juego  
   
2. El menú de juego es una función recursiva, la cual obtiene los datos para cuando se quiere seguir jugando, el caso que se guarde o no la partida se abre el menu de    inicio con os.system() 

3. El menú de inicio cuando se debe abrir nuevamente desde si mismo es con os.system(), que es cuando no exite usuario o ya se creo el usuario o se pidió ver ranking.
   Con sys.exit() se abandona el programa.
   

## Referencias de código externo :book:

No utilicé.


## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
