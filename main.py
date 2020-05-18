

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
    # sauvegarde des cartes deja créer





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
            print(event)
            if event.type == pygame.QUIT:
                end = 1





init_pygame()



#^ fin de test de home page ^#