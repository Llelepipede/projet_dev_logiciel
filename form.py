import pygame



def zonetext(fenetre,xa,ya,xb,yb):
    pygame.draw.rect(fenetre,(0,0,0),[xa-3,ya-3,xb+6,yb+6])
    pygame.draw.rect(fenetre,(255,255,255),[xa,ya,xb,yb])

def jeu_zone(fenetre,xa,ya,xb,yb,color):
    pygame.draw.rect(fenetre,(30,30,30),[xa-10,ya-10,xb+20,yb+20])
    pygame.draw.rect(fenetre,(100,100,100),[xa-8,ya-8,xb+16,yb+16])
    pygame.draw.rect(fenetre,(30,30,30),[xa-2,ya-2,xb+4,yb+4])
    pygame.draw.rect(fenetre,color,[xa,ya,xb,yb])

def message_display(fenetre,text,taille,color,x,y):
    R=255
    G=255
    B=255
    font = pygame.font.Font('freesansbold.ttf', taille)
    fenetre.blit(font.render(text, True, color), (x,y))

def menu_form(fenetre,message=[]):

    size_x = 320
    size_y = 55
    start_x = 440
    start_y = 710 - (len(message)*65)
    decalage_y = size_y + 50

    color = (0,0,0)

    taille_text = 30
    for text in message :
        size = len(text)
        decalage_x = 140 - ((size-1)*6 )
        zonetext(fenetre,start_x,start_y,size_x,size_y)
        message_display(fenetre,text,taille_text,color,start_x + decalage_x,start_y+10)
        start_y += decalage_y


def jeu_form(fenetre, choix):
    #le fond gris
    pygame.draw.rect(fenetre,(150,150,150),[0,0,2000,2000])

    #la zone en bas avec les choix
    jeu_zone(fenetre,11,720,1208,349,(130,130,130))

    #les portraits
    jeu_zone(fenetre,21,350,500,331,(60,60,60))
    jeu_zone(fenetre,709,21,500,331,(60,60,60))

    #les cases des choix
    jeu_zone(fenetre,90,800,270,40,(130,130,130)) # main
    jeu_zone(fenetre,490,980,270,40,(130,130,130)) # plateau
    jeu_zone(fenetre,490,800,270,40,(130,130,130)) # option
    jeu_zone(fenetre,90,980,270,40,(130,130,130)) # defausser
    jeu_zone(fenetre,890,800,270,40,(130,130,130)) # se rendre
    jeu_zone(fenetre,890,980,270,40,(130,130,130)) # fin de tour




    #le carré de selection
    if choix == 0:
        jeu_zone(fenetre,35,810,20,20,(30,30,30))
    elif choix == 1:
        jeu_zone(fenetre,435,810,20,20,(30,30,30))
    elif choix == 2:
        jeu_zone(fenetre,835,810,20,20,(30,30,30))
    elif choix == 3:
        jeu_zone(fenetre,35,990,20,20,(30,30,30))
    elif choix == 4:
        jeu_zone(fenetre,435,990,20,20,(30,30,30))
    elif choix == 5:
        jeu_zone(fenetre,835,990,20,20,(30,30,30))


def jeu_form_text(fenetre):
    message_display(fenetre,"main",40,(0,0,0),100,800)
    message_display(fenetre,"plateau",40,(0,0,0),500,800)
    message_display(fenetre,"option",40,(0,0,0),900,800)
    message_display(fenetre,"defausser",40,(0,0,0),100,980)
    message_display(fenetre,"se rendre",40,(0,0,0),500,980)
    message_display(fenetre,"fin de tour",40,(0,0,0),900,980)

def quit_menu_form(fenetre,message=[]):

    jeu_zone(fenetre,325,200,650,650,(180,180,180))

    size_x = 320
    size_y = 55
    start_x = 490
    start_y = 600 - (len(message)*65)
    decalage_y = size_y + 50

    color = (0,0,0)



    taille_text = 30
    for text in message :
        size = len(text)
        decalage_x = 140 - ((size-1)*6 )
        zonetext(fenetre,start_x,start_y,size_x,size_y)
        message_display(fenetre,text,taille_text,color,start_x + decalage_x,start_y+10)
        start_y += decalage_y



