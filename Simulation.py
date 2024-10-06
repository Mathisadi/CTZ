import Modele
from Variables import *
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import numpy as np

# Simulation

def simulation(frame, ax, traffic_matrix, n_rows, n_cols):
    ax.clear()  # Effacer l'axe pour le prochain frame

    # Parcourir la matrice et ajouter des éléments graphiques
    for i in range(n_rows):
        for j in range(n_cols):
            value = traffic_matrix[i][j]

            # Si c'est une case vide (0)
            if value == 0:
                ax.add_patch(
                    patches.Rectangle(
                        (j, n_rows - 1 - i), 1, 1, fill=True, color="white"
                    )
                )

            # Si c'est une voiture simple (1)
            elif value == [1]:
                ax.add_patch(
                    patches.Rectangle(
                        (j, n_rows - 1 - i), 1, 1, fill=True, color="black"
                    )
                )

            # Si c'est une route (liste avec plusieurs valeurs)
            elif isinstance(value, list) and len(value) > 1:
                route_len = len(value)
                sub_w = 1 / route_len  # Largeur de la sous-case

                # Diviser la case en plusieurs sous-cases pour chaque élément de la route
                for k, sub_value in enumerate(value):
                    sub_x = j + (k * sub_w)  # Position en x de la sous-case
                    color = "Grey" if sub_value == 1 else "white"
                    ax.add_patch(
                        patches.Rectangle(
                            (sub_x, n_rows - 1 - i), sub_w, 1, fill=True, color=color
                        )
                    )

            # Si c'est une zone de départ ou fin (nombre > 1)
            elif isinstance(value, list) and value[0] > 1:
                ax.add_patch(
                    patches.Rectangle(
                        (j, n_rows - 1 - i), 1, 1, fill=True, color="lightblue"
                    )
                )
                ax.text(
                    j + 0.5,
                    n_rows - 1 - i + 0.5,
                    str(value[0]),
                    color="red",
                    weight="bold",
                    ha="center",
                    va="center",
                )

    # Réglages de la grille
    ax.set_xlim(0, n_cols)
    ax.set_ylim(0, n_rows)
    ax.set_xticks(np.arange(0, n_cols, 1))
    ax.set_yticks(np.arange(0, n_rows, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True)

    ax.set_aspect("equal", adjustable="box")
    ax.set_title("Simulation du traffic au temps : " + str(frame))


# Fonction pour générer une animation en mettant à jour la matrice de trafic
def update(frame, ax, route, direction, traffic):
    # Simuler le mouvement des véhicules (fonction fictive)
    r = Modele.mouvement(route, direction, traffic, frame)
    direction, traffic = r[1], r[2]

    # Taille de la matrice
    n_rows = len(traffic)
    n_cols = len(traffic[0])

    # Appeler la fonction de simulation pour mettre à jour le graphique
    simulation(frame, ax, traffic, n_rows, n_cols)


# Initialisation de la simulation
fig, ax = plt.subplots()
n_rows = len(traffic_etude)
n_cols = len(traffic_etude[0])

# Créer l'animation
ani = FuncAnimation(
    fig,
    update,
    frames=duree,
    fargs=(ax, route_etude, direction_etude, traffic_etude),
    repeat=False,
)

# Afficher l'animation
plt.show()
