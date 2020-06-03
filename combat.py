import pygame
from menu import *
from form import *
from cartes import *
from classes import *

def jouer_local(fenetre):
    data_partie = demarrage_partie(fenetre)
    return ecran_jeu(fenetre,data_partie)


def ecran_jeu(fenetre,data):
    end = 0
    choix = 0

    while not end :
        pygame.display.update()

        if data.tour % 2 == 0:
            joueur = data.joueur0
        else:
            joueur = data.joueur1
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(event.pos)
            if event.type == pygame.KEYDOWN :
                print(event.key)
                if event.key == 273: # haut
                    choix -= 3
                if event.key == 275: # droite
                    choix += 1
                if event.key == 274: # bas
                    choix += 3
                if event.key == 276: # gauche
                    choix -= 1
                if event.key == 13: # entrée
                    data = activate_choix(fenetre,data,choix)
                    data = actualise(data)

                if event.key == 27: # echap
                    print("ok")
                    end = quit_menu(fenetre,data) - 1

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1:
        choix = choix % 6


        jeu_form(fenetre,choix)
        jeu_form_text(fenetre)
        jeu_form_data(fenetre,data)

    return end

def actualise(data):
    data.joueur0 = armee(data.joueur0)
    data.joueur1= armee(data.joueur1)

    return data

def quit_menu(fenetre,data):
    end = 0
    while not end :
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(event.pos)
                    if event.pos[0] > 490 and event.pos[0] < 810 and event.pos[1] > 340 and event.pos[1] < 395 :
                        print("carré 1")
                        end = 1
                    elif event.pos[0] > 490 and event.pos[0] < 810 and event.pos[1] > 445 and event.pos[1] < 500 :
                        print("carré 2")
                        option()
                    elif event.pos[0] > 490 and event.pos[0] < 810 and event.pos[1] > 550 and event.pos[1] < 605 :
                        print("carré 3")

                        end = 2
                    elif event.pos[0] > 490 and event.pos[0] < 810 and event.pos[1] > 655 and event.pos[1] < 710 :
                        print("carré 4")
                        end = 4
        quit_menu_form(fenetre,("retour au jeu","option","retour au menu","quitter le jeu"))

    return end



def demarrage_partie(fenetre):
    joueurs = initialiser_joueur()
    data = data_jeu(joueurs[0],joueurs[1])
    return data


def activate_choix(fenetre,data,choix):
    if choix == 0:
        return voir_main(fenetre,data)
    elif choix == 1:
        return voir_plateau(fenetre,data)
    elif choix == 5:
        return fin_de_tour(fenetre,data)

def fin_de_tour(fenetre,data):

    if data.tour %2 == 0:
        data.joueur1 = piocher(data.joueur1)
        augm_ressource(data.joueur1)
    elif data.tour %2 == 1:
        data.joueur0 = piocher(data.joueur0)
        augm_ressource(data.joueur0)
    data.tour += 1
    data = attaquer_armee(data)
    return data


def voir_main(fenetre,data):
    cursor_y = 0
    end = 0
    while not end:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == 273: # haut
                    cursor_y -= 1
                if event.key == 274: # bas
                    cursor_y += 1
                if event.key == 13: # entrée
                    if (not cursor_y > len(data.joueur0.main)) and len(data.joueur0.main):
                        data = jouer_carte(data,cursor_y)

                if event.key == 27: # echap
                    end = 1



        cursor_y = cursor_y % 7
        voir_main_form(fenetre,cursor_y)
        voir_main_form_data(fenetre,data)

    return data

def jouer_carte(data,choix):
    joueur = data.joueur0 if data.tour % 2 == 0 else data.joueur1

    joueur, jouable = cout_carte(joueur,joueur.main[choix])

    if not jouable:
        return data
    else:
        #effet_carte(joueur.main[choix], joueur)

        ajouter_au_plateau(joueur,joueur.main[choix])
        del joueur.main[choix]
        return data

def voir_plateau(fenetre,data):
    cursor_y = 0
    end = 0
    while not end:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("ok")
            if event.type == pygame.KEYDOWN :
                print(event.key)
                if event.key == 273: # haut
                    cursor_y -= 1
                if event.key == 274: # bas
                    cursor_y += 1
                #if event.key == 13: # entrée
                    #if cursor_y == 7-len(data.joueur0.main)

                if event.key == 27: # echap
                    end = 1


        voir_plateau_form(fenetre)
        voir_plateau_form_data(fenetre,data)

    return data
