import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, regularizers
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Fonction pour charger les données
def load_takuzu_data(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    grids = []
    grid = []
    for line in lines:
        if line.startswith("#") or line.strip() == "":
            continue
        grid.append([int(num) for num in line.strip().split()])
        if len(grid) == 6:
            grids.append(np.array(grid))
            grid = []

    grids = np.array(grids).reshape(-1, 6, 6)
    return grids

# Charger les données
data = load_takuzu_data('variations_takuzu.csv')

# Diviser les données en ensembles d'entraînement (80%) et de validation (20%)
train_data, val_data = train_test_split(data, test_size=0.2, random_state=42)

# Reshaper les données pour inclure la dimension des canaux (le modèle attend des entrées avec une dimension de canal)
train_data = train_data.reshape(-1, 6, 6, 1)
val_data = val_data.reshape(-1, 6, 6, 1)

# Création du modèle
def create_model():
    input_layer = layers.Input(shape=(6, 6, 1))

    # Bloc résiduel 1
    x = layers.Conv2D(16, (3, 3), activation='relu', padding='same', kernel_regularizer=regularizers.l2(0.001))(input_layer)
    x = layers.Conv2D(16, (3, 3), activation='relu', padding='same', kernel_regularizer=regularizers.l2(0.001))(x)
    shortcut = layers.Conv2D(16, (1, 1), padding='same', kernel_regularizer=regularizers.l2(0.001))(input_layer)
    x = layers.add([x, shortcut])

    # Bloc résiduel 2
    x = layers.Conv2D(32, (3, 3), activation='relu', padding='same', kernel_regularizer=regularizers.l2(0.001))(x)
    x = layers.Conv2D(32, (3, 3), activation='relu', padding='same', kernel_regularizer=regularizers.l2(0.001))(x)
    shortcut = layers.Conv2D(32, (1, 1), padding='same', kernel_regularizer=regularizers.l2(0.001))(x)
    x = layers.add([x, shortcut])

    # Couche de sortie
    x = layers.Flatten()(x)
    x = layers.Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.001))(x)
    x = layers.Dense(6 * 6, activation='sigmoid')(x)
    output_layer = layers.Reshape((6, 6, 1))(x)

    model = tf.keras.Model(inputs=input_layer, outputs=output_layer)
    return model

# Création du modèle
model = create_model()

# Fonction de perte personnalisée
def takuzu_loss(y_true, y_pred):
    bce = tf.keras.losses.BinaryCrossentropy()
    bce_loss = bce(y_true, y_pred)

    y_pred_rounded = tf.round(y_pred)
    takuzu_loss = 0.0

    # Calculer la perte en fonction des règles du Takuzu
    for i in range(6):
        for j in range(4):
            equal_rows = tf.equal(y_pred_rounded[:, i, j:j+3, 0], tf.expand_dims(y_pred_rounded[:, i, j], -1))
            takuzu_loss += tf.reduce_sum(tf.cast(tf.reduce_all(equal_rows, axis=-1), tf.float32)) * 1.0

            equal_cols = tf.equal(y_pred_rounded[:, j:j+3, i, 0], tf.expand_dims(y_pred_rounded[:, j, i], -1))
            takuzu_loss += tf.reduce_sum(tf.cast(tf.reduce_all(equal_cols, axis=-1), tf.float32)) * 1.0

    return bce_loss + takuzu_loss

# Compiler le modèle
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001), loss=takuzu_loss, metrics=['accuracy'])

# Entraîner le modèle
epochs = 20
batch_size = 10

history = model.fit(
    train_data, 
    train_data, 
    validation_data=(val_data, val_data),
    epochs=epochs, 
    batch_size=batch_size
)

# Visualiser les courbes de perte et de précision
# plt.plot(history.history['loss'], label='Perte - Entraînement')
# plt.plot(history.history['val_loss'], label='Perte - Validation')
# plt.legend()
# plt.title('Perte au fil des époques')
# plt.show()

# plt.plot(history.history['accuracy'], label='Précision - Entraînement')
# plt.plot(history.history['val_accuracy'], label='Précision - Validation')
# plt.legend()
# plt.title('Précision au fil des époques')
# plt.show()

# Fonction de validation et de correction des grilles
def validate_and_correct(grid):
    for i in range(6):
        # Corriger les violations des lignes
        row = grid[i, :]
        for j in range(4):
            if np.array_equal(row[j:j+3], [0, 0, 0]):
                grid[i, j+2] = 1
            elif np.array_equal(row[j:j+3], [1, 1, 1]):
                grid[i, j+2] = 0
        
        # Corriger les violations des colonnes
        col = grid[:, i]
        for j in range(4):
            if np.array_equal(col[j:j+3], [0, 0, 0]):
                grid[j+2, i] = 1
            elif np.array_equal(col[j:j+3], [1, 1, 1]):
                grid[j+2, i] = 0
    
    # Vérifier l'équilibre entre 0 et 1 dans chaque ligne et colonne
    for i in range(6):
        row = grid[i, :]
        col = grid[:, i]
        if np.sum(row) != 3:
            grid[i, :] = balance_zeros_and_ones(row)
        if np.sum(col) != 3:
            grid[:, i] = balance_zeros_and_ones(col)

    return grid

def balance_zeros_and_ones(array):
    # Fonction pour équilibrer une ligne ou colonne
    while np.sum(array) > 3:
        array[np.argmax(array)] = 0
    while np.sum(array) < 3:
        array[np.argmin(array)] = 1
    return array

