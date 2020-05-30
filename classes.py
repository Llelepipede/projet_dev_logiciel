class Carte:
    """Classe définissant une carte caractérisé par :
    - son nom
    - son coût
    - ses ressources
    - son effet
    - sa cible
    - sa valeur
    - se la précédente carte du deck 
    - se la prochaine carte du deck """
    id_carte = 0

    def __init__(self, c_nom, c_cout, c_ressource, c_effet, c_cible, c_valeur=0, c_previous=0, c_next=0):
        self.id_carte = Carte.id_carte
        self.nom = c_nom
        self.cout = c_cout
        self.effet = c_effet
        self.valeur = c_valeur
        self.ressource = c_ressource
        self.cible = c_cible
        self.previous = c_previous
        self.next = c_next

        Carte.id_carte += 1
    
    def index(self,id_carte):
        i = 0
        while (i < id_carte):
            carte = self.next
        return carte

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_ressource(self):
        return self.ressource

    def set_ressource(self, new_ressource):
        self.ressource = new_ressource

    def get_cout(self):
        return self.cout

    def set_cout(self, new_cout):
        self.cost = new_cout

    def get_effet(self):
        return self.effet

    def set_effect(self, new_effet):
        self.effet = new_effet

    def get_valeur(self):
        return self.valeur

    def set_valeur(self, new_valeur):
        self.valeur = new_valeur

    def get_cible(self):
        return self.cible

    def set_cible(self, new_cible):
        self.target = new_cible

    def get_rarete(self):
        return self.rarete

    def set_rarete(self, new_rarete):
        self.rarete = new_rarete

    def get_description(self):
        return self.description

    def set_description(self, new_description):
        self.description = new_description

class Deck:
    def __init__(self, name):
        self.name = name
        self.cartes = []

    def reset_deck(self):
        self.cartes = []

    def add_card_to_deck(self, Carte):
        self.cartes.append(Carte)

    def get_cards_from_deck(self):
        return self.cartes

    def del_card_from_deck(self, Carte):
        self.cartes.remove(Carte)

    def get_nb_cards_in_deck(self):
        return len(self.cartes)

class Card:
    def __init__(self, name, ressource_type, cost, effect, value, target, rarity, description):
        self.name = name
        self.ressource_type = ressource_type
        self.cost = cost
        self.effect = effect
        self.value = value
        self.target = target
        self.rarity = rarity
        self.description = description

    
class Joueur:
    """Classe définissant un joueur caractérisé par :
    - son pseudo
    - sa vie
    - son bouclier
    - attaque = à la valeur d'armée
    - son deck 
    - sa main
    - sa defausse
    - ses ressources 
    - son etat"""

    def __init__(self, j_pseudo, j_vie, j_bouclier,j_deck,j_main=0,j_defausse=0,j_ressource=0,j_etat=0):
        self.pseudo = j_pseudo
        self.vie = j_vie
        self.bouclier = j_bouclier
        self.deck = j_deck
        self.main = j_main
        self.plateau = {}
        self.defausse = j_defausse
        self.ressource = j_ressource
        self.etat = j_etat
    
    def __str__(self):
        """Méthode permettant d'afficher notre objet"""
        return "pseudo : {}, vie : {}, bouclier : {}".format(
                self.pseudo, self.vie, self.bouclier)
    
    def recherche_p(self, carte):
        for i in self.plateau:
            if (i == carte):
                return i
        return 0


