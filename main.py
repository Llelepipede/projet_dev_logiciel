

# definir un univers
# menu
    # 2 mode de jeu
        # ia
        # jeu en local
# ecran jeu
    # 2 camp
        # un joueur
            # vie ( 100 max )
            # bouclier( 30 max )

        # des ressources ( 3 types )
            # bois
            # nouritures
            # pierres
        # des fournisseurs de ressources
        # une main
            # 7 cartes
                # un nom
                # un cout
                    # 0 si fournisseur de ressources ( arbitraire pour l'instant )
                # un effet
                    # soin
                    # dammage
                    # pioche
                    # ...
                # des valeurs
                    # ???
                # une cible
        # un deck
            # pioche aléatoire
        # defausse

    # tour a tour
        # +1 par fournisseur dans la ressource en question
        # une pioche ( si carte < 7 )
            # pioche aléatoire
        # auto deffausse si > 7 cartes en main
        # jouer une carte si les ressources le permettent

    # historique des tours

    # fin partie si joueur a pv <= pv
# ecran victoire
    # stats de la partie
# ecran tuto
    # explique comment on joue
# ecran option
    # créer
    # consulter
    # supprimer
    # modifier
    # sauvegarde des cartes de
    # a créer


#v test de home page v#


#v les includes v#
from math import *
from menu import *
from local import *
from classes import *
from form import *
import pygame
from random import *
#^ les includes ^#

#v fonction d'initialisation de pygame v#

def init_pygame():

    pygame.init()  #initialise le moteur pygame
    fenetre = create_windows()
    boucle_jeu(fenetre)
    quit_pygame()



def quit_pygame():
    pygame.quit()




def create_windows():
    dim_x = 1300  #set les dimension souhaité pour la fenetre
    dim_y = 0
    fenetre = pygame.display.set_mode((dim_x,dim_y),pygame.FULLSCREEN)  #crée la fenetre de taille dim_x/dim_y


    pygame.display.set_caption('projet python')  #mets le titre de la fenetre

    return fenetre
#^ fonction d'initialisation de pygame ^#



def boucle_jeu(fenetre):
    end = 0
    while not end:

        end = menu_principal(fenetre)



init_pygame()



#^ fin de test de home page ^#