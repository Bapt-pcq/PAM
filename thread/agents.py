
import time
import etat_partage  # Importez le module partagé


class Agents :
     # # Fonction pour surveiller et réagir à la mise à jour de la variable
    def surveiller_valeur(row,col,grid_values):
        
        
        grid_col = []
               
        while  etat_partage.running:
            with  etat_partage.verrou:                   
                    Mem_row = grid_values[row]
                   
                    grid_col = []
        
                   # Parcourir chaque colonne de la grille
                    for col in range(len(grid_values[0])):
                        current_column = [grid_values[lig][col] for lig in range(len(grid_values))]
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
                    
            print(Mem,row,col)
            time.sleep(1)  # Fréquence de vérification    