def voir_main_form(fenetre,choix):
    #le fond gris
    pygame.draw.rect(fenetre,(150,150,150),[0,0,2000,2000])

    for k in range(0,7):

        jeu_zone(fenetre,11,11+(k*154),1208,131,(100,100,100))
        if k == choix:
            jeu_zone(fenetre,35,90+(k*154),20,20,(30,30,30))




def voir_main_form_data(fenetre,data):

    i = 0
    joueur = data.joueur0 if data.tour % 2 == 0 else data.joueur1
    size_of_text = 25
    for carte in joueur.main:

        message_display(fenetre,"nom: " + str(carte.nom),size_of_text,(0,0,0),17,15+(i*154))
        message_display(fenetre,"cout: " + str(carte.cout),size_of_text,(0,0,0),327,15+(i*154))
        message_display(fenetre,"type: " + str(type_convert(carte.type)),size_of_text,(0,0,0),17,45+(i*154))
        message_display(fenetre,"description: ",size_of_text,(0,0,0),517,15+(i*154))
        message_display(fenetre,str(carte.description),size_of_text,(0,0,0),517,45+(i*154))

        i += 1


def voir_plateau_form(fenetre):
    #le fond gris
    pygame.draw.rect(fenetre,(150,150,150),[0,0,2000,2000])

    for k in range(0,7):
        jeu_zone(fenetre,11,11+(k*154),1208,131,(100,100,100))

def voir_plateau_form_data(fenetre,data):

    i = 0
    joueur = data.joueur0 if data.tour % 2 == 0 else data.joueur1
    size_of_text = 25
    for carte in joueur.plateau:

        message_display(fenetre,"nom: " + str(carte.nom),size_of_text,(0,0,0),17,15+(i*154))
        message_display(fenetre,"valeur d'armée': " + str(joueur.plateau[carte]),size_of_text,(0,0,0),17,45+(i*154))
        i += 1


def type_convert(var):
    return "unitée" if var == "U" else("sort" if var == "S" else ("fournisseur" if var == "F" else("unitée naine" if var == "UN" else ("unitée elfe"))))



def jeu_form_data(fenetre,data):
    if data.tour % 2 == 0:
        joueur = data.joueur0
        advers = data.joueur1
    else:
        joueur = data.joueur1
        advers = data.joueur0


    message_display(fenetre,joueur.pseudo,40,(0,0,0),30,370)
    message_display(fenetre,"vie: "+str(joueur.vie),40,(0,0,0),30,420)
    message_display(fenetre,"bouclier: "+str(joueur.bouclier),40,(0,0,0),30,470)
    message_display(fenetre,"main: "+str(len(joueur.main))+"/7",40,(0,0,0),30,520)
    message_display(fenetre,"ressource: ",30,(0,0,0),30,610)
    message_display(fenetre,"Acier: "+str(joueur.ressource["A"])+"  Bois: "+str(joueur.ressource["B"])+"  Nouriture: "+str(joueur.ressource["N"]),30,(0,0,0),30,640)
    message_display(fenetre,"valeur d'armée: " + str(joueur.valeur),30,(0,0,0),560,640)

    message_display(fenetre,advers.pseudo,40,(0,0,0),718,41)
    message_display(fenetre,"vie: "+str(advers.vie),40,(0,0,0),718,91)
    message_display(fenetre,"bouclier: "+str(advers.bouclier),40,(0,0,0),718,141)
    message_display(fenetre,"main: "+str(len(advers.main))+"/7",40,(0,0,0),718,191)
    message_display(fenetre,"ressource: ",30,(0,0,0),718,281)
    message_display(fenetre,"Acier: "+str(advers.ressource["A"])+"  Bois: "+str(advers.ressource["B"])+"  Nouriture: "+str(advers.ressource["N"]),30,(0,0,0),718,311)
    message_display(fenetre,"valeur d'armée: " + str(advers.valeur),30,(0,0,0),420,41)



