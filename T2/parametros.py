import os

# Los intervalos están en milisegundos
INTERVALO_DISPARO = 2000
INTERVALO_SOLES_GIRASOL = 20000
INTERVALO_APARICION_SOLES = 10000
INTERVALO_TIEMPO_MORDIDA = 5000
INTERVALO_ACTUALIZAR_JUEGO = 50
INTERVALO_FIN_RONDA = 3000
# El daño y la vida tienen las mismas medidas
DANO_PROYECTIL = 5
DANO_MORDIDA = 5
VIDA_PLANTA = 100
VIDA_ZOMBIE = 80
# Número de zombies por carril
N_ZOMBIES = 7
# Porcentaje de ralentización
RALENTIZAR_ZOMBIE = 0.25
# Soles iniciales por ronda
SOLES_INICIALES = 250
# Número de soles generados por planta
CANTIDAD_SOLES = 2
# Valores plantas
VALOR_GIRASOL = 50
VALOR_PLANTA_CLASICA = 100
VALOR_PLANTA_AZUL = 150
VALOR_PAPA = 75
# Número de soles agregados a la cuenta por recolección
SOLES_POR_RECOLECCION = 50
# Número de soles agregados a la cuenta por Cheatcode
SOLES_EXTRA = 25
# Ponderadores de escenarios
PONDERADOR_NOCTURNO = 0.8
PONDERADOR_DIURNO = 0.9
# La velocidad del zombie en milisegundos
VELOCIDAD_ZOMBIE = 5000
ANIMACION_ZOMBIE = 250
# Velocidad en pixeles
VELOCIDAD_BALA = 8
VELOCIDAD_ZOMBIE_X = 10
# Puntaje por eliminar zombie
PUNTAJE_ZOMBIE_DIURNO = 50
PUNTAJE_ZOMBIE_NOCTURNO = 100
# Costo por avanzar de ronda
COSTO_AVANZAR = 500
# Costo tiendas
COSTO_LANZAGUISANTE = 50
COSTO_LANZAGUISANTE_HIELO = 100
COSTO_GIRASOL = 50
COSTO_PAPA = 75
# Caracteres de nombre usuario
MIN_CARACTERES = 3
MAX_CARACTERES = 15
# Limites juego
X_LIM_PIERDE = 340
X_LIM_INFERIOR = 352
X_LIM_SUPERIOR = 934
Y_LIM_INFERIOR = 6
Y_LIM_SUPERIOR = 450
Y_FILA_1 = 125
Y_FILA_2 = 218

# Ancho y largo imagenes
DESPLAZAMIENTO_PLANTA = 10
ANCHO_PLANTA = 40
LARGO_PLANTA = 80
ANCHO_ZOMBIE = 50
LARGO_ZOMBIE = 90
ANCHO_SOL = 30
LARGO_SOL = 30
ANCHO_BALA = 30
LARGO_BALA = 30
IMG_SOL = os.path.join("frontend", "sprites", "Elementos de juego", "sol.png")
# Imagenes fondo
IMG_JARDIN = os.path.join("frontend", "sprites", "Fondos", "jardinAbuela.png")
IMG_OSCURO = os.path.join("frontend", "sprites", "Fondos", "salidaNocturna.png")

# Imagenes girasol
IMG_GIRASOL_1 = os.path.join("frontend", "sprites", "Plantas", "girasol_1.png")
IMG_GIRASOL_2 = os.path.join("frontend", "sprites", "Plantas", "girasol_2.png")
# Imagenes planta clasica
IMG_PC_1 = os.path.join("frontend", "sprites", "Plantas", "lanzaguisantes_1.png")
IMG_PC_2 = os.path.join("frontend", "sprites", "Plantas", "lanzaguisantes_2.png")
IMG_PC_3 = os.path.join("frontend", "sprites", "Plantas", "lanzaguisantes_3.png")
IMG_BALA_C_1 = os.path.join("frontend", "sprites", "Elementos de juego", "guisante_1.png")
IMG_BALA_C_2 = os.path.join("frontend", "sprites", "Elementos de juego", "guisante_2.png")
IMG_BALA_C_3 = os.path.join("frontend", "sprites", "Elementos de juego", "guisante_3.png")

# Imagenes planta azul
IMG_PA_1 = os.path.join("frontend", "sprites", "Plantas", "lanzaguisantesHielo_1.png")
IMG_PA_2 = os.path.join("frontend", "sprites", "Plantas", "lanzaguisantesHielo_2.png")
IMG_PA_3 = os.path.join("frontend", "sprites", "Plantas", "lanzaguisantesHielo_3.png")
IMG_BALA_A_1 = os.path.join("frontend", "sprites", "Elementos de juego", "guisanteHielo_1.png")
IMG_BALA_A_2 = os.path.join("frontend", "sprites", "Elementos de juego", "guisanteHielo_2.png")
IMG_BALA_A_3 = os.path.join("frontend", "sprites", "Elementos de juego", "guisanteHielo_3.png")

# Imagenes papa
IMG_PAPA_1 = os.path.join("frontend", "sprites", "Plantas", "papa_1.png")
IMG_PAPA_2 = os.path.join("frontend", "sprites", "Plantas", "papa_2.png")
IMG_PAPA_3 = os.path.join("frontend", "sprites", "Plantas", "papa_3.png")
# Imagenes zombie runner
IMG_Z_R_W1 = os.path.join("frontend", "sprites", "Zombies", "Caminando",
                          "zombieHernanRunner_1.png")
IMG_Z_R_W2 = os.path.join("frontend", "sprites", "Zombies", "Caminando",
                          "zombieHernanRunner_2.png")
IMG_Z_R_C1 = os.path.join("frontend", "sprites", "Zombies", "Comiendo",
                          "zombieHernanComiendo_1.png")
IMG_Z_R_C2 = os.path.join("frontend", "sprites", "Zombies", "Comiendo",
                          "zombieHernanComiendo_2.png")
IMG_Z_R_C3 = os.path.join("frontend", "sprites", "Zombies", "Comiendo",
                          "zombieHernanComiendo_3.png")
# Imagenes zombie walker
IMG_Z_W_W1 = os.path.join("frontend", "sprites", "Zombies", "Caminando",
                          "zombieNicoWalker_1.png")
IMG_Z_W_W2 = os.path.join("frontend", "sprites", "Zombies", "Caminando",
                          "zombieNicoWalker_2.png")
IMG_Z_W_C1 = os.path.join("frontend", "sprites", "Zombies", "Comiendo",
                          "zombieNicoComiendo_1.png")
IMG_Z_W_C2 = os.path.join("frontend", "sprites", "Zombies", "Comiendo",
                          "zombieNicoComiendo_2.png")
IMG_Z_W_C3 = os.path.join("frontend", "sprites", "Zombies", "Comiendo",
                          "zombieNicoComiendo_3.png")

RUTA_PUNTAJES = os.path.join("puntajes.txt")
RUTA_VENTANA_INICIO = os.path.join("frontend", "ui_file", "ventana_inicio.ui")
RUTA_VENTANA_JUEGO = os.path.join("frontend", "ui_file", "ventana_juego.ui")
RUTA_VENTANA_POST_RONDA = os.path.join("frontend", "ui_file", "ventana_post_ronda.ui")
RUTA_VENTANA_PRINCIPAL = os.path.join("frontend", "ui_file", "ventana_principal.ui")
RUTA_VENTANA_RANKING = os.path.join("frontend", "ui_file", "ventana_ranking.ui")