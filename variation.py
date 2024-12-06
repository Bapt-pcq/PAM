import numpy as np

def is_valid_takuzu(grid):
    n = len(grid)

    # Vérification des lignes et des colonnes
    for i in range(n):
        # Vérification des lignes
        if np.sum(grid[i] == 0) != n // 2 or np.sum(grid[i] == 1) != n // 2:
            return False
        if i > 0 and np.all(grid[i] == grid[i - 1]):
            return False
        
        # Vérification des colonnes
        column = grid[:, i]
        if np.sum(column == 0) != n // 2 or np.sum(column == 1) != n // 2:
            return False
        if i > 0 and np.all(column == grid[:, i - 1]):
            return False

    # Vérification des séquences
    for i in range(n):
        for j in range(n - 2):
            if (grid[i][j] == grid[i][j + 1] == grid[i][j + 2] or 
                grid[j][i] == grid[j + 1][i] == grid[j + 2][i]):
                return False

    return True

def invert_grid(grid):
    """Inverse les valeurs de la grille (0 à 1 et 1 à 0)."""
    return np.where(grid == 0, 1, 0)

def swap_rows(grid, i, j):
    """Échange deux lignes dans la grille."""
    grid[i], grid[j] = grid[j], grid[i]

def swap_columns(grid, i, j):
    """Échange deux colonnes dans la grille."""
    grid[:, [i, j]] = grid[:, [j, i]]

def rotate_grid(grid):
    """Fait une rotation de la grille de 90 degrés dans le sens horaire."""
    return np.rot90(grid, k=-1)

def rotate_grid_counterclockwise(grid):
    """Fait une rotation de la grille de 90 degrés dans le sens antihoraire."""
    return np.rot90(grid, k=1)

def mirror_grid(grid):
    """Fait un miroir de la grille."""
    return np.flipud(grid)

def generate_variations(grid, num_variations, max_attempts=5000):
    """Génère des variations uniques de la grille Takuzu."""
    variations = set()
    variations.add(tuple(map(tuple, grid)))

    attempts = 0
    while len(variations) < num_variations and attempts < max_attempts:
        new_grid = np.copy(grid)
        action = np.random.choice(['invert', 'swap_rows', 'swap_columns', 'rotate', 'mirror', 'rotate_counterclockwise'])

        if action == 'invert':
            new_grid = invert_grid(new_grid)
        elif action == 'swap_rows':
            i, j = np.random.choice(len(grid), 2, replace=False)
            swap_rows(new_grid, i, j)
        elif action == 'swap_columns':
            i, j = np.random.choice(len(grid), 2, replace=False)
            swap_columns(new_grid, i, j)
        elif action == 'rotate':
            new_grid = rotate_grid(new_grid)
        elif action == 'mirror':
            new_grid = mirror_grid(new_grid)
        elif action == 'rotate_counterclockwise':
            new_grid = rotate_grid_counterclockwise(new_grid)

        if is_valid_takuzu(new_grid):
            variations.add(tuple(map(tuple, new_grid)))
        
        attempts += 1

    return variations

def write_variations_to_csv(variations, filename='variations_takuzu.csv'):
    """Écrit les variations dans un fichier CSV."""
    with open(filename, 'w') as f:
        for header, variation in variations:
            f.write(f"{header}\n")
            for row in variation:
                f.write('\t'.join(map(str, row)) + '\n')
            f.write('\n')  # Ajoute une ligne vide entre les grilles

