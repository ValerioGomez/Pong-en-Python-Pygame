from pickle import TRUE
import pygame

pygame.init()

# Definimos las variables
ANCHO=700
tamannio_pantalla = (ANCHO, 500)       # Ancho y alto
bg  = (0,0,0)
blanco = (255,255,255)
pad = 20
w_pal = 10
h_pal = 90
c_x = int(tamannio_pantalla[0]/2)
c_y = int(tamannio_pantalla[1]/2)

puntuacion = [0, 0]

def texto(texto, tam=20, color=(0, 0, 0)):
    #Pasamos como parametros el tipo de letra y tamaño
    fuente = pygame.font.SysFont("comicsanz", tam)
    #retornamos la Funcion con los mismos parametros
    return fuente.render(texto, True, color)
#Creamos la Clase Barra

# Inicializar las variables
Fin = False
pelota_x = c_x
pelota_y = c_y
velocidad_pelota_x = 2
velocidad_pelota_y = 2
radio = 10

y_p1 = c_y - h_pal/2
y_p2 = c_y - h_pal/2

velocidad_p1 = 0
velocidad_p2 = 0

contador = 0

pantalla = pygame.display.set_mode(tamannio_pantalla)
reloj = pygame.time.Clock()

while not Fin:
    # Est parte es para capturar los eventos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Fin = True

        # Eventos del Teclado
        if event.type == pygame.KEYDOWN:
            # Jugador 1
            if event.key == pygame.K_w:
                velocidad_p1 = -3
            if event.key == pygame.K_s:
                velocidad_p1 = 3
            # Jugador 2
            if event.key == pygame.K_o:
                velocidad_p2 = -3
            if event.key == pygame.K_l:
                velocidad_p2 = 3

        if event.type == pygame.KEYUP:
            # Jugador 1
            if event.key == pygame.K_w:
                velocidad_p1 = 0
            if event.key == pygame.K_s:
                velocidad_p1 = 0

            # Jugador 2
            if event.key == pygame.K_o:
                velocidad_p2 = 0
            if event.key == pygame.K_l:
                velocidad_p2 = 0

    # Aqui todo el codigo

    # Restricciones para la pelota
    # Eje X
    if pelota_x > (tamannio_pantalla[0]-radio) or pelota_x < radio:
        pelota_x = c_x
        pelota_y = c_y
        velocidad_pelota_x *= -1
        velocidad_pelota_y *= -1

    # Eje Y
    if pelota_y > (tamannio_pantalla[1]-radio) or pelota_y < radio:
        velocidad_pelota_y *= -1

    # Movimiento de la pelota
    pelota_x += velocidad_pelota_x
    pelota_y += velocidad_pelota_y

    # Movimiento de los jugadores (Paletas)
    y_p1 = y_p1 + velocidad_p1
    y_p2 = y_p2 + velocidad_p2

    # Renderizar la pantalla y los objetos
    pantalla.fill(bg)
    pel = pygame.draw.circle(pantalla, blanco, (pelota_x, pelota_y), radio)
    p1 = pygame.draw.rect(pantalla, blanco,(pad, y_p1, w_pal, h_pal))
    p2 = pygame.draw.rect(pantalla, blanco,(tamannio_pantalla[0] - (pad + w_pal), y_p2, w_pal, h_pal))

    # Detectando las colisiones
    if pel.colliderect(p1) or pel.colliderect(p2):
        if pel.colliderect(p1):
            puntuacion[1] += 1

        else:
            puntuacion[0] += 1
        velocidad_pelota_x *= -1
    pantalla.blit(texto("Jugador A = "+str(puntuacion[0]), 40, (255,0,0)), (ANCHO / 8+20, 10))
    pantalla.blit(texto("Jugador B = "+str(puntuacion[1]), 40, (0,0,255)), ((ANCHO * 3 / 4) - 100, 10))
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
