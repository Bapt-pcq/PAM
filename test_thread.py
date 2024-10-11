import threading
import time

def afficher_nombres():
    for i in range(1, 6):
        print(f"Nombre : {i}")
        time.sleep(1)

def afficher_lettres():
    for lettre in ['A', 'B', 'C', 'D', 'E']:
        print(f"Lettre : {lettre}")
        time.sleep(1.5)
def grilles():
    global grille
    
    for i in range(5):
        grille[i]=-1

def case_11():
    global grille
    ligne1=grille
    print(ligne1)
    

grille=["","","",0,1,""]
# Création de deux threads
t1 = threading.Thread(target=afficher_nombres)
t2 = threading.Thread(target=afficher_lettres)
t3 = threading.Thread(target=case_11)
t4 = threading.Thread(target=grilles)
# Démarrage des threads
t1.start()
t2.start()
t3.start()
t4.start()
print("hello")
# Joindre les threads pour s'assurer qu'ils se terminent
t1.join()
t2.join()
t3.join()
t4.join()

print("Les quatres threads sont terminés.")
