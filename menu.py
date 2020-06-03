import pygame
from form import *
from combat import *

def menu_principal(fenetre):
    end = 0
    while not end :
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if event.pos[0] > 440 and event.pos[0] < 760 and event.pos[1] > 450 and event.pos[1] < 505 :
                        end = menu_l_partie(fenetre) -1
                        print("carré 1")
                    elif event.pos[0] > 440 and event.pos[0] < 760 and event.pos[1] > 555 and event.pos[1] < 610 :
                        #end = option()
                        print("carré 2")
                    elif event.pos[0] > 440 and event.pos[0] < 760 and event.pos[1] > 660 and event.pos[1] < 715 :
                        #end = a_propos()
                        print("carré 3")
                    elif event.pos[0] > 440 and event.pos[0] < 760 and event.pos[1] > 765 and event.pos[1] < 820 :
                        print("carré 4")
                        end = 1

            if event.type == pygame.QUIT:
                end = 1
        fond_ecran = pygame.image.load('img/misc/fond-ecran-png-2 - Copie.png')
        fenetre.blit(fond_ecran,(0,-100))
        menu_form(fenetre,("Jouer","option","a propos","quiter"))





def menu_l_partie(fenetre):
    end = 0
    while not end :
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if event.pos[0] > 440 and event.pos[0] < 760 and event.pos[1] > 450 and event.pos[1] < 505 :
                        end = jouer_local(fenetre) - 1
                        print("carré 1")
                    elif event.pos[0] > 440 and event.pos[0] < 760 and event.pos[1] > 555 and event.pos[1] < 610 :
                        end = jouer_ia(fenetre) - 1
                        print("carré 2")
                    elif event.pos[0] > 440 and event.pos[0] < 760 and event.pos[1] > 660 and event.pos[1] < 715 :
                        end = jouer_tuto(fenetre) - 1
                        print("carré 3")
                    elif event.pos[0] > 440 and event.pos[0] < 760 and event.pos[1] > 765 and event.pos[1] < 820 :
                        print("carré 4")
                        end = 1
        fond_ecran = pygame.image.load('img/misc/fond-ecran-png-2 - Copie.png')
        fenetre.blit(fond_ecran,(0,-100))
        menu_form(fenetre,("en local","contre ia","tuto","retour"))

    return end

def a_propos():
    print("en cours de construction")





