import pygame,sys
import random
from pygame.locals import *
""" variables globales"""
ancho = 900
alto = 500

class jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenCarro = pygame.image.load("imagenes/sprites_gold.png")
        self.imagenCarro.set_clip(pygame.Rect(126,26,190,140))
        self.image = self.imagenCarro.subsurface(self.imagenCarro.get_clip())



        self.rect = self.image.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto-65

        self.vida = True
        self.velocidad = 50

        self.frame = 0
        """ animacion """
        self.right_states = {0: (41,26,98,134),1:(126,26,190,140),2:(213,26,280,138)}


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
            if self.rect.left <= 10 :
                self.rect.left = 11
                """ animacion"""

    def get_frame(self,frame_set):
        self.frame += 1
        if self.frame > (len(frame_set)-1):
            self.frame = 0
        return frame_set[self.frame]
    def clip(self,clipped_rect):
        if type(clipped_rect) is dict:
            self.imagenCarro.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.imagenCarro.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self,direction):
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.centerx += 2

        self.image = self.imagenCarro.subsurface(self.imagenCarro.get_clip())

    def dibujar(self,superficie):
        superficie.blit(self.image,self.rect)




class Enemigos(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite._init__(self)
        self.imagenEnemigo = pygame.imagen.load("imanagenes/caja.png")


        """ atributos del enemigo"""
        self.imagenPos = 0 # la posicion por defecto que se va a ir graduando manualmente

        self.rect = self.imagenEnemigo.get_rect()


        self.velocidad = 5 # velocidad con la que va a bajar
        self.MaxDescenso = self.rect.top + 40


    def dibujar(self,superficie):
        self.imagenEnemigo = self.imagenPos
        superficie.blit(sel.imagenEnemigo,self.rect)



def goldTraver():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Gold Traver")
    imagenFondo = pygame.image.load("imagenes/carretera1.png").convert_alpha()
    """ me permite configurar la imagen el ancho y el alto de la imagen"""
    imagenFondo = pygame.transform.scale(imagenFondo, (900, 500))



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
                        player.update('right')








        ventana.blit(imagenFondo,(0,0))
        """ pinta el jugador en la ventana y la dibuja """
        player.dibujar(ventana)












        pygame.display.update()

goldTraver()