# Grilles de base
grids = [
    np.array([[0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0],
              [0, 1, 1, 0, 0, 1],
              [1, 0, 0, 1, 1, 0],
              [1, 1, 0, 0, 1, 0],
              [0, 0, 1, 1, 0, 1]]),
    np.array([[1, 1, 0, 0, 1, 0],
              [1, 0, 1, 0, 0, 1],
              [0, 1, 0, 1, 0, 1],
              [0, 1, 0, 1, 1, 0],
              [1, 0, 1, 0, 1, 0],
              [0, 0, 1, 1, 0, 1]]),
    np.array([[1, 0, 1, 1, 0, 0],
              [1, 0, 1, 0, 1, 0],
              [0, 1, 1, 0, 0, 1],
              [1, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1],
              [0, 0, 1, 1, 0, 1]]),
    np.array([[0, 1, 1, 0, 1, 0],
              [1, 0, 1, 1, 0, 0],
              [0, 1, 0, 1, 0, 1],
              [0, 0, 1, 0, 1, 1],
              [1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 1, 0]]),
    np.array([[0, 1, 1, 0, 0, 1],
              [1, 1, 0, 0, 1, 0],
              [0, 0, 1, 1, 0, 1],
              [1, 0, 1, 0, 0, 1],
              [0, 1, 0, 1, 1, 0],
              [1, 0, 0, 1, 1, 0]]),
    np.array([[0, 0, 1, 0, 1, 1],
              [1, 0, 1, 1, 0, 0],
              [1, 1, 0, 0, 0, 1],
              [0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 1, 0]]),
    np.array([[1, 0, 1, 1, 0, 0],
              [1, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1],
              [1, 0, 1, 0, 0, 1],
              [0, 1, 0, 1, 1, 0],
              [0, 0, 1, 0, 1, 1]]),
    np.array([[0, 0, 1, 0, 1, 1],
              [1, 0, 0, 1, 0, 1],
              [0, 1, 1, 0, 1, 0],
              [0, 0, 1, 1, 0, 1],
              [1, 1, 0, 1, 0, 0],
              [1, 1, 0, 0, 1, 0]]),
    np.array([[0, 0, 1, 1, 0, 1],
              [1, 1, 0, 1, 0, 0],
              [0, 0, 1, 0, 1, 1],
              [1, 1, 0, 0, 1, 0],
              [0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0]]),
    np.array([[1, 1, 0, 0, 1, 0],
              [0, 0, 1, 0, 1, 1],
              [1, 1, 0, 1, 0, 1],
              [0, 0, 1, 1, 0, 1],
              [1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1]]),
    np.array([[1, 0, 0, 1, 1, 0],
              [1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1],
              [0, 1, 0, 1, 1, 0],
              [1, 0, 1, 0, 0, 1],
              [0, 1, 1, 0, 0, 1]]),
    np.array([[0, 0, 1, 1, 0, 1],
              [1, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1],
              [1, 0, 1, 0, 0, 1],
              [0, 1, 0, 1, 1, 0],
              [1, 0, 1, 0, 1, 0]]),
    np.array([[1, 0, 1, 1, 0, 0],
              [1, 0, 0, 1, 0, 1],
              [0, 1, 1, 0, 1, 0],
              [1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1],
              [0, 1, 0, 0, 1, 1]]),
    np.array([[1, 1, 0, 1, 0, 0],
              [1, 1, 0, 0, 1, 0],
              [0, 0, 1, 1, 0, 1],
              [1, 0, 0, 1, 0, 1],
              [0, 1, 1, 0, 1, 0],
              [0, 0, 1, 0, 1, 1]]),
    np.array([[0, 1, 1, 0, 1, 0],
              [0, 1, 0, 0, 1, 1],
              [1, 0, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1],
              [1, 0, 1, 1, 0, 0]]),
    np.array([[1, 1, 0, 1, 0, 0],
              [0, 0, 1, 0, 1, 1],
              [1, 1, 0, 0, 1, 0],
              [0, 1, 0, 1, 0, 1],
              [0, 0, 1, 1, 0, 1],
              [1, 0, 1, 0, 1, 0]]),
    np.array([[1, 0, 1, 0, 1, 0],
              [0, 0, 1, 1, 0, 1],
              [0, 1, 0, 1, 1, 0],
              [1, 1, 0, 0, 1, 0],
              [1, 0, 1, 0, 0, 1],
              [0, 1, 0, 1, 0, 1]]),
    np.array([[0, 0, 1, 0, 1, 1],
              [1, 0, 1, 1, 0, 0],
              [1, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1],
              [1, 0, 1, 0, 0, 1],
              [0, 1, 0, 1, 1, 0]]),
    np.array([[1, 0, 0, 1, 0, 1],
              [0, 0, 1, 0, 1, 1],
              [0, 1, 0, 1, 1, 0],
              [1, 0, 1, 0, 0, 1],
              [1, 1, 0, 1, 0, 0],
              [0, 1, 1, 0, 1, 0]]),
    np.array([[1, 0, 1, 0, 0, 1],
              [0, 1, 0, 1, 1, 0],
              [0, 0, 1, 1, 0, 1],
              [1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1],
              [1, 1, 0, 0, 1, 0]]),
    np.array([[1, 0, 1, 0, 0, 1],
              [1, 0, 1, 1, 0, 0],
              [0, 1, 0, 1, 1, 0],
              [0, 0, 1, 0, 1, 1],
              [1, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1]]),
    np.array([[0, 1, 1, 0, 1, 0],
              [1, 1, 0, 1, 0, 0],
              [1, 0, 1, 0, 0, 1],
              [0, 1, 0, 1, 1, 0],
              [1, 0, 0, 1, 0, 1],
              [0, 0, 1, 0, 1, 1]]),
    np.array([[1, 0, 1, 0, 0, 1],
              [0, 1, 0, 1, 1, 0],
              [0, 0, 1, 0, 1, 1],
              [1, 1, 0, 1, 0, 0],
              [1, 0, 1, 1, 0, 0],
              [0, 1, 0, 0, 1, 1]]),
    np.array([[0, 1, 0, 0, 1, 1],
              [1, 0, 1, 0, 0, 1],
              [0, 1, 0, 1, 0, 0],
              [0, 0, 1, 0, 1, 1],
              [0, 1, 0, 1, 1, 0],
              [1, 0, 1, 1, 0, 0]]),
    np.array([[1, 0, 1, 1, 0, 0],
              [0, 1, 0, 0, 1, 1],
              [1, 1, 0, 1, 0, 0],
              [0, 0, 1, 0, 1, 1],
              [0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0]]),
    np.array([[0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0],
              [0, 1, 1, 0, 1, 0],
              [1, 0, 0, 1, 0, 1],
              [1, 0, 1, 1, 0, 0],
              [0, 1, 0, 0, 1, 1]]),
    np.array([[0, 1, 0, 0, 1, 1],
              [1, 1, 0, 1, 0, 0],
              [0, 0, 1, 0, 1, 1],
              [0, 1, 0, 1, 1, 0],
              [1, 0, 1, 1, 0, 0],
              [1, 0, 1, 0, 0, 1]]),
    np.array([[0, 1, 1, 0, 0, 1],
              [0, 1, 1, 0, 0, 1],
              [1, 0, 0, 1, 1, 0],
              [1, 0, 1, 0, 0, 1],
              [0, 1, 0, 1, 1, 0],
              [1, 0, 1, 1, 0, 0]]),
    np.array([[1, 1, 0, 0, 1, 0],
              [1, 0, 1, 1, 0, 0],
              [0, 1, 0, 0, 1, 1],
              [1, 1, 0, 1, 0, 0],
              [0, 0, 1, 1, 0, 1],
              [0, 0, 1, 0, 1, 1]]),
    np.array([[1, 0, 1, 1, 0, 0],
              [0, 0, 1, 0, 1, 1],
              [1, 1, 0, 0, 1, 0],
              [1, 0, 0, 1, 0, 1],
              [0, 1, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1]]),
    np.array([[1, 0, 0, 1, 1, 0],
              [1, 0, 1, 0, 0, 1],
              [0, 1, 0, 0, 1, 1],
              [0, 1, 0, 1, 1, 0],
              [1, 0, 1, 1, 0, 0],
              [0, 1, 1, 0, 0, 1]]),
    np.array([[0, 0, 1, 0, 1, 1],
              [0, 1, 0, 0, 1, 1],
              [1, 1, 0, 1, 0, 0],
              [1, 0, 1, 0, 0, 1],
              [0, 1, 0, 1, 1, 0],
              [1, 0, 1, 1, 0, 0]]),
    np.array([[0, 1, 0, 1, 1, 0],
              [1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1],
              [0, 1, 1, 0, 1, 0],
              [1, 0, 1, 0, 0, 1],
              [1, 0, 0, 1, 0, 1]]),
    np.array([[0, 1, 0, 0, 1, 1],
              [1, 0, 1, 1, 0, 0],
              [1, 1, 0, 0, 1, 0],
              [0, 0, 1, 1, 0, 1],
              [1, 1, 0, 1, 0, 0],
              [0, 0, 1, 0, 1, 1]]),
    np.array([[1, 0, 1, 0, 1, 0],
              [0, 0, 1, 1, 0, 1],
              [0, 1, 0, 1, 1, 0],
              [1, 0, 1, 0, 0, 1],
              [1, 1, 0, 0, 1, 0],
              [0, 1, 0, 1, 0, 1]]),
    np.array([[1, 0, 1, 1, 0, 0],
              [0, 1, 1, 0, 0, 1],
              [0, 1, 0, 1, 1, 0],
              [1, 0, 1, 0, 0, 1],
              [0, 1, 0, 0, 1, 1],
              [1, 0, 0, 1, 1, 0]]),
    np.array([[0, 1, 1, 0, 0, 1],
              [0, 1, 0, 1, 1, 0],
              [1, 0, 1, 1, 0, 0],
              [0, 1, 0, 0, 1, 1],
              [1, 0, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0]]),
    np.array([[1, 0, 1, 1, 0, 0],
              [0, 1, 0, 1, 0, 1],
              [0, 1, 1, 0, 1, 0],
              [1, 0, 0, 1, 1, 0],
              [1, 0, 1, 0, 0, 1],
              [0, 1, 0, 0, 1, 1]]),
    np.array([[1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 1, 0],
              [1, 0, 0, 1, 0, 1],
              [1, 0, 1, 0, 0, 1],
              [0, 1, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1]]),
    np.array([[0, 1, 1, 0, 0, 1],
              [1, 0, 1, 1, 0, 0],
              [1, 1, 0, 0, 1, 0],
              [0, 0, 1, 1, 0, 1],
              [0, 1, 0, 0, 1, 1],
              [1, 0, 0, 1, 1, 0]]),
    np.array([[0, 0, 1, 1, 0, 1],
              [0, 1, 0, 0, 1, 1],
              [1, 0, 1, 0, 0, 1],
              [0, 1, 1, 0, 0, 1],
              [1, 1, 0, 0, 1, 0],
              [1, 0, 0, 1, 1, 0]]),
    np.array([[1, 1, 0, 1, 0, 0],
              [0, 0, 1, 0, 1, 1],
              [1, 0, 0, 1, 1, 0],
              [0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 0, 1],
              [0, 1, 1, 0, 1, 0]]),
    np.array([[1, 0, 0, 1, 0, 1],
              [0, 0, 1, 0, 1, 1],
              [1, 1, 0, 0, 1, 0],
              [0, 1, 0, 1, 0, 1],
              [1, 0, 1, 1, 0, 0],
              [0, 1, 1, 0, 1, 0]]),
    np.array([[1, 0, 1, 0, 1, 0],
              [1, 0, 0, 1, 0, 1],
              [0, 1, 1, 0, 1, 0],
              [1, 0, 1, 1, 0, 0],
              [0, 1, 0, 0, 1, 1],
              [0, 1, 0, 1, 0, 1]]),
    np.array([[0, 0, 1, 0, 1, 1],
              [1, 1, 0, 1, 0, 0],
              [0, 1, 1, 0, 0, 1],
              [1, 0, 0, 1, 1, 0],
              [0, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 0]]),
    np.array([[1, 0, 1, 0, 0, 1],
              [0, 1, 1, 0, 1, 0],
              [1, 0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0, 1],
              [0, 1, 0, 1, 1, 0],
              [1, 0, 0, 1, 0, 1]]),
    np.array([[1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 0, 1],
              [1, 1, 0, 0, 1, 0],
              [0, 0, 1, 1, 0, 1],
              [0, 1, 0, 0, 1, 1],
              [1, 0, 1, 1, 0, 0]]),
    np.array([[1, 1, 0, 0, 1, 0],
              [0, 0, 1, 1, 0, 1],
              [0, 1, 1, 0, 1, 0],
              [1, 0, 0, 1, 0, 1],
              [1, 1, 0, 1, 0, 0],
              [0, 0, 1, 0, 1, 1]])
]

# Générer les variations
all_variations = []
for grid_index, grid in enumerate(grids):
    variations = generate_variations(grid, 100)  # Ajustez le nombre de variations
    for variation_index, variation in enumerate(variations):
        all_variations.append((f"# Grille {grid_index + 1}.{variation_index + 1}", variation))

# Écrire dans le fichier CSV
write_variations_to_csv(all_variations)

print("Variations sauvegardées dans variations_takuzu.csv")
