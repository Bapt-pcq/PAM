import tkinter as tk



from ihm.ihm_6x6 import ihm_6x6
from ihm.ihm_8x8 import ihm_8x8
from ihm.ihm_10x10 import ihm_10x10

taille = 3
page1_ouverte = True
ihm6x6 = ihm_6x6()
ihm8x8 = ihm_8x8()
ihm10x10 = ihm_10x10()
def first_page() :
    global canva, roots, page1_ouverte
    roots = tk.Tk()
    roots.title("Page d'accueil")

    page1_ouverte = False
    # Création du canvas pour dessiner la grille
    canva = tk.Canvas(roots, width=500, height=400)
    canva.pack()
    canva.create_text(250, 50, text="TAKUZU", font=('Helvetica', 20), fill="black")
    canva.create_text(135, 170, text="Sélectionner la taille de la grille :", font=('Helvetica', 10), fill="black")


    
    button_8x8 = tk.Button(roots, text="8x8", command=appel8x8,width=15, height=3)
    button_10x10 = tk.Button(roots, text="10x10", command=appel10x10,width=15, height=3)
    button_6x6 = tk.Button(roots, text="6x6", command=appel6x6,width=15, height=3)
    # Placement du bouton dans la fenêtre
    button_8x8.place(x=200, y=200)
    button_10x10.place(x=350, y=200)
    button_6x6.place(x=50, y=200)

    
    roots.mainloop()


def appel6x6():
    global roots
    roots.destroy()
    ihm6x6.grille6x6()
def appel8x8():
    global roots
    roots.destroy()
    ihm8x8.grille8x8()
def appel10x10():
    global roots
    roots.destroy()
    ihm10x10.grille10x10()



first_page()
