import time
import etat_partage  # Importez le module partagé
import threading
class Agents:
    # Fonction pour surveiller et réagir à la mise à jour de la variable
    @staticmethod #afin que python puisse l'appeler dans la classe agent
    def surveiller_valeur(row, col):
        
        
        
        Mem = [None]*15
        while etat_partage.running:
            with etat_partage.verrou:
                Mem_row = etat_partage.grid_values[row]
                grid_col = []
        
                # Parcourir chaque colonne de la grille
                for col_idx in range(len(etat_partage.grid_values[0])):
                    current_column = [etat_partage.grid_values[lig][col_idx] for lig in range(len(etat_partage.grid_values))]
                    grid_col.append(current_column)

                Mem_col = grid_col[row]

                if Mem[0]!=Mem_col[row]:
                    #Mem[0]
                    
                    Mem[0]=Mem_col[row] #valeur de la case
                
                # Mem[1] : Deux cases au-dessus
                if row - 2 < 0:
                    if Mem[1] != -2:
                        Mem[1] = -2  # Case en dehors de la grille
                else:
                    if Mem[1] != Mem_col[row - 2]:
                        Mem[1] = Mem_col[row - 2]  # Valeur de la deuxième case au-dessus

                # Mem[2] : Une case au-dessus
                if row - 1 < 0:
                    if Mem[2] != -2:
                        Mem[2] = -2  # Case en dehors de la grille
                else:
                    if Mem[2] != Mem_col[row - 1]:
                        Mem[2] = Mem_col[row - 1]  # Valeur de la première case au-dessus

                # Mem[3] : Deux cases à droite
                if col + 2 >= len(Mem_row):
                    if Mem[3] != -2:
                        Mem[3] = -2  # Case en dehors de la grille
                else:
                    if Mem[3] != Mem_row[col + 2]:
                        Mem[3] = Mem_row[col + 2]  # Valeur de la deuxième case à droite

                # Mem[4] : Une case à droite
                if col + 1 >= len(Mem_row):
                    if Mem[4] != -2:
                        Mem[4] = -2  # Case en dehors de la grille
                else:
                    if Mem[4] != Mem_row[col + 1]:
                        Mem[4] = Mem_row[col + 1]  # Valeur de la première case à droite

                # Mem[5] : Deux cases en dessous
                if row + 2 >= len(Mem_col):
                    if Mem[5] != -2:
                        Mem[5] = -2  # Case en dehors de la grille
                else:
                    if Mem[5] != Mem_col[row + 2]:
                        Mem[5] = Mem_col[row + 2]  # Valeur de la deuxième case en dessous

                # Mem[6] : Une case en dessous
                if row + 1 >= len(Mem_col):
                    if Mem[6] != -2:
                        Mem[6] = -2  # Case en dehors de la grille
                else:
                    if Mem[6] != Mem_col[row + 1]:
                        Mem[6] = Mem_col[row + 1]  # Valeur de la première case en dessous

                # Mem[7] : Deux cases à gauche
                if col - 2 < 0:
                    if Mem[7] != -2:
                        Mem[7] = -2  # Case en dehors de la grille
                else:
                    if Mem[7] != Mem_row[col - 2]:
                        Mem[7] = Mem_row[col - 2]  # Valeur de la deuxième case à gauche

                # Mem[8] : Une case à gauche
                if col - 1 < 0:
                    if Mem[8] != -2:
                        Mem[8] = -2  # Case en dehors de la grille
                else:
                    if Mem[8] != Mem_row[col - 1]:
                        Mem[8] = Mem_row[col - 1]  # Valeur de la première case à gauche

                # Comptage des valeurs 1 et 0 dans la ligne et la colonne avec vérification
                nb_1_ligne = sum(1 for val in Mem_row if val == 1)   # Nombre de 1 dans la ligne
                nb_0_ligne = sum(1 for val in Mem_row if val == 0)   # Nombre de 0 dans la ligne
                nb_1_colonne = sum(1 for val in Mem_col if val == 1) # Nombre de 1 dans la colonne
                nb_0_colonne = sum(1 for val in Mem_col if val == 0) # Nombre de 0 dans la colonne

                if Mem[9]!=nb_1_ligne:
                    Mem[9]=nb_1_ligne
                    #Mem[9]
                
                if Mem[10]!=nb_0_ligne:
                    Mem[10]=nb_0_ligne
                    
                if Mem[11]!=nb_1_colonne:
                    Mem[11]=nb_1_colonne
                    
                if Mem[12]!=nb_0_colonne:
                    Mem[12]=nb_0_colonne
                
                if Mem[13]!=row:
                    Mem[13]=row
                    
                if Mem[14]!=col:
                    Mem[14]=col                    
                
            #print(Mem, row, col)
            time.sleep(0.1)  # Fréquence de vérification   
    
   