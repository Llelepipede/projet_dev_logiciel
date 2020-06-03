import pygame
from classes import *
from cartes import * 

def initia_deck(encyclo_c):
    deck1 = Deck("joueur1")
    deck2 = Deck("joueur2")
    for i in range(0,Carte.id_carte-1):
        deck1.cartes.append(encyclo_c)
        deck2.cartes.append(encyclo_c)
        encyclo_c = encyclo_c.next

    return deck1, deck2

def initialiser_joueur():
    encyclo_c = initia_carte()
    deck1, deck2 = initia_deck(encyclo_c)
    pseudo = input("entrez un pseudo pour le joueur 1 : ")
    joueur1 = Joueur(pseudo, 100, 30, deck1)

    pseudo = input("entrez un pseudo pour le joueur 2 : ")  
    joueur2 = Joueur(pseudo, 100, 30, deck2)
    for i in range(0,7):
        joueur1.main.append(piocher(joueur1))
        joueur2.main.append(piocher(joueur1))
    print (joueur1.deck)
    return joueur1, joueur2

def attaquer(data):
    if data.tour % 2 == 0:
        if data.joueur2.bouclier - data.joueur1.valeur < 0 :
            reste = data.joueur1.valeur - data.joueur2.bouclier
            data.joueur2.vie = data.joueur2.vie - reste
        else:
            data.joueur2.bouclier = data.joueur2.bouclier - data.joueur1.valeur
    else:
        if data.joueur1.bouclier - data.joueur2.valeur < 0 :
            reste = data.joueur2.valeur - data.joueur1.bouclier
            data.joueur1.vie = data.joueur1.vie - reste
        else:
            data.joueur1.bouclier = data.joueur1.bouclier - data.joueur1.valeur

    return data

def augm_ressource(joueur):
    for carte in joueur.plateau:
        if carte.type == "F":
            if joueur.ressources[carte.effet[1]] + int(carte.effet[0]) <= 10:
                joueur.ressource[carte.effet[1]] = joueur.ressource + int(carte.effet[0])
            else: 
                joueur.ressource[carte.effet[1]] = 10

def augm_valeur(joueur):
    for carte in joueur.plateau:
        if carte.type == "U":
            joueur.valeur += int(carte.valeur)

def joueur_local():
    joueur1, joueur2 = initialiser_joueur()
    data = data_jeu(joueur1, joueur2)
    print (joueur1.pseudo, joueur2.pseudo)
    print (joueur1.deck.nom, joueur2.deck.nom)

#joueur_local()