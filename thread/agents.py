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
    
    @staticmethod
    def resolution(taille):  # fonction qui permet de résoudre la valeur de la case du thread à partir des valeurs évidentes
        nb_0_ou_1 = taille / 2
        threads = []  # Liste pour stocker les threads
        while etat_partage.running:
            progress = False  # Indicateur de progression pour vérifier si on avance
            with etat_partage.verrou:
            # Parcourir toute la grille
                    
                    if Mem[0] not in (1, 0):  # Case non remplie
                        print("case non rempli")
                        
                        if Mem[0] ==-1: 
                            print("je cherche")
                            print(Mem)
                            # Règles logiques pour déterminer la valeur
                            if Mem[1] == Mem[2] and Mem[2] != -2 and Mem[2] != -1 :
                                print("condition",1)
                                print(Mem)
                                Mem[0] = abs(Mem[1] - 1)
                            elif Mem[3] == Mem[4] and Mem[4] != -2 and Mem[4] != -1:
                                print("condition",2)
                                print(Mem)
                                Mem[0] = abs(Mem[3] - 1)
                            elif Mem[5] == Mem[6] and Mem[6] != -2 and Mem[6] != -1:
                                print("condition",3)
                                print(Mem)                               
                                Mem[0] = abs(Mem[5] - 1)
                            elif Mem[7] == Mem[8] and Mem[8] != -2 and Mem[8] != -1:
                                print("condition",4)
                                print(Mem)
                                Mem[0] = abs(Mem[7] - 1)
                            elif Mem[2] == Mem[6] and Mem[2] != -2 and Mem[2] != -1 :
                                print("condition",5)
                                print(Mem)
                                Mem[0] = abs(Mem[2] - 1)
                            elif Mem[4] == Mem[8] and Mem[4] != -2 and Mem[4] != -1:
                                print("condition",6)
                                print(Mem)
                                Mem[0] = abs(Mem[4] - 1)
                            elif Mem[9] == nb_0_ou_1:  # Nb de 1 dans la ligne atteint
                                print("condition",7)
                                print(Mem)
                                Mem[0] = 0
                            elif Mem[10] == nb_0_ou_1:  # Nb de 0 dans la ligne atteint
                                print("condition",8)
                                print(Mem)
                                Mem[0] = 1
                            elif Mem[11] == nb_0_ou_1:  # Nb de 1 dans la colonne atteint
                                print("condition",9)
                                print(Mem)
                                Mem[0] = 0
                            elif Mem[12] == nb_0_ou_1:  # Nb de 0 dans la colonne atteint
                                print("condition",10)
                                print(Mem)
                                Mem[0] = 1

                            if Mem[0] == 1 or Mem[0] == 0:    
                                etat_partage.grid_values[Mem[13]][Mem[14]] = Mem[0]
                                x = 50 + Mem[14] * 60 + 60 // 2
                                y = 50 + Mem[13] * 60 + 60 // 2
                                valeur_str = str(Mem[0])
                                etat_partage.text_ids[Mem[13]][Mem[14]] = etat_partage.canvas.create_text(x, y, text=valeur_str, font=('Helvetica', 12), fill="green")
                                etat_partage.text_ids[Mem[13]][Mem[14]] = "Rempli"
                                progress = True
                                print(Mem[13], Mem[14], "Trouvée ! Avec la valeur :", Mem[0])
                    
            time.sleep(2)  # Fréquence de vérification   
            grille_complete = all(all(case == 1 or case == 0 for case in row) for row in etat_partage.grid_values)
            if grille_complete:
                etat_partage.running = False
                print("Grille complétée !")
                break


