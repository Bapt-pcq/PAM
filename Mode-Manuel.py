import tkinter as tk
import random



taille = 3
page1_ouverte = True
def first_page() :
    global canva, roots, page1_ouverte
    roots = tk.Tk()
    roots.title("Page d'accueil222222s")

    page1_ouverte = False
    # Création du canvas pour dessiner la grille
    canva = tk.Canvas(roots, width=500, height=400)
    canva.pack()
    canva.create_text(250, 50, text="TAKUZU", font=('Helvetica', 20), fill="black")
    canva.create_text(135, 170, text="Sélectionner la taille de grille :", font=('Helvetica', 10), fill="black")

    button_8x8 = tk.Button(roots, text="8x8", command=grille8x8,width=15, height=3)
    button_10x10 = tk.Button(roots, text="10x10", command=grille10x10,width=15, height=3)
    button_6x6 = tk.Button(roots, text="6x6", command=grille6x6,width=15, height=3)
    # Placement du bouton dans la fenêtre
    button_8x8.place(x=200, y=200)
    button_10x10.place(x=350, y=200)
    button_6x6.place(x=50, y=200)

    roots.mainloop()

def create_grid():
    global taille

    if taille == 0  :
        grille6x6()
    if taille == 1  :
        grille8x8()
    if taille == 2  :
        grille10x10()









