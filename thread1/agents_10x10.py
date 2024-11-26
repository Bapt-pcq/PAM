
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
                    print(etat_partage.debug)
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
                        if Mem_resolution[1] == Mem_resolution[2] and Mem_resolution[2] != -2 and Mem_resolution[2] != -1 :
                            #print("condition",1)
                            #print(Mem_resolution)
                            Mem_resolution[0] = abs(Mem_resolution[1] - 1)
                            etat_partage.debug.append(("condition 1",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                        elif Mem_resolution[3] == Mem_resolution[4] and Mem_resolution[4] != -2 and Mem_resolution[4] != -1:
                            #print("condition",2)
                            #print(Mem_resolution)
                            Mem_resolution[0] = abs(Mem_resolution[3] - 1)
                            etat_partage.debug.append(("condition 2",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                        elif Mem_resolution[5] == Mem_resolution[6] and Mem_resolution[6] != -2 and Mem_resolution[6] != -1:
                            #print("condition",3)
                            #print(Mem_resolution)                               
                            Mem_resolution[0] = abs(Mem_resolution[5] - 1)
                            etat_partage.debug.append(("condition 3",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                        elif Mem_resolution[7] == Mem_resolution[8] and Mem_resolution[8] != -2 and Mem_resolution[8] != -1:
                            #print("condition",4)
                            #print(Mem_resolution)
                            Mem_resolution[0] = abs(Mem_resolution[7] - 1)
                            etat_partage.debug.append(("condition 4",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                        elif Mem_resolution[2] == Mem_resolution[6] and Mem_resolution[2] != -2 and Mem_resolution[2] != -1 :
                            #print("condition",5)
                            #print(Mem_resolution)
                            Mem_resolution[0] = abs(Mem_resolution[2] - 1)
                            etat_partage.debug.append(("condition 5",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                        elif Mem_resolution[4] == Mem_resolution[8] and Mem_resolution[4] != -2 and Mem_resolution[4] != -1:
                            #print("condition",6)
                            #print(Mem_resolution)
                            Mem_resolution[0] = abs(Mem_resolution[4] - 1)
                            etat_partage.debug.append(("condition 6",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                        elif Mem_resolution[9] == nb_0_ou_1:  # Nb de 1 dans la ligne atteint
                            #print("condition",7)
                            #print(Mem_resolution)
                            Mem_resolution[0] = 0
                            etat_partage.debug.append(("condition 7",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                        elif Mem_resolution[10] == nb_0_ou_1:  # Nb de 0 dans la ligne atteint
                            #print("condition",8)
                            #print(Mem_resolution)
                            Mem_resolution[0] = 1
                            etat_partage.debug.append(("condition 8",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                        elif Mem_resolution[11] == nb_0_ou_1:  # Nb de 1 dans la colonne atteint
                            #print("condition",9)
                            #print(Mem_resolution)
                            Mem_resolution[0] = 0
                            etat_partage.debug.append(("condition 9",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution))
                        elif Mem_resolution[12] == nb_0_ou_1:  # Nb de 0 dans la colonne atteint
                            #print("condition",10)
                            #print(Mem_resolution)
                            Mem_resolution[0] = 1
                            etat_partage.debug.append(("condition 10",Mem_resolution[13],Mem_resolution[14],Mem_resolution[0], "Mem :", Mem_resolution,"colone:",Mem_resolution_col))
                        if tour>10:   
                            if Mem_resolution[1] ==-1 and Mem_resolution[2] ==-1 and Mem_resolution[6] ==-1 :
                            
                                if Mem_resolution[11] == (taille/2 -1) and Mem_resolution[5] ==0 :
                                    Mem_resolution[0] = 1
                                elif Mem_resolution[11] == (taille/2 -1) and Mem_resolution[5] ==1 :
                                    #Mem_resolution[6] == 0
                                    
                                    row_bis = Mem_resolution[13]+1
                                    col_bis = Mem_resolution[14]
                                    etat_partage.grid_values2[row_bis][col_bis] = 0
                                    etat_partage.debug.append(("condition 11",row_bis,col_bis,0, "Mem :", Mem_resolution))

                                    #Mem_resolution[1] == 0
                                    row_bis2 = Mem_resolution[13]-2
                                    col_bis2 = Mem_resolution[14]
                                    etat_partage.grid_values2[row_bis2][col_bis2] = 0
                                    etat_partage.debug.append(("condition 11",row_bis2,col_bis2,0, "Mem :", Mem_resolution))                              
                                    
                                elif Mem_resolution[12] == (taille/2 -1) and Mem_resolution[5] ==0 :
                                    
                                    row_bis = Mem_resolution[13]+1
                                    col_bis = Mem_resolution[14]
                                    etat_partage.grid_values2[row_bis][col_bis] = 1
                                    etat_partage.debug.append(("condition 12",row_bis,col_bis,1, "Mem :", Mem_resolution))
                                    
                                    #Mem_resolution[1] == 1
                                    row_bis2 = Mem_resolution[13]-2
                                    col_bis2 = Mem_resolution[14]
                                    etat_partage.grid_values2[row_bis2][col_bis2] = 1
                                    etat_partage.debug.append(("condition 12",row_bis2,col_bis2,1, "Mem :", Mem_resolution)) 
                                elif Mem_resolution[12] == (taille/2 -1) and Mem_resolution[5] ==1 :
                                    Mem_resolution[0] = 0

                            elif Mem_resolution[2]== -1 and Mem_resolution[6]== -1 and Mem_resolution[5] == -1 :
                                if Mem_resolution[11] == (taille/2 -1) and Mem_resolution[1] ==0 :
                                    Mem_resolution[0] = 1
                                elif Mem_resolution[11] == (taille/2 -1) and Mem_resolution[1] ==1 :
                                    #Mem_resolution[2] == 0
                                    row_bis = Mem_resolution[13]-1
                                    col_bis = Mem_resolution[14]
                                    etat_partage.grid_values2[row_bis][col_bis] = 0
                                    etat_partage.debug.append(("condition 13",row_bis,col_bis,0, "Mem :", Mem_resolution))
                                    #Mem_resolution[5] == 0
                                    row_bis2 = Mem_resolution[13]+2
                                    col_bis2 = Mem_resolution[14]
                                    etat_partage.grid_values2[row_bis2][col_bis2] = 0
                                    etat_partage.debug.append(("condition 13",row_bis2,col_bis2,0, "Mem :", Mem_resolution)) 
                                elif Mem_resolution[12] == (taille/2 -1) and Mem_resolution[1] ==0 :
                                    #Mem_resolution[2] == 1
                                    row_bis = Mem_resolution[13]-1
                                    col_bis = Mem_resolution[14]
                                    etat_partage.grid_values2[row_bis][col_bis] = 1
                                    etat_partage.debug.append(("condition 14",row_bis,col_bis,1, "Mem :", Mem_resolution))
                                    
                                    #Mem_resolution[5] == 1
                                    row_bis2 = Mem_resolution[13]+2
                                    col_bis2 = Mem_resolution[14]
                                    etat_partage.grid_values2[row_bis2][col_bis2] = 1
                                    etat_partage.debug.append(("condition 14",row_bis2,col_bis2,1, "Mem :", Mem_resolution)) 
                                elif Mem_resolution[12] == (taille/2 -1) and Mem_resolution[1] ==1 :
                                    Mem_resolution[0] = 0

                            elif Mem_resolution[3]== -1 and Mem_resolution[4]== -1 and Mem_resolution[8] == -1 :
                                if Mem_resolution[9] == (taille/2 -1) and Mem_resolution[7]==0 :
                                    Mem_resolution[0]=1
                                elif Mem_resolution[9] == (taille/2 -1) and Mem_resolution[7]==1 :
                                    # Mem_resolution[8]=0
                                    row_bis = Mem_resolution[13]
                                    col_bis = Mem_resolution[14]-1
                                    etat_partage.grid_values2[row_bis][col_bis] = 0
                                    etat_partage.debug.append(("condition 15",row_bis,col_bis,0, "Mem :", Mem_resolution))
                                    #Mem_resolution[3]=0
                                    row_bis2 = Mem_resolution[13]
                                    col_bis2 = Mem_resolution[14]+2
                                    etat_partage.grid_values2[row_bis2][col_bis2] = 0
                                    etat_partage.debug.append(("condition 15",row_bis2,col_bis2,0, "Mem :", Mem_resolution)) 
                                elif Mem_resolution[10] == (taille/2 -1) and Mem_resolution[7]==0 :
                                    # Mem_resolution[8]=1
                                    row_bis = Mem_resolution[13]
                                    col_bis = Mem_resolution[14]-1
                                    etat_partage.grid_values2[row_bis][col_bis] = 1
                                    etat_partage.debug.append(("condition 16",row_bis,col_bis,1, "Mem :", Mem_resolution))
                                    #Mem_resolution[3]=1
                                    row_bis2 = Mem_resolution[13]+2
                                    col_bis2 = Mem_resolution[14]
                                    etat_partage.grid_values2[row_bis2][col_bis2] = 1
                                    etat_partage.debug.append(("condition 16",row_bis2,col_bis2,1, "Mem :", Mem_resolution)) 
                                elif Mem_resolution[10] == (taille/2 -1) and Mem_resolution[7]==1 :
                                    Mem_resolution[0]=0
                            elif Mem_resolution[7]== -1 and Mem_resolution[8]== -1 and Mem_resolution[4] ==-1 :
                                
                                if Mem_resolution[9] == (taille/2 -1) and Mem_resolution[3]==0 :
                                    Mem_resolution[0]=1
                                elif Mem_resolution[9] == (taille/2 -1) and Mem_resolution[3]==1 :
                                    # Mem_resolution[4]=0
                                    row_bis = Mem_resolution[13]
                                    col_bis = Mem_resolution[14]+1
                                    etat_partage.grid_values2[row_bis][col_bis] = 0
                                    etat_partage.debug.append(("condition 17",row_bis,col_bis,0, "Mem :", Mem_resolution))
                                    #Mem_resolution[7]=0
                                    row_bis2 = Mem_resolution[13]
                                    col_bis2 = Mem_resolution[14]-2
                                    etat_partage.grid_values2[row_bis2][col_bis2] = 0
                                    etat_partage.debug.append(("condition 17",row_bis2,col_bis2,0, "Mem :", Mem_resolution)) 
                                elif Mem_resolution[10] == (taille/2 -1) and Mem_resolution[3]==0 :
                                    # Mem_resolution[4]=1
                                    row_bis = Mem_resolution[13]
                                    col_bis = Mem_resolution[14]+1
                                    etat_partage.grid_values2[row_bis][col_bis] = 1
                                    etat_partage.debug.append(("condition 18",row_bis,col_bis,1, "Mem :", Mem_resolution))
                                    #Mem_resolution[7]=1
                                    row_bis2 = Mem_resolution[13]
                                    col_bis2 = Mem_resolution[14]-2
                                    etat_partage.grid_values2[row_bis2][col_bis2] = 1
                                    etat_partage.debug.append(("condition 18",row_bis2,col_bis2,1, "Mem :", Mem_resolution)) 
                                elif Mem_resolution[10] == (taille/2 -1) and Mem_resolution[3]==1 :
                                    Mem_resolution[0]=0
                        if tour>20 : 
                            Mem_lignes = [24,25,26,27,28,29,30,31,32,42,43,44,45,46,47,48,49,50]
                            Mem_colonnes = [15,16,17,18,19,20,21,22,23,33,34,35,36,37,38,39,40,41]
                            #On crée une nouvelle liste pour stocker les indices ayant un -1 
                            indices =[]
                            #on travail sur la ligne
                            if Mem_resolution[9] ==4 or Mem_resolution[10] ==4:
                                for i in Mem_lignes :
                                    if Mem_resolution[i] == -1 :
                                        indices.append(i)
                                indices_0 = [24,42]
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
                                        if 24 <= indices[0] <= 32 :
                                            row_bis2 = Mem_resolution[13]
                                            col_bis2 = Mem_resolution[14]+(indices[0]-23)
                                        elif 42 <= indices[0] <= 50 :
                                            row_bis2 = Mem_resolution[13]
                                            col_bis2 = Mem_resolution[14]-(indices[0]-23) 
                                        if num_final == 24 :
                                            #dans le cas ou on a 4 1
                                            if Mem_resolution[9] ==4 and (Mem_resolution[3] ==0 or Mem_resolution[8] ==0):                    
                                                etat_partage.grid_values2[row_bis2][col_bis2] = 0
                                                etat_partage.debug.append(("condition 19",row_bis2,col_bis2,0, "Mem :", Mem_resolution))
                                                #dans le cas ou on a 4 0
                                            elif  Mem_resolution[10] ==4 and (Mem_resolution[3] ==1 or Mem_resolution[8] ==1):                     
                                                etat_partage.grid_values2[row_bis2][col_bis2] = 1
                                                etat_partage.debug.append(("condition 20",row_bis2,col_bis2,1, "Mem :", Mem_resolution))
                                        elif num_final == 42 :
                                            #dans le cas ou on a 4 1
                                            
                                            if Mem_resolution[9] ==4 and (Mem_resolution[4] ==0 or Mem_resolution[7] ==0):
                                                etat_partage.grid_values2[row_bis2][col_bis2] = 0
                                                etat_partage.debug.append(("condition 21",row_bis2,col_bis2,0, "Mem :", Mem_resolution))
                                            #dans le cas ou on a 4 0
                                            elif  Mem_resolution[10] ==4 and (Mem_resolution[4] ==1 or Mem_resolution[7] ==1):   
                                                etat_partage.grid_values2[row_bis2][col_bis2] = 1
                                                etat_partage.debug.append(("condition 22",row_bis2,col_bis2,1, "Mem :", Mem_resolution))
                            indices=[]                    
                            #on travail sur la colonne
                            if Mem_resolution[11] ==4 or Mem_resolution[12] ==4:
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
                                            if Mem_resolution[11] ==4 and (Mem_resolution[1] ==0 or Mem_resolution[6] ==0):                    
                                                etat_partage.grid_values2[row_bis2][col_bis2] = 0
                                                etat_partage.debug.append(("condition 23",row_bis2,col_bis2,0, "Mem :", Mem_resolution))
                                                #dans le cas ou on a 4 0
                                            elif  Mem_resolution[12] ==4 and (Mem_resolution[1] ==1 or Mem_resolution[6] ==1):                     
                                                etat_partage.grid_values2[row_bis2][col_bis2] = 1
                                                etat_partage.debug.append(("condition 24",row_bis2,col_bis2,1, "Mem :", Mem_resolution))
                                        elif num_final == 33 :
                                            #dans le cas ou on a 4 1
                                            if Mem_resolution[11] ==4 and (Mem_resolution[2] ==0 or Mem_resolution[5] ==0):
                                                etat_partage.grid_values2[row_bis2][col_bis2] = 0
                                                etat_partage.debug.append(("condition 25",row_bis2,col_bis2,0, "Mem :", Mem_resolution))
                                            #dans le cas ou on a 4 0
                                            elif  Mem_resolution[12] ==4 and (Mem_resolution[2] ==1 or Mem_resolution[5] ==1):
                                                etat_partage.grid_values2[row_bis2][col_bis2] = 1
                                                etat_partage.debug.append(("condition 26",row_bis2,col_bis2,1, "Mem :", Mem_resolution))   
                       
                                     
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
                        

    
    