
import time
import etat_partage  # Importez le module partagé
import threading


class Agents_10x10:
    # Fonction pour surveiller et réagir à la mise à jour de la variable
    
    
    
    @staticmethod #afin que python puisse l'appeler dans la classe agent
    def resolution(row, col, taille,trou):  
        thread_name = threading.current_thread().name
        Mem_resolution = [None] * 51
        a_trouver=taille*taille-trou
        nb_0_ou_1 = taille / 2
        tour = 0
        print(etat_partage.grid_values2)
        while etat_partage.running:
            with etat_partage.verrou:
                
                #grille_complete = all(all(case == 1 or case == 0 for case in row) for row in etat_partage.grid_values2)
                if etat_partage.grille_complete==a_trouver or tour == 30:
                    
                    etat_partage.test ==1
                    etat_partage.running = False
                    print("Grille complétée !")
                    tour = 0
                    
                    
                    print(etat_partage.grid_values2)
                    break
                    
                Mem_resolution_row = etat_partage.grid_values2[row]
                grid_col = []
                # Parcourir chaque colonne de la grille
                for col_idx in range(len(etat_partage.grid_values2[0])):
                    current_column = [etat_partage.grid_values2[lig][col_idx] for lig in range(len(etat_partage.grid_values2))]
                    grid_col.append(current_column)

                Mem_resolution_col = grid_col[col]
                #print("Mem col.", Mem_resolution_col, "row :",row, "col :",col)
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

                # 3 à 9 cases au dessus Mem[15]->Mem[23]
                for i in range(9):
                    if row - 1-i < 0:
                        if Mem_resolution[15+i] != -2:
                            Mem_resolution[15+i] = -2  # Case en dehors de la grille
                    else:
                        if Mem_resolution[15+i] != Mem_resolution_col[row - 1-i]:
                            Mem_resolution[15+i] = Mem_resolution_col[row - 1-i]  
                            
                # 3 à 9 cases à droite Mem[24] -> Mem[32]
                for i in range(9):
                    if col + 1 +i >= len(Mem_resolution_row):
                        if Mem_resolution[24+i] != -2:
                            Mem_resolution[24+i] = -2  # Case en dehors de la grille
                    else:
                        if Mem_resolution[24+i] != Mem_resolution_row[col + 1+i]:
                            Mem_resolution[24+i] = Mem_resolution_row[col + 1+i]  
                # 3 à 9 cases en dessous Mem[33] -> Mem[41]
                for i in range(9):
                    if row + 1+i >= len(Mem_resolution_col):
                        if Mem_resolution[33+i] != -2:
                            Mem_resolution[33+i] = -2  # Case en dehors de la grille
                    else:
                        if Mem_resolution[33+i] != Mem_resolution_col[row + 1+i]:
                            Mem_resolution[33+i] = Mem_resolution_col[row + 1+i]        
                # 3 à 9 cases a gauche Mem[42] -> Mem[50]
                for i in range(9):
                    if col - 1 -i < 0:
                        if Mem_resolution[42+i] != -2:
                            Mem_resolution[42+i] = -2  # Case en dehors de la grille
                    else:
                        if Mem_resolution[42+i] != Mem_resolution_row[col - 1-i]:
                            Mem_resolution[42+i] = Mem_resolution_row[col - 1-i]       
                        
                if etat_partage.text_ids2[Mem_resolution[13]][Mem_resolution[14]] != "Rempli": 
                    #print(Mem_resolution)
                    if Mem_resolution[0] != 1 and Mem_resolution[0] != 0 :
                        # Règles logiques pour déterminer la valeur
                        if Mem_resolution[1] == Mem_resolution[2] and Mem_resolution[2] != -2 and Mem_resolution[2] != -1 : #Règle 1 : Les 2 valeurs au dessus sont identiques, alors Mem[0] égal la valeur opposée
                            Mem_resolution[0] = abs(Mem_resolution[1] - 1)
                            etat_partage.debug.append(("condition 1",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution)) #stockage des informations dans l'ordre de complétion
                        elif Mem_resolution[3] == Mem_resolution[4] and Mem_resolution[4] != -2 and Mem_resolution[4] != -1: #Règle 2 : Les 2 valeurs à droite sont identiques, alors Mem[0] égal la valeur opposée
                            Mem_resolution[0] = abs(Mem_resolution[3] - 1)
                            etat_partage.debug.append(("condition 2",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                        elif Mem_resolution[5] == Mem_resolution[6] and Mem_resolution[6] != -2 and Mem_resolution[6] != -1: #Règle 3 : Les 2 valeurs en dessous sont identiques, alors Mem[0] égal la valeur opposée                            
                            Mem_resolution[0] = abs(Mem_resolution[5] - 1)
                            etat_partage.debug.append(("condition 3",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                        elif Mem_resolution[7] == Mem_resolution[8] and Mem_resolution[8] != -2 and Mem_resolution[8] != -1: #Règle 4 : Les 2 valeurs à gauches sont identiques, alors Mem[0] égal la valeur opposée
                            Mem_resolution[0] = abs(Mem_resolution[7] - 1)
                            etat_partage.debug.append(("condition 4",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                        elif Mem_resolution[2] == Mem_resolution[6] and Mem_resolution[2] != -2 and Mem_resolution[2] != -1 : #Règle 5 : Les 2 valeurs de la colonne entourant la case sont identiques, alors Mem[0] égal la valeur opposée
                            Mem_resolution[0] = abs(Mem_resolution[2] - 1)
                            etat_partage.debug.append(("condition 5",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                        elif Mem_resolution[4] == Mem_resolution[8] and Mem_resolution[4] != -2 and Mem_resolution[4] != -1: #Règle 6 : Les 2 valeurs de la ligne entourant la case sont identiques, alors Mem[0] égal la valeur opposée
                            Mem_resolution[0] = abs(Mem_resolution[4] - 1)
                            etat_partage.debug.append(("condition 6",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                        elif Mem_resolution[9] == nb_0_ou_1:  # Règle 7 : Nb de 1 dans la ligne atteint, alors Mem[0]=0
                            Mem_resolution[0] = 0
                            etat_partage.debug.append(("condition 7",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                        elif Mem_resolution[10] == nb_0_ou_1:  # Règle 8 :Nb de 0 dans la ligne atteint, alors Mem[0]=1
                            Mem_resolution[0] = 1
                            etat_partage.debug.append(("condition 8",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                        elif Mem_resolution[11] == nb_0_ou_1:  # Règle 9 :Nb de 1 dans la colonne atteint, alors Mem[0]=0
                            Mem_resolution[0] = 0
                            etat_partage.debug.append(("condition 9",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                        elif Mem_resolution[12] == nb_0_ou_1:  # Règle 10 :Nb de 0 dans la colonne atteint, alors Mem[0]=1
                            Mem_resolution[0] = 1
                            etat_partage.debug.append(("condition 10",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution,"colone:",Mem_resolution_col))
                        if tour>10:   #les conditions suivantes entre en jeux uniquement si l'on commence à boucler plus de 10 fois
                            if Mem_resolution[1] ==-1 and Mem_resolution[2] ==-1 and Mem_resolution[6] ==-1 : #on vérifie si 3 valeurs spécifiques sont vides
                            
                                if Mem_resolution[11] == (taille/2 -1) and Mem_resolution[5] ==0 : #Règle 11 : Les 2 valeurs au dessus et celle en dessous sont vides, il reste un seul 1 dans la colonne, la valeur 2 cases en dessous est égal à 0, alors Mem[0] = 1
                                    Mem_resolution[0] = 1
                                    etat_partage.debug.append(("condition 11",Mem_resolution[13],Mem_resolution[14],1, "Mem :", Mem_resolution)) 
                                elif Mem_resolution[11] == (taille/2 -1) and Mem_resolution[5] ==1 :#Règle 12 : Les 2 valeurs au dessus et celle en dessous sont vides, il reste un seul 1 dans la colonne, la valeur 2 cases en dessous est égal à 1, alors la valeur en dessous et 2 au dessus sont égals à 0
                                    
                                    row_bis = Mem_resolution[13]+1
                                    col_bis = Mem_resolution[14]
                                    etat_partage.grid_values2[row_bis][col_bis] = 0
                                    etat_partage.debug.append(("condition 12",row_bis,col_bis,0, "Mem :", Mem_resolution))

                                    #Mem_resolution[1] == 0
                                    row_bis2 = Mem_resolution[13]-2
                                    col_bis2 = Mem_resolution[14]
                                    etat_partage.grid_values2[row_bis2][col_bis2] = 0
                                    etat_partage.debug.append(("condition 12",row_bis2,col_bis2,0, "Mem :", Mem_resolution))                              
                                    
                                elif Mem_resolution[12] == (taille/2 -1) and Mem_resolution[5] ==0 :  #Règle 13 : Les 2 valeurs au dessus et celle en dessous sont vides, il reste un seul 0 dans la colonne, la valeur 2 cases en dessous est égal à 0, , alors la valeur en dessous et 2 au dessus sont égals à 1
                                    
                                    row_bis = Mem_resolution[13]+1
                                    col_bis = Mem_resolution[14]
                                    etat_partage.grid_values2[row_bis][col_bis] = 1
                                    etat_partage.debug.append(("condition 13",row_bis,col_bis,1, "Mem :", Mem_resolution))
                                    
                                    #Mem_resolution[1] == 1
                                    row_bis2 = Mem_resolution[13]-2
                                    col_bis2 = Mem_resolution[14]
                                    etat_partage.grid_values2[row_bis2][col_bis2] = 1
                                    etat_partage.debug.append(("condition 13",row_bis2,col_bis2,1, "Mem :", Mem_resolution)) 
                                elif Mem_resolution[12] == (taille/2 -1) and Mem_resolution[5] ==1 : #Règle 14 : Les 2 valeurs au dessus et celle en dessous sont vides, il reste un seul 0 dans la colonne, la valeur 2 cases en dessous est égal à 1, alors Mem[0] = 0
                                    Mem_resolution[0] = 0
                                    etat_partage.debug.append(("condition 14",Mem_resolution[13],Mem_resolution[14],0, "Mem :", Mem_resolution)) 
                            elif Mem_resolution[2]== -1 and Mem_resolution[6]== -1 and Mem_resolution[5] == -1 :
                                if Mem_resolution[11] == (taille/2 -1) and Mem_resolution[1] ==0 : #Règle 15 : Les 2 valeurs en dessous et celle au dessus sont vides, il reste un seul 1 dans la colonne, la valeur 2 cases au dessus est égal à 0, alors Mem[0] = 1
                                    Mem_resolution[0] = 1
                                    etat_partage.debug.append(("condition 15",Mem_resolution[13],Mem_resolution[14],1, "Mem :", Mem_resolution)) 
                                elif Mem_resolution[11] == (taille/2 -1) and Mem_resolution[1] ==1 :  #Règle 16 : Les 2 valeurs en dessous et celle au dessus sont vides, il reste un seul 1 dans la colonne, la valeur 2 cases au dessus est égal à 1, alors la valeur en dessous et 2 au dessus sont égals à 0
                                    #Mem_resolution[2] == 0
                                    row_bis = Mem_resolution[13]-1
                                    col_bis = Mem_resolution[14]
                                    etat_partage.grid_values2[row_bis][col_bis] = 0
                                    etat_partage.debug.append(("condition 16",row_bis,col_bis,0, "Mem :", Mem_resolution))
                                    #Mem_resolution[5] == 0
                                    row_bis2 = Mem_resolution[13]+2
                                    col_bis2 = Mem_resolution[14]
                                    etat_partage.grid_values2[row_bis2][col_bis2] = 0
                                    etat_partage.debug.append(("condition 16",row_bis2,col_bis2,0, "Mem :", Mem_resolution)) 
                                elif Mem_resolution[12] == (taille/2 -1) and Mem_resolution[1] ==0 : #Règle 17 : Les 2 valeurs en dessous et celle au dessus sont vides, il reste un seul 0 dans la colonne, la valeur 2 cases au dessus est égal à 0, alors la valeur en dessous et 2 au dessus sont égals à 1
                                    #Mem_resolution[2] == 1
                                    row_bis = Mem_resolution[13]-1
                                    col_bis = Mem_resolution[14]
                                    etat_partage.grid_values2[row_bis][col_bis] = 1
                                    etat_partage.debug.append(("condition 17",row_bis,col_bis,1, "Mem :", Mem_resolution))
                                    
                                    #Mem_resolution[5] == 1
                                    row_bis2 = Mem_resolution[13]+2
                                    col_bis2 = Mem_resolution[14]
                                    etat_partage.grid_values2[row_bis2][col_bis2] = 1
                                    etat_partage.debug.append(("condition 17",row_bis2,col_bis2,1, "Mem :", Mem_resolution)) 
                                elif Mem_resolution[12] == (taille/2 -1) and Mem_resolution[1] ==1 : #Règle 18 : Les 2 valeurs en dessous et celle au dessus sont vides, il reste un seul 0 dans la colonne, la valeur 2 cases au dessus est égal à 1, alors Mem[0] = 0
                                    Mem_resolution[0] = 0
                                    etat_partage.debug.append(("condition 18",Mem_resolution[13],Mem_resolution[14],1, "Mem :", Mem_resolution)) 
                            elif Mem_resolution[3]== -1 and Mem_resolution[4]== -1 and Mem_resolution[8] == -1 :
                                if Mem_resolution[9] == (taille/2 -1) and Mem_resolution[7]==0 : #Règle 19 : Les 2 valeurs à droite et celle à gauche sont vides, il reste un seul 1 dans la ligne, la valeur 2 cases à gauche est égal à 0, alors Mem[0] = 1
                                    Mem_resolution[0]=1
                                    etat_partage.debug.append(("condition 19",Mem_resolution[13],Mem_resolution[14],1, "Mem :", Mem_resolution)) 
                                elif Mem_resolution[9] == (taille/2 -1) and Mem_resolution[7]==1 : #Règle 20 : Les 2 valeurs à droite et celle à gauche sont vides, il reste un seul 1 dans la ligne, la valeur 2 cases à gauche est égal à 1, alors la valeur à gauche et celle 2 à droite sont égals à 0
                                    # Mem_resolution[8]=0
                                    row_bis = Mem_resolution[13]
                                    col_bis = Mem_resolution[14]-1
                                    etat_partage.grid_values2[row_bis][col_bis] = 0
                                    etat_partage.debug.append(("condition 20",row_bis,col_bis,0, "Mem :", Mem_resolution))
                                    #Mem_resolution[3]=0
                                    row_bis2 = Mem_resolution[13]
                                    col_bis2 = Mem_resolution[14]+2
                                    etat_partage.grid_values2[row_bis2][col_bis2] = 0
                                    etat_partage.debug.append(("condition 20",row_bis2,col_bis2,0, "Mem :", Mem_resolution)) 
                                elif Mem_resolution[10] == (taille/2 -1) and Mem_resolution[7]==0 : #Règle 21 : Les 2 valeurs à droite et celle à gauche sont vides, il reste un seul 0 dans la ligne, la valeur 2 cases à gauche est égal à 0, alors la valeur à gauche et celle 2 à droite sont égals à 1
                                    # Mem_resolution[8]=1
                                    row_bis = Mem_resolution[13]
                                    col_bis = Mem_resolution[14]-1
                                    etat_partage.grid_values2[row_bis][col_bis] = 1
                                    etat_partage.debug.append(("condition 21",row_bis,col_bis,1, "Mem :", Mem_resolution))
                                    #Mem_resolution[3]=1
                                    row_bis2 = Mem_resolution[13]+2
                                    col_bis2 = Mem_resolution[14]
                                    etat_partage.grid_values2[row_bis2][col_bis2] = 1
                                    etat_partage.debug.append(("condition 21",row_bis2,col_bis2,1, "Mem :", Mem_resolution)) 
                                elif Mem_resolution[10] == (taille/2 -1) and Mem_resolution[7]==1 : #Règle 22 : Les 2 valeurs à droite et celle à gauche sont vides, il reste un seul 0 dans la ligne, la valeur 2 cases à gauche est égal à 1, alors Mem[0] = 0
                                    Mem_resolution[0]=0
                                    etat_partage.debug.append(("condition 22",Mem_resolution[13],Mem_resolution[14],0, "Mem :", Mem_resolution)) 
                            elif Mem_resolution[7]== -1 and Mem_resolution[8]== -1 and Mem_resolution[4] ==-1 :
                                
                                if Mem_resolution[9] == (taille/2 -1) and Mem_resolution[3]==0 : #Règle 23 : Les 2 valeurs à gauche et celle à droite sont vides, il reste un seul 1 dans la ligne, la valeur 2 cases à droite est égal à 0, alors Mem[0] = 1
                                    Mem_resolution[0]=1
                                    etat_partage.debug.append(("condition 23",Mem_resolution[13],Mem_resolution[14],1, "Mem :", Mem_resolution)) 
                                elif Mem_resolution[9] == (taille/2 -1) and Mem_resolution[3]==1 : #Règle 24 : Les 2 valeurs à gauche et celle à droite sont vides, il reste un seul 1 dans la ligne, la valeur 2 cases à droite est égal à 1, alors la valeur à droite et celle 2 à gauche sont égals à 0
                                    # Mem_resolution[4]=0
                                    row_bis = Mem_resolution[13]
                                    col_bis = Mem_resolution[14]+1
                                    etat_partage.grid_values2[row_bis][col_bis] = 0
                                    etat_partage.debug.append(("condition 24",row_bis,col_bis,0, "Mem :", Mem_resolution))
                                    #Mem_resolution[7]=0
                                    row_bis2 = Mem_resolution[13]
                                    col_bis2 = Mem_resolution[14]-2
                                    etat_partage.grid_values2[row_bis2][col_bis2] = 0
                                    etat_partage.debug.append(("condition 24",row_bis2,col_bis2,0, "Mem :", Mem_resolution)) 
                                elif Mem_resolution[10] == (taille/2 -1) and Mem_resolution[3]==0 : #Règle 25 : Les 2 valeurs à gauche et celle à droite sont vides, il reste un seul 0 dans la ligne, la valeur 2 cases à droite est égal à 0, alors la valeur à droite et celle 2 à gauche sont égals à 1
                                    # Mem_resolution[4]=1
                                    row_bis = Mem_resolution[13]
                                    col_bis = Mem_resolution[14]+1
                                    etat_partage.grid_values2[row_bis][col_bis] = 1
                                    etat_partage.debug.append(("condition 25",row_bis,col_bis,1, "Mem :", Mem_resolution))
                                    #Mem_resolution[7]=1
                                    row_bis2 = Mem_resolution[13]
                                    col_bis2 = Mem_resolution[14]-2
                                    etat_partage.grid_values2[row_bis2][col_bis2] = 1
                                    etat_partage.debug.append(("condition 25",row_bis2,col_bis2,1, "Mem :", Mem_resolution)) 
                                elif Mem_resolution[10] == (taille/2 -1) and Mem_resolution[3]==1 : #Règle 26 : Les 2 valeurs à gauche et celle à droite sont vides, il reste un seul 0 dans la ligne, la valeur 2 cases à droite est égal à 1, alors Mem[0] = 0
                                    Mem_resolution[0]=0
                                    etat_partage.debug.append(("condition 26",Mem_resolution[13],Mem_resolution[14],0, "Mem :", Mem_resolution)) 
                        if tour>20 : 
                            #Les indices de la Mem correspondant à la ligne ou la colonne
                            Mem_lignes = [24,25,26,27,28,29,30,31,32,42,43,44,45,46,47,48,49,50]
                            Mem_colonnes = [15,16,17,18,19,20,21,22,23,33,34,35,36,37,38,39,40,41]
                            #On crée une nouvelle liste pour stocker les indices ayant un -1 
                            indices =[]
                            #on travail sur la ligne
                            if Mem_resolution[9] ==(taille/2 -1) or Mem_resolution[10] ==(taille/2 -1):
                                for i in Mem_lignes :
                                    if Mem_resolution[i] == -1 :
                                        indices.append(i) #on recupere les indices vide dans la ligne
                                indices_0 = [24,42] #indices voisin à Mem[0]
                                valeur = 0
                                num_final = 0
                                
                                if len(indices)==2 :
                                    for num in indices_0 :
                                        if num in indices :
                                            valeur +=1
                                            num_final = num #indice voisin
                                            indices.remove(num)
                                            
                                    
                                    if valeur == 1 : #Si 1 seul valeur voisine
                                        #case a ecrire
                                        if 24 <= indices[0] <= 32 :
                                            row_bis2 = Mem_resolution[13]
                                            col_bis2 = Mem_resolution[14]+(indices[0]-23)
                                        elif 42 <= indices[0] <= 50 :
                                            row_bis2 = Mem_resolution[13]
                                            col_bis2 = Mem_resolution[14]-(indices[0]-23) 
                                        if num_final == 24 :
                                            #dans le cas ou on a 4 1
                                            if Mem_resolution[9] ==(taille/2 -1) and (Mem_resolution[3] ==0 or Mem_resolution[8] ==0): #Règle 27 : Si dans la ligne il y a 3 valeurs vides (dont Mem[0]), 1 de ces valeurs est voisine à Mem[0] et égal à 0, et il reste un 1 dans la ligne, alors l'autre valeur vide est égale à 0               
                                                etat_partage.grid_values2[row_bis2][col_bis2] = 0
                                                etat_partage.debug.append(("condition 27",row_bis2,col_bis2,0, "Mem :", Mem_resolution))
                                                #dans le cas ou on a 4 0
                                            elif  Mem_resolution[10] ==(taille/2 -1) and (Mem_resolution[3] ==1 or Mem_resolution[8] ==1): #Règle 28 : Si dans la ligne il y a 3 valeurs vides (dont Mem[0]), 1 de ces valeurs est voisine à Mem[0] et égal à 1, et il reste un 0 dans la ligne, alors l'autre valeur vide est égale à 1                      
                                                etat_partage.grid_values2[row_bis2][col_bis2] = 1
                                                etat_partage.debug.append(("condition 28",row_bis2,col_bis2,1, "Mem :", Mem_resolution))
                                        elif num_final == 42 :
                                            #dans le cas ou on a 4 1
                                            
                                            if Mem_resolution[9] ==(taille/2 -1) and (Mem_resolution[4] ==0 or Mem_resolution[7] ==0):
                                                etat_partage.grid_values2[row_bis2][col_bis2] = 0
                                                etat_partage.debug.append(("condition 27",row_bis2,col_bis2,0, "Mem :", Mem_resolution))
                                            #dans le cas ou on a 4 0
                                            elif  Mem_resolution[10] ==(taille/2 -1) and (Mem_resolution[4] ==1 or Mem_resolution[7] ==1):   
                                                etat_partage.grid_values2[row_bis2][col_bis2] = 1
                                                etat_partage.debug.append(("condition 28",row_bis2,col_bis2,1, "Mem :", Mem_resolution))
                            indices=[]                    
                            #on travail sur la colonne
                            if Mem_resolution[11] ==(taille/2 -1) or Mem_resolution[12] ==(taille/2 -1):
                                for i in Mem_colonnes :
                                    if Mem_resolution[i] == -1 :
                                        indices.append(i)
                                indices_0 = [15,33]
                                valeur = 0
                                num_final = 0

                                if len(indices)==2 :
                                    for num in indices_0 :
                                        if num in indices :
                                            valeur +=1
                                            num_final = num
                                            indices.remove(num)
                                            
                                
                                    if valeur == 1 :
                                        #case a ecrire
                                        if 15 <= indices[0] <= 23 :
                                            row_bis2 = Mem_resolution[13]-(indices[0]-14)
                                            col_bis2 = Mem_resolution[14]
                                        elif 33 <= indices[0] <= 41 :
                                            row_bis2 = Mem_resolution[13]+(indices[0]-32)
                                            col_bis2 = Mem_resolution[14] 
                                        if num_final == 15 :
                                            #dans le cas ou on a 4 1
                                            if Mem_resolution[11] ==(taille/2 -1) and (Mem_resolution[1] ==0 or Mem_resolution[6] ==0): #Règle 29 : Si dans la colonne il y a 3 valeurs vides (dont Mem[0]), 1 de ces valeurs est voisine à Mem[0] et égal à 0, et il reste un 1 dans la colonne, alors l'autre valeur vide est égale à 0                      
                                                etat_partage.grid_values2[row_bis2][col_bis2] = 0
                                                etat_partage.debug.append(("condition 29",row_bis2,col_bis2,0, "Mem :", Mem_resolution))
                                                #dans le cas ou on a 4 0
                                            elif  Mem_resolution[12] ==(taille/2 -1) and (Mem_resolution[1] ==1 or Mem_resolution[6] ==1):  #Règle 30 : Si dans la colonne il y a 3 valeurs vides (dont Mem[0]), 1 de ces valeurs est voisine à Mem[0] et égal à 1, et il reste un 0 dans la colonne, alors l'autre valeur vide est égale à 1                     
                                                etat_partage.grid_values2[row_bis2][col_bis2] = 1
                                                etat_partage.debug.append(("condition 30",row_bis2,col_bis2,1, "Mem :", Mem_resolution))
                                        elif num_final == 33 :
                                            #dans le cas ou on a 4 1
                                            if Mem_resolution[11] ==(taille/2 -1) and (Mem_resolution[2] ==0 or Mem_resolution[5] ==0):
                                                etat_partage.grid_values2[row_bis2][col_bis2] = 0
                                                etat_partage.debug.append(("condition 29",row_bis2,col_bis2,0, "Mem :", Mem_resolution))
                                            #dans le cas ou on a 4 0
                                            elif  Mem_resolution[12] ==(taille/2 -1) and (Mem_resolution[2] ==1 or Mem_resolution[5] ==1):
                                                etat_partage.grid_values2[row_bis2][col_bis2] = 1
                                                etat_partage.debug.append(("condition 30",row_bis2,col_bis2,1, "Mem :", Mem_resolution))   
                       
                                     
                    if Mem_resolution[0] == 1 or Mem_resolution[0] == 0: 
                        print("========================================================================================================")                       
                        etat_partage.grid_values2[Mem_resolution[13]][Mem_resolution[14]] = Mem_resolution[0]
                        etat_partage.text_ids2[Mem_resolution[13]][Mem_resolution[14]] = "Rempli"
                        etat_partage.col_ligne.append((Mem_resolution[13],Mem_resolution[14]))
                        
                        print(Mem_resolution[13], Mem_resolution[14], "Trouvée ! Avec la valeur :", Mem_resolution[0], Mem_resolution)
                        print("je sors du thread", thread_name,a_trouver)
                        etat_partage.grille_complete+=1 
                        print(etat_partage.grille_complete) 
                        tour = 0
                        return
                    tour+=1
                    print(tour)
            time.sleep(0.1)  # Fréquence de vérification 
                        

    
    