def grille8x8():
    global taille, text_id_message, text_ids, grid_values, rows, cols, cell_size, canvas, roots, page1_ouverte, root
    taille =1
    # Définition des paramètres graphique
    if page1_ouverte == False :
        roots.destroy()
    page1_ouverte = True
    root = tk.Tk()
    root.title("Grille 8x8")

    # Dimensions de la grille
    rows, cols = 8, 8
    cell_size = 50  # Taille des cellules en pixels

    # Création du canvas pour dessiner la grille
    canvas = tk.Canvas(root, width=cols*cell_size*1.9, height=rows*cell_size*1.3)
    canvas.pack()
    text_ids = [[None for _ in range(cols)] for _ in range(rows)]
    grid_values = [["" for _ in range(cols)] for _ in range(rows)]
    text_id_message = None
    grid_values1 = [["" for _ in range(cols)] for _ in range(rows)]
     # Dessin des lignes horizontales et verticales
    for i in range(rows+1):
        canvas.create_line(0, i*cell_size, cols*cell_size, i*cell_size)
    for j in range(cols+1):
        canvas.create_line(j*cell_size, 0, j*cell_size, rows*cell_size)
    canvas.bind("<Button-1>", on_click)
    # creation des boutons
    button_clear = tk.Button(root, text="Clear", command=clear,width=15, height=3)
    button_verif = tk.Button(root, text="Vérifier", command=verifier,width=15, height=3)
    button_valider = tk.Button(root, text="Valider", command=verifier,width=15, height=3)
    # Placement du bouton dans la fenêtre
    button_clear.place(x=530, y=100)
    button_verif.place(x=530, y=200)
    button_valider.place(x=530, y=300)


    canvas.create_text(590, 40, text="TAKUZU grille 8x8", font=('Helvetica', 20), fill="black")

    canvas.create_text(130, 440, text="Message", font=('Helvetica', 10), fill="black")



    canvas.create_rectangle(100, 450, 450, 480, outline="black", width=1, fill="")


    # Remplir le canvas avec les valeurs générées dans grid_values
    text_ids[0][3] = canvas.create_text(3 * cell_size + cell_size // 2, 0 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[0][3]=0
    text_ids[0][5] = canvas.create_text(5 * cell_size + cell_size // 2, 0 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[0][5]=0
    text_ids[1][0] = canvas.create_text(0 * cell_size + cell_size // 2, 1 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
    grid_values[1][0]=1
    text_ids[1][7] = canvas.create_text(7 * cell_size + cell_size // 2, 1 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[1][7]=0
    text_ids[2][4] = canvas.create_text(4 * cell_size + cell_size // 2, 2 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[2][4]=0
    text_ids[3][2] = canvas.create_text(2 * cell_size + cell_size // 2, 3 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
    grid_values[3][2]=1
    text_ids[4][4] = canvas.create_text(4 * cell_size + cell_size // 2, 4 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[4][4]=0
    text_ids[4][5] = canvas.create_text(5 * cell_size + cell_size // 2, 4 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[4][5]=0
    text_ids[4][7] = canvas.create_text(7 * cell_size + cell_size // 2, 4 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[4][7]=0
    text_ids[6][0] = canvas.create_text(0 * cell_size + cell_size // 2, 6 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[6][0]=0
    text_ids[6][2] = canvas.create_text(2 * cell_size + cell_size // 2, 6 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[6][2]=0
    text_ids[6][5] = canvas.create_text(5 * cell_size + cell_size // 2, 6 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[6][5]=0
    text_ids[6][7] = canvas.create_text(7 * cell_size + cell_size // 2, 6 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[6][7]=0
    text_ids[7][0] = canvas.create_text(0 * cell_size + cell_size // 2, 7 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[7][0]=0
    text_ids[7][3] = canvas.create_text(3 * cell_size + cell_size // 2, 7 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[7][3]=0
    text_ids[7][5] = canvas.create_text(5 * cell_size + cell_size // 2, 7 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
    grid_values[7][5]=1
    text_ids[7][6] = canvas.create_text(6 * cell_size + cell_size // 2, 7 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
    grid_values[7][6]=1

    for i in range(8) :
        print(grid_values[i])


def grille10x10():
    return 0

def grille6x6():
    return 0




def verifier():
    # Vérifier les lignes
    global text_id_message, grid_values
    if text_id_message != None:
        canvas.delete(text_id_message)
    if not all_unique(grid_values):

        text_id_message = canvas.create_text(250, 465, text="Faux - Lignes ou colonnes identiques", font=('Helvetica', 10), fill="black")

        return False
    for row in range(rows):
        if not is_valid_sequence(grid_values[row]) :

            text_id_message = canvas.create_text(250, 465, text="Faux ligne "+ str(row + 1), font=('Helvetica', 10), fill="black")

            return False
        if not has_equal_zeros_ones(grid_values[row]) :
            text_id_message = canvas.create_text(250, 465, text="Faux ligne " + str(row + 1) + " dif nb 0 et 1", font=('Helvetica', 10), fill="black")

            return False
    # Vérifier les colonnes
    for col in range(cols):
        column = [grid_values[row][col] for row in range(rows)]
        if not is_valid_sequence(column) :
            text_id_message = canvas.create_text(250, 465, text="Faux colonne "+ str(col + 1), font=('Helvetica', 10), fill="black")

            return False
        if not has_equal_zeros_ones(column):
            text_id_message = canvas.create_text(250, 465, text="Faux colonne " + str(col + 1) + " dif nb 0 et 1", font=('Helvetica', 10), fill="black")

            return False
    text_id_message = canvas.create_text(250, 465, text="Vrai", font=('Helvetica', 10), fill="black")

    return True







# effacer et regenerer la grille
def clear():
    global root
    root.destroy()
    for row in range(rows):
        for col in range(cols):
            grid_values[row][col] = ""
    create_grid()



def is_valid_sequence(sequence):
    # Vérifie qu'il n'y a pas plus de deux 0 ou 1 consécutifs
    count = 1

    for i in range(1, len(sequence)):

        if sequence[i] != "" or sequence[i-1] != "":
            if sequence[i] == sequence[i - 1]  :
                count += 1
                if count > 2:
                    return False
            else:
                count = 1
    return True


def has_equal_zeros_ones(sequence):
    # Vérifie qu'il y a le même nombre de 0 et de 1
    vide = sequence.count("")
    if vide!=0:
        return True
    zeros = sequence.count(0)
    ones = sequence.count(1)
    if zeros != ones :
        return False
    return True

def all_unique(sequences):
    # Vérifie qu'aucune ligne/colonne n'est identique
    seen = set()
    vide = sequences.count("")
    if vide!=0:
        return True
    for seq in sequences:
        # Convertir en tuple pour pouvoir l'ajouter à un set
        seq_tuple = tuple(seq)
        if seq_tuple in seen:
            return False
        seen.add(seq_tuple)
    return True



def on_click(event):
    global cell_size, grid_values, text_ids, cols, rows, canvas
    # Trouver les coordonnées de la cellule cliquée
    col = event.x // cell_size
    row = event.y // cell_size

    # Vérifier que les coordonnées sont dans la grille
    if 0 <= row < rows and 0 <= col < cols:
        # Calculer la position pour centrer le texte dans la cellule
        x = col * cell_size + cell_size // 2
        y = row * cell_size + cell_size // 2

        # Ajouter ou modifier le texte au centre de la cellule cliquée
        if text_ids[row][col] is not None:
            canvas.delete(text_ids[row][col])  # Effacer le texte existant

        if grid_values[row][col] == 0 or grid_values[row][col] == "":
            grid_values[row][col] = 1
            text_ids[row][col] = canvas.create_text(x, y, text="1", font=('Helvetica', 12), fill="green")
        elif grid_values[row][col] == 1:
            grid_values[row][col] = 0
            text_ids[row][col] = canvas.create_text(x, y, text="0", font=('Helvetica', 12), fill="green")

first_page()