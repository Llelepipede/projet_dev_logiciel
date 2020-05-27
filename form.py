import pygame



def zonetext(fenetre,xa,ya,xb,yb):
    pygame.draw.rect(fenetre,(0,0,0),[xa-3,ya-3,xb+6,yb+6])
    pygame.draw.rect(fenetre,(255,255,255),[xa,ya,xb,yb])

def message_display(fenetre,text,taille,color,x,y):
    R=255
    G=255
    B=255
    font = pygame.font.Font('freesansbold.ttf', taille)
    fenetre.blit(font.render(text, True, color), (x,y))