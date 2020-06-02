def open_fichier(chemin):
    fichier = open(chemin, "r")
    contenu = fichier.read()
    tableau = []
    ligne = ""
    for i in contenu:
        if i != "\n":
            ligne = ligne + i
        else:
            tableau.append(ligne)
            ligne = ""
    fichier.close()
    return tableau
    

