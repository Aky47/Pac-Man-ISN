#CrÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©e Par Constant Dassonville pour le projet ISN : Pac-Man
from tkinter import *
from PIL import *
from random import *
#Creation des fonctions

def haut(evenement):
    global x_joueur ,y_joueur ,pas_x_joueur ,pas_y_joueur
    pas_y_joueur= -10
    y_joueur = y_joueur + pas_y_joueur
    can.coords(id_img_pacman, x_joueur, y_joueur)
    fen.after(10,haut)

def bas(evenement):
    global x_joueur ,y_joueur ,pas_x_joueur ,pas_y_joueur
    pas_y_joueur = 10
    y_joueur = y_joueur + pas_y_joueur
    can.coords(id_img_pacman, x_joueur, y_joueur)
    fen.after(10,bas)

def gauche(evenement):
    global x_joueur ,y_joueur ,pas_x_joueur ,pas_y_joueur
    pas_x_joueur= -10
    x_joueur = x_joueur + pas_x_joueur
    can.coords(id_img_pacman, x_joueur, y_joueur)
    fen.after(10,gauche)

def droite(evenement):
    global x_joueur ,y_joueur ,pas_x_joueur ,pas_y_joueur
    pas_x_joueur= 10
    x_joueur = x_joueur + pas_x_joueur
    can.coords(id_img_pacman, x_joueur, y_joueur)
    fen.after(10,droite)

"""creation des ia"""
def ia1():
    global x_ia1, y_ia1, pas_x_ia1, pas_y_ia1, x_joueur, y_joueur
    a=randrange(0,10,1)
    if x_joueur < 512:
        if x_ia1 > 512:
            if a > 1:
                pas_x_ia1 = -10
            if a > 9:
                pas_x_ia1 = 10
        if x_ia1 < 512:
            if x_joueur-x_ia1 > 0:
                if a > 2:
                    pas_x_ia1 = 10
                if a > 8:
                    pas_x_ia1 = -10
            if x_ia1-x_joueur > 0:
                if a > 2:
                    pas_x_ia1 = -10
                if a > 8:
                    pas_x_ia1 = 10
    x_ia1 = x_ia1 + pas_x_ia1
    can.coords(id_img_fantome1,x_ia1,y_ia1)
    if x_joueur > 512:
        if x_ia1 < 512:
            if a > 1:
                pas_x_ia1 = 10
            if a > 9:
                pas_x_ia1 = -10
        if x_ia1 > 512:
            if x_joueur-x_ia1 > 0:
                if a > 2:
                    pas_x_ia1 = 10
                if a > 8:
                    pas_x_ia1 = -10
            if x_ia1-x_joueur > 0:
                if a > 2:
                    pas_x_ia1 = -10
                if a > 8:
                    pas_x_ia1 = 10
    x_ia1 = x_ia1 + pas_x_ia1
    can.coords(id_img_fantome1,x_ia1,y_ia1)
    if y_joueur < 512:
        if y_ia1 > 512:
            if a > 1:
                pas_y_ia1 = -10
            if a > 9:
                pas_y_ia1 = 10
        if y_ia1 < 512:
            if y_joueur-y_ia1 > 0:
                if a > 2:
                    pas_y_ia1 = 10
                if a > 8:
                    pas_y_ia1 = -10
            if y_ia1-y_joueur > 0:
                if a > 2:
                    pas_y_ia1 = -10
                if a > 8:
                    pas_y_ia1 = 10
    y_ia1 = y_ia1 + pas_y_ia1
    can.coords(id_img_fantome1,x_ia1,y_ia1)
    if y_joueur > 512:
        if y_ia1 < 512:
            if a > 1:
                pas_y_ia1 = 10
            if a > 9:
                pas_y_ia1 = -10
        if y_ia1 > 512:
           if x_joueur-y_ia1 > 0:
                if a > 2:
                    pas_y_ia1 = 10
                if a > 8:
                    pas_y_ia1 = -10
           if y_ia1-y_joueur > 0:
                if a > 2:
                    pas_y_ia1 = -10
                if a > 8:
                    pas_y_ia1 = 10
    y_ia1 = y_ia1 + pas_y_ia1
    can.coords(id_img_fantome1,x_ia1,y_ia1)
    fen.after(150,ia1)

