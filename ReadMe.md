#Projet PAM Takuzu 
description TBD


#Fonctionnement du code : 
Le code comporte 2 dossiers + un fichier .py principal: 
    - grille : contient les txt avec les différentes grilles de départ
    - ihm : contient les differentes classes et fonction pour la construction de l'interface
    - Main-manuel.py : permet de lancer le jeu


Fonctionnement du code : 
    - le main renvoie sur le fichier first_page
    - first_page permet de créer la page d'acceuil du jeu comportent les différents boutons du jeu (6x6, 8x8, 10x10, ...), chaque bouton renvoie sur l'une des fonctions du dossier ihm
    - le dossier ihm permet de créer la grille avec les 0 et 1 (grille de départ contenu dan sle dossier grille) placés pour commencer une partie, elle comporte également les fonctions de vérification des règles du jeu.
