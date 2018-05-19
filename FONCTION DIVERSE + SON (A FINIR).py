from tkinter import *
from random import *

import simpleaudio as sa 

#Creation des fonctions

"""
cette fonction sert aux fonctions de déplacement, elle permet de vérifier l'état de
la case adjacente (0,1 ou 2) 
"""
def position():
    global x_joueur ,y_joueur ,pas_x_joueur ,pas_y_joueur, carte
    
    pos_x = (x_joueur-16)//32   # On divise la position actuel du joueur par 32 pour se repérer
    pos_y = (y_joueur-16)//32   # selon un repère de 32cases par 32cases (on -16 car on utilise 
                                # les coordonnées images qui sont décalé de 16px en x et y)


    pos_map = (pos_y)*24+pos_x  # Formule permettant de retrouver l'emplacement actuel dans la liste
                                # " carte[] "

    return pos_map

    """
    Prints de débugage 
    print('(',x_joueur,':',y_joueur,')')
    print(pos_x,' ', pos_y,'    ',pos_map,' ')
    print('Statut',carte[pos_map])
    """

    


def haut(event):
    global x_joueur ,y_joueur ,pas_x_joueur ,pas_y_joueur
    pas_y_joueur = -32
    
    verif = position()        # On appelle la fonction position(), cette fonction donne à quelle endroit
    if carte[verif-24] == 2:  # on se situe selon la liste carte[] , si la case au-dessus (donc -24 car
        print('Collision !')  # c'est une liste) est un 2 alors on fait rien, sinon on peut se déplacer 
    else:                     # au-dessus
        y_joueur = y_joueur + pas_y_joueur
        can.coords(id_img_pacman, x_joueur, y_joueur)

    verif_piece=position()        #On vérifie si le joueur
    if carte[verif_piece] == 1:   #se trouve sur une pièce.
        carte[verif_piece] = 0    #Si c'est le cas, la piece disparait de la liste map[]
        can.delete(dico_terrain['zone'+str(verif_piece)])  #on efface le pièce affichée de la carte
                                                # en s'aidant du dictionnaire dico_terrain{}
        son_piece.play()


    fen.after(10,haut)




def bas(evenement):
    global x_joueur ,y_joueur ,pas_x_joueur ,pas_y_joueur
    pas_y_joueur = 32

    verif = position()        # On appelle la fonction position(), cette fonction donne à quelle endroit
    if carte[verif+24] == 2:  # on se situe selon la liste carte[] , si la case en-dessous (donc +24 car
        print('Collision !')  # c'est une liste) est un 2 alors on fait rien, sinon on peut se déplacer 
    else:                     # en-dessous
        y_joueur = y_joueur + pas_y_joueur
        can.coords(id_img_pacman, x_joueur, y_joueur)

    verif_piece=position()        #On vérifie si le joueur
    if carte[verif_piece] == 1:   #se trouve sur une pièce.
        carte[verif_piece] = 0    #Si c'est le cas, la piece disparait de la liste map[]
        can.delete(dico_terrain['zone'+str(verif_piece)]) #on efface le pièce affichée de la carte
                                                      # en s'aidant du dictionnaire dico_terrain{}
        son_piece.play()
    fen.after(10,bas)




def gauche(evenement):
    global x_joueur ,y_joueur ,pas_x_joueur ,pas_y_joueur
    pas_x_joueur= -32

    verif = position()        # On appelle la fonction position(), cette fonction donne à quelle endroit
    if carte[verif-1] == 2:  # on se situe selon la liste carte[] , si la case à gauche (donc -1 dans la liste) 
        print('Collision !')  #) est un 2 alors on fait rien, sinon on peut se déplacer à gauche
    else:                     # 
        x_joueur = x_joueur + pas_x_joueur
        can.coords(id_img_pacman, x_joueur, y_joueur)

    verif_piece=position()        #On vérifie si le joueur
    if carte[verif_piece] == 1:   #se trouve sur une pièce.
        carte[verif_piece] = 0    #Si c'est le cas, la piece disparait de la liste map[]
        can.delete(dico_terrain['zone'+str(verif_piece)]) #on efface le pièce affichée de la carte
                                                  # en s'aidant du dictionnaire dico_terrain{}
        son_piece.play()
    fen.after(10,gauche)