def ia2():
    global x_ia2, y_ia2, pas_x_ia2, pas_y_ia2, x_joueur, y_joueur
    a=randrange(0,10,1)
    if x_joueur < 512:
        if x_ia2 > 512:
            if a > 1:
                pas_x_ia2 = -10
            if a > 9:
                pas_x_ia2 = 10
        if x_ia2 < 512:
            if x_joueur-x_ia2 > 0:
                if a > 2:
                    pas_x_ia2 = 10
                if a > 8:
                    pas_x_ia2 = -10
            if x_ia1-x_joueur > 0:
                if a > 2:
                    pas_x_ia2 = -10
                if a > 8:
                    pas_x_ia2 = 10
    x_ia2 = x_ia2 + pas_x_ia2
    can.coords(id_img_fantome2,x_ia2,y_ia2)
    if x_joueur > 512:
        if x_ia2 < 512:
            if a > 1:
                pas_x_ia2 = 10
            if a > 9:
                pas_x_ia2 = -10
        if x_ia2 > 512:
            if x_joueur-x_ia2 > 0:
                if a > 2:
                    pas_x_ia2 = 10
                if a > 8:
                    pas_x_ia2 = -10
            if x_ia2-x_joueur > 0:
                if a > 2:
                    pas_x_ia2 = -10
                if a > 8:
                    pas_x_ia2 = 10
    x_ia2 = x_ia2 + pas_x_ia2
    can.coords(id_img_fantome2,x_ia2,y_ia2)
    if y_joueur < 512:
        if y_ia2 > 512:
            if a > 1:
                pas_y_ia2 = -10
            if a > 9:
                pas_y_ia2 = 10
        if y_ia2 < 512:
            if y_joueur-y_ia2 > 0:
                if a > 2:
                    pas_y_ia2 = 10
                if a > 8:
                    pas_y_ia2 = -10
            if y_ia2-y_joueur > 0:
                if a > 2:
                    pas_y_ia1 = -10
                if a > 8:
                    pas_y_ia2 = 10
    y_ia2 = y_ia2 + pas_y_ia2
    can.coords(id_img_fantome2,x_ia2,y_ia2)
    if y_joueur > 512:
        if y_ia2 < 512:
            if a > 1:
                pas_y_ia2 = 10
            if a > 9:
                pas_y_ia2 = -10
        if y_ia2 > 512:
           if x_joueur-y_ia2 > 0:
                if a > 2:
                    pas_y_ia2 = 10
                if a > 8:
                    pas_y_ia2 = -10
           if y_ia2-y_joueur > 0:
                if a > 2:
                    pas_y_ia2 = -10
                if a > 8:
                    pas_y_ia2 = 10
    y_ia2 = y_ia2 + pas_y_ia2
    can.coords(id_img_fantome2,x_ia2,y_ia2)
    fen.after(150,ia2)

def ia3():
    global x_ia3, y_ia3, pas_x_ia3, pas_y_ia3, x_joueur, y_joueur
    a=randrange(0,10,1)
    if x_joueur < 512:
        if x_ia3 > 512:
            if a > 1:
                pas_x_ia3 = -10
            if a > 9:
                pas_x_ia3 = 10
        if x_ia3 < 512:
            if x_joueur-x_ia3 > 0:
                if a > 2:
                    pas_x_ia3 = 10
                if a > 8:
                    pas_x_ia3 = -10
            if x_ia3-x_joueur > 0:
                if a > 2:
                    pas_x_ia3 = -10
                if a > 8:
                    pas_x_ia3 = 10
    x_ia3 = x_ia3 + pas_x_ia3
    can.coords(id_img_fantome3,x_ia3,y_ia3)
    if x_joueur > 512:
        if x_ia3 < 512:
            if a > 1:
                pas_x_ia3 = 10
            if a > 9:
                pas_x_ia3 = -10
        if x_ia3 > 512:
            if x_joueur-x_ia3 > 0:
                if a > 2:
                    pas_x_ia3 = 10
                if a > 8:
                    pas_x_ia3 = -10
            if x_ia3-x_joueur > 0:
                if a > 2:
                    pas_x_ia3 = -10
                if a > 8:
                    pas_x_ia3 = 10
    x_ia3 = x_ia3 + pas_x_ia3
    can.coords(id_img_fantome3,x_ia3,y_ia3)
    if y_joueur < 512:
        if y_ia3 > 512:
            if a > 1:
                pas_y_ia3 = -10
            if a > 9:
                pas_y_ia3 = 10
        if y_ia3 < 512:
            if y_joueur-y_ia3 > 0:
                if a > 2:
                    pas_y_ia3 = 10
                if a > 8:
                    pas_y_ia3 = -10
            if y_ia3-y_joueur > 0:
                if a > 2:
                    pas_y_ia3 = -10
                if a > 8:
                    pas_y_ia3 = 10
    y_ia3 = y_ia3 + pas_y_ia3
    can.coords(id_img_fantome3,x_ia3,y_ia3)
    if y_joueur > 512:
        if y_ia3 < 512:
            if a > 1:
                pas_y_ia3 = 10
            if a > 9:
                pas_y_ia3 = -10
        if y_ia3 > 512:
           if x_joueur-y_ia3 > 0:
                if a > 2:
                    pas_y_ia3 = 10
                if a > 8:
                    pas_y_ia3 = -10
           if y_ia3-y_joueur > 0:
                if a > 2:
                    pas_y_ia3 = -10
                if a > 8:
                    pas_y_ia3 = 10
    y_ia3 = y_ia3 + pas_y_ia3
    can.coords(id_img_fantome3,x_ia3,y_ia3)
    fen.after(150,ia3)

