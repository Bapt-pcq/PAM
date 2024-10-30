

class lecture:
    def lire_grille_depuis_fichier(fichier):
        # Ouvrir le fichier en lecture
        with open(fichier, 'r') as f:
            # Lire le contenu ligne par ligne et convertir chaque ligne en une liste d'entiers
            grille = [list(map(int, ligne.split())) for ligne in f]
        
        return grille