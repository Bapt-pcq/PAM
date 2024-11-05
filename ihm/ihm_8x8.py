import tkinter as tk

class ihm_8x8:


    def grille8x8(self, timer_enabled):
        global taille, text_id_message, text_ids, grid_values, rows, cols, cell_size, canvas, root,offset_x,offset_y
        taille =1
        # Définition des paramètres graphique
        root = tk.Tk()
        root.title("Grille 8x8")
        # Dimensions de la grille
        rows, cols = 8, 8
        cell_size = 50  # Taille des cellules en pixels
        
        
        ################################### Timer ##########################################
        self.timer_enabled = timer_enabled
        self.elapsed_time = 0  # Temps écoulé en secondes

        
        if self.timer_enabled :
            self.timer_label = tk.Label(root, text="Chronomètre : 0s")
            self.timer_label.pack()
            self.start_chronometer()
            
        #####################################################################################
        
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
        canvas.bind("<Button-1>", ihm_8x8.on_click)
        # creation des boutons
        button_clear = tk.Button(root, text="Réinitialiser", command=ihm_8x8.clear,width=15, height=3)
        button_verif = tk.Button(root, text="Vérifier", command=ihm_8x8.verifier,width=15, height=3)
        button_valider = tk.Button(root, text="Valider", command=ihm_8x8.valider,width=15, height=3)
        button_home = tk.Button(root, text="Accueil", command=self.home,width=7, height=2)
        # Placement du bouton dans la fenêtre
        button_clear.place(x=530, y=100)
        button_verif.place(x=530, y=200)
        button_valider.place(x=530, y=300)
        button_home.place(x=710, y=0)
        canvas.create_text(590, 40, text="TAKUZU grille 8x8", font=('Helvetica', 20), fill="black")
        canvas.create_text(80, 440, text="Message", font=('Helvetica', 10), fill="black")
        canvas.create_rectangle(50, 450, 500, 480, outline="black", width=1, fill="")

        #numérotation ligne
        for i in range(8):
            canvas.create_text(offset_x-10, offset_y+10+50*i, text=i+1, font=('Helvetica', 10), fill="black")


        #numérotation colonne
        for i in range(8):
            canvas.create_text(offset_x+10+50*i, offset_y-10, text=i+1, font=('Helvetica', 10), fill="black")


        # Remplir le canvas avec les valeurs générées dans grid_values
               # Remplir le canvas avec les valeurs générées dans grid_values
        fichier_grille = "grille/8x8_1.txt"  # Chemin vers ton fichier txt
        grille = ihm_8x8.lire_grille_depuis_fichier(fichier_grille)
        
        for row in range(8):
            for col in range(8):
                print(grille[row][col])
                if grille[row][col]!=-1:
                    text_ids[row][col] = "Rempli"
                    canvas.create_text(offset_x+col * cell_size + cell_size // 2,offset_y+ row * cell_size + cell_size // 2, text=grille[row][col], font=('Helvetica', 12), fill="black")
                    grid_values[row][col]=grille[row][col]
        for i in range(8) :
            print(grid_values[i])
   
    def lire_grille_depuis_fichier(fichier):
        # Ouvrir le fichier en lecture
        with open(fichier, 'r') as f:
            # Lire le contenu ligne par ligne et convertir chaque ligne en une liste d'entiers
            grille = [list(map(int, ligne.split())) for ligne in f]
        
        return grille


    # effacer et regenerer la grille
    def clear():
        global root, canvas, text_id_message
        root.destroy()
        for row in range(rows):
            for col in range(cols):
                grid_values[row][col] = ""
        ihm_8x8.grille8x8("a")
        text_id_message = canvas.create_text(250, 465, text="La grille a été réinitialisée", font=('Helvetica', 10), fill="black")



    def home(self):
        if self.timer_enabled ==True :
            self.stop_chronometer()
        from first_page import first_page 
        global root
        root.destroy()
        first_page()


    def valider():
        global text_id_message, grid_values
        from vérification.verification import verification
        if not verification.check_empty_cells(grid_values) :
            if not ihm_8x8.verifier():
                canvas.delete(text_id_message)
                text_id_message = canvas.create_text(310, 465, text="Malheureusement, la grille est fausse vous devez recommencer !", font=('Helvetica', 10), fill="black")
                return False
            canvas.delete(text_id_message)
            text_id_message = canvas.create_text(310, 465, text="Vous avez correctement complété la grille, félicitation !", font=('Helvetica', 10), fill="black")    
            return True
        canvas.delete(text_id_message)
        text_id_message = canvas.create_text(310, 465, text="Vous devez d'abord terminer la grille !", font=('Helvetica', 10), fill="black")
    def verifier():
        # Vérifier les lignes
        global text_id_message, grid_values
        from vérification.verification import verification
        if text_id_message != None:
            canvas.delete(text_id_message)
        if not verification.all_unique(grid_values):

            text_id_message = canvas.create_text(250, 465, text="Il y a une erreur, deux lignes sont identiques", font=('Helvetica', 10), fill="black")

            return False
        grid_col = []
        
        # Parcourir chaque colonne de la grille
        for col in range(len(grid_values[0])):
            # Initialiser une liste pour la colonne actuelle
            current_column = []
            
            # Parcourir chaque ligne pour extraire l'élément de la colonne actuelle
            for lig in range(len(grid_values)):
                current_column.append(grid_values[lig][col])
            
            # Ajouter la colonne actuelle à la liste des colonnes
            grid_col.append(current_column)
        if not verification.all_unique(grid_col):

            text_id_message = canvas.create_text(250, 465, text="Il y a une erreur, deux colonnes sont identiques", font=('Helvetica', 10), fill="black")

            return False
        for row in range(rows):
            if not verification.is_valid_sequence(grid_values[row]) :

                text_id_message = canvas.create_text(250, 465, text="Il y a une erreur dans la ligne "+ str(row + 1), font=('Helvetica', 10), fill="black")

                return False
            if not verification.has_equal_zeros_ones(grid_values[row]) :
                text_id_message = canvas.create_text(250, 465, text="Il y a une erreur dans la ligne " + str(row + 1) + " le nombre de 0 et de 1 est différent", font=('Helvetica', 10), fill="black")

                return False
        # Vérifier les colonnes
        for col in range(cols):
            column = [grid_values[row][col] for row in range(rows)]
            if not verification.is_valid_sequence(column) :
                text_id_message = canvas.create_text(250, 465, text="Il y a une erreur dans la colonne "+ str(col + 1), font=('Helvetica', 10), fill="black")

                return False
            if not verification.has_equal_zeros_ones(column):
                text_id_message = canvas.create_text(250, 465, text="Il y a une erreur dans la colonne " + str(col + 1) + " le nombre de 0 et de 1 est différent", font=('Helvetica', 10), fill="black")

                return False
        text_id_message = canvas.create_text(250, 465, text="Il n'y a pas d'erreur", font=('Helvetica', 10), fill="black")

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

    def start_chronometer(self):
        self.elapsed_time += 1  # Incrémente le temps écoulé
        minutes = self.elapsed_time // 60  # Calcul des minutes
        seconds = self.elapsed_time % 60  # Calcul des secondes
        self.timer_label.config(text=f"Chronomètre : {minutes:02}:{seconds:02}")  # Affichage formaté MM:SS
        #root.after(1000, self.start_chronometer)  # Relance après 1 seconde
        self._chronometer_running = root.after(1000, self.start_chronometer)
        
    def stop_chronometer(self):
        """Arrête le chronomètre et affiche la valeur finale."""
        root.after_cancel(self._chronometer_running)  # Annule l'appel programmé
        minutes = self.elapsed_time // 60
        seconds = self.elapsed_time % 60
        print(f"Temps final du chronomètre : {minutes:02}:{seconds:02}")
        self.timer_label.config(text=f"Chronomètre arrêté à : {minutes:02}:{seconds:02}")