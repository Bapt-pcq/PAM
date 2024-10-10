import tkinter as tk

class ihm_10x10:

        
    def grille10x10(self):
        global taille, text_id_message, text_ids, grid_values, rows, cols, cell_size, canvas,  root,offset_x,offset_y
        taille =2
        # Définition des paramètres graphique
        root = tk.Tk()
        root.title("Grille 10x10")

        # Dimensions de la grille
        rows, cols = 10, 10
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
        canvas.bind("<Button-1>", ihm_10x10.on_click)
        # creation des boutons
        button_clear = tk.Button(root, text="Réinitialiser", command=ihm_10x10.clear10x10,width=15, height=3)
        button_verif = tk.Button(root, text="Vérifier", command=ihm_10x10.verifier10x10,width=15, height=3)
        button_valider = tk.Button(root, text="Valider", command=ihm_10x10.valider10x10,width=15, height=3)
        button_home = tk.Button(root, text="Accueil", command=ihm_10x10.home,width=7, height=2)
        # Placement du bouton dans la fenêtre
        button_clear.place(x=700, y=100)
        button_verif.place(x=700, y=200)
        button_valider.place(x=700, y=300)
        button_home.place(x=900, y=0)

        canvas.create_text(750, 40, text="TAKUZU grille 10x10", font=('Helvetica', 20), fill="black")

        canvas.create_text(180, 560, text="Message", font=('Helvetica', 10), fill="black")



        canvas.create_rectangle(150, 570, 570, 600, outline="black", width=1, fill="")
        #numérotation ligne
        canvas.create_text(offset_x-10, offset_y+10, text="1", font=('Helvetica', 10), fill="black")
        canvas.create_text(offset_x-10, offset_y+60, text="2", font=('Helvetica', 10), fill="black")
        canvas.create_text(offset_x-10, offset_y+110, text="3", font=('Helvetica', 10), fill="black")
        canvas.create_text(offset_x-10, offset_y+160, text="4", font=('Helvetica', 10), fill="black")
        canvas.create_text(offset_x-10, offset_y+210, text="5", font=('Helvetica', 10), fill="black")
        canvas.create_text(offset_x-10, offset_y+260, text="6", font=('Helvetica', 10), fill="black")
        canvas.create_text(offset_x-10, offset_y+310, text="7", font=('Helvetica', 10), fill="black")
        canvas.create_text(offset_x-10, offset_y+360, text="8", font=('Helvetica', 10), fill="black")
        canvas.create_text(offset_x-10, offset_y+410, text="9", font=('Helvetica', 10), fill="black")
        canvas.create_text(offset_x-10, offset_y+460, text="10", font=('Helvetica', 10), fill="black")
        

        #numérotation colonne
        canvas.create_text(offset_x+10, offset_y-10, text="1", font=('Helvetica', 10), fill="black")
        canvas.create_text(offset_x+60, offset_y-10, text="2", font=('Helvetica', 10), fill="black")
        canvas.create_text(offset_x+110, offset_y-10, text="3", font=('Helvetica', 10), fill="black")
        canvas.create_text(offset_x+160, offset_y-10, text="4", font=('Helvetica', 10), fill="black")
        canvas.create_text(offset_x+210, offset_y-10, text="5", font=('Helvetica', 10), fill="black")
        canvas.create_text(offset_x+260, offset_y-10, text="6", font=('Helvetica', 10), fill="black")
        canvas.create_text(offset_x+310, offset_y-10, text="7", font=('Helvetica', 10), fill="black")
        canvas.create_text(offset_x+360, offset_y-10, text="8", font=('Helvetica', 10), fill="black")
        canvas.create_text(offset_x+410, offset_y-10, text="9", font=('Helvetica', 10), fill="black")
        canvas.create_text(offset_x+460, offset_y-10, text="10", font=('Helvetica', 10), fill="black")

        # Remplir le canvas avec les valeurs générées dans grid_values
        text_ids[4][0] = "Rempli"
        canvas.create_text(offset_x+0 * cell_size + cell_size // 2,offset_y+ 4 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
        grid_values[4][0]=0
        text_ids[5][0] = "Rempli"
        canvas.create_text(offset_x+0 * cell_size + cell_size // 2,offset_y+ 5 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
        grid_values[5][0]=0
        text_ids[8][0] = "Rempli"
        canvas.create_text(offset_x+0 * cell_size + cell_size // 2,offset_y+ 8 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
        grid_values[8][0]=1
        text_ids[1][1] = "Rempli"
        canvas.create_text(offset_x+1 * cell_size + cell_size // 2,offset_y+ 1 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
        grid_values[1][1]=0
        text_ids[2][1] = "Rempli"
        canvas.create_text(offset_x+1 * cell_size + cell_size // 2,offset_y+ 2 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
        grid_values[2][1]=0
        text_ids[8][1] = "Rempli"
        canvas.create_text(offset_x+1 * cell_size + cell_size // 2,offset_y+ 8 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
        grid_values[8][1]=0
        text_ids[9][1] = "Rempli"
        canvas.create_text(offset_x+ 1 * cell_size + cell_size // 2,offset_y+ 9 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
        grid_values[9][1]=1
        text_ids[1][2] = "Rempli"
        canvas.create_text(offset_x+ 2 * cell_size + cell_size // 2,offset_y+ 1 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
        grid_values[1][2]=1
        text_ids[5][2] = "Rempli"
        canvas.create_text(offset_x+ 2 * cell_size + cell_size // 2,offset_y+ 5 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
        grid_values[5][2]=1
        text_ids[0][3] = "Rempli"
        canvas.create_text(offset_x+ 3 * cell_size + cell_size // 2,offset_y+ 0 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
        grid_values[0][3]=0
        text_ids[3][3] = "Rempli"
        canvas.create_text(offset_x+ 3 * cell_size + cell_size // 2,offset_y+ 3 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
        grid_values[3][3]=0
        text_ids[2][4] = "Rempli"
        canvas.create_text(offset_x+ 4 * cell_size + cell_size // 2,offset_y+ 2 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
        grid_values[2][4]=0
        text_ids[6][4] = "Rempli"
        canvas.create_text(offset_x+ 4 * cell_size + cell_size // 2,offset_y+ 6 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
        grid_values[6][4]=0
        text_ids[7][4] = "Rempli"
        canvas.create_text(offset_x+ 4 * cell_size + cell_size // 2,offset_y+ 7 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
        grid_values[7][4]=0
        text_ids[9][4] = "Rempli"
        canvas.create_text(offset_x+ 4 * cell_size + cell_size // 2,offset_y+ 9 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
        grid_values[9][4]=1
        text_ids[0][5] = "Rempli"
        canvas.create_text(offset_x+ 5 * cell_size + cell_size // 2,offset_y+ 0 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
        grid_values[0][5]=1
        text_ids[4][5] = "Rempli"
        canvas.create_text(offset_x+ 5 * cell_size + cell_size // 2,offset_y+ 4 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
        grid_values[4][5]=1
        text_ids[5][5] = "Rempli"
        canvas.create_text(offset_x+ 5 * cell_size + cell_size // 2,offset_y+ 5 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
        grid_values[5][5]=1
        text_ids[7][5] = "Rempli"
        canvas.create_text(offset_x+ 5 * cell_size + cell_size // 2,offset_y+ 7 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
        grid_values[7][5]=0
        text_ids[0][6] = "Rempli"
        canvas.create_text(offset_x+ 6 * cell_size + cell_size // 2,offset_y+ 0 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
        grid_values[0][6]=1
        text_ids[4][7] = "Rempli"
        canvas.create_text(offset_x+ 7 * cell_size + cell_size // 2,offset_y+ 4 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
        grid_values[4][7]=1
        text_ids[5][7] = "Rempli"
        canvas.create_text(offset_x+ 7 * cell_size + cell_size // 2,offset_y+ 5 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
        grid_values[5][7]=1
        text_ids[1][8] = "Rempli"
        canvas.create_text(offset_x+ 8 * cell_size + cell_size // 2,offset_y+ 1 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
        grid_values[1][8]=1
        text_ids[4][8] = "Rempli"
        canvas.create_text(offset_x+ 8 * cell_size + cell_size // 2,offset_y+ 4 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
        grid_values[4][8]=0
        text_ids[3][9] = "Rempli"
        canvas.create_text(offset_x+ 9 * cell_size + cell_size // 2,offset_y+ 3 * cell_size + cell_size // 2, text=1, font=('Helvetica', 12), fill="black")
        grid_values[3][9]=1
        text_ids[6][9] = "Rempli"
        canvas.create_text(offset_x+ 9 * cell_size + cell_size // 2,offset_y+ 6 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
        grid_values[6][9]=0
        text_ids[8][9] = "Rempli"
        canvas.create_text(offset_x+ 9 * cell_size + cell_size // 2,offset_y+ 8 * cell_size + cell_size // 2, text=0, font=('Helvetica', 12), fill="black")
        grid_values[8][9]=0

        for i in range(10) :
            print(grid_values[i])
    
    def check_empty_cells(grid):
            # Parcourir chaque ligne de la grille
            for row in grid:
                # Vérifier s'il y a une cellule vide ('') dans la ligne
                if '' in row:
                    return True  # Il y a au moins une cellule vide
            return False  # Pas de cellules vides




    def clear10x10():
        global root, canvas, text_id_message
        root.destroy()
        for row in range(rows):
            for col in range(cols):
                grid_values[row][col] = ""
        ihm_10x10.grille10x10("a")
        text_id_message = canvas.create_text(350, 585, text="La grille a été réinitialisée", font=('Helvetica', 10), fill="black")

    def home():
        from first_page import first_page 
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


    def verifier10x10():
    # Vérifier les lignes
        global text_id_message, grid_values
        if text_id_message != None:
            canvas.delete(text_id_message)
        if not ihm_10x10.all_unique(grid_values):

            text_id_message = canvas.create_text(350, 585, text="Il y a une erreur, deux lignes sont identiques", font=('Helvetica', 10), fill="black")

            return False
        grid_col = []
        for col in range(len(grid_values[0])):
                # Initialiser une liste pour la colonne actuelle
                current_column = []
                
                # Parcourir chaque ligne pour extraire l'élément de la colonne actuelle
                for lig in range(len(grid_values)):
                    current_column.append(grid_values[lig][col])
                
                # Ajouter la colonne actuelle à la liste des colonnes
                grid_col.append(current_column)
        if not ihm_10x10.all_unique(grid_col):

            text_id_message = canvas.create_text(350, 585, text="Il y a une erreur, deux colonnes sont identiques", font=('Helvetica', 10), fill="black")

            return False
        for row in range(rows):
            if not ihm_10x10.is_valid_sequence(grid_values[row]) :

                text_id_message = canvas.create_text(350, 585, text="Il y a une erreur dans la ligne "+ str(row + 1), font=('Helvetica', 10), fill="black")

                return False
            if not ihm_10x10.has_equal_zeros_ones(grid_values[row]) :
                text_id_message = canvas.create_text(350, 585, text="Il y a une erreur dans la ligne " + str(row + 1) + " le nombre de 0 et de 1 est différent", font=('Helvetica', 10), fill="black")

                return False
        # Vérifier les colonnes
        for col in range(cols):
            column = [grid_values[row][col] for row in range(rows)]
            if not ihm_10x10.is_valid_sequence(column) :
                text_id_message = canvas.create_text(350, 585, text="Il y a une erreur dans la colonne "+ str(col + 1), font=('Helvetica', 10), fill="black")

                return False
            if not ihm_10x10.has_equal_zeros_ones(column):
                text_id_message = canvas.create_text(350, 585, text="Il y a une erreur dans la colonne " + str(col + 1) + " le nombre de 0 et de 1 est différent", font=('Helvetica', 10), fill="black")

                return False
        text_id_message = canvas.create_text(350, 585, text="Il n'y a pas d'erreur", font=('Helvetica', 10), fill="black")

        return True

    def valider10x10():
        global text_id_message, grid_values
        if not ihm_10x10.check_empty_cells(grid_values) :
            if not ihm_10x10.verifier():
                canvas.delete(text_id_message)
                text_id_message = canvas.create_text(390, 585, text="Malheureusement, la grille est fausse vous devez recommencer !", font=('Helvetica', 10), fill="black")
                return False
            canvas.delete(text_id_message)
            text_id_message = canvas.create_text(390, 585, text="Vous avez correctement complété la grille, félicitation !", font=('Helvetica', 10), fill="black")    
            return True
        canvas.delete(text_id_message)
        text_id_message = canvas.create_text(390, 585,  text="Vous devez d'abord terminer la grille !", font=('Helvetica', 10), fill="black")
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

            if grid_values[row][col] == "":
                grid_values[row][col] = 0
                text_ids[row][col] = canvas.create_text(x, y, text="0", font=('Helvetica', 12), fill="green")
            elif grid_values[row][col] == 0:
                grid_values[row][col] = 1
                text_ids[row][col] = canvas.create_text(x, y, text="1", font=('Helvetica', 12), fill="green")
            elif grid_values[row][col] == 1:
                grid_values[row][col] = ''
                text_ids[row][col] = canvas.create_text(x, y, text='', font=('Helvetica', 12), fill="green")