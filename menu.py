import pygame
from option import *

def menu_principal(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if event.pos[0] > 100 and event.pos[0] < 200 and event.pos[1] > 100 and event.pos[1] < 200 :
                menu_l_partie()
                return 0
            elif event.pos[0] > 100 and event.pos[0] < 200 and event.pos[1] > 250 and event.pos[1] < 350 :
                #option()
                return 0
            elif event.pos[0] > 100 and event.pos[0] < 200 and event.pos[1] > 400 and event.pos[1] < 500 :
                #a_propos()
                return 0
            elif event.pos[0] > 100 and event.pos[0] < 200 and event.pos[1] > 550 and event.pos[1] < 650 :
                return 1
    return 0

def menu_l_partie():
    for event in pygame.event.get():
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

def menu_option():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[0] > 100 and event.pos[0] < 200 and event.pos[1] > 100 and event.pos[1] < 200 :
                    ajouter_carte()
                    return 0
                elif event.pos[0] > 100 and event.pos[0] < 200 and event.pos[1] > 250 and event.pos[1] < 350 :
                    #supprimer_carte()
                    return 0
                elif event.pos[0] > 100 and event.pos[0] < 200 and event.pos[1] > 400 and event.pos[1] < 500 :
                    #modifier_carte()
                    return 0
                elif event.pos[0] > 100 and event.pos[0] < 200 and event.pos[1] > 550 and event.pos[1] < 650 :
                    menu_principal(event)
def a_propos():
    print("en cours de construction")



            

