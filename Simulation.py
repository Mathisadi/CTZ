# @Autor : Mathis Adinolfi
# @Date of creation : 25/09/2024

# Bibliothéques utilisées
from Modele import *
from Data import *
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import numpy as np

# Objectif : Faire une simulation

def simulation(frame, ax, route, direction, trafic, n_rows, n_cols):
    ax.clear()  # Effacer l'axe pour le prochain frame

    # Parcourir la matrice et ajouter des éléments graphiques
    for i in range(n_rows):
        for j in range(n_cols):
            elm = route[i][j]
            dir = direction[i][j]
            value = trafic[i][j]

            # Si c'est une case vide (0)
            if elm == 0:
                ax.add_patch(
                    patches.Rectangle(
                        (j, n_rows - 1 - i),
                        1,
                        1,
                        fill=True,
                        color="white",
                    )
                )

            # Si c'est une route
            elif elm[0] == "Route":
                route_len = len(value)
                sub_w = 1 / route_len  # Largeur de la sous-case
                dir = elm[1]

                if dir == 0:
                    value = value[::-1]
                    # Diviser la case en plusieurs sous-cases pour chaque élément de la route
                    for k, sub_value in enumerate(value):
                        sub_x = j + (k * sub_w)  # Position en x de la sous-case
                        color = "Grey" if sub_value == 1 else "white"
                        ax.add_patch(
                            patches.Rectangle(
                                (sub_x, n_rows - 1 - i),
                                sub_w,
                                1,
                                fill=True,
                                color=color,
                            )
                        )

                elif dir == 1:
                    value = value[::-1]
                    # Diviser la case en plusieurs sous-cases pour chaque élément de la route
                    for k, sub_value in enumerate(value):
                        sub_y = (
                            n_rows - 1 - i + (k * sub_w)
                        )  # Position en x de la sous-case
                        color = "Grey" if sub_value == 1 else "white"
                        ax.add_patch(
                            patches.Rectangle(
                                (j, sub_y), 1, sub_w, fill=True, color=color
                            )
                        )

                elif dir == 2:
                    # Diviser la case en plusieurs sous-cases pour chaque élément de la route
                    for k, sub_value in enumerate(value):
                        sub_x = j + (k * sub_w)  # Position en x de la sous-case
                        color = "Grey" if sub_value == 1 else "white"
                        ax.add_patch(
                            patches.Rectangle(
                                (sub_x, n_rows - 1 - i),
                                sub_w,
                                1,
                                fill=True,
                                color=color,
                            )
                        )

                else:
                    # Diviser la case en plusieurs sous-cases pour chaque élément de la route
                    for k, sub_value in enumerate(value):
                        sub_y = (
                            n_rows - 1 - i + (k * sub_w)
                        )  # Position en x de la sous-case
                        color = "Grey" if sub_value == 1 else "white"
                        ax.add_patch(
                            patches.Rectangle(
                                (j, sub_y), 1, sub_w, fill=True, color=color
                            )
                        )

            # Si c'est une intersection et pleine
            elif value == [1] and elm[0] == "Intersection":
                ax.add_patch(
                    patches.Rectangle(
                        (j, n_rows - 1 - i), 1, 1, fill=True, color="Grey"
                    )
                )

                if dir[0] == 0:  # Gauche
                    pos_a = (j + 3 / 4, n_rows - 1 - i + 1 / 2)  # Position initiale (centre, bas)
                    dx, dy = -1 / 2, 0  # Incrément vertical
                elif dir[0] == 1:  # Bas
                    pos_a = (j + 1 / 2, n_rows - 1 - i + 3 / 4)
                    dx, dy = 0, -1 / 2  # Incrément vertica l
                elif dir[0] == 2:  # Droite
                    pos_a = (j + 1 / 4, n_rows - 1 - i + 1 / 2)  # Position initiale (droite, centre)
                    dx, dy = 1 / 2, 0  # Incrément horizontal
                else:  # Haut
                    pos_a = (j + 1 / 2, n_rows - 1 - i + 1 / 4)
                    dx, dy = 0, 1 / 2  # Incrément horizontal

                # Ajouter la flèche (avec coordonnées de départ et direction)
                ax.add_patch(
                    patches.FancyArrow(
                        pos_a[0], pos_a[1], dx, dy, width=0.02, color="black"
                    )
                )

            # Si c'est une priorité
            elif elm[0] == "Priorite":
                # Pleine
                if value == [1]:
                    ax.add_patch(
                        patches.Rectangle(
                            (j, n_rows - 1 - i), 1, 1, fill=True, color="black"
                        )
                    )
                # Vide
                else:
                    ax.add_patch(
                        patches.Rectangle(
                            (j, n_rows - 1 - i), 1, 1, fill=True, color="white"
                        )
                    )

                # On ajoute le STOP
                dir = elm[1]

                if dir == 0:
                    ax.add_patch(
                        patches.Rectangle(
                            (j, n_rows - 1 - i), 1 / 4, 1, fill=True, color="red"
                        )
                    )

                    ax.text(
                        (j + 1 / 8, n_rows - 1 - i + 1 / 2),
                        "STOP",
                        horizontalalignment="center",
                        verticalalignment="center",
                        fontsize=10,
                        color="white",
                        rotation=90,
                    )

                elif dir == 1:
                    ax.add_patch(
                        patches.Rectangle(
                            (j, n_rows - 1 - i), 1, 1 / 4, fill=True, color="red"
                        )
                    )

                    ax.text(
                        (j + 1 / 2, n_rows - 1 - i + 1 / 8),
                        "STOP",
                        horizontalalignment="center",
                        verticalalignment="center",
                        fontsize=10,
                        color="white",
                        rotation=180,
                    )

                elif dir == 2:
                    ax.add_patch(
                        patches.Rectangle(
                            (j + 3 / 4, n_rows - 1 - i + 3 / 4),
                            1 / 4,
                            1,
                            fill=True,
                            color="red",
                        )
                    )

                    ax.text(
                        (j + 7 / 8, n_rows - 1 - i + 1 / 2),
                        "STOP",
                        horizontalalignment="center",
                        verticalalignment="center",
                        fontsize=10,
                        color="white",
                        rotation=270,
                    )

                else:
                    ax.add_patch(
                        patches.Rectangle(
                            (j, n_rows - 1 - i + 3 / 4),
                            1,
                            1 / 4,
                            fill=True,
                            color="red",
                        )
                    )

                    ax.text(
                        (j + 1 / 2, n_rows - 1 - i + 7 / 8),
                        "STOP",
                        horizontalalignment="center",
                        verticalalignment="center",
                        fontsize=10,
                        color="white",
                      rotation=0,
                    )

            # Si c'est un feu rouge
            elif elm[0] == "Feu":
                # Couleur Feu
                couleur_feu = "green" if elm[-1] == True else "red"

                ax.add_patch(
                    patches.Rectangle(
                        (j, n_rows - 1 - i),
                        1,
                        1,
                        fill=True,
                        color=couleur_feu,
                    )
                )
                
                couleur = "Grey" if value == [1] else "white"
                
                ax.add_patch(
                    patches.Circle((j + 1 / 2, n_rows - 1 - i + 1 / 2),
                                    1/16,
                                    fill = True,
                                    color = couleur)
                )

            # Si c'est une zone de départ ou fin (nombre > 1)
            elif elm[0] == "Fin" or elm[0] == "Depart":
                ax.add_patch(
                    patches.Rectangle(
                        (j, n_rows - 1 - i), 1, 1, fill=True, color="lightblue"
                    )
                )

                ax.text(
                    j + 0.5,
                    n_rows - 1 - i + 0.5,
                    str(elm[0]) + " : " + str(value[0]),
                    color="black",
                    fontsize = 8,
                    ha="center",
                    va="center",
                )
            
            # Si c'est un depart de passage pieton
            elif elm[0] == "Depart_pieton":
                ax.add_patch(
                    patches.Rectangle(
                        (j, n_rows - 1 - i), 1, 1, fill=True, color="lightgreen"
                    )
                )

                ax.text(
                    j + 0.5,
                    n_rows - 1 - i + 0.5,
                    'Pieton',
                    color="black",
                    fontsize = 8,
                    ha="center",
                    va="center",
                )
            
            # Si c'est un passage piéton
            elif elm[0] == "Pieton":
                # Couleur paddage
                if elm[1] == [0,2]:
                    couleur_bas = "orange" if elm[-1][0] == True else "white"
                    couleur_haut = "orange" if elm[-1][2] == True else "white"
                    
                    # Rectangle bas
                    ax.add_patch(
                        patches.Rectangle(
                            (j, n_rows - 1 - i),
                            1,
                            1/2,
                            fill=True,
                            color=couleur_bas,
                        )
                    )
                    
                    # Rectangle haut
                    ax.add_patch(
                        patches.Rectangle(
                            (j, n_rows - 1 - i + 1/2),
                            1,
                            1/2,
                            fill=True,
                            color=couleur_haut,
                        )
                    )
                    
                    couleur = "Grey" if value == [1] else "white"
                    
                    ax.add_patch(
                        patches.Circle((j + 1 / 2, n_rows - 1 - i + 1 / 2),
                                        1/16,
                                        fill = True,
                                        color = couleur)
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
    ax.set_title("Simulation du trafic au temps : " + str(frame), pad = 20)

# Fonction pour générer une animation en mettant à jour la matrice de trafic
def update(frame, ax, route, direction, trafic):
    # Simuler le mouvement des véhicules (fonction fictive)
    r = mouvement(route, direction, trafic, frame)
    route, direction, trafic = r[0], r[1], r[2]

    # Taille de la matrice
    n_rows = len(trafic)
    n_cols = len(trafic[0])

    # Appeler la fonction de simulation pour mettre à jour le graphique
    simulation(frame, ax, route, direction, trafic, n_rows, n_cols)

# Initialisation de la simulation
fig, ax = plt.subplots()
n_rows = len(trafic_etude)
n_cols = len(trafic_etude[0])

# Créer l'animation
ani = FuncAnimation(
    fig,
    update,
    frames=range(1, duree + 1),
    fargs=(ax, route_etude, direction_etude, trafic_etude),
    repeat=False,
)

# Afficher l'animation
plt.show()