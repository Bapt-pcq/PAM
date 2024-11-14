import tkinter as tk
import threading
import random
import threading
from grille.lecture import lecture
from thread1.agents import Agents
import etat_partage  # Importez le module partagé

class ihm_6x6:     
    def grille6x6(self):
        global taille, text_id_message, text_ids, grid_values, rows, cols, cell_size, canvas, root, offset_x, offset_y
        taille =0
        # Définition des paramètres graphique
       
        root = tk.Tk()
        root.title("Grille 6x6")

        # Drapeau pour arrêter les threads
        etat_partage.running = True
        # Création du canvas pour dessiner la grille
        canvas = tk.Canvas(root, width=8*50*1.9, height=8*50*1.3)
        canvas.pack()

        # creation des boutons
        button_clear = tk.Button(root, text="Réinitialiser", command=ihm_6x6.clear,width=15, height=3)
        button_verif = tk.Button(root, text="Vérifier", command=ihm_6x6.verifier,width=15, height=3)
        button_valider = tk.Button(root, text="Valider", command=ihm_6x6.valider,width=15, height=3)
        button_home = tk.Button(root, text="Accueil", command=ihm_6x6.home,width=7, height=2)
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

        canvas.bind("<Button-1>", ihm_6x6.on_click)
        canvas.create_text(590, 40, text="TAKUZU grille 6x6", font=('Helvetica', 20), fill="black")

        canvas.create_text(80, 440, text="Message", font=('Helvetica', 10), fill="black")
        canvas.create_rectangle(50, 450, 500, 480, outline="black", width=1, fill="")
        #numérotation ligne
        for i in range(6):
            canvas.create_text(offset_x-10, offset_y +10+60*i, text=i+1, font=('Helvetica', 10), fill="black")


        #numérotation colonne
        for i in range(6):
            canvas.create_text(offset_x+10+60*i, offset_y-10, text=i+1, font=('Helvetica', 10), fill="black")


        # Générer un nombre aléatoire entre 1 et 3
        nombre_aleatoire = random.randint(1, 3)
        # Remplir le canvas avec les valeurs générées dans grid_values
        if nombre_aleatoire==1:
            fichier_grille = "grille/6x6_1.txt"  # Chemin vers ton fichier txt
        elif nombre_aleatoire==2:
            fichier_grille = "grille/6x6_2.txt"  # Chemin vers ton fichier txt
        elif nombre_aleatoire==3:
            fichier_grille = "grille/6x6_3.txt"  # Chemin vers ton fichier txt
        grille = lecture.lire_grille_depuis_fichier(fichier_grille)
        
        for row in range(6):
            for col in range(6):
                print(grille[row][col])
                if grille[row][col]!=-1:
                    text_ids[row][col] = "Rempli"
                    canvas.create_text(offset_x+col * cell_size + cell_size // 2,offset_y+ row * cell_size + cell_size // 2, text=grille[row][col], font=('Helvetica', 12), fill="black")
                    grid_values[row][col]=grille[row][col]
        

        #Threads
        etat_partage.verrou = threading.Lock()
        
        #creation d'un thread par case
        for i in range(6):  # Boucle pour les lignes
            for j in range(6):  # Boucle pour les colonnes
                ihm_6x6.create_thread(i, j)
        #ihm_6x6.etat_page()
        print(grid_values)

        root.protocol("WM_DELETE_WINDOW", self.on_close)
            # Utilisation des fonctions

        return True
    
    def create_thread(i, j):
        global grid_values
        thread_name = f"t{i}{j}"
        print(f"Création du thread {thread_name}")
        thread = threading.Thread(target=Agents.surveiller_valeur, args=(i, j, grid_values), daemon=True, name=thread_name)
        thread.start()

    # effacer et regenerer la grille
    def clear():
        global root, canvas, text_id_message 
        etat_partage.running = False
        etat_partage.verrou = None 
        root.destroy()
        for row in range(rows):
            for col in range(cols):
                grid_values[row][col] = ""
        ihm_6x6.grille6x6("a")
        text_id_message = canvas.create_text(250, 465, text="La grille a été réinitialisée", font=('Helvetica', 10), fill="black")



    def home():
        from first_page import first_page 
        global root 
        etat_partage.running = False
        etat_partage.verrou = None 
        root.destroy()
        first_page()



    def valider():
        from vérification.verification import verification
        global text_id_message, grid_values
        if not verification.check_empty_cells(grid_values) :
            if not ihm_6x6.verifier():
                canvas.delete(text_id_message)
                text_id_message = canvas.create_text(310, 465, text="Malheureusement, la grille est fausse vous devez recommencer !", font=('Helvetica', 10), fill="black")
                return False
            canvas.delete(text_id_message)
            text_id_message = canvas.create_text(310, 465, text="Vous avez correctement complété la grille, félicitation !", font=('Helvetica', 10), fill="black")    
            return True
        canvas.delete(text_id_message)
        text_id_message = canvas.create_text(310, 465, text="Vous devez d'abord terminer la grille !", font=('Helvetica', 10), fill="black")
        
    def verifier():
        from vérification.verification import verification
        # Vérifier les lignes
        global text_id_message, grid_values
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

            if grid_values[row][col] == "":
                grid_values[row][col] = 0
                text_ids[row][col] = canvas.create_text(x, y, text="0", font=('Helvetica', 12), fill="green")
            elif grid_values[row][col] == 0:
                grid_values[row][col] = 1
                text_ids[row][col] = canvas.create_text(x, y, text="1", font=('Helvetica', 12), fill="green")
            elif grid_values[row][col] == 1:
                grid_values[row][col] = ''
                text_ids[row][col] = canvas.create_text(x, y, text='', font=('Helvetica', 12), fill="green")
                
    def on_close(self):
       
        print("Fermeture de la fenêtre...")
        etat_partage.running = False  # Mettre le drapeau à False pour arrêter les threads
        etat_partage.verrou = None 
        
        root.destroy()  # Détruire la fenêtre principale
    