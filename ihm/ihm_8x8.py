import tkinter as tk
import threading
import random
import threading
from grille.lecture import lecture
from thread1.agents import Agents
from thread1.agents2 import Agents2
import etat_partage  # Importez le module partagé
import time 


class ihm_8x8:


    def grille8x8(self, timer_enabled):
        global taille, text_id_message, rows, cols, cell_size,offset_x,offset_y
        taille =1
        # Définition des paramètres graphique
        etat_partage.root = tk.Tk()
        etat_partage.root.title("Grille 8x8")
        # Dimensions de la grille
        rows, cols = 8, 8
        cell_size = 50  # Taille des cellules en pixels
        # Création du canvas pour dessiner la grille
        etat_partage.canvas = tk.Canvas(etat_partage.root, width=cols*cell_size*1.9, height=rows*cell_size*1.3)
        etat_partage.canvas.pack()
        etat_partage.running=True
        etat_partage.text_ids = [[None for _ in range(cols)] for _ in range(rows)]
        etat_partage.grid_values = [["" for _ in range(cols)] for _ in range(rows)]
        etat_partage.text_ids2 = [[None for _ in range(cols)] for _ in range(rows)]
        etat_partage.grid_values2 = [["" for _ in range(cols)] for _ in range(rows)]
        text_id_message = None
        
        # Définir les décalages pour centrer la grille
        offset_x = 30  # Décalage horizontal
        offset_y = 20  # Décalage vertical
        
        # Dessin des lignes horizontales et verticales
        for i in range(rows + 1):
             etat_partage.canvas.create_line(offset_x, offset_y + i * cell_size, offset_x + cols * cell_size, offset_y + i * cell_size)  # Lignes horizontales
        for j in range(cols + 1):
             etat_partage.canvas.create_line(offset_x + j * cell_size, offset_y, offset_x + j * cell_size, offset_y + rows * cell_size)  # Lignes verticales
        etat_partage.canvas.bind("<Button-1>", ihm_8x8.on_click)
        
        ################################### Timer ##########################################
        self.timer_enabled = timer_enabled
        self.elapsed_time = 0  # Temps écoulé en secondes

        
        if self.timer_enabled :
            self.timer_label = tk.Label(etat_partage.root, text="Chronomètre : 0s")
            self.timer_label.pack()
            self.start_chronometer()
            
        #####################################################################################
        
        ############################## Aide #################################################
        # Ajouter le bouton d'aide
        button_aide = tk.Button(etat_partage.root, text="[?]", command=self.afficher_aide, width=4, height=1)
        #button_aide.pack(side='right'& 'bottom')  # Position en bas à droite width=760 ; height=520
        button_aide.place(x=760, y=520, anchor="se")
        #####################################################################################
        
        # creation des boutons
        button_clear = tk.Button(etat_partage.root, text="Réinitialiser", command=self.clear,width=15, height=3)
        button_verif = tk.Button(etat_partage.root, text="Vérifier", command=ihm_8x8.verifier,width=15, height=3)
        button_valider = tk.Button(etat_partage.root, text="Valider", command=self.afficher_msg_valider,width=15, height=3)
        button_home = tk.Button(etat_partage.root, text="Accueil", command=self.home,width=7, height=2)
        button_resoudre = tk.Button(etat_partage.root, text="Resolution", command=self.ecrire_valeur,width=15, height=3)
        button_aide = tk.Button(etat_partage.root, text="Aide", command=ihm_8x8.aide,width=15, height=3)
        
        # # Placement du bouton dans la fenêtre
        # button_clear.place(x=530, y=100)
        # button_verif.place(x=530, y=200)
        # button_valider.place(x=530, y=300)
        button_home.place(x=710, y=0)
        # button_resoudre.place(x=530, y=400)
        # button_aide.place(x=530, y=500)
        
        # Dimensions de la grille
        grid_width = 8 * 50  # Largeur totale de la grille
        grid_height = 8 * 50  # Hauteur totale de la grille

        # Position des boutons par rapport à la grille
        button_clear.place(x=grid_width + 150, y=grid_height // 2 - 100)  # Réinitialiser
        button_verif.place(x=grid_width + 150, y=grid_height // 2 - 50)   # Vérifier
        button_valider.place(x=grid_width + 150, y=grid_height // 2)      # Valider
        button_resoudre.place(x=grid_width + 150, y=grid_height // 2 + 50)  # Résolution
        button_aide.place(x=grid_width + 150, y=grid_height // 2 + 100)    # Aide
        
        etat_partage.canvas.create_text(590, 40, text="TAKUZU grille 8x8", font=('Helvetica', 20), fill="black")
        etat_partage.canvas.create_text(80, 440, text="Message", font=('Helvetica', 10), fill="black")
        etat_partage.canvas.create_rectangle(50, 450, 500, 480, outline="black", width=1, fill="")

        #numérotation ligne
        for i in range(8):
            etat_partage.canvas.create_text(offset_x-10, offset_y+10+50*i, text=i+1, font=('Helvetica', 10), fill="black")


        #numérotation colonne
        for i in range(8):
            etat_partage.canvas.create_text(offset_x+10+50*i, offset_y-10, text=i+1, font=('Helvetica', 10), fill="black")


        # Remplir le canvas avec les valeurs générées dans grid_values
               # Remplir le canvas avec les valeurs générées dans grid_values
        # Générer un nombre aléatoire entre 1 et 3
        nombre_aleatoire = random.randint(1, 3)
       
        if etat_partage.num_grille != 0 :
            nombre_aleatoire = etat_partage.num_grille
        # Remplir le canvas avec les valeurs générées dans grid_values
        if nombre_aleatoire==1:
            fichier_grille = "grille/8x8_1.txt"  # Chemin vers ton fichier txt
            etat_partage.num_grille=1
        elif nombre_aleatoire==2:
            fichier_grille = "grille/8x8_2.txt"  # Chemin vers ton fichier txt
            etat_partage.num_grille=2
        elif nombre_aleatoire==3:
            fichier_grille = "grille/8x8_3.txt"  # Chemin vers ton fichier txt
            etat_partage.num_grille=3
        
        grille = lecture.lire_grille_depuis_fichier(fichier_grille)
        
        for row in range(8):
            for col in range(8):
                print(grille[row][col])
                if grille[row][col]!=-1:
                    etat_partage.text_ids[row][col] = "Rempli"
                    etat_partage.text_ids2[row][col] = "Rempli"
                    etat_partage.canvas.create_text(offset_x+col * cell_size + cell_size // 2,offset_y+ row * cell_size + cell_size // 2, text=grille[row][col], font=('Helvetica', 12), fill="black")
                    etat_partage.grid_values[row][col]=grille[row][col]
                    etat_partage.grid_values2[row][col]=grille[row][col]
                else:
                    etat_partage.grid_values[row][col]=-1
                    etat_partage.grid_values2[row][col]=-1

            
        #Threads
        # etat_partage.verrou = threading.Lock()
        
        # #creation d'un thread par case
        # for i in range(8):  # Boucle pour les lignes
        #     for j in range(8):  # Boucle pour les colonnes
        #         ihm_8x8.create_thread(i, j)
        #ihm_6x6.etat_page()
        print(etat_partage.grid_values)
        etat_partage.verrou = threading.Lock()
        
        #Création des threads de résolution en arrière plan
        ihm_8x8.init_resolution()

        etat_partage.root.protocol("WM_DELETE_WINDOW", self.on_close)
            # Utilisation des fonctions
        return True
   
   
   
    def create_thread(i, j):
       
        thread_name = f"t{i}{j}"
        print(f"Création du thread {thread_name}")
        thread = threading.Thread(target=Agents.surveiller_valeur, args=(i, j), daemon=True, name=thread_name)
        thread.start()


      
  



    # effacer et regenerer la grille
    def clear(self):
        global text_id_message 
        etat_partage.running = False
        etat_partage.verrou = None 
        etat_partage.verrou2 = None   # Le verrou peut être initialisé dans le script principal pour synchroniser les threads
        etat_partage.canvas = None
        etat_partage.grid_values = None
        etat_partage.text_ids = None
        etat_partage.grid_values2 = None
        etat_partage.text_ids2 = None
        etat_partage.col_ligne = []

        etat_partage.grille_complete =0
        etat_partage.debug=[]
        etat_partage.root.destroy()
        etat_partage.root = None
        ihm_8x8.grille8x8(self, self.timer_enabled)
        text_id_message = etat_partage.canvas.create_text(250, 465, text="La grille a été réinitialisée", font=('Helvetica', 10), fill="black")



    def home(self):
        from first_page import first_page 
        etat_partage.running = False
        etat_partage.verrou = None 
        etat_partage.verrou2 = None   # Le verrou peut être initialisé dans le script principal pour synchroniser les threads
        etat_partage.canvas = None
        etat_partage.grid_values = None
        etat_partage.text_ids = None
        etat_partage.grid_values2 = None
        etat_partage.text_ids2 = None
        etat_partage.col_ligne = []
        etat_partage.num_grille = 0

        etat_partage.grille_complete =0
        etat_partage.debug=[]
        if self.timer_enabled ==True :
            self.stop_chronometer()
        etat_partage.root.destroy()
        etat_partage.root = None
        first_page()

    def afficher_msg_valider(self):
        from vérification.verification import verification
        global grid_values, text_id_message
        if verification.check_empty_cells(etat_partage.grid_values) : 
            etat_partage.canvas.delete(text_id_message)
            text_id_message = etat_partage.canvas.create_text(310, 465, text="Vous devez d'abord terminer la grille !", font=('Helvetica', 10), fill="black")
        else :
            ihm_8x8.valider()
            self.stop_chronometer()
            if self.timer_enabled == True :
                minutes = self.elapsed_time // 60
                seconds = self.elapsed_time % 60
                aide_message = (
                        "Félicitation, vous avez correctement completé la grille !\n\n"
                        f"Temps final de jeu : {minutes:02}:{seconds:02}"
                )
            else :
                aide_message = (
                        "Félicitation, vous avez correctement completé la grille !\n\n")
            tk.messagebox.showinfo("Bravo", aide_message)
            self.home()

    def valider():
        global text_id_message, grid_values
        from vérification.verification import verification
        if not verification.check_empty_cells(etat_partage.grid_values) :
            if not ihm_8x8.verifier():
                etat_partage.canvas.delete(text_id_message)
                text_id_message = etat_partage.canvas.create_text(310, 465, text="Malheureusement, la grille est fausse vous devez recommencer !", font=('Helvetica', 10), fill="black")
                return False
            etat_partage.canvas.delete(text_id_message)
            #text_id_message = canvas.create_text(310, 465, text="Vous avez correctement complété la grille, félicitation !", font=('Helvetica', 10), fill="black")    
            return True
         
    def verifier():
        # Vérifier les lignes
        global text_id_message
        from vérification.verification import verification
        if text_id_message != None:
            etat_partage.canvas.delete(text_id_message)
        if not verification.all_unique(etat_partage.grid_values):

            text_id_message = etat_partage.canvas.create_text(250, 465, text="Il y a une erreur, deux lignes sont identiques", font=('Helvetica', 10), fill="black")

            return False
        grid_col = []
        
        # Parcourir chaque colonne de la grille
        for col in range(len(etat_partage.grid_values[0])):
            # Initialiser une liste pour la colonne actuelle
            current_column = []
            
            # Parcourir chaque ligne pour extraire l'élément de la colonne actuelle
            for lig in range(len(etat_partage.grid_values)):
                current_column.append(etat_partage.grid_values[lig][col])
            
            # Ajouter la colonne actuelle à la liste des colonnes
            grid_col.append(current_column)
        if not verification.all_unique(grid_col):

            text_id_message = etat_partage.canvas.create_text(250, 465, text="Il y a une erreur, deux colonnes sont identiques", font=('Helvetica', 10), fill="black")

            return False
        for row in range(rows):
            if not verification.is_valid_sequence(etat_partage.grid_values[row]) :

                text_id_message = etat_partage.canvas.create_text(250, 465, text="Il y a une erreur dans la ligne "+ str(row + 1), font=('Helvetica', 10), fill="black")

                return False
            if not verification.has_equal_zeros_ones(etat_partage.grid_values[row]) :
                text_id_message = etat_partage.canvas.create_text(250, 465, text="Il y a une erreur dans la ligne " + str(row + 1) + " le nombre de 0 et de 1 est différent", font=('Helvetica', 10), fill="black")

                return False
        # Vérifier les colonnes
        for col in range(cols):
            column = [etat_partage.grid_values[row][col] for row in range(rows)]
            if not verification.is_valid_sequence(column) :
                text_id_message = etat_partage.canvas.create_text(250, 465, text="Il y a une erreur dans la colonne "+ str(col + 1), font=('Helvetica', 10), fill="black")

                return False
            if not verification.has_equal_zeros_ones(column):
                text_id_message = etat_partage.canvas.create_text(250, 465, text="Il y a une erreur dans la colonne " + str(col + 1) + " le nombre de 0 et de 1 est différent", font=('Helvetica', 10), fill="black")

                return False
        text_id_message = etat_partage.canvas.create_text(250, 465, text="Il n'y a pas d'erreur", font=('Helvetica', 10), fill="black")
        return True
    
    def init_resolution():
         #creation d'un thread par case
        trou=0
        print(etat_partage.text_ids2)
        for row in range(rows):
            for col in range(cols):
                if(etat_partage.text_ids2[row][col]=="Rempli"):
                    trou+=1
        for i in range(8):  # Boucle pour les lignes
            for j in range(8):  # Boucle pour les colonnes
                ihm_8x8.create_thread_resolution(i, j,trou)
        
    def create_thread_resolution(i, j,trou):
        thread_name = f"t{i}{j}b"
        print(f"Création du thread {thread_name}")
        thread = threading.Thread(target=Agents2.resolution, args=(i, j,8,trou), daemon=True, name=thread_name)
        thread.start()
        
    def ecrire_valeur(self):
        if self.timer_enabled ==True :
            self.stop_chronometer()
        for i in range(len(etat_partage.col_ligne)):
            
            col = etat_partage.col_ligne[i][1]
            row = etat_partage.col_ligne[i][0]
            x = offset_x + col * cell_size + cell_size // 2
            y = offset_y + row * cell_size + cell_size // 2

            # Ajouter ou modifier le texte au centre de la cellule cliquée

            if etat_partage.text_ids[row][col] is not None and etat_partage.text_ids[row][col] != "Rempli":
                
                if etat_partage.grid_values[row][col] != etat_partage.grid_values2[row][col]:
                    etat_partage.canvas.delete(etat_partage.text_ids[row][col])  # Effacer le texte existant
                    etat_partage.grid_values[row][col] = etat_partage.grid_values2[row][col]
                    valeur_str = str(etat_partage.grid_values[row][col])
                    etat_partage.text_ids[row][col] = etat_partage.canvas.create_text(x, y, text=valeur_str, font=('Helvetica', 12), fill="red")
            elif etat_partage.text_ids[row][col] != "Rempli" :
            
                etat_partage.grid_values[row][col] = etat_partage.grid_values2[row][col]
                valeur_str = str(etat_partage.grid_values[row][col])
                etat_partage.text_ids[row][col] = etat_partage.canvas.create_text(x, y, text=valeur_str, font=('Helvetica', 12), fill="blue")
            time.sleep(0.3)
            etat_partage.canvas.update_idletasks()   
             
    def aide():
        arret = 0
        i=0
        while arret==0:
            col = etat_partage.col_ligne[i][1]
            row = etat_partage.col_ligne[i][0]
            x = offset_x + col * cell_size + cell_size // 2
            y = offset_y + row * cell_size + cell_size // 2

            # Ajouter ou modifier le texte au centre de la cellule cliquée
            print(row,col,etat_partage.grid_values[row][col],etat_partage.grid_values2[row][col],etat_partage.text_ids[row][col])
            if etat_partage.text_ids[row][col] is not None and etat_partage.text_ids[row][col] != "Rempli":
                
                if etat_partage.grid_values[row][col] != etat_partage.grid_values2[row][col] and etat_partage.grid_values[row][col]!=-1:
                    etat_partage.canvas.delete(etat_partage.text_ids[row][col])  # Effacer le texte existant
                    etat_partage.grid_values[row][col] = etat_partage.grid_values2[row][col]
                    valeur_str = str(etat_partage.grid_values[row][col])
                    etat_partage.text_ids[row][col] = etat_partage.canvas.create_text(x, y, text=valeur_str, font=('Helvetica', 12), fill="red")
                    arret+=1
            elif etat_partage.text_ids[row][col] != "Rempli" :
            
                etat_partage.grid_values[row][col] = etat_partage.grid_values2[row][col]
                valeur_str = str(etat_partage.grid_values[row][col])
                etat_partage.text_ids[row][col] = etat_partage.canvas.create_text(x, y, text=valeur_str, font=('Helvetica', 12), fill="blue")
                arret+=1
            etat_partage.canvas.update_idletasks()
            i+=1   
                  
    def on_click(event):
        global cell_size,cols, rows, offset_x, offset_y
    # Trouver les coordonnées de la cellule cliquée en prenant en compte les offsets
        col = (event.x - offset_x) // cell_size
        row = (event.y - offset_y) // cell_size

        # Vérifier que les coordonnées sont dans la grille
        if 0 <= row < rows and 0 <= col < cols:
            # Calculer la position pour centrer le texte dans la cellule
            x = offset_x + col * cell_size + cell_size // 2
            y = offset_y + row * cell_size + cell_size // 2

            # Ajouter ou modifier le texte au centre de la cellule cliquée

            if etat_partage.text_ids[row][col] is not None:
                etat_partage.canvas.delete(etat_partage.text_ids[row][col])  # Effacer le texte existant

            if etat_partage.text_ids[row][col] == "Rempli" :
                return False

            if etat_partage.grid_values[row][col] == -1:
                etat_partage.grid_values[row][col] = 0
                etat_partage.text_ids[row][col] = etat_partage.canvas.create_text(x, y, text="0", font=('Helvetica', 12), fill="green")
            elif etat_partage.grid_values[row][col] == 0:
                etat_partage.grid_values[row][col] = 1
                etat_partage.text_ids[row][col] = etat_partage.canvas.create_text(x, y, text="1", font=('Helvetica', 12), fill="green")
            elif etat_partage.grid_values[row][col] == 1:
                etat_partage.grid_values[row][col] = -1
                etat_partage.text_ids[row][col] = etat_partage.canvas.create_text(x, y, text='', font=('Helvetica', 12), fill="green")
                etat_partage.text_ids[row][col] = None
    def on_close(self):
        
        print("Fermeture de la fenêtre...")
        etat_partage.running = False  # Mettre le drapeau à False pour arrêter les threads
        etat_partage.verrou = None
        etat_partage.root.destroy()  # Détruire la fenêtre principale
        

    def start_chronometer(self):
        self.elapsed_time += 1  # Incrémente le temps écoulé
        minutes = self.elapsed_time // 60  # Calcul des minutes
        seconds = self.elapsed_time % 60  # Calcul des secondes
        self.timer_label.config(text=f"Chronomètre : {minutes:02}:{seconds:02}")  # Affichage formaté MM:SS
        #root.after(1000, self.start_chronometer)  # Relance après 1 seconde
        self._chronometer_running = etat_partage.root.after(1000, self.start_chronometer)
        
    def stop_chronometer(self):
        if self.timer_enabled == True :
            etat_partage.root.after_cancel(self._chronometer_running)  # Annule l'appel programmé
            minutes = self.elapsed_time // 60
            seconds = self.elapsed_time % 60
            print(f"Temps final du chronomètre : {minutes:02}:{seconds:02}")
            self.timer_label.config(text=f"Chronomètre arrêté à : {minutes:02}:{seconds:02}")
            
        
    def afficher_aide(self):
        #"""Fonction appelée lors du clic sur le bouton Aide."""
        aide_message = (
            "Bienvenue dans le jeu Takuzu!\n\n"
            "Objectif : Remplir la grille en suivant ces règles :\n"
            "- Aucun chiffre ne doit se répéter plus de deux fois à la suite dans une ligne ou une colonne.\n"
            "- Chaque ligne et chaque colonne doivent contenir un nombre égal de 0 et de 1.\n"
            "- Les lignes et les colonnes doivent être uniques.\n\n"
            "Bonne chance!"
            )
        tk.messagebox.showinfo("Aide Takuzu", aide_message)