<<<<<<< HEAD
import tkinter as tk

# Fonction pour recommencer le jeu
def recommencer():
    canvas.delete("all")  # Efface tout sur le canvas
    dessiner_jeu()  # Redessine les éléments du jeu

# Fonction pour dessiner un élément du jeu + bouton
def dessiner_jeu():
    # Exemple d'un élément du jeu
    canvas.create_oval(150, 100, 250, 200, fill="red", outline="black")

    # Création du bouton "Recommencer" dans le Canvas
    bouton_recommencer = tk.Button(root, text="Recommencer", command=recommencer, font=("Arial", 12), bg="red", fg="white")
    
    # Ajout du bouton dans le canvas
    bouton_window = canvas.create_window(200, 250, window=bouton_recommencer)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Jeu avec Canvas")
root.geometry("400x300")

# Création du Canvas
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Lancer le jeu 
dessiner_jeu()

# Lancer la boucle Tkinter
root.mainloop()

# Paramètres de la grille
ROWS = 6
COLS = 7
CELL_SIZE = 80
RADIUS = CELL_SIZE // 2 - 5

# Couleurs des jetons
PLAYER_COLORS = {1: "red", 2: "yellow"}

# Grille de jeu (0 = vide, 1 = joueur 1, 2 = joueur 2)
grid = [[0] * COLS for _ in range(ROWS)]
current_player = 1  # j1 commence

def draw_grid():
    """Dessine la grille et les jetons déjà placés."""
    canvas.delete("all")
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE + CELL_SIZE // 2
            y = row * CELL_SIZE + CELL_SIZE // 2
            color = PLAYER_COLORS.get(grid[row][col], "white")
            canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS, fill=color, outline="black")

def handle_click(event):
    """Ajoute un jeton dans la colonne sélectionnée."""
    global current_player
    col = event.x // CELL_SIZE
    for row in range(ROWS - 1, -1, -1):
        if grid[row][col] == 0:
            grid[row][col] = current_player
            current_player = 3 - current_player  # Alterne entre 1 et 2
            draw_grid()
            return
        
def recommencer():
    global grid
    grid = [[0] * COLS for _ in range(ROWS)]
    draw_grid()
    
# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Jouons au puissance 4 !")

canvas = tk.Canvas(fenetre, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE, bg="blue")
canvas.pack()
button_recommencer = tk.Button(fenetre, text="Recommencer", command=recommencer)
draw_grid()
canvas.bind("<Button-1>", handle_click)

fenetre.mainloop()
=======
def check_winner():
    """Vérifie si un joueur a gagné."""
    # Vérification horizontale
    df
<<<<<<< HEAD
    sdsd dd
>>>>>>> 8d846a409d969c20986f84c9092d2a5ffb75ba36
=======

    dd

    azaz

    khalifa



>>>>>>> 4fba9ffb6cdd0fac6db523558a94092a3a9db407


dsdsdsdsdsdsdsdsdsdsd