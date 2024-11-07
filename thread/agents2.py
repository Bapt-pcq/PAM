import time
import etat_partage  # Importez le module partagé
import threading


class Agents2:
    # Fonction pour surveiller et réagir à la mise à jour de la variable
    
    
    grille_complete =0
    @staticmethod #afin que python puisse l'appeler dans la classe agent
    def resolution(row, col, taille,trou):  
        thread_name = threading.current_thread().name
        Mem_resolution = [None] * 15
        a_trouver=taille*taille-trou
        nb_0_ou_1 = taille / 2
        while etat_partage.running:
            with etat_partage.verrou:
                
                #grille_complete = all(all(case == 1 or case == 0 for case in row) for row in etat_partage.grid_values2)
                if Agents2.grille_complete==a_trouver:
                    
                    etat_partage.running = False
                    print("Grille complétée !")
                    
                    
                    print(etat_partage.grid_values2)
                    break

                Mem_resolution_row = etat_partage.grid_values2[row]
                grid_col = []
                # Parcourir chaque colonne de la grille
                for col_idx in range(len(etat_partage.grid_values2[0])):
                    current_column = [etat_partage.grid_values2[lig][col_idx] for lig in range(len(etat_partage.grid_values2))]
                    grid_col.append(current_column)

                Mem_resolution_col = grid_col[row]
                
                if Mem_resolution[0]!=Mem_resolution_col[row]:
                    #Mem_resolution[0]
                    
                    Mem_resolution[0]=Mem_resolution_col[row] #valeur de la case
                
                # Mem_resolution[1] : Deux cases au-dessus
                if row - 2 < 0:
                    if Mem_resolution[1] != -2:
                        Mem_resolution[1] = -2  # Case en dehors de la grille
                else:
                    if Mem_resolution[1] != Mem_resolution_col[row - 2]:
                        Mem_resolution[1] = Mem_resolution_col[row - 2]  # Valeur de la deuxième case au-dessus

                # Mem_resolution[2] : Une case au-dessus
                if row - 1 < 0:
                    if Mem_resolution[2] != -2:
                        Mem_resolution[2] = -2  # Case en dehors de la grille
                else:
                    if Mem_resolution[2] != Mem_resolution_col[row - 1]:
                        Mem_resolution[2] = Mem_resolution_col[row - 1]  # Valeur de la première case au-dessus

                # Mem_resolution[3] : Deux cases à droite
                if col + 2 >= len(Mem_resolution_row):
                    if Mem_resolution[3] != -2:
                        Mem_resolution[3] = -2  # Case en dehors de la grille
                else:
                    if Mem_resolution[3] != Mem_resolution_row[col + 2]:
                        Mem_resolution[3] = Mem_resolution_row[col + 2]  # Valeur de la deuxième case à droite

                # Mem_resolution[4] : Une case à droite
                if col + 1 >= len(Mem_resolution_row):
                    if Mem_resolution[4] != -2:
                        Mem_resolution[4] = -2  # Case en dehors de la grille
                else:
                    if Mem_resolution[4] != Mem_resolution_row[col + 1]:
                        Mem_resolution[4] = Mem_resolution_row[col + 1]  # Valeur de la première case à droite

                # Mem_resolution[5] : Deux cases en dessous
                if row + 2 >= len(Mem_resolution_col):
                    if Mem_resolution[5] != -2:
                        Mem_resolution[5] = -2  # Case en dehors de la grille
                else:
                    if Mem_resolution[5] != Mem_resolution_col[row + 2]:
                        Mem_resolution[5] = Mem_resolution_col[row + 2]  # Valeur de la deuxième case en dessous

                # Mem_resolution[6] : Une case en dessous
                if row + 1 >= len(Mem_resolution_col):
                    if Mem_resolution[6] != -2:
                        Mem_resolution[6] = -2  # Case en dehors de la grille
                else:
                    if Mem_resolution[6] != Mem_resolution_col[row + 1]:
                        Mem_resolution[6] = Mem_resolution_col[row + 1]  # Valeur de la première case en dessous

                # Mem_resolution[7] : Deux cases à gauche
                if col - 2 < 0:
                    if Mem_resolution[7] != -2:
                        Mem_resolution[7] = -2  # Case en dehors de la grille
                else:
                    if Mem_resolution[7] != Mem_resolution_row[col - 2]:
                        Mem_resolution[7] = Mem_resolution_row[col - 2]  # Valeur de la deuxième case à gauche

                # Mem_resolution[8] : Une case à gauche
                if col - 1 < 0:
                    if Mem_resolution[8] != -2:
                        Mem_resolution[8] = -2  # Case en dehors de la grille
                else:
                    if Mem_resolution[8] != Mem_resolution_row[col - 1]:
                        Mem_resolution[8] = Mem_resolution_row[col - 1]  # Valeur de la première case à gauche

                # Comptage des valeurs 1 et 0 dans la ligne et la colonne avec vérification
                nb_1_ligne = sum(1 for val in Mem_resolution_row if val == 1)   # Nombre de 1 dans la ligne
                nb_0_ligne = sum(1 for val in Mem_resolution_row if val == 0)   # Nombre de 0 dans la ligne
                nb_1_colonne = sum(1 for val in Mem_resolution_col if val == 1) # Nombre de 1 dans la colonne
                nb_0_colonne = sum(1 for val in Mem_resolution_col if val == 0) # Nombre de 0 dans la colonne

                if Mem_resolution[9]!=nb_1_ligne:
                    Mem_resolution[9]=nb_1_ligne
                    #Mem_resolution[9]
                
                if Mem_resolution[10]!=nb_0_ligne:
                    Mem_resolution[10]=nb_0_ligne
                    
                if Mem_resolution[11]!=nb_1_colonne:
                    Mem_resolution[11]=nb_1_colonne
                    
                if Mem_resolution[12]!=nb_0_colonne:
                    Mem_resolution[12]=nb_0_colonne
                
                if Mem_resolution[13]!=row:
                    Mem_resolution[13]=row
                    
                if Mem_resolution[14]!=col:
                    Mem_resolution[14]=col                    
                
                
                    
                    
                if etat_partage.text_ids2[Mem_resolution[13]][Mem_resolution[14]] != "Rempli": 
                    print(Mem_resolution)
                    
                    # Règles logiques pour déterminer la valeur
                    if Mem_resolution[1] == Mem_resolution[2] and Mem_resolution[2] != -2 and Mem_resolution[2] != -1 :
                        print("condition",1)
                        print(Mem_resolution)
                        Mem_resolution[0] = abs(Mem_resolution[1] - 1)
                        etat_partage.debug.append(("condition 1",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                    elif Mem_resolution[3] == Mem_resolution[4] and Mem_resolution[4] != -2 and Mem_resolution[4] != -1:
                        print("condition",2)
                        print(Mem_resolution)
                        Mem_resolution[0] = abs(Mem_resolution[3] - 1)
                        etat_partage.debug.append(("condition 2",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                    elif Mem_resolution[5] == Mem_resolution[6] and Mem_resolution[6] != -2 and Mem_resolution[6] != -1:
                        print("condition",3)
                        print(Mem_resolution)                               
                        Mem_resolution[0] = abs(Mem_resolution[5] - 1)
                        etat_partage.debug.append(("condition 3",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                    elif Mem_resolution[7] == Mem_resolution[8] and Mem_resolution[8] != -2 and Mem_resolution[8] != -1:
                        print("condition",4)
                        print(Mem_resolution)
                        Mem_resolution[0] = abs(Mem_resolution[7] - 1)
                        etat_partage.debug.append(("condition 4",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                    elif Mem_resolution[2] == Mem_resolution[6] and Mem_resolution[2] != -2 and Mem_resolution[2] != -1 :
                        print("condition",5)
                        print(Mem_resolution)
                        Mem_resolution[0] = abs(Mem_resolution[2] - 1)
                        etat_partage.debug.append(("condition 5",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                    elif Mem_resolution[4] == Mem_resolution[8] and Mem_resolution[4] != -2 and Mem_resolution[4] != -1:
                        print("condition",6)
                        print(Mem_resolution)
                        Mem_resolution[0] = abs(Mem_resolution[4] - 1)
                        etat_partage.debug.append(("condition 6",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                    elif Mem_resolution[9] == nb_0_ou_1:  # Nb de 1 dans la ligne atteint
                        print("condition",7)
                        print(Mem_resolution)
                        Mem_resolution[0] = 0
                        etat_partage.debug.append(("condition 7",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                    elif Mem_resolution[10] == nb_0_ou_1:  # Nb de 0 dans la ligne atteint
                        print("condition",8)
                        print(Mem_resolution)
                        Mem_resolution[0] = 1
                        etat_partage.debug.append(("condition 8",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                    elif Mem_resolution[11] == nb_0_ou_1:  # Nb de 1 dans la colonne atteint
                        print("condition",9)
                        print(Mem_resolution)
                        Mem_resolution[0] = 0
                        etat_partage.debug.append(("condition 9",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                    elif Mem_resolution[12] == nb_0_ou_1:  # Nb de 0 dans la colonne atteint
                        print("condition",10)
                        print(Mem_resolution)
                        Mem_resolution[0] = 1
                        etat_partage.debug.append(("condition 10",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution,"colone:",Mem_resolution_col))
                    
                    if Mem_resolution[0] == 1 or Mem_resolution[0] == 0: 
                        print("========================================================================================================")   
                        
                        
                        etat_partage.grid_values2[Mem_resolution[13]][Mem_resolution[14]] = Mem_resolution[0]
                        # x = 50 + Mem_resolution[14] * 60 + 60 // 2
                        # y = 50 + Mem_resolution[13] * 60 + 60 // 2
                        # valeur_str = str(Mem_resolution[0])
                        # etat_partage.root.after(0, lambda: Agents2.update_canvas_text(x, y, valeur_str))
                        # etat_partage.canvas.create_text(x, y, text=valeur_str, font=('Helvetica', 12), fill="green")
                        etat_partage.text_ids2[Mem_resolution[13]][Mem_resolution[14]] = "Rempli"
                        progress = True
                        print(Mem_resolution[13], Mem_resolution[14], "Trouvée ! Avec la valeur :", Mem_resolution[0])
                        print("je sors du thread", thread_name)
                        Agents2.grille_complete+=1 
                        print(Agents2.grille_complete) 
                        return
            time.sleep(0.1)  # Fréquence de vérification 
                        

                    
                    
             
            
            #print(Mem_resolution, row, col)
                    
    # def update_canvas_text(x,y,valeur_str):
    #     etat_partage.canvas.create_text(x, y, text=valeur_str, font=('Helvetica', 12), fill="green")
    
    