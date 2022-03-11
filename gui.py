from tkinter import *
from random import random
import random
from time import sleep

window = Tk()

window.title("BlackJack")
window.geometry('500x500')
window.configure(bg='black')

### Modules de traitement de texte
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

### Action de tirer une carte
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
  global ytextjoueur
  ytextjoueur += 30

  textupdatejoueur = "Vous venez de tirer :", main1num, nomcarte(main1signe), "| Votre main :", mainjoueurtext(mainjoueur), "| Score : ", scorejoueur
  textupdatejoueur = str(main1num) + " " + str(nomcarte(main1signe))

  global updatetextjoueur, updatetextjoueurstate
  updatetextjoueur = Label(window, text=textupdatejoueur, font=("Arial Bold", 15))
  updatetextjoueur.config(background="black", foreground="#ffffff")
  updatetextjoueur.place(x=455, y=(70+ytextjoueur), anchor="e")
  updatetextjoueurstate = True
  
  if scorejoueur == 21:
      winning = True
      replay(winning)
  elif scorejoueur > 21:
      winning = False
      replay(winning)

### Action du croupier, s'active lorsque le joueur RESTE
def croupier():
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

  global ytextcroup, updatetextcroupier, updatetextcroupierstate
  ytextcroup = ytextcroup + 30

  textupdatecroupier = "Le croupier vient de tirer :", main1num, nomcarte(main1signe), "| Sa main :", maincroupiertext(maincroupier), "| Score : ", scorecroupier
  textupdatecroupier = str(main1num) + " " + str(nomcarte(main1signe))

  updatetextcroupier = Label(window, text=textupdatecroupier, font=("Arial Bold", 15))
  updatetextcroupier.config(background="black", foreground="#ffffff")
  updatetextcroupier.place(x=5, y=(70+ytextcroup), anchor="w")
  updatetextcroupierstate = True

  #PUTAIN CA FAIT 12 JOURS QUE JE GALERE FALLAIT JUSTE RAJOUTER CETTE LIGNE
  Tk.update(updatetextcroupier)
  #JOELKGHJNALG/ZJAHKLZJANKLZAJHKZLM

  sleep(0.8)

  if scorecroupier <= scorejoueur:
    croupier()
  elif scorecroupier > 21:
    sleep(2)
    winning = True
    replay(winning)
  else:
    sleep(2)
    winning = False
    replay(winning)

# Mise en place des éléments du jeu S'ACTIVE QUAND CLIQUE SUR JOUER
def start():
  for widget in window.winfo_children():
    widget.destroy()
  global tirerbtn, resterbtn, croupierguitext, joueurguitext, ytextcroup, ytextjoueur
  ytextcroup = 0
  ytextjoueur = 0

  tirerbtn = Button(window, text="Tirer", bg="black", fg="#ffffff", height = 2, width = 10, font=("Arial Bold", 20), command=tirer)
  tirerbtn.place(x=150, y=350, anchor="center")

  resterbtn = Button(window, text="Rester", bg="black", fg="#ffffff", height = 2, width = 10, font=("Arial Bold", 20), command=croupier)
  resterbtn.place(x=350, y=350, anchor="center")

  croupierguitext = Label(window, text="Main Croupier :", font=("Arial Bold", 20))
  croupierguitext.config(background="black", foreground="#ffffff")
  croupierguitext.place(x=100, y=75, anchor="center")

  joueurguitext = Label(window, text="Main Joueur :", font=("Arial Bold", 20))
  joueurguitext.config(background="black", foreground="#ffffff")
  joueurguitext.place(x=405, y=75, anchor="center")

### S'active lors de la fin de jeu
def replay(winning):
  global winningtext
  for widget in window.winfo_children():
    widget.destroy()
  
  refresh()

  if winning == True:
    winningtext = "Vous avez gagné !"
  else:
    winningtext = "Vous avez perdu !"

  lbl = Label(window, text="Blackjack", font=("Arial Bold", 25))
  lbl.config(background="black", foreground="#ffffff")
  lbl.place(x=250, y=25, anchor="center")

  lbl2 = Label(window, text=winningtext, font=("Arial Bold", 25))
  lbl2.config(background="black", foreground="#ffffff")
  lbl2.place(x=250, y=125, anchor="center")

  global playbtn
  playbtn = Button(window, text="Rejouer", bg="black", fg="#ffffff", height = 2, width = 10, font=("Arial Bold", 20), command=start)
  playbtn.place(x=250, y=250, anchor="center")

### REFRESH DES VARIABLES
def refresh():
  global paquet, mainjoueur, maincroupier, scorejoueur, scorecroupier, textmainjoueur, textmaincroupier, ytextcroup, ytextjoueur, updatetextjoueurstate, updatetextcroupierstate
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
  ytextcroup = 0
  ytextjoueur = 0
  updatetextjoueurstate = False
  updatetextcroupierstate = False

### Menu d'introduction lors du démarrage de l'application

def intro():  
  refresh()

  lbl = Label(window, text="Blackjack", font=("Arial Bold", 25))
  lbl.config(background="black", foreground="#ffffff")
  lbl.place(x=250, y=25, anchor="center")

  global playbtn
  playbtn = Button(window, text="Jouer", bg="black", fg="#ffffff", height = 2, width = 10, font=("Arial Bold", 20), command=start)
  playbtn.place(x=250, y=250, anchor="center")

intro()

window.mainloop()