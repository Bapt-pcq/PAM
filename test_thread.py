import threading
import time

# Variable partagée
valeur_partagee = 0
# Verrou pour synchronisation
verrou = threading.Lock()

# Fonction pour modifier la variable
def modifier_valeur():
    global valeur_partagee
    for i in range(1, 6):
        with verrou:
            valeur_partagee = i
            print(f"Valeur modifiée : {valeur_partagee}")
        time.sleep(2)  # Simule un traitement qui prend du temps

# Fonction pour surveiller et réagir à la mise à jour de la variable
def surveiller_valeur():
    valeur_precedente = -1
    while True:
        with verrou:
            if valeur_partagee != valeur_precedente:
                print(f"Thread mis à jour avec nouvelle valeur : {valeur_partagee}")
                valeur_precedente = valeur_partagee
        time.sleep(1)  # Fréquence de vérification

# Création des threads
t1 = threading.Thread(target=modifier_valeur)
t2 = threading.Thread(target=surveiller_valeur, daemon=True) #thread de type deamon qui s'execute en arrière plan 
                                                             #s'arrete lorsque tous les threads non Deamon sont terminés

# Démarrage des threads
t1.start()
t2.start()

# Attendre que le premier thread se termine
t1.join()

print("Le thread de modification est terminé.")
