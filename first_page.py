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
    global canva, roots, page1_ouverte, timer_var
    roots = tk.Tk()
    roots.title("Page d'accueil")

    page1_ouverte = False
    # Création du canvas pour dessiner la grille
    canva = tk.Canvas(roots, width=500, height=400)
    canva.pack()
    canva.create_text(250, 50, text="TAKUZU", font=('Helvetica', 20), fill="black")
    canva.create_text(135, 170, text="Sélectionner la taille de la grille :", font=('Helvetica', 10), fill="black")

    check_var = tk.IntVar(value=1)
    timer_var = tk.BooleanVar(value=False)  # Variable pour activer/désactiver le timer
    
    checkbutton_test1 = tk.Radiobutton(roots, text="6x6", variable = check_var, value=1, height=1, width=7 )
    checkbutton_test2 = tk.Radiobutton(roots, text="8x8", variable = check_var, value = 2, height=1, width=7 )
    checkbutton_test3 = tk.Radiobutton(roots, text="10x10", variable = check_var, value= 3, height=1, width=7 )      

    timer_checkbox = tk.Checkbutton(roots, text="Activer le chronomètre", variable=timer_var)



    def get_size_grille():
        size_grille = check_var.get()
        
        if size_grille == 1:
            appel6x6()
        elif size_grille == 2:
            appel8x8()
        elif size_grille == 3:
            appel10x10()

    
    jouer_button = tk.Button(roots, text="Jouer", command=get_size_grille)
    
    checkbutton_test1.place(x=50, y=200)
    checkbutton_test2.place(x=200, y=200)
    checkbutton_test3.place(x=350, y=200)
    jouer_button.place(x= 50, y = 250 )
    timer_checkbox.place(x=100,y=250)
    
    roots.mainloop()


def appel6x6():
    global roots
    roots.destroy()
    ihm6x6.grille6x6(timer_var.get())
def appel8x8():
    global roots
    roots.destroy()
    ihm8x8.grille8x8(timer_var.get())  
def appel10x10():
    global roots
    roots.destroy()
    ihm10x10.grille10x10(timer_var.get())


