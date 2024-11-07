# etat_partage.py
running = False  # Drapeau de contrôle pour les threads
verrou = None   # Le verrou peut être initialisé dans le script principal pour synchroniser les threads
verrou2 = None   # Le verrou peut être initialisé dans le script principal pour synchroniser les threads
canvas = None
grid_values = None
text_ids = None
grid_values2 = None
text_ids2 = None


root = None
debug=[]