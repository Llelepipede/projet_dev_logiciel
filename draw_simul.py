import pygame


class carte:

    id_carte = 0

    def __init__(self, c_name, c_previous=0, c_next=0):
        self.id_carte = carte.id_carte
        self.name = c_name

        self.previous = c_previous
        self.next = c_next

        carte.id_carte += 1

def draw(deck, main):
    if deck and len(main)< 7:
        main.append(deck.id_carte)
        return deck.next,main

def print_hand(main):
    for k in main:
        print(k)





def sizeof_deck(deck):
    actual = deck
    compt = 0
    while actual:
        actual = actual.next
        compt+=1
    return compt



def simul_game():
    deck = carte("\"carte de base\"")
    actual = deck
    for k in range(9):
        actual.next = carte("\"carte de base\"")
        actual.next.previous = actual
        actual = actual.next

    main = []
    while len(main)<7:
        print("pioche ! \n")
        draw_value = draw(deck,main)

        deck = draw_value[0]
        main = draw_value[1]
        print(main)
        print(sizeof_deck(deck))

simul_game()