import pygame
from form import *


def menu_principal(fenetre):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[0] > 440 and event.pos[0] < 760 and event.pos[1] > 450 and event.pos[1] < 505 :
                    #menu_l_partie()
                    print("carré 1")
                    return 0
                elif event.pos[0] > 440 and event.pos[0] < 760 and event.pos[1] > 555 and event.pos[1] < 610 :
                    #option()
                    print("carré 2")

                    return 0
                elif event.pos[0] > 440 and event.pos[0] < 760 and event.pos[1] > 660 and event.pos[1] < 715 :
                    #a_propos()
                    print("carré 3")

                    return 0
                elif event.pos[0] > 440 and event.pos[0] < 760 and event.pos[1] > 765 and event.pos[1] < 820 :
                    print("carré 4")

                    return 1

        if event.type == pygame.QUIT:
            return 1
    affichage_menu(fenetre)
    return 0




def affichage_menu(fenetre):
    ''' affichage des objet visuel sur la fenettre du menu '''

    size_x = 320
    size_y = 55
    start_x = 440
    start_y = 450
    decalage = size_y + 50

    taille_text = 30
    color = (0,0,0)
    fond_ecran = pygame.image.load('img/misc/fond-ecran-png-2 - Copie.png')

    fenetre.blit(fond_ecran,(0,-100))
    zonetext(fenetre,start_x,start_y,size_x,size_y)
    zonetext(fenetre,start_x,start_y + decalage,size_x,size_y)
    zonetext(fenetre,start_x,start_y + decalage * 2,size_x,size_y)
    zonetext(fenetre,start_x,start_y + decalage * 3,size_x,size_y)

    message_display(fenetre,"jouer",taille_text,color,start_x + 120,start_y+10)
    message_display(fenetre,"option",taille_text,color,start_x + 115,start_y + decalage+10)
    message_display(fenetre,"a propos",taille_text,color,start_x + 100,start_y + decalage * 2+10)
    message_display(fenetre,"quiter",taille_text,color,start_x + 120,start_y + decalage * 3+10)

    pygame.display.update()



def menu_l_partie(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if event.pos[0] > 100 and event.pos[0] < 200 and event.pos[1] > 100 and event.pos[1] < 200 :
                #joueur_local()
                return 0
            elif event.pos[0] > 100 and event.pos[0] < 200 and event.pos[1] > 250 and event.pos[1] < 350 :
                #contre_IA()
                return 0
            elif event.pos[0] > 100 and event.pos[0] < 200 and event.pos[1] > 400 and event.pos[1] < 500 :
                #Tuto()
                return 0
            elif event.pos[0] > 100 and event.pos[0] < 200 and event.pos[1] > 550 and event.pos[1] < 650 :
                menu_principal(event)
    return 0

def a_propos():
    print("en cours de construction")





