import pygame
from classes import *

def initialiser_joueur():
    pseudo = input("entrez un pseudo pour le joueur 1 : ")
    deck = Carte("carte1", 3, "bois", "tue une unité", "ennemie")
    Joueur_un = Joueur(pseudo, 100, 0, deck)

    pseudo = input("entrez un pseudo pour le joueur 2 : ")
    deck = Carte("carte2", 4, "pierre", "tue une unité", "ennemie")
    Joueur_deux = Joueur(pseudo, 100, 0, deck)

    return Joueur_un, Joueur_deux

def joueur_local():
    joueur_un, joueur_deux = initialiser_joueur()
    print (joueur_un.pseudo, joueur_deux.pseudo)
    print (joueur_un.deck.nom, joueur_deux.deck.nom)
    print (joueur_un.deck.effet, joueur_deux.deck.effet)

#joueur_local()