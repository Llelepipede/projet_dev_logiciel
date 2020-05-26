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

    def __init__(self, c_name, c_cost, c_ressource, c_effect, c_target, c_value=0, c_previous=0, c_next=0):
        self.id_carte = Carte.id_carte
        self.name = c_name
        self.cost = c_cost
        self.effect = c_effect
        self.value = c_value
        self.target = c_target
        self.previous = c_previous
        self.next = c_next

        Carte.id_carte += 1
    
    def index(self,id_carte):
        i = 0
        while (i < id_carte):
            carte = self.next
        return carte
class Joueur:
    """Classe définissant un joueur caractérisé par :
    - son pseudo
    - sa vie
    - son bouclier
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
        self.defausse = j_defausse
        self.ressource = j_ressource
        self.etat = j_etat
    
    def __str__(self):
        """Méthode permettant d'afficher notre objet"""
        return "pseudo : {}, vie : {}, bouclier : {}".format(
                self.pseudo, self.vie, self.bouclier)



