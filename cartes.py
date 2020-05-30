from classes import *

#SORTS BOIS
def Pluie_de_fleche(lanceur, cible): #a finir
    #pluie de fleche :
    #(cout : 3b | effet : A-1x"elfe des bois" | cible: unitée | valeur d'armée : 1++ )
    carte = lanceur.recherche_p("elfe des bois")
    if (carte):
        attaque = carte.items()

    for i in range(0, attaque):
        print("test1")

#UNITE BOIS 
def elfe_des_bois(joueur) : 
    #elfes des bois :
    #(cout : 1b,1n | effet : NULL | cible: NULL | valeur d'armée : 2++ | point de vie : 2 )
    if (joueur.recherche_p("elfe des bois")):
        joueur.plateau["elfe des bois"] = joueur.plateau["elfe des bois"] + 2
    else:
        joueur.plateau["elfe des bois"] = 2


def dryade (joueur):
    #dryade :
    #(cout : 3b,1n | effet : S-1 | cible: alliés | valeur d'armée : 1++ | point de vie : 3)
    if (joueur.recherche_p("dryade")):
        joueur.plateau["dryade"] = joueur.plateau["dryade"] + 1
    else:
        joueur.plateau["dryade"] = 1


def etre_sylvestre(joueur):
        #Etre sylvestre :
        #(cout : 4b | effet : S-15 | cible: chateau | valeur d'armée : 4++ | point de vie : 3)
        if (joueur.recherche_p("etre sylvestre")):
            joueur.plateau["etre sylvestre"] = joueur.plateau["etre sylvestre"] + 4
        else:
            joueur.plateau["etre sylvestre"] = 4

def seigneur_dlf(joueur):
    #Seigneur de la foret :
    #(cout : 9b,2n | effet : V--1000 | cible: adv | valeur d'armée : 7++ | point de vie : 3)
    if (joueur.recherche_p("seigneur dlf")):
        print("vous ne pouvez avoir qu'un seul seigneur de la forêt sur le plateau")
    else:
        joueur.plateau["seigneur dlf"] = 7

#SORTS ACIER

def Allumer_forge(joueur):
    #ALLUMER LA FORGE ! :
    #(cout : 2a | effet : B-5x"forgeron" | cible: chateau)
    if(joueur.recherche_p("forgeron")):
        joueur.bouclier = joueur.bouclier +  5 * joueur.plateau["forgeron"]
    else:
        print("Vous n'avez pas de forgeron sur le jeu")

def la_tournee(joueur): #a faire
    #C'est ma tournée :
    #(cout : 1a, 3n | effet : S-2 | cible: nain)

#UNITE