from random import random
import random
from time import sleep

def CESOIRCESTMATCH():
    choix = input("Souhaitez vous faire une partie ? (oui/non) : ")
    if choix == "oui":
        reset()
        tirer()
        croupier()
    else:
        print("Ok bye")
        quit()

def reset():
    global paquet, mainjoueur, maincroupier, scorejoueur, scorecroupier, textmainjoueur, textmaincroupier
    paquet = [
        ('co', 1), ('co', 2), ('co', 3), ('co', 4), ('co', 5), ('co', 6), ('co', 7), ('co', 8), ('co', 9), ('co', 10),
        ('ca', 1), ('ca', 2), ('ca', 3), ('ca', 4), ('ca', 5), ('ca', 6), ('ca', 7), ('ca', 8), ('ca', 9), ('ca', 10), 
        ('pi', 1), ('pi', 2), ('pi', 3), ('pi', 4), ('pi', 5), ('pi', 6), ('pi', 7), ('pi', 8), ('pi', 9), ('pi', 10), 
        ('tr', 1), ('tr', 2), ('tr', 3), ('tr', 4), ('tr', 5), ('tr', 6), ('tr', 7), ('tr', 8), ('tr', 9), ('tr', 10),
        ('roi', 10), ('dame', 10), ('valet', 10), ('as', 11), ('as', 1),  ('as', 1), ('as', 1)
    ]
    mainjoueur = []
    maincroupier = []
    scorejoueur = 0
    scorecroupier = 0
    textmainjoueur = []
    textmaincroupier = []

def nomcarte(carte):
    if carte == 'co':
        return("de Coeur")
    elif carte == 'ca':
        return("de Carreaux")
    elif carte == 'pi':
        return("de Pique")
    elif carte == 'tr':
        return("de Trefle")
    elif carte == 'roi':
        return("de Roi")
    elif carte == 'dame':
        return("de Dame")
    elif carte == 'valet':
        return("de Valet")
    elif carte == 'as':
        return("d'As")
    else:
        print("bug")

def mainjoueurtext(main):
    main = main[-1]
    a, b = main
    signe = nomcarte(a)
    numero = b
    signe = str(signe)
    numero = str(numero)
    final = numero + " " + signe
    textmainjoueur.append(final)
    return(', '.join(textmainjoueur))

def maincroupiertext(main):
    main = main[-1]
    a, b = main
    signe = nomcarte(a)
    numero = b
    signe = str(signe)
    numero = str(numero)
    final = numero + " " + signe
    textmaincroupier.append(final)
    return(', '.join(textmaincroupier))


def tirer():
    main1 = random.choice(paquet)

    main1index = paquet.index(main1)
    paquet.pop(main1index)

    mainjoueur.append(main1)

    lastmainjoueur = mainjoueur[-1]
    a, b = lastmainjoueur
    global scorejoueur
    if b == 11:
        if (scorejoueur + 11) > 21:
            b = 1
    scorejoueur += b

    a, b = main1
    main1signe = a
    main1num = b

    print("Vous venez de tirer :", main1num, nomcarte(main1signe), "| Votre main :", mainjoueurtext(mainjoueur), "| Score : ", scorejoueur)
    if scorejoueur == 21:
        print("Blackjack ! Vous gagnez")
        CESOIRCESTMATCH()
    elif scorejoueur > 21:
        print("Burst ! Vous perdez")
        CESOIRCESTMATCH()
    
    choice = input("Souhaitez-vous tirer ou rester ? : ")
    if choice == "tirer":
        tirer()

def croupier():

    sleep(1)

    main1 = random.choice(paquet)

    main1index = paquet.index(main1)
    paquet.pop(main1index)

    maincroupier.append(main1)

    lastmaincroupier = maincroupier[-1]
    a, b = lastmaincroupier
    global scorecroupier
    if b == 100:
        if (scorecroupier + 11) > 21:
            b = 1
    scorecroupier += b

    a, b = main1
    main1signe = a
    main1num = b

    print("Le croupier vient de tirer :", main1num, nomcarte(main1signe), "| Sa main :", maincroupiertext(maincroupier), "| Score : ", scorecroupier)

    if scorecroupier <= scorejoueur:
        croupier()
    elif scorecroupier > 21:
        print("Croupier Burst, vous gagnez")
        CESOIRCESTMATCH()
    else:
        print("Croupier Gagne, vous perdez")
        CESOIRCESTMATCH()

CESOIRCESTMATCH()