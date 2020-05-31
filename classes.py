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

    def __init__(self, c_nom,c_type, c_cout, c_effet=0, c_cible=0, c_valeur=0,c_pdv=0, c_previous=0, c_next=0, c_head=0):
        self.id_carte = Carte.id_carte
        self.nom = c_nom
        self.type = c_type
        self.cout = c_cout
        self.effet = c_effet
        self.cible = c_cible
        self.valeur = c_valeur
        self.pdv = c_pdv
        self.previous = c_previous
        self.next = c_next
        self.head = c_head

        Carte.id_carte += 1
    
    def index(self,id_carte):
        i = 0
        while (i < id_carte):
            carte = self.next
        return carte

    def afficher(self):
        """Méthode permettant d'afficher notre objet"""
        return "nom : ",self.nom, "cout :", self.cout, "effet :", self.effet, "cible :", self.cible,
        "valeur :", self.valeur, "pdv :", self.pdv, "previous :", self.previous.nom, "next :", self.next.nom, "head :", self.head.nom
                

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


