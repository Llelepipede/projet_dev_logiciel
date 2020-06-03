

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



# les cartes


# -bois
#     fournisseur : bucheron(1++) - scierie(2++)

#     sort :
#         pluie de fleche :
#             (cout : 3b | effet : A-1x"elfe des bois" | cible: unitée )
#         "name_is_not_define" :
#             (cout : 3b | effet : V-2 | cible: alliés )


#     unité :
#         elfe des bois :
#             (cout : 1b,1n | effet : NULL | cible: NULL | valeur d'armée : 2++ | point de vie : 2 )
#         dryade :
#             (cout : 3b,1n | effet : S-1 | cible: alliés | valeur d'armée : 1++ | point de vie : 3)
#         Etre sylvestre :
#             (cout : 4b | effet : S-15 | cible: chateau | valeur d'armée : 4++ | point de vie : 3)
#         Seigneur de la foret :
#             (cout : 9b,2n | effet : V--1000 | cible: adv | valeur d'armée : 7++ | point de vie : 3)




# -nouriture
#     fournisseur : paysan(1++) - ferme(2++)

#     unité :
#         soldat :
#             (cout : 1n | effet : NULL | cible: NULL | valeur d'armée : 1++ | point de vie : 2)

#         explorateur :
#             (cout : 2n | effet : P-1 | cible: joueur | valeur d'armée : 1++ | point de vie : 2)


# -acier
#     fournisseur : mineur(1++) - forge(2++)

#     sort :
#         ALLUMER LA FORGE ! :
#             (cout : 2a | effet : B-5x"forgeron" | cible: chateau)

#         C'est ma tournée :
#             (cout : 1a, 3n | effet : S-2 | cible: nain)

#     unité :
#         guerrier :
#             (cout : 1a,1n | effet : NULL | cible: NULL | valeur d'armée : 2++ | point de vie : 2)
#         forgeron :
#             (cout : 3a,1n | effet : B-10 | cible: chateau | valeur d'armée : 1++ | point de vie : 4)
#         lanceur de hache :
#             (cout : 4a,2n | effet : A-2 | cible: unité | valeur d'armée : 3++ | point de vie : 3)
#         roi de la montagne :
#             (cout : 9a,3n | effet :  | cible:  | valeur d'armée : 7++ | point de vie : 9)

#





#v test de home page v#


#v les includes v#
from math import *
from menu import *
from local import *
from classes import *
from form import *
from cartes import *
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
    dim_x = 1230  #set les dimension souhaité pour la fenetre
    dim_y = 0 #1080
    fenetre = pygame.display.set_mode((dim_x,dim_y),pygame.FULLSCREEN)  #crée la fenetre de taille dim_x/dim_y


    pygame.display.set_caption('projet python')  #mets le titre de la fenetre

    return fenetre
#^ fonction d'initialisation de pygame ^#



def boucle_jeu(fenetre):

    menu_principal(fenetre)



init_pygame()



#^ fin de test de home page ^#