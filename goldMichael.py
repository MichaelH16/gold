import base64
import StringIO
import json
import gzip

import pygame,sys
import random
from pygame.locals import *



""" variables globales"""
ancho = 900
alto = 500
""" mapa """
_tileWidh = 0
_widhtMapa = 0
_heighMapa = 0
_tileHeight = 0

_matrizMapa = []


class jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenCarro = pygame.image.load("sprites_gold.png")
        self.imagenCarro.set_clip(pygame.Rect(126,26,90,140))
        self.image = self.imagenCarro.subsurface(self.imagenCarro.get_clip())
        self.inv_imagencarro = pygame.transform.flip(self.imagenCarro,True,False)
        self.inv_imagencarro.set_clip(pygame.Rect(41,26,90,140))
        self.Rimage = self.inv_imagencarro.subsurface(self.inv_imagencarro.get_clip())



        self.rect = self.image.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto-65

        self.vida = True
        self.velocidad = 50

        self.frame = 0
        """ animacion """
        self.right_states = {0: (41,26,90,134),1:(200,26,80,140),2:(140,26,70,138)}
        self.Rright_states = {0: (41,26,90,134),1:(500,26,200,140),2:(140,26,70,138)}


        self.direct = True
        self.salto = False
        self.salto_par = False
        self.bajada = True
        self.contadorfun = 0



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


    def Rclip (self, Rclipped_rect):
        if type (Rclipped_rect) is dict:
            self.inv_imagencarro.set_clip(pygame.Rect(self.get_frame(Rclipped_rect)))
        else:
            self.inv_imagencarro.set_clip(pygame.Rect(Rclipped_rect))
        return Rclipped_rect


    def update(self,direction):
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.centerx += 5

        elif direction == "left":
            self.Rclip(self.Rright_states)
            self.rect.centerx -= 5


        self.Rimage = self.inv_imagencarro.subsurface(self.inv_imagencarro.get_clip())
        self.image = self.imagenCarro.subsurface(self.imagenCarro.get_clip())

    def saltar(self,superficie):

        if self.salto == True:

            if self.direct == True:
                superficie.blit(self.image,(self.rect.centerx,self.rect.centery),(self.right_states[1]))

            if self.direct == False:
                superficie.blit(self.Rimage,(self.rect.centerx,self.rect.centery),(self.Rright_states[1]))

            if self.bajada == False:
                self.rect.centery -= 4

            if self.bajada == True:
                self.rect.centery += 4

            if self.rect.centery == 186:
                self.bajada = True

            if self.rect.centery == 318:
                self.bajada == False
                self.salto = False


    def dibujar(self,superficie):
        superficie.blit(self.image,self.rect)

    def rdibujar(self,superficie):
        superficie.blit(self.Rimage,self.rect)




class Enemigos(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite._init__(self)
        self.imagenEnemigo = pygame.imagen.load("caja.png")


        """ atributos del enemigo"""
        self.imagenPos = 0 # la posicion por defecto que se va a ir graduando manualmente

        self.rect = self.imagenEnemigo.get_rect()


        self.velocidad = 5 # velocidad con la que va a bajar
        self.MaxDescenso = self.rect.top + 40


    def dibujar(self,superficie):
        self.imagenEnemigo = self.imagenPos
        superficie.blit(self.imagenEnemigo,self.rect)


def cargar_mapa(nivel1):
    global _tileWidh,_widhtMapa,_heighMapa,_tileHeight,_matrizMapa#global indica las variables que se definen arriba

    f = open("../maps/"+nivel1+".json","r")# accedemos al archivo nivel 1 y el r es par que sea de lectura
    data  =  json.load(f)# almacenamos la informacion de f y con jso.load decimos que es json
    f.close()

    _tileWidht = data["tilewidth"]# utiliza el ancho del data del mapa
    _tileHeight = data["tileheight"]#utiliza el alto del mapa

    _widhtMapa = data["width"]
    _heighMapa = data["height"]

    """obtener el mapa """
    for item in data["layers"]:#layers son las capas que hicimos como suelo...
        mapa = item["data"]

    print (mapa)

    """decodificar"""
    mapa = base64.decodestring(mapa)
    #print mapa

    """descomprimir"""
    cadena = gzip.zlib.descompress(mapa);

    #print cadena

    """ convertir caracteres a numeros"""



def goldTraver():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Gold Traver")
    imagenFondo = pygame.image.load("carretera1.png").convert_alpha()
    """ me permite configurar la imagen el ancho y el alto de la imagen"""
    imagenFondo = pygame.transform.scale(imagenFondo, (900, 500))
    clock = pygame.time.Clock()



    """ creacion del jugador"""
    player = jugador()

    enJuego = True



    while True:
        time = clock.tick(60)
        """ si el jugador da a la x de la venta se cierra la pantalla"""

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            """ crear eventos cuando se oprime una telca"""

            if enJuego == True:# se usa para saber si el jugador no ha perdido

                if evento.type == pygame.KEYDOWN:
                    key = evento.dict["key"]
                    print(key)

                    if evento.key == 276:#izquierda
                        player.movimientoIzquierda()
                        player.update("left")

                        player.direct = False


                    if evento.key == 275:#derecha
                        player.movimientoDerecha()
                        player.update('right')

                        player.direct = True

                    if evento.key == 273 and player.salto == False and player.salto_par == False:


                        player.saltar(ventana)
                        player.salto = True





                    """
                    if evento.key == 273:
                        player.salto = True
                        if player.contadorfun == 0:
                            player.rect.y -= player.velocidad
                            player.contadorfun += 1
                        if player.contadorfun == 1:
                            player.contadorfun -= 1
                            player.rect.y += player.velocidad
                if evento.type ==pygame.KEYUP:
                    if evento.key == 273:
                        player.contadorfun -= 1
                        player.rect.y += player.velocidad
                        """















        ventana.blit(imagenFondo,(0,0))
        """ pinta el jugador en la ventana y la dibuja """
        if player.direct == True:
            player.dibujar(ventana)
        elif player.direct == False:
            player.rdibujar(ventana)















        pygame.display.update()

goldTraver()
