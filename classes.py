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

    def __init__(self, c_nom,c_type, c_cout, c_effet, c_cible, c_valeur, c_pdv, c_rarete,c_description, c_previous=0, c_next=0, c_head=0):
        self.id_carte = Carte.id_carte
        self.nom = c_nom
        self.type = c_type
        self.cout = c_cout
        self.effet = c_effet
        self.cible = c_cible
        self.valeur = c_valeur
        self.rarete = c_rarete
        self.pdv = c_pdv
        self.pdv_max = c_pdv
        self.description = c_description
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
        return "nom : "+ self.nom + "cout :"+ self.cout + "effet :"+ self.effet + "cible :"+ self.cible +"valeur :" + self.valeur + "pdv :"+ self.pdv + "previous :" + self.previous.nom + "next :"+ self.next.nom + "head :"+ self.head.nom
                

class Deck:
    def __init__(self, nom):
        self.nom = nom
        self.cartes = []

class Joueur:
    """Classe définissant un joueur caractérisé par :
    - son pseudo
    - sa vie
    - son bouclier
    - La valeur d'armée
    - son deck 
    - sa main
    - ses ressources """

    def __init__(self, j_pseudo, j_vie, j_bouclier,j_deck):
        self.pseudo = j_pseudo
        self.vie = j_vie
        self.bouclier = j_bouclier
        self.valeur = 0
        self.deck = j_deck
        self.main = []
        self.plateau = {}
        self.ressource = {"A" : 0, "B" : 0, "N" : 0}
    
    def __str__(self):
        """Méthode permettant d'afficher notre objet"""
        return "pseudo : {}, vie : {}, bouclier : {}".format(
                self.pseudo, self.vie, self.bouclier)
    
    def recherche_p(self, carte):
        for i in self.plateau:
            if (i == carte):
                return i
        return 0

class data_jeu:
    def __init__(self,d_joueur0, d_joueur1, d_tour = 0):
        self.joueur0 = d_joueur0
        self.joueur1 = d_joueur1
        self.tour = d_tour

