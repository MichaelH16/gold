import pygame,sys
import random
from pygame.locals import *
""" variables globales"""
ancho = 500
alto = 560

class jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenCarro = pygame.image.load("imagenes/car.jpg")

        self.rect = self.imagenCarro.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto-30

        self.vida = True
        self.velocidad = 40

    def dibujar(self,superficie):
        superficie.blit(self.imagenCarro,self.rect)


def goldTraver():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Gold Traver")
    imagenFondo = pygame.image.load("imagenes/carretera1.png").convert_alpha()



    """ creacion del jugador"""
    player = jugador()

    enJuego = True


    while True:
        """ si el jugador da a la x de la venta se cierra la pantalla"""

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

            """ ejecucion del juego"""

        player.dibujar(ventana)
        ventana.blit(imagenFondo,(0,0))












        pygame.display.update()

goldTraver()
