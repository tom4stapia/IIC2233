from abc import abstractmethod, ABC
from random import randint
from parametros import AUMENTO_DEFENSA, GASTO_ENERGIA_BAYA, GASTO_ENERGIA_CARAMELO, \
                       GASTO_ENERGIA_POCION, PROB_EXITO_BAYA, PROB_EXITO_CARAMELO, \
                       PROB_EXITO_POCION
                       

class Objetos(ABC):
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    @abstractmethod
    def aplicar_objeto(self, programon):
        pass


class Baya(Objetos):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gasto = GASTO_ENERGIA_BAYA
        self.prob_exito = PROB_EXITO_BAYA
    
    def aplicar_objeto(self, programon):
        super().aplicar_objeto(programon)
        vida_pasada = programon.vida
        aumento = randint(1, 10)
        print(f"Aumento vida: {aumento}")
        programon.vida += aumento
        print(f"La vida subio de {vida_pasada} a {programon.vida}")


class Pocion(Objetos):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gasto = GASTO_ENERGIA_POCION
        self.prob_exito = PROB_EXITO_POCION
    
    def aplicar_objeto(self, programon):
        super().aplicar_objeto(programon)
        ataque_pasado = programon.ataque
        aumento = randint(1, 7)
        print(f"Aumento ataque: {aumento}")
        programon.ataque += aumento
        print(f"El ataque subio de {ataque_pasado} a {programon.ataque}")
    
    
class Caramelo(Baya, Pocion):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gasto = GASTO_ENERGIA_CARAMELO
        self.prob_exito = PROB_EXITO_CARAMELO
    
    def aplicar_objeto(self, programon):
        super().aplicar_objeto(programon)
        defensa_pasada = programon.defensa
        programon.defensa += AUMENTO_DEFENSA
        print(f"Aumento defesa: {AUMENTO_DEFENSA}")
        print(f"La defensa subio de {defensa_pasada} a {programon.defensa}")
