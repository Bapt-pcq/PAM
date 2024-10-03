import tkinter as tk
import random



taille = 3
page1_ouverte = True
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
    global taille, text_id_message, text_ids, grid_values, rows, cols, cell_size, canvas, roots, page1_ouverte, root,offset_x,offset_y
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
    # Définir les décalages pour centrer la grille
    offset_x = 30  # Décalage horizontal
    offset_y = 20  # Décalage vertical

    # Dessin des lignes horizontales et verticales
    for i in range(rows + 1):
        canvas.create_line(offset_x, offset_y + i * cell_size, offset_x + cols * cell_size, offset_y + i * cell_size)  # Lignes horizontales

    for j in range(cols + 1):
        canvas.create_line(offset_x + j * cell_size, offset_y, offset_x + j * cell_size, offset_y + rows * cell_size)  # Lignes verticales
    canvas.bind("<Button-1>", on_click)
    # creation des boutons
    button_clear = tk.Button(root, text="Réinitialiser", command=clear,width=15, height=3)
    button_verif = tk.Button(root, text="Vérifier", command=verifier,width=15, height=3)
    button_valider = tk.Button(root, text="Valider", command=verifier,width=15, height=3)
    button_home = tk.Button(root, text="Accueil", command=home,width=7, height=2)
    # Placement du bouton dans la fenêtre
    button_clear.place(x=530, y=100)
    button_verif.place(x=530, y=200)
    button_valider.place(x=530, y=300)
    button_home.place(x=710, y=0)

    canvas.create_text(590, 40, text="TAKUZU grille 8x8", font=('Helvetica', 20), fill="black")

    canvas.create_text(130, 440, text="Message", font=('Helvetica', 10), fill="black")



    canvas.create_rectangle(100, 450, 450, 480, outline="black", width=1, fill="")
    #numérotation ligne
    canvas.create_text(offset_x-10, offset_y+10, text="1", font=('Helvetica', 10), fill="black")
    canvas.create_text(offset_x-10, offset_y+60, text="2", font=('Helvetica', 10), fill="black")
    canvas.create_text(offset_x-10, offset_y+110, text="3", font=('Helvetica', 10), fill="black")
    canvas.create_text(offset_x-10, offset_y+160, text="4", font=('Helvetica', 10), fill="black")
    canvas.create_text(offset_x-10, offset_y+210, text="5", font=('Helvetica', 10), fill="black")
    canvas.create_text(offset_x-10, offset_y+260, text="6", font=('Helvetica', 10), fill="black")
    canvas.create_text(offset_x-10, offset_y+310, text="7", font=('Helvetica', 10), fill="black")
    canvas.create_text(offset_x-10, offset_y+360, text="8", font=('Helvetica', 10), fill="black")

    #numérotation colonne
    canvas.create_text(offset_x+10, offset_y-10, text="1", font=('Helvetica', 10), fill="black")
    canvas.create_text(offset_x+60, offset_y-10, text="2", font=('Helvetica', 10), fill="black")
    canvas.create_text(offset_x+110, offset_y-10, text="3", font=('Helvetica', 10), fill="black")
    canvas.create_text(offset_x+160, offset_y-10, text="4", font=('Helvetica', 10), fill="black")
    canvas.create_text(offset_x+210, offset_y-10, text="5", font=('Helvetica', 10), fill="black")
    canvas.create_text(offset_x+260, offset_y-10, text="6", font=('Helvetica', 10), fill="black")
    canvas.create_text(offset_x+310, offset_y-10, text="7", font=('Helvetica', 10), fill="black")
    canvas.create_text(offset_x+360, offset_y-10, text="8", font=('Helvetica', 10), fill="black")

    # Remplir le canvas avec les valeurs générées dans grid_values
    text_ids[0][3] = "Rempli"
    canvas.create_text(offset_x+3 * cell_size + cell_size // 2,offset_y+ 0 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[0][3]=0
    text_ids[0][5] = "Rempli"
    canvas.create_text(offset_x + 5 * cell_size + cell_size // 2,offset_y+ 0 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[0][5]=0
    text_ids[1][0] = "Rempli"
    canvas.create_text(offset_x+0 * cell_size + cell_size // 2, offset_y+1 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
    grid_values[1][0]=1
    text_ids[1][7] = "Rempli"
    canvas.create_text(offset_x+7 * cell_size + cell_size // 2,offset_y+ 1 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[1][7]=0
    text_ids[2][4] = "Rempli"
    canvas.create_text(offset_x+4 * cell_size + cell_size // 2,offset_y+ 2 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[2][4]=0
    text_ids[3][2] = "Rempli"
    canvas.create_text(offset_x+2 * cell_size + cell_size // 2,offset_y+ 3 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
    grid_values[3][2]=1
    text_ids[4][4] = "Rempli"
    canvas.create_text(offset_x+4 * cell_size + cell_size // 2,offset_y+ 4 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[4][4]=0
    text_ids[4][5] = "Rempli"
    canvas.create_text(offset_x+5 * cell_size + cell_size // 2,offset_y+ 4 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[4][5]=0
    text_ids[4][7] = "Rempli"
    canvas.create_text(offset_x+7 * cell_size + cell_size // 2,offset_y+ 4 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[4][7]=0
    text_ids[6][0] = "Rempli"
    canvas.create_text(offset_x+0 * cell_size + cell_size // 2,offset_y+ 6 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[6][0]=0
    text_ids[6][2] = "Rempli"
    canvas.create_text(offset_x+2 * cell_size + cell_size // 2,offset_y+ 6 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[6][2]=0
    text_ids[6][5] = "Rempli"
    canvas.create_text(offset_x+5 * cell_size + cell_size // 2,offset_y+ 6 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[6][5]=0
    text_ids[6][7] = "Rempli"
    canvas.create_text(offset_x+7 * cell_size + cell_size // 2,offset_y+ 6 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[6][7]=0
    text_ids[7][0] = "Rempli"
    canvas.create_text(offset_x+0 * cell_size + cell_size // 2,offset_y+ 7 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[7][0]=0
    text_ids[7][3] = "Rempli"
    canvas.create_text(offset_x+3 * cell_size + cell_size // 2,offset_y+ 7 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[7][3]=0
    text_ids[7][5] = "Rempli"
    canvas.create_text(offset_x+5 * cell_size + cell_size // 2,offset_y+ 7 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
    grid_values[7][5]=1
    text_ids[7][6] = "Rempli"
    canvas.create_text(offset_x+6 * cell_size + cell_size // 2,offset_y+ 7 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
    grid_values[7][6]=1

    for i in range(8) :
        print(grid_values[i])


def grille10x10():
    return 0

def grille6x6():
    global taille, text_id_message, text_ids, grid_values, rows, cols, cell_size, canvas, roots, page1_ouverte, root, offset_x, offset_y
    taille =0
    # Définition des paramètres graphique
    if page1_ouverte == False :
        roots.destroy()
    page1_ouverte = True
    root = tk.Tk()
    root.title("Grille 6x6")

    # Création du canvas pour dessiner la grille
    canvas = tk.Canvas(root, width=8*50*1.9, height=8*50*1.3)
    canvas.pack()


    # creation des boutons
    button_clear = tk.Button(root, text="Réinitialiser", command=clear,width=15, height=3)
    button_verif = tk.Button(root, text="Vérifier", command=verifier,width=15, height=3)
    button_valider = tk.Button(root, text="Valider", command=verifier,width=15, height=3)
    button_home = tk.Button(root, text="Accueil", command=home,width=7, height=2)
    # Placement du bouton dans la fenêtre
    button_clear.place(x=530, y=100)
    button_verif.place(x=530, y=200)
    button_valider.place(x=530, y=300)
    button_home.place(x=710, y=0)
    # Dimensions de la grille
    rows, cols = 6, 6
    cell_size = 60  # Taille des cellules en pixels

    text_ids = [[None for _ in range(cols)] for _ in range(rows)]
    grid_values = [["" for _ in range(cols)] for _ in range(rows)]
    text_id_message = None
    grid_values1 = [["" for _ in range(cols)] for _ in range(rows)]
    # Définir les décalages pour centrer la grille
    offset_x = 50  # Décalage horizontal
    offset_y = 50  # Décalage vertical

    # Dessin des lignes horizontales et verticales
    for i in range(rows + 1):
        canvas.create_line(offset_x, offset_y + i * cell_size, offset_x + cols * cell_size, offset_y + i * cell_size)  # Lignes horizontales

    for j in range(cols + 1):
        canvas.create_line(offset_x + j * cell_size, offset_y, offset_x + j * cell_size, offset_y + rows * cell_size)  # Lignes verticales

    canvas.bind("<Button-1>", on_click)
    canvas.create_text(590, 40, text="TAKUZU grille 6x6", font=('Helvetica', 20), fill="black")

    canvas.create_text(130, 440, text="Message", font=('Helvetica', 10), fill="black")

    #numérotation ligne
    canvas.create_text(40, 60, text="1", font=('Helvetica', 10), fill="black")
    canvas.create_text(40, 120, text="2", font=('Helvetica', 10), fill="black")
    canvas.create_text(40, 180, text="3", font=('Helvetica', 10), fill="black")
    canvas.create_text(40, 240, text="4", font=('Helvetica', 10), fill="black")
    canvas.create_text(40, 300, text="5", font=('Helvetica', 10), fill="black")
    canvas.create_text(40, 360, text="6", font=('Helvetica', 10), fill="black")

    #numérotation colonne
    canvas.create_text(60, 40, text="1", font=('Helvetica', 10), fill="black")
    canvas.create_text(120, 40, text="2", font=('Helvetica', 10), fill="black")
    canvas.create_text(180, 40, text="3", font=('Helvetica', 10), fill="black")
    canvas.create_text(240, 40, text="4", font=('Helvetica', 10), fill="black")
    canvas.create_text(300, 40, text="5", font=('Helvetica', 10), fill="black")
    canvas.create_text(360, 40, text="6", font=('Helvetica', 10), fill="black")

    canvas.create_rectangle(100, 450, 450, 480, outline="black", width=1, fill="")
    # Remplir le canvas avec les valeurs générées dans grid_values
    text_ids[0][3] = "Rempli"
    canvas.create_text(offset_x+3 * cell_size + cell_size // 2,offset_y+ 0 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[0][3]=0
    text_ids[1][0] = "Rempli"
    canvas.create_text(offset_x+0 * cell_size + cell_size // 2,offset_y+ 1 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
    grid_values[1][0]=1
    text_ids[1][2] = "Rempli"
    canvas.create_text(offset_x+2 * cell_size + cell_size // 2,offset_y+ 1 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
    grid_values[1][2]=1
    text_ids[2][4] = "Rempli"
    canvas.create_text(offset_x+4 * cell_size + cell_size // 2,offset_y+ 2 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[2][4]=0
    text_ids[3][2] = "Rempli"
    canvas.create_text(offset_x+2 * cell_size + cell_size // 2,offset_y+ 3 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
    grid_values[3][2]=1
    text_ids[3][3] = "Rempli"
    canvas.create_text(offset_x+3 * cell_size + cell_size // 2,offset_y+ 3 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
    grid_values[3][3]=1
    text_ids[3][5] = "Rempli"
    canvas.create_text(offset_x+5 * cell_size + cell_size // 2,offset_y+ 3 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[3][5]=0
    text_ids[4][1] = "Rempli"
    canvas.create_text(offset_x+1 * cell_size + cell_size // 2,offset_y+ 4 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
    grid_values[4][1]=0
    text_ids[5][0] = "Rempli"
    canvas.create_text(offset_x+0 * cell_size + cell_size // 2,offset_y+ 5 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
    grid_values[5][0]=1

    for i in range(6) :
        print(grid_values[i])
def valider():
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
    global root, canvas
    root.destroy()
    for row in range(rows):
        for col in range(cols):
            grid_values[row][col] = ""
    create_grid()


def home():
    global root
    root.destroy()
    first_page()

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

def all_unique(sequence):
    # Filtrer les lignes qui ne contiennent pas de ''
    filtered_rows = [row for row in sequence if '' not in row]

    # Vérifier les lignes identiques
    identical_rows = []
    for i in range(len(filtered_rows)):
        for j in range(i+1, len(filtered_rows)):
            if filtered_rows[i] == filtered_rows[j]:
                identical_rows.append((i, j))

    # Afficher les résultats

    if identical_rows:
        return False
    else:
        return True



def on_click(event):
    global cell_size, grid_values, text_ids, cols, rows, canvas, offset_x, offset_y
   # Trouver les coordonnées de la cellule cliquée en prenant en compte les offsets
    col = (event.x - offset_x) // cell_size
    row = (event.y - offset_y) // cell_size

    # Vérifier que les coordonnées sont dans la grille
    if 0 <= row < rows and 0 <= col < cols:
        # Calculer la position pour centrer le texte dans la cellule
        x = offset_x + col * cell_size + cell_size // 2
        y = offset_y + row * cell_size + cell_size // 2

        # Ajouter ou modifier le texte au centre de la cellule cliquée

        if text_ids[row][col] is not None:
            canvas.delete(text_ids[row][col])  # Effacer le texte existant

        if text_ids[row][col] == "Rempli" :
            return False

        if grid_values[row][col] == 0 or grid_values[row][col] == "":
            grid_values[row][col] = 1
            text_ids[row][col] = canvas.create_text(x, y, text="1", font=('Helvetica', 12), fill="green")
        elif grid_values[row][col] == 1:
            grid_values[row][col] = 0
            text_ids[row][col] = canvas.create_text(x, y, text="0", font=('Helvetica', 12), fill="green")

first_page()
