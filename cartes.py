from classes import *
from fichier import *
from random import *

#CREATION CARTES
def initia_carte():
    cartes = open_fichier("cartes/cartes.txt")
    for i in range(1,len(cartes)-1):
        carte = cartes[i].split("|")
        if i == 1:
            encyclo_c = Carte(carte[0],carte[1],carte[2],carte[3],carte[4],carte[5],int(carte[6]), carte[7],carte[8])
            encyclo_c.head = encyclo_c
        else:
            encyclo_c = crea_carte(cartes[i].split("|"),encyclo_c)
    return encyclo_c

def crea_carte(carte, encyclo):
    while encyclo.next != 0:
        encyclo = encyclo.next
    encyclo.next = Carte(carte[0],carte[1],carte[2],carte[3],carte[4],carte[5],int(carte[6]),carte[7],carte[8], encyclo,0,encyclo.head)
    return encyclo.head

def initia_deck(encyclo_c):
    deck1 = Deck("joueur1")
    deck2 = Deck("joueur2")
    for i in range(0,17):
        print(i)
        deck1.cartes.append(encyclo_c)
        deck2.cartes.append(encyclo_c)
        encyclo_c = encyclo_c.next

    return deck1, deck2

def initialiser_joueur():
    encyclo_c = initia_carte()
    deck1, deck2 = initia_deck(encyclo_c)

    joueur1 = Joueur("Bertrand",deck1,[])

    joueur2 = Joueur("René", deck2,[])
    return joueur1, joueur2

def piocher(joueur):
    if len(joueur.main) >= 7:
        return joueur
    rarete = {"un" : 0, "deux" : 0, "trois" : 0}
    for carte in joueur.deck.cartes:
        if carte.rarete == "1":
            rarete["un"] = rarete["un"] + 1
        elif carte.rarete == "2":
            rarete["deux"] = rarete["deux"] + 1
        else:
            rarete["trois"] = rarete["trois"] + 1

    alea = randrange(0,100)
    if alea % 8 == 0:
        carte_rarete = "3"

        num_carte = randrange(0,rarete["trois"])

    elif alea % 3 == 0:
        carte_rarete = "2"
        num_carte = randrange(0,rarete["deux"])
    else:
        carte_rarete = "1"
        num_carte = randrange(0,rarete["un"])

    count = 0

    for i in range(0, Carte.id_carte):
        print("num: ",num_carte,"count: ",count,"rareté: ",carte_rarete)
        if joueur.deck.cartes[i].rarete == carte_rarete:

            if count == num_carte:
                joueur.main.append(joueur.deck.cartes[i])
                return joueur
            count = count + 1

def effet_carte(carte, data):
    joueur = data.joueur0 if data.tour % 2 == 0 else data.joueur1

    print(carte.effet[0])
    if carte.effet[0] == 'S':
        data = effet_soin(data, carte.effet, carte.cible)
    elif carte.effet[0] == 'V':
        data = effet_valeur(data, carte.effet, carte.cible)
    elif carte.effet[0] == "B":
        data = effet_bouclier(data, carte.effet)
    elif carte.effet[0] == "A":
        data = effet_attaque(data, carte.effet, carte.cible)
    elif carte.effet[0] == "P":
        joueur = piocher(joueur)

    return data
def suppr_carte_plateau(joueur, carte):
    del joueur.plateau[carte]

def attaquer(data, carte, attaque, c_type):
    joueur = data.joueur0 if data.tour % 2 == 0 else data.joueur1
    if carte.type == c_type:
        if carte.pdv - attaque >= 0:
            carte.pdv = carte.pdv - attaque
        else:
            suppr_carte_plateau(joueur, carte)
    else:
        return 1
    return 0

def attaquer_armee(data):
    if data.tour % 2 == 1:
        if data.joueur0.bouclier - data.joueur1.valeur < 0 :
            reste = data.joueur1.valeur - data.joueur0.bouclier
            data.joueur0.bouclier = data.joueur1.valeur - reste
            data.joueur0.vie = data.joueur0.vie - reste
        else:
            data.joueur0.bouclier = data.joueur0.bouclier - data.joueur1.valeur
    else:
        if data.joueur1.bouclier - data.joueur0.valeur < 0 :
            reste = data.joueur0.valeur - data.joueur1.bouclier
            data.joueur0.bouclier = data.joueur1.valeur - reste
            data.joueur1.vie = data.joueur1.vie - reste
        else:
            data.joueur1.bouclier = data.joueur1.bouclier - data.joueur1.valeur

    return data

def augm_ressource(joueur):
    for carte in joueur.plateau:
        if carte.type == "F":
            if joueur.ressource[carte.effet[1]] + int(carte.effet[0]) <= 10:
                joueur.ressource[carte.effet[1]] = joueur.ressource[carte.effet[1]] + int(carte.effet[0])
            else:
                joueur.ressource[carte.effet[1]] = 10

def effet_attaque(data, attaque, cible):
    joueur = data.joueur0 if data.tour % 2 == 0 else data.joueur1
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
def effet_bouclier(data, bouclier):
    joueur = data.joueur0 if data.tour % 2 == 0 else data.joueur1
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

def effet_valeur(data, valeur, cible):

    joueur = data.joueur0 if data.tour % 2 == 0 else data.joueur1
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
def effet_soin(data, soin, cible):
    joueur = data.joueur0 if data.tour % 2 == 0 else data.joueur1
    nbr = ""
    soin = int(soin[1:])
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

def armee(joueur):
    armee = 0
    for k in joueur.plateau:
        armee += int(k.valeur)
    joueur.valeur = armee
    return joueur




def cout_carte(joueur, carte):
    if int(carte.cout[0]) == 0:
        return joueur, 1
    if int(carte.cout[0]) <= joueur.ressource[carte.cout[1]]:
        if len(carte.cout) > 2:
            if int(carte.cout[3]) <= joueur.ressource[carte.cout[4]]:
                joueur.ressource[carte.cout[1]] -= int(carte.cout[0])
                joueur.ressource[carte.cout[4]] -= int(carte.cout[3])
                return joueur, 1
        else:
            joueur.ressource[carte.cout[1]] -= int(carte.cout[0])
            return joueur, 1
    return joueur, 0




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
        joueur.plateau[carte] = joueur.plateau[carte] + int(carte.valeur)
    else:
        joueur.plateau[carte] = int(carte.valeur)
    return joueur