def droite(evenement):
    global x_joueur ,y_joueur ,pas_x_joueur ,pas_y_joueur
    pas_x_joueur= 32

    verif = position()        # On appelle la fonction position(), cette fonction donne à quelle endroit
    if carte[verif+1] == 2:  # on se situe selon la liste carte[] , si la case à droite (donc +1 dans la liste) 
        print('Collision !')  #) est un 2 alors on fait rien, sinon on peut se déplacer à droite
    else:                     # 
        x_joueur = x_joueur + pas_x_joueur
        can.coords(id_img_pacman, x_joueur, y_joueur)


    verif_piece=position()        #On vérifie si le joueur
    if carte[verif_piece] == 1:   #se trouve sur une pièce.
        carte[verif_piece] = 0    #Si c'est le cas, la piece disparait de la liste map[] 
        can.delete(dico_terrain['zone'+str(verif_piece)]) #on efface le pièce affichée de la carte
                                                  # en s'aidant du dictionnaire dico_terrain{}
        son_piece.play()
    fen.after(10,droite)





def map():
    global statut,carte,pas,dico_terrain
    carte=[1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
           1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
           2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
           2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
           2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
           2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
           2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
           2,2,1,1,1,1,1,1,1,1,1,1,1,0,1,2,1,1,1,1,1,1,2,2,
           2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
           2,2,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,2,2,
           2,2,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,2,2,
           2,2,1,1,1,1,1,1,0,0,0,0,0,2,0,1,1,1,1,1,1,1,2,2,
           2,2,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,2,2,
           2,2,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,2,2,
           2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
           2,2,1,1,1,1,1,1,1,1,1,1,1,0,1,2,1,1,1,1,1,1,2,2,
           2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
           2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
           2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
           2,2,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
           2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
           2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,
           2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
           2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2] 
           

    pas=0
    dico_terrain={}
    for rang_y in range(0,768,32):
        for rang_x in range(0,768,32):
           
           if carte[pas] == 0:
               
               dico_terrain['zone{0}'.format(pas)]=0

           if carte[pas] == 1:


               dico_terrain['zone{0}'.format(pas)]=can.create_image(rang_x+16 , rang_y+16 , image=img_piece)
              
           if carte[pas] == 2:
               
               dico_terrain['zone{0}'.format(pas)]=can.create_image(rang_x+16 , rang_y+16 , image=img_mur)
               
           pas=pas+1
       





           
y_joueur = 368
x_joueur = 368
pas_y_joueur = 0
pas_x_joueur = 0
statut = [0,1,2]  # 0 = vide, 1 = piece, 2 = mur


#Creation des variables pour appeler les sons (utilisées dans les fonctions)
son_piece = sa.WaveObject.from_wave_file("coin.wav")
son_mort = sa.WaveObject.from_wave_file("mort.wav")



"""---creation du widget principal ("maitre")---"""
fen=Tk()
fen.title("Pac-Man")

"""---creation des widgets "esclaves"---"""
#creation des Canvas

can=Canvas(fen, bg='black', height=768, width=768)
can.pack(side=LEFT, padx=5, pady=5)
can.focus_set()

#importation des images pacman
img_pacman = PhotoImage(file='pacman.png')
id_img_pacman = can.create_image(x_joueur , y_joueur , image=img_pacman)
img_mur=PhotoImage(file='mur.png')
img_piece=PhotoImage(file='piece.png')




#QUADRILLAGE TEMPORAIRE POUR SE REPERER

for rang_x in range(0,768,32):
    can.create_line(rang_x,0,rang_x,1024,fill='RED',width=1)
        
for rang_y in range(0,768,32):
    can.create_line(0,rang_y,1024,rang_y,fill='RED',width=1)


###

"""On appelle les commandes soit par des boutons, soit en continue"""
can.bind('<Up>',haut)
can.pack()

can.bind('<Down>',bas)
can.pack()

can.bind('<Left>',gauche)
can.pack()

can.bind('<Right>',droite)
can.pack()


map() #On appelle la fonction map pour générer le terrain

fen.mainloop()
