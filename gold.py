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
        self.velocidad = 100

    def dibujar(self,superficie):
        superficie.blit(self.imagenCarro,self.rect)
    """ mover a la derecha """
    def movimientoDerecha(self):
        """ que se pueda mover a la derecha en el eje x """

        self.rect.right += self.velocidad
        self.movimiento()


    def movimientoIzquierda(self):
        """ que se pueda mover a la izquierda """
        self.rect.left -= self.velocidad
        self.movimiento()


    def movimiento(self):
        if self.vida == True:
            """ crear hasta donde se puede mover"""
            if    self.rect.left <= 100 :
                self.rect.left = 100
            if self.rect.right >= 400:
                self.rect.right = 400

class Enemigos(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite._init__(self)
        self.imagenA = pygame.imagen.load("imanagenes/")


def goldTraver():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Gold Traver")
    imagenFondo = pygame.image.load("imagenes/carretera1.png").convert_alpha()
    """ me permite configurar la imagen el anho y el alto de la imagen"""
    imagenFondo = pygame.transform.scale(imagenFondo, (500, 560))



    """ creacion del jugador"""
    player = jugador()

    enJuego = True


    while True:
        """ si el jugador da a la x de la venta se cierra la pantalla"""

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            """ crear eventos cuando se oprime una telca"""

            if enJuego == True:# se usa para saber si el jugador no ha perdido

                if evento.type == pygame.KEYDOWN:
                    if evento.key == K_LEFT:
                        player.movimientoIzquierda()
                    if evento.key == K_RIGHT:
                        player.movimientoDerecha()









        ventana.blit(imagenFondo,(0,0))
        """ pinta el jugador en la ventana y la dibuja """
        player.dibujar(ventana)












        pygame.display.update()

goldTraver()
