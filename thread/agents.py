import time
import etat_partage  # Importez le module partagé

class Agents:
    # Fonction pour surveiller et réagir à la mise à jour de la variable
    
    def surveiller_valeur(row, col, grid_values):
        global Mem
        
        grid_col = []
        
        while etat_partage.running:
            with etat_partage.verrou:
                Mem_row = grid_values[row]
                grid_col = []
        
                # Parcourir chaque colonne de la grille
                for col_idx in range(len(grid_values[0])):
                    current_column = [grid_values[lig][col_idx] for lig in range(len(grid_values))]
                    grid_col.append(current_column)

                Mem_col = grid_col[row]
                Mem = [
                    Mem_col[row],                              # Mem[0] : Valeur de la case 
                    Mem_col[row - 2] if row - 2 >= 0 else -2,  # Mem[1] : Deux cases au-dessus
                    Mem_col[row - 1] if row - 1 >= 0 else -2,  # Mem[2] : Une case au-dessus
                    Mem_row[col + 2] if col + 2 < len(Mem_row) else -2,  # Mem[3] : Deux cases à droite
                    Mem_row[col + 1] if col + 1 < len(Mem_row) else -2,  # Mem[4] : Une case à droite
                    Mem_col[row + 2] if row + 2 < len(Mem_col) else -2,  # Mem[5] : Deux cases en dessous
                    Mem_col[row + 1] if row + 1 < len(Mem_col) else -2,  # Mem[6] : Une case en dessous
                    Mem_row[col - 2] if col - 2 >= 0 else -2,  # Mem[7] : Deux cases à gauche
                    Mem_row[col - 1] if col - 1 >= 0 else -2   # Mem[8] : Une case à gauche
                ]

                # Comptages pour lignes et colonnes
                Mem.extend([
                    sum(1 for val in Mem_row if val == 1),  # Mem[9] : Nb de 1 dans la ligne
                    sum(1 for val in Mem_row if val == 0),  # Mem[10] : Nb de 0 dans la ligne
                    sum(1 for val in Mem_col if val == 1),  # Mem[11] : Nb de 1 dans la colonne
                    sum(1 for val in Mem_col if val == 0)   # Mem[12] : Nb de 0 dans la colonne
                ])
                
                Mem.append(row)  # Mem[13] : ligne de la case
                Mem.append(col)  # Mem[14] : colonne de la case
                
            print(Mem, row, col)
            time.sleep(2)  # Fréquence de vérification   
    
    
    def resolution(taille):  # fonction qui permet de résoudre la valeur de la case du thread à partir des valeurs évidentes
        global Mem 
        
        nb_0_ou_1 = taille / 2
        while etat_partage.running:
            with etat_partage.verrou:
                if Mem[1] == Mem[2] and Mem[1] != -2 and Mem[2] != -2 and Mem[1] != '' and Mem[2] != ''  :  # les 2 valeurs au-dessus sont identiques
                    Mem[0] = abs(Mem[1] - 1)
                elif Mem[3] == Mem[4] and Mem[3] != -2 and Mem[4] != -2 and Mem[3] != '' and Mem[4] != '':  # les 2 valeurs à droite sont identiques
                    Mem[0] = abs(Mem[3] - 1)        
                elif Mem[5] == Mem[6] and Mem[5] != -2 and Mem[6] != -2 and Mem[5] != '' and Mem[6] != '':  # les 2 valeurs en dessous sont identiques
                    Mem[0] = abs(Mem[5] - 1)       
                elif Mem[7] == Mem[8] and Mem[7] != -2 and Mem[8] != -2 and Mem[7] != '' and Mem[8] != '':  # les 2 valeurs à gauche sont identiques
                    Mem[0] = abs(Mem[7] - 1)
                elif Mem[2] == Mem[6] and Mem[2] != -2 and Mem[6] != -2 and Mem[2] != '' and Mem[6] != '':  # les 2 premières valeurs en dessous et au-dessus sont identiques
                    Mem[0] = abs(Mem[2] - 1)
                elif Mem[4] == Mem[8] and Mem[4] != -2 and Mem[8] != -2 and Mem[4] != '' and Mem[8] != '':  # les 2 premières valeurs à droite et à gauche sont identiques
                    Mem[0] = abs(Mem[2] - 1)
                elif Mem[9] == nb_0_ou_1:  # le nombre de 1 dans la ligne a atteint la valeur max
                    Mem[0] = 0  # Correction d'affectation
                elif Mem[10] == nb_0_ou_1:  # le nombre de 0 dans la ligne a atteint la valeur max
                    Mem[0] = 1  # Correction d'affectation
                elif Mem[11] == nb_0_ou_1:  # le nombre de 1 dans la colonne a atteint la valeur max
                    Mem[0] = 0  # Correction d'affectation
                elif Mem[12] == nb_0_ou_1:  # le nombre de 0 dans la colonne a atteint la valeur max
                    Mem[0] = 1  # Correction d'affectation
            if Mem[0]==1 or Mem[0]==0:    
                if taille == 6:
                    from ihm.ihm_6x6 import ihm_6x6  # L'importation ici devrait être gérée
                    print("j'écris", Mem[0])
                    ihm_6x6.ecrire_valeur(Mem[13], Mem[14], Mem[0])
                break 
        print(Mem[13], Mem[14], "Trouvée ! Avec la valeur :", Mem[0]) 