def ia4():
    global x_ia4, y_ia4, pas_x_ia4, pas_y_ia4, x_joueur, y_joueur
    a=randrange(0,10,1)
    if x_joueur < 512:
        if x_ia4 > 512:
            if a > 1:
                pas_x_ia4 = -10
            if a > 9:
                pas_x_ia4 = 10
        if x_ia4 < 512:
            if x_joueur-x_ia4 > 0:
                if a > 2:
                    pas_x_ia4 = 10
                if a > 8:
                    pas_x_ia4 = -10
            if x_ia4-x_joueur > 0:
                if a > 2:
                    pas_x_ia4 = -10
                if a > 8:
                    pas_x_ia4 = 10
    x_ia4 = x_ia4 + pas_x_ia4
    can.coords(id_img_fantome4,x_ia4,y_ia4)
    if x_joueur > 512:
        if x_ia4 < 512:
            if a > 1:
                pas_x_ia4 = 10
            if a > 9:
                pas_x_ia4 = -10
        if x_ia4 > 512:
            if x_joueur-x_ia4 > 0:
                if a > 2:
                    pas_x_ia4 = 10
                if a > 8:
                    pas_x_ia4 = -10
            if x_ia4-x_joueur > 0:
                if a > 2:
                    pas_x_ia4 = -10
                if a > 8:
                    pas_x_ia4 = 10
    x_ia4 = x_ia4 + pas_x_ia4
    can.coords(id_img_fantome4,x_ia4,y_ia4)
    if y_joueur < 512:
        if y_ia4 > 512:
            if a > 1:
                pas_y_ia4 = -10
            if a > 9:
                pas_y_ia4 = 10
        if y_ia4 < 512:
            if y_joueur-y_ia4 > 0:
                if a > 2:
                    pas_y_ia4 = 10
                if a > 8:
                    pas_y_ia4 = -10
            if y_ia4-y_joueur > 0:
                if a > 2:
                    pas_y_ia4 = -10
                if a > 8:
                    pas_y_ia4 = 10
    y_ia4 = y_ia4 + pas_y_ia4
    can.coords(id_img_fantome4,x_ia4,y_ia4)
    if y_joueur > 512:
        if y_ia4 < 512:
            if a > 1:
                pas_y_ia4 = 10
            if a > 9:
                pas_y_ia4 = -10
        if y_ia4 > 512:
           if x_joueur-y_ia4 > 0:
                if a > 2:
                    pas_y_ia4 = 10
                if a > 8:
                    pas_y_ia4 = -10
           if y_ia4-y_joueur > 0:
                if a > 2:
                    pas_y_ia4 = -10
                if a > 8:
                    pas_y_ia4 = 10
    y_ia4 = y_ia4 + pas_y_ia4
    can.coords(id_img_fantome4,x_ia4,y_ia4)
    fen.after(150,ia4)

y_joueur = 50
x_joueur = 50
pas_y_joueur = 0
pas_x_joueur = 0

x_ia1 = 15
y_ia1 = 15
pas_x_ia1 = 0
pas_y_ia1 = 0

x_ia2 = 75
y_ia2 = 75
pas_x_ia2 = 0
pas_y_ia2 = 0

x_ia3 = 125
y_ia3 = 125
pas_x_ia3 = 0
pas_y_ia3 = 0

x_ia4 = 175
y_ia4 = 175
pas_x_ia4 = 0
pas_y_ia4 = 0


"""---creation du widget principal ("maitre")---"""
fen=Tk()
fen.title("Pac-Man")

"""---creation des widgets "esclaves"---"""
#creation des Canvas

can1=Canvas(fen, bg='green', height=1024, width=275)
can1.pack(side=LEFT, padx=5, pady=5)

can=Canvas(fen, bg='black', height=1024, width=1024)
can.pack(side=LEFT, padx=5, pady=5)
can.focus_set()

can2=Canvas(fen, bg='red', height=1024, width=275)
can2.pack(side=LEFT, padx=5, pady=5)

#importation des images pacman

img_pacman = PhotoImage(file='pacman.png')
id_img_pacman = can.create_image(x_joueur , y_joueur , image=img_pacman)

img_fantome1 = PhotoImage(file='pacman 1.png')
id_img_fantome1 = can.create_image(x_ia1 , y_ia1 , image=img_fantome1)

img_fantome2 = PhotoImage(file='pacman 2.png')
id_img_fantome2 = can.create_image(x_ia2 , y_ia2 , image=img_fantome2)

img_fantome3 = PhotoImage(file='pacman 3.png')
id_img_fantome3 = can.create_image(x_ia3 , y_ia3 , image=img_fantome3)

img_fantome4 = PhotoImage(file='pacman 4.png')
id_img_fantome4 = can.create_image(x_ia4 , y_ia4 , image=img_fantome4)

"""On appelle les commandes soit par des boutons, soit en continue"""
can.bind('<Up>',haut)
can.pack()

can.bind('<Down>',bas)
can.pack()

can.bind('<Left>',gauche)
can.pack()

can.bind('<Right>',droite)
can.pack()

ia1()
ia2()
ia3()
ia4()
fen.mainloop()

