from classes import *
from fichier import *
from random import *

#CREATION CARTES
def initia_carte():
    cartes = open_fichier("cartes/cartes.txt")
    for i in range(1,len(cartes)):
        carte = cartes[i].split("|")
        if i == 1:
            encyclo_c = Carte(carte[0],carte[1],carte[2],carte[3],carte[4],carte[5],int(carte[6]), carte[7], carte[8])
            encyclo_c.head = encyclo_c
        else:
            encyclo_c = crea_carte(cartes[i].split("|"),encyclo_c) 
    return encyclo_c

def crea_carte(carte, encyclo):
    while encyclo.next != 0:
        encyclo = encyclo.next
    encyclo.next = Carte(carte[0],carte[1],carte[2],carte[3],carte[4],carte[5],int(carte[6]),carte[7],carte[8], encyclo,0,encyclo.head)
    return encyclo.head

def effet_carte(carte, joueur):
    if carte.effet[0] == 'S':
        effet_soin(joueur, carte.effet, carte.cible)
    elif carte.effet[0] == 'V':
        effet_valeur(joueur, carte.effet, carte.cible)
    elif carte.effet[0] == "B":
        effet_bouclier(joueur, carte.effet)
    elif carte.effet[0] == "A":
        effet_attaque(joueur, carte.effet, carte.cible)

def suppr_carte_plateau(joueur, carte):
    del joueur.plateau[carte]

def attaquer(joueur, carte, attaque, c_type):
    if carte.type == c_type:
        if carte.pdv - attaque >= 0:
            carte.pdv = carte.pdv - attaque
        else:
            suppr_carte_plateau(joueur, carte)
    else:
        return 1    
    return 0

def effet_attaque(joueur, attaque, cible):
    attaque = int(attaque[1:])
    if cible[1] == "R":
        verif = 1
        while verif == 1 :
            alea = randint(0,len(joueur.plateau))
            count = 0
            for carte in joueur.plateau:
                if count == alea:
                    verif = attaquer(joueur, carte, attaque, "U")
                else:
                    count = count + 1
def effet_bouclier(joueur, bouclier):
    bouclier = int(bouclier[1:])
    joueur.bouclier += bouclier
            
def change_valeur(carte, valeur, c_type, signe):
    if carte.type[0] == c_type:
        if signe == "+":
            if carte.valeur + valeur <= 10:
                carte.valeur = carte.valeur + valeur
            else:
                carte.valeur = 10
        elif signe == "-":
            if carte.valeur - valeur >= 1 :
                carte.valeur = carte.valeur - valeur
            else:
                carte.valeur = 1

def effet_valeur(joueur, valeur, cible):
    
    valeur = int(valeur[2:])
    if type(cible) == Carte:
        change_valeur(cible, valeur, "U", "+")
    elif cible[1] == "A":
        for carte in joueur.plateau:
            change_valeur(cible, valeur, "U", cible[0])
    elif cible[1] == "R":
        alea = randint(0,len(joueur.plateau))
        count = 0
        for carte in joueur.plateau:
            if count == alea:
                change_valeur(carte, valeur, "U", cible[0])
            else:
                count = count + 1  

def soigner(carte, soin, c_type):
    if carte.type[0] == c_type:
        if (carte.pdv + soin) <= carte.pdv_max:
            carte.pdv = carte.pv + soin
        else:
            carte.pdv = carte.pdv_max
    else:
        return 1
    return 0
def effet_soin(joueur, soin, cible):
    nbr = ""
    soin.remove(soin[0])
    soin = int(soin)
    verif = 1
    while verif == 1:
        if type(cible) is Carte:
            verif = soigner(cible, soin, "U")
        if cible[1] == "C": #soigne le chateau
            if joueur.vie + soin <= 100:
                joueur.vie = joueur.vie + soin
            else:
                joueur.vie = 100
        elif cible[1] == "A": #soigne toute l'armee le chateau
            for carte in joueur.plateau:
                verif = soigner(carte, soin, "U") 
        elif cible[1] =="N": #soigne les nains
            for carte in joueur.plateau:
                verif = soigner(carte, soin, "N")
        elif cible[1] =="R": #soigne un allié random
            alea = randint(0,len(joueur.plateau))
            count = 0
            for carte in joueur.plateau:
                if count == alea:
                    verif = soigner(carte, soin, "U")
                else:
                    count = count + 1



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


def ajouter_au_plateau(joueur, carte):
    if (joueur.recherche_p(carte.nom)):
        joueur.plateau[carte.nom] = joueur.plateau[carte.nom] + int(valeur) 
    else:
        joueur.plateau[carte.nom] = int(valeur)


def piocher(joueur):
    if len(joueur.deck.cartes) > 7:
        return joueur
    rarete = {"un" : 1, "deux" : 2, "trois" : 3}
    for carte in joueur.deck.cartes:
        if joueur.deck.cartes.rarete == "1":
            rarete["un"] = rarete["un"] + 1
        elif joueur.deck.cartes.rarete == "2":
            rarete["deux"] = rarete["deux"] + 1
        else:
            rarete["trois"] = rarete["trois"] + 1
    alea = randint(0,100)
    if alea % 2 == 0:
        rarete = 1
        num_carte = randint(0,rarete["un"])
    elif alea % 3 == 0:
        rarete = 2
        num_carte = randint(0,rarete["deux"])
    else:
        rarete = 3
        num_carte = randint(0,rarete["trois"])
    count = 0
    for i in range(0, Carte.id_carte):
        if joueur.deck.cartes[i].rarete == '1':
            count + count + 1
            if count == num_carte:
                return joueur.deck.cartes[i]


        