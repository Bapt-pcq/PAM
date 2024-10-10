

class verification : 
    def is_valid_sequence(self,sequence):
        # Vérifie qu'il n'y a pas plus de deux 0 ou 1 consécutifs
        count = 1

        for i in range(1, len(sequence)):

            if sequence[i] != "" or sequence[i-1] != "":
                if sequence[i] == sequence[i - 1]  :
                    count += 1
                    if count > 2:
                        return False
                else:
                    count = 1
        return True


    def has_equal_zeros_ones(self,sequence):
        # Vérifie qu'il y a le même nombre de 0 et de 1
        vide = sequence.count("")
        if vide!=0:
            return True
        zeros = sequence.count(0)
        ones = sequence.count(1)
        if zeros != ones :
            return False
        return True

    def all_unique(self,sequence):
        # Filtrer les lignes qui ne contiennent pas de ''
        filtered_rows = [row for row in sequence if '' not in row]

        # Vérifier les lignes identiques
        identical_rows = []
        for i in range(len(filtered_rows)):
            for j in range(i+1, len(filtered_rows)):
                if filtered_rows[i] == filtered_rows[j]:
                    identical_rows.append((i, j))

        # Afficher les résultats

        if identical_rows:
            return False
        else:
            return True
    def check_empty_cells(self,grid):
        # Parcourir chaque ligne de la grille
        for row in grid:
            # Vérifier s'il y a une cellule vide ('') dans la ligne
            if '' in row:
                return True  # Il y a au moins une cellule vide
        return False  # Pas de cellules vides


    