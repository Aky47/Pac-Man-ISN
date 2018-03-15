#CrÃ©e Par Constant Dassonville pour le projet ISN : Pac-Man
from tkinter import *
from PIL import *
#Creation des fonctions

def haut(evenement):
    global x ,y ,pas_x ,pas_y
    pas_y= -10
    y = y + pas_y
    can.coords(id_img_pacman, x, y)
    img_pacman.rotate(90, filter=NEAREST, expand=1)
    fen.after(10,haut)

def bas(evenement):
    global x ,y ,pas_x ,pas_y
    pas_y= 10
    y = y + pas_y
    can.coords(id_img_pacman, x, y)
    fen.after(10,bas)

def gauche(evenement):
    global x ,y ,pas_x ,pas_y
    pas_x= -10
    x = x + pas_x
    can.coords(id_img_pacman, x, y)
    fen.after(10,gauche)

def droite(evenement):
    global x ,y ,pas_x ,pas_y
    pas_x= 10
    x = x + pas_x
    can.coords(id_img_pacman, x, y)
    fen.after(10,droite)








y = 50
x = 50
pas_y = 0
pas_x = 0


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

#importation de l'image pacman
img_pacman = PhotoImage(file='pacman.png')
id_img_pacman = can.create_image(x , y , image=img_pacman)

can.bind('<Up>',haut)
can.pack()

can.bind('<Down>',bas)
can.pack()

can.bind('<Left>',gauche)
can.pack()

can.bind('<Right>',droite)
can.pack()

fen.mainloop()

