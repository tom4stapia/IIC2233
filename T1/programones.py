from abc import ABC, abstractmethod
from random import randint
from parametros import AUMENTAR_ATAQUE_FUEGO, AUMENTAR_VELOCIDAD_AGUA, AUMENTAR_VIDA_PLANTA,\
                       MAX_AUMENTO_ENTRENAMIENTO, MIN_AUMENTO_ENTRENAMIENTO, \
                       MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA


class Programon(ABC):
    def __init__(self, nombre, nivel: int, tipo, vida: int, ataque: int, \
                 defensa: int, velocidad: int):
        self.nombre = nombre
        self._nivel = nivel
        self.tipo = tipo
        self._vida = vida 
        self._experiencia = 0
        self._ataque = ataque
        self._defensa = defensa
        self._velocidad = velocidad
    
    @abstractmethod
    def entrenamiento(self):
        pass

    @abstractmethod
    def luchar(self):
        pass

    @abstractmethod
    def gano_ronda(self):
        pass
    
    @property
    def nivel(self):
        return self._nivel
    
    @nivel.setter
    def nivel(self, agregar):
        if agregar > 100:
            self._nivel = 100
        elif agregar < 1:
            self._nivel = 1
        else:
            self._nivel = agregar
        return self._nivel
    
    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, xp):
        if xp >= 100:
            subir_nivel = xp//100
            self.nivel += subir_nivel
            self._experiencia = xp % 100
            for _ in range(subir_nivel):
                sube = randint(MIN_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_ENTRENAMIENTO)
                self.vida += sube
                self.ataque += sube
                self.velocidad += sube
                self.defensa += sube
        else:
            self._experiencia = xp
        
        return self._experiencia
    
    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, agregar):
        if agregar > 255:
            self._vida = 255
        elif agregar < 1:
            self._vida = 1
        else:
            self._vida = agregar
    
        return self._vida
    
    @property
    def ataque(self):
        return self._ataque

    @ataque.setter
    def ataque(self, agregar):
        if agregar > 190:
            self._ataque = 190
        elif agregar < 5:
            self._ataque = 1
        else:
            self._ataque = agregar
    
        return self._ataque
    
    @property
    def defensa(self):
        return self._defensa

    @defensa.setter
    def defensa(self, agregar):
        if agregar > 250:
            self._defensa = 250
        elif agregar < 5:
            self._defensa = 5
        else:
            self._defensa = agregar
    
        return self._defensa
    
    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, agregar):
        if agregar > 200:
            self._velocidad = 200
        elif agregar < 5:
            self._velocidad = 5
        else:
            self._velocidad = agregar
    
        return self._velocidad
    
    
class TipoPlanta(Programon):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.debil = "fuego"
        self.fuerte = "agua"

    def entrenamiento(self):
        xp_antes = self.experiencia
        nivel_antes = self.nivel
        sube = randint(MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA)
        self.experiencia += sube
        nivel_despues = self.nivel
        xp_despues = self.experiencia
        if xp_despues > xp_antes and nivel_antes == nivel_despues:
            print(f"La experiencia de {self.nombre} ha subido en {sube}")
            print(f"Ha subido de {xp_antes} a {xp_despues}")
        else:
            print(f"{self.nombre} ha subido de nivel! De {nivel_antes} a {nivel_despues}")
            print(f"Su experiencia ha subido en {sube}, quedando en {xp_despues}")
        print()

    def luchar(self, ventaja):
        ingresar = self.vida * 0.2 + self.nivel * 0.3 + self.ataque * 0.15\
                   + self.defensa * 0.15 + self.velocidad * 0.2 + ventaja * 40
        return max(0, (ingresar))

    def gano_ronda(self):
        self.vida += AUMENTAR_VIDA_PLANTA

        
class TipoFuego(Programon):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.debil = "agua"
        self.fuerte = "planta"

    def entrenamiento(self):
        xp_antes = self.experiencia
        nivel_antes = self.nivel
        sube = randint(MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA)
        self.experiencia += sube
        nivel_despues = self.nivel
        xp_despues = self.experiencia
        if xp_despues > xp_antes and nivel_antes == nivel_despues:
            print(f"La experiencia de {self.nombre} ha subido en {sube}")
            print(f"Ha subido de {xp_antes} a {xp_despues}")
        else:
            print(f"{self.nombre} ha subido de nivel! De {nivel_antes} a {nivel_despues}")
            print(f"Su experiencia ha subido en {sube}, quedando en {xp_despues}")
        print()

    def luchar(self, ventaja):
        ingresar = self.vida * 0.2 + self.nivel * 0.3 + self.ataque * 0.15\
                   + self.defensa * 0.15 + self.velocidad * 0.2 + ventaja * 40
        return max(0, (ingresar))

    def gano_ronda(self):
        self.ataque += AUMENTAR_ATAQUE_FUEGO


class TipoAgua(Programon):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.debil = "planta"
        self.fuerte = "fuego"

    def entrenamiento(self):
        xp_antes = self.experiencia
        nivel_antes = self.nivel
        sube = randint(MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA)
        self.experiencia += sube
        nivel_despues = self.nivel
        xp_despues = self.experiencia
        if xp_despues > xp_antes and nivel_antes == nivel_despues:
            print(f"La experiencia de {self.nombre} ha subido en {sube}")
            print(f"Ha subido de {xp_antes} a {xp_despues}")
        else:
            print(f"{self.nombre} ha subido de nivel! De {nivel_antes} a {nivel_despues}")
            print(f"Su experiencia ha subido en {sube}, quedando en {xp_despues}")
        print()

    def luchar(self, ventaja):
        ingresar = self.vida * 0.2 + self.nivel * 0.3 + self.ataque * 0.15\
                   + self.defensa * 0.15 + self.velocidad * 0.2 + ventaja * 40
        return max(0, (ingresar))
    
    def gano_ronda(self):
        self.velocidad += AUMENTAR_VELOCIDAD_AGUA