def ensure_unique_rows(grid):
    seen = set()
    for i in range(6):
        row_tuple = tuple(grid[i, :])
        if row_tuple in seen:
            # Ajuster la ligne en changeant des valeurs
            grid[i, :] = flip_row(grid[i, :])
        else:
            seen.add(row_tuple)
    return grid

def flip_row(row):
    row_copy = row.copy()
    for i in range(len(row)):
        if row[i] == 0:
            row_copy[i] = 1
            break
        else:
            row_copy[i] = 0
            break
    return row_copy

def generate_grids(model, num_grids):
    generated_grids = []
    for _ in range(num_grids):
        random_input = np.random.rand(1, 6, 6, 1)  # Générer une entrée aléatoire
        generated_grid = model.predict(random_input)  # Prédiction par le modèle
        grid = np.round(generated_grid[0, :, :, 0])  # Arrondir la sortie

        # Appliquer les corrections et validations
        grid = validate_and_correct(grid)  # Corriger selon les règles du Takuzu
        grid = ensure_unique_rows(grid)    # Garantir l'unicité des lignes

        generated_grids.append(grid)
    return np.array(generated_grids)

def is_valid_grid(grid):
    # Vérification des séquences de 3 éléments égaux sur chaque ligne et colonne
    for i in range(6):
        for j in range(4):
            if (grid[i, j] == grid[i, j + 1] == grid[i, j + 2]) or (grid[j, i] == grid[j + 1, i] == grid[j + 2, i]):
                return False
    # Vérification que chaque ligne et chaque colonne contient exactement 3 zéros et 3 uns
    for i in range(6):
        if np.sum(grid[i, :]) != 3 or np.sum(grid[:, i]) != 3:
            return False
    # Vérification que chaque ligne et chaque colonne sont uniques
    for i in range(6):
        for j in range(i + 1, 6):
            if np.array_equal(grid[i], grid[j]) or np.array_equal(grid[:, i], grid[:, j]):
                return False
    return True

def fill_obvious_values(grid):
    """
    Remplir les cases évidentes dans la grille en respectant les règles de Takuzu.
    La grille doit être remplie avec des -1 pour les cases vides.
    """
    changed = True
    while changed:
        changed = False
        
        # Appliquer les règles aux lignes
        for i in range(6):
            for j in range(4):  # Jusqu'à j+2 pour éviter les IndexError
                # Si deux éléments identiques sont suivis d'un -1, remplacer ce -1 par l'inverse
                if grid[i, j] != -1 and grid[i, j] == grid[i, j + 1] and grid[i, j + 2] == -1:
                    grid[i, j + 2] = 1 - grid[i, j]
                    changed = True
                
                # Remplir les -1 dans les séquences opposées comme 0,-1,0
                if j + 2 < 6:
                    if grid[i, j] == 0 and grid[i, j + 1] == -1 and grid[i, j + 2] == 0:
                        grid[i, j + 1] = 1
                        changed = True
                    elif grid[i, j] == 1 and grid[i, j + 1] == -1 and grid[i, j + 2] == 1:
                        grid[i, j + 1] = 0
                        changed = True
        
        # Appliquer les règles aux colonnes
        for j in range(6):
            for i in range(4):  # Jusqu'à i+2 pour éviter les IndexError
                # Si deux éléments identiques sont suivis d'un -1 dans une colonne
                if grid[i, j] != -1 and grid[i, j] == grid[i + 1, j] and grid[i + 2, j] == -1:
                    grid[i + 2, j] = 1 - grid[i, j]
                    changed = True
                
                # Remplir les -1 dans les séquences opposées dans une colonne
                if i + 2 < 6:
                    if grid[i, j] == 0 and grid[i + 1, j] == -1 and grid[i + 2, j] == 0:
                        grid[i + 1, j] = 1
                        changed = True
                    elif grid[i, j] == 1 and grid[i + 1, j] == -1 and grid[i + 2, j] == 1:
                        grid[i + 1, j] = 0
                        changed = True
        
        # Compléter la grille si une ligne/colonne contient déjà 3 0 ou 3 1
        for i in range(6):
            zeros = np.sum(grid[i, :] == 0)
            ones = np.sum(grid[i, :] == 1)
            empty = np.sum(grid[i, :] == -1)
            
            if zeros == 3 and empty > 0:
                grid[i, grid[i, :] == -1] = 1
                changed = True
            elif ones == 3 and empty > 0:
                grid[i, grid[i, :] == -1] = 0
                changed = True
        
        for j in range(6):
            zeros = np.sum(grid[:, j] == 0)
            ones = np.sum(grid[:, j] == 1)
            empty = np.sum(grid[:, j] == -1)
            
            if zeros == 3 and empty > 0:
                grid[grid[:, j] == -1, j] = 1
                changed = True
            elif ones == 3 and empty > 0:
                grid[grid[:, j] == -1, j] = 0
                changed = True
    
    return grid

# Test pour générer 5 grilles
# generated_grids = generate_grids(model, 5)

# Afficher les grilles générées
# for i, grid in enumerate(generated_grids):
#     if is_valid_grid(grid):
#         print(f"Grille valide générée {i+1} :\n{grid}")
#     else:
#         print(f"Grille non valide générée {i+1} :\n{grid}")

# 100 tentatives

while True:
    generated_grid = generate_grids(model, 1)
    if is_valid_grid(generated_grid[0]):
        partial_grid = fill_obvious_values(generated_grid[0].copy())
        print(f"Grille valide générée :\n{generated_grid[0]}")
        print(f"Grille partielle :\n{partial_grid}")
        break