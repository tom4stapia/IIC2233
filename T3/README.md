# Tarea 3: DCCard-Jitsu 🐧🥋


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

La tarea no la alcance a terminar :(, gran parte es gracias a la AF3.

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Networking: 26 pts (19%)
##### 🟠 Protocolo	
##### ✅ Correcto uso de sockets		
##### ✅ Conexión	
##### 🟠 Manejo de Clientes	
##### ✅ Desconexión Repentina
#### Arquitectura Cliente - Servidor: 31 pts (23%)			
##### ✅ Roles			
##### 🟠 Consistencia		
##### 🟠 Logs
#### Manejo de Bytes: 27 pts (20%)
##### 🟠 Codificación			
##### 🟠 Decodificación			
##### ✅ Encriptación		
##### ✅Desencriptación	
##### 🟠 Integración
#### Interfaz Gráfica: 27 pts (20%)	
##### ✅ Ventana inicio		
##### ✅ Sala de Espera			
##### ✅ Ventana de juego							
##### ✅ Ventana final
#### Reglas de DCCard-Jitsu: 17 pts (13%)
##### ❌ Inicio del juego			
##### ❌ Ronda				
##### ❌ Termino del juego
#### Archivos: 8 pts (6%)
##### ✅ Parámetros (JSON)		
##### ✅ Cartas.py	
##### ✅ Cripto.py
#### Bonus: 8 décimas máximo
##### ❌ Cheatcodes	
##### ❌ Bienestar	
##### ❌ Chat

## Ejecución :computer:
El módulo principal de la tarea a ejecutar son  ```main.py``` en las carpetas ```servidor``` y ```cliente``` respectivamente. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```sprites``` en ```cliente/frontend``` entregada en un comienzo (gitignore)



## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```Pyqt5```: Para realizar ventanas

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Descripción/consideración 1 y justificación del por qué es válido/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


-------



**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. Mi codigo es basado en la AF3 de este año y la solución de la ayudantía 8 del 2022-1, de hecho es literalmente el mismo con pequeños cambios, por lo que puedo tener funciones o señales con no utilicé porque no me dio el tiempo para terminar la tarea y hacerlo de una forma mas correcta.

## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/master/Tareas/Descuentos.md).
