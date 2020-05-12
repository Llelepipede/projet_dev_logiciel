#v test de home page v#

#v les includes v#
from math import *
import pygame
from random import *
#^ les includes ^#

#v fonction d'initialisation de pygame v#

def init_pygame():

    pygame.init()  #initialise le moteur pygame
    create_windows()
    boucle_jeu()
    quit_pygame()



def quit_pygame():
    pygame.quit()




def create_windows():
    dim_x = 1200  #set les dimension souhaité pour la fenetre
    dim_y = 1000
    pygame.display.set_mode((dim_x,dim_y))  #crée la fenetre de taille dim_x/dim_y

    pygame.display.set_caption('projet python')  #mets le titre de la fenetre

#^ fonction d'initialisation de pygame ^#



def boucle_jeu():
    end = 0
    while not end:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                end = 1





init_pygame()



#^ fin de test de home page ^#