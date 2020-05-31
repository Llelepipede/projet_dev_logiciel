from classes import *
from fichier import *

#CREATION CARTES
def initia_carte():
    cartes = open_fichier("cartes/cartes.txt")
    for i in range(1,len(cartes)):
        carte = cartes[i].split("|")
        if i == 1:
            encyclo_c = Carte(carte[0],carte[1],carte[2],carte[3],carte[4],carte[5],carte[6])
            encyclo_c.head = encyclo_c
        else:
            encyclo_c = crea_carte(cartes[i].split("|"),encyclo_c) 
    return encyclo_c
def crea_carte(carte, encyclo):
    while encyclo.next != 0:
        encyclo = encyclo.next
    encyclo.next = Carte(carte[0],carte[1],carte[2],carte[3],carte[4],carte[5],carte[6], encyclo,0,encyclo.head)
    return encyclo.head

# def symbole_type(c_type):
#     if c_type == 'F':
#         return "Fournisseur"
#     elif c_type == 'S':
#         return "Sort"
#     else:
#         return "Unite"

# def symbole_cout(c_cout):
#     if c_cout[1] == "B":
#         bois = c_cout[0]
#         acier = 0
#     elif c_cout[1] == "A":
#         acier = c_cout[0]
#         bois = 0
#     elif c_cout[1] == "X":
#         bois = 0
#         acier = 0
#     if (c_cout[2] == ','):
#         nourriture = c_cout[3]
#     else:
#         nourriture = 0
#     return {"Bois" : bois, "Acier" : acier, "Nourriture" : nourriture}


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
    return 0

#UNITE ACIER

def guerrier(joueur):
    #guerrier :
    #(cout : 1a,1n | effet : NULL | cible: NULL | valeur d'armée : 2++ | point de vie : 2)
    if (joueur.recherche_p("guerrier")):
        joueur.plateau["guerrier"] = joueur.plateau["guerrier"] + 2
    else:
        joueur.plateau["guerrier"] = 2

def forgeron(joueur):
    #forgeron :
    #(cout : 3a,1n | effet : B-10 | cible: chateau | valeur d'armée : 1++ | point de vie : 4)
    if (joueur.recherche_p("forgeron")):
        joueur.plateau["forgeron"] = joueur.plateau["forgeron"] + 1
    else:
        joueur.plateau["forgeron"] = 1

def lanceur_de_hache(joueur):
    #lanceur de hache :
    #(cout : 4a,2n | effet : A-2 | cible: unité | valeur d'armée : 3++ | point de vie : 3)
    if (joueur.recherche_p("lanceur_de_hache")):
        joueur.plateau["lanceur_de_hache"] = joueur.plateau["lanceur_de_hache"] + 1
    else:
        joueur.plateau["lanceur_de_hache"] = 1
    
def roi_dlm(joueur):
    #roi de la montagne :
    #(cout : 9a,3n | effet : "a decider" | cible: unité | valeur d'armée : 7++ | point de vie : 9)
    if (joueur.recherche_p("roi dlm")):
        print("vous ne pouvez avoir qu'un seul roi de la montagne sur le plateau")
    else:
        joueur.plateau["roi dlm"] = 7

#UNITE NOURRITURE

def soldat(joueur):
    #soldat :
    #(cout : 1n | effet : NULL | cible: NULL | valeur d'armée : 1++ | point de vie : 2)
    if (joueur.recherche_p("soldat")):
        joueur.plateau["soldat"] = joueur.plateau["soldat"] + 1
    else:
        joueur.plateau["soldat"] = 1

def explorateur(joueur):
    #explorateur :
    #(cout : 2n | effet : P-1 | cible: joueur | valeur d'armée : 1++ | point de vie : 2)
    if (joueur.recherche_p("explorateur")):
        joueur.plateau["explorateur"] = joueur.plateau["explorateur"] + 1
    else:
        joueur.plateau["explorateur"] = 1