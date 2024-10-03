# Tous les imports et variables

import copy
import time
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
matplotlib.use('TkAgg')
import numpy as np
import random

Route_02 = ["Fin"]
Route_03 = ["Intersection"]
Route_04 = ["Intersection"]
Route_05 = ['Feu', 0, 30, True]
Route_06 = ["Route", 0]
Route_07 = ["Depart", 0, 5]
Route_10 = ["Depart", 2, 5]
Route_11 = ["Route", 2]
Route_12 = ['Feu', 2, 30, True]
Route_13 = ["Intersection"]
Route_14 = ["Intersection"]
Route_15 = ["Fin"]
Route_23 = ["Fin"]
Route_24 = ["Feu", 3, 30, False]
Route_34 = ["Route", 3]
Route_44 = ["Depart", 3, 5]

Traffic_02 = [0]
Traffic_03 = [0]
Traffic_04 = [0]
Traffic_05 = [0]
Traffic_06 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Traffic_07 = [0]
Traffic_10 = [0]
Traffic_11 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Traffic_12 = [0]
Traffic_13 = [0]
Traffic_14 = [0]
Traffic_15 = [0]
Traffic_23 = [0]
Traffic_24 = [0]
Traffic_34 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Traffic_44 = [0]

Direction_02 = []
Direction_03 = []
Direction_04 = []
Direction_05 = [[0.5, 0.5, 0, 0], 0]
Direction_06 = [[1, 0, 0, 0], 0]
Direction_07 = [[1, 0, 0, 0], 0]
Direction_10 = [[0, 0, 1, 0], 0]
Direction_11 = [[0, 0, 1, 0], 0]
Direction_12 = [[0, 0.5, 0.5, 0], 0]
Direction_13 = []
Direction_14 = []
Direction_15 = []
Direction_23 = []
Direction_24 = [[0.5, 0, 0.5, 0], 0]
Direction_34 = [[0, 0, 0, 1], 0]
Direction_44 = [[0, 0, 0, 1], 0]

route = [
    [0, 0, Route_02, Route_03, Route_04, Route_05, Route_06, Route_07],
    [Route_10, Route_11, Route_12, Route_13, Route_14, Route_15, 0, 0],
    [0, 0, 0, Route_23, Route_24, 0, 0, 0],
    [0, 0, 0, 0, Route_34, 0, 0, 0],
    [0, 0, 0, 0, Route_44, 0, 0, 0],
]

traffic = [
    [0, 0, Traffic_02, Traffic_03, Traffic_04, Traffic_05, Traffic_06, Traffic_07],
    [Traffic_10, Traffic_11, Traffic_12, Traffic_13, Traffic_14, Traffic_15, 0, 0],
    [0, 0, 0, Traffic_23, Traffic_24, 0, 0, 0],
    [0, 0, 0, 0, Traffic_34, 0, 0, 0],
    [0, 0, 0, 0, Traffic_44, 0, 0, 0],
]

direction = [
    [0, 0, Direction_02, Direction_03, Direction_04, Direction_05, Direction_06, Direction_07],
    [Direction_10, Direction_11, Direction_12, Direction_13, Direction_14, Direction_15, 0, 0],
    [0, 0, 0, Direction_23, Direction_24, 0, 0, 0],
    [0, 0, 0, 0, Direction_34, 0, 0, 0],
    [0, 0, 0, 0, Direction_44, 0, 0, 0],
]

temps = 0


def update_direction():

    for i in range(len(route)):
        for j in range(len(route[i])):
            if route[i][j] != 0:
                if route[i][j][0] != "Fin" and route[i][j][0] != "Intersection":
                    direction[i][j][1] = random.choices(
                        [0, 1, 2, 3], weights=direction[i][j][0], k=1
                    )[0]


def update_départ():

    global temps

    for i in range(len(route)):
        for j in range(len(route[i])):
            if route[i][j] != 0:
                if route[i][j][0] == "Depart":
                    if random.random() <= route[i][j][2]/60:
                        traffic[i][j][0] += 1


def update_feux_rouges():

    global temps

    for i in range(len(route)):
        for j in range(len(route[i])):
            if route[i][j] != 0:
                if route[i][j][0] == "Feu":
                    if (temps % route[i][j][2]) == 0:
                        route[i][j][3] = not (route[i][j][3])

def update_route():
    update_direction()
    update_départ()
    update_feux_rouges()

"""Fonction qui retourne le chemin pour sortir des intersections"""

def chemin_intersection(pos_x, pos_y):

    pos = route[pos_x][pos_y][1]
    dir = direction[pos_x][pos_y][1]

    if pos == dir:
        return [pos, pos]

    if pos == (dir + 1) % 4:
        return [dir]

    if dir == (pos + 1) % 4:
        return [pos, dir, dir]

"""Donne la liste des intentions"""


def intentions():

    res = []

    for i in range(len(route)):
        for j in range(len(route[i])):
            if route[i][j] != 0:
                if traffic[i][j][-1] >= 1:
                    """Pour la route et les départ la voiture voudra toujour suivre la direction aucune perturbation n'est à prévoir"""
                    """Les questions de priorité se pose généralement sur les bloc intersections ou feu rouge ou priorité"""
                    if route[i][j][0] == "Route" or route[i][j][0] == "Depart":
                        dir_route = route[i][j][1]
                        if dir_route == 0:
                            res.append([i, j, i, j - 1])
                        elif dir_route == 1:
                            res.append([i, j, i + 1, j])
                        elif dir_route == 2:
                            res.append([i, j, i, j + 1])
                        else:
                            res.append([i, j, i - 1, j])

                    """Pour les intersections ca se complique en effet il faut faire attention au priorité à droite"""
                    """La prioirité à droite s'applique si le bloc à droite de la destination est une route occupée"""
                    """De ce fait sur une intersection on peut avancer si le bloc à droite de la destination n'est pas une route"""
                    """Ou alors c'est une route non occupée"""
                    """Dépend de la direction et c'est la où c'est plus chaud matrice des chemins"""
                    if route[i][j][0] == "Intersection":
                        if traffic[i][j][0] == 1:
                            dir_inter = direction[i][j][0]
                            if dir_inter == 0:
                                if 0 <= i - 1 <= len(route) and 0 <= j - 1 <= len(
                                    route[i]
                                ):
                                    if route[i - 1][j - 1] != 0:
                                        if route[i - 1][j - 1][0] != "Route":
                                            res.append([i, j, i, j - 1])
                                        elif traffic[i - 1][j - 1][-1] == 0:
                                            res.append([i, j, i, j - 1])
                                    else:
                                        res.append([i, j, i, j - 1])
                                else:
                                    res.append([i, j, i, j - 1])
                            elif dir_inter == 1:
                                if 0 <= i + 1 <= len(route) and 0 <= j - 1 <= len(
                                    route[i]
                                ):
                                    if route[i + 1][j - 1] != 0:
                                        if route[i + 1][j - 1][0] != "Route":
                                            res.append([i, j, i + 1, j])
                                        elif traffic[i + 1][j - 1][-1] == 0:
                                            res.append([i, j, i + 1, j])
                                    else:
                                        res.append([i, j, i + 1, j])
                                else:
                                    res.append([i, j, i + 1, j])
                            elif dir_inter == 2:
                                if 0 <= i + 1 <= len(route) and 0 <= j + 1 <= len(
                                    route[i]
                                ):
                                    if route[i + 1][j + 1] != 0:
                                        if (
                                            route[i + 1][j + 1][0] != "Route"
                                            or traffic[i + 1][j + 1][-1] == 0
                                        ):
                                            res.append([i, j, i, j + 1])
                                    else:
                                        res.append([i, j, i, j + 1])
                                else:
                                    res.append([i, j, i, j + 1])
                            else:
                                if 0 <= i - 1 <= len(route) and 0 <= j + 1 <= len(
                                    route[i]
                                ):
                                    if route[i - 1][j + 1] != 0:
                                        if (
                                            route[i - 1][j + 1][0] != "Route"
                                            or traffic[i - 1][j + 1][-1] == 0
                                        ):
                                            res.append([i, j, i - 1, j])
                                    else:
                                        res.append([i, j, i - 1, j])
                                else:
                                    res.append([i, j, i - 1, j])

                    """Feux rouges : pour les feux rouges il va dans la direction si le feu est vert"""
                    """Attention execption si le feu rouge est relier à une intersection"""
                    """Et que celle-ci est pleine (voiture sur la gauche) alors on le laisse passer = évite les blocages"""
                    if route[i][j][0] == "Feu":
                        if route[i][j][-1] == True:
                            dir_feu = route[i][j][1]
                            if dir_feu == 0:
                                if 0 <= i + 1 <= len(route) and 0 <= j - 1 <= len(
                                    route[i]
                                ):
                                    if route[i][j - 1] != 0:
                                        if (
                                            route[i][j - 1][0] == "Intersection"
                                            and traffic[i + 1][j - 1][-1] == 0
                                        ):
                                            res.append([i, j, i, j - 1])
                                    else:
                                        res.append([i, j, i, j - 1])
                                else:
                                    res.append([i, j, i, j - 1])
                            elif dir_feu == 1:
                                if 0 <= i + 1 <= len(route) and 0 <= j + 1 <= len(
                                    route[i]
                                ):
                                    if route[i + 1][j] != 0:
                                        if (
                                            route[i + 1][j][0] == "Intersection"
                                            and traffic[i + 1][j + 1][-1] == 0
                                        ):
                                            res.append([i, j, i + 1, j])
                                    else:
                                        res.append([i, j, i + 1, j])
                                else:
                                    res.append([i, j, i + 1, j])
                            elif dir_feu == 2:
                                if 0 <= i - 1 <= len(route) and 0 <= j + 1 <= len(
                                    route[i]
                                ):
                                    if route[i][j + 1] != 0:
                                        if (
                                            route[i][j + 1][0] == "Intersection"
                                            and traffic[i - 1][j + 1][-1] == 0
                                        ):
                                            res.append([i, j, i, j + 1])
                                    else:
                                        res.append([i, j, i, j + 1])
                                else:
                                    res.append([i, j, i, j + 1])
                            else:
                                if 0 <= i - 1 <= len(route) and 0 <= j - 1 <= len(
                                    route[i]
                                ):
                                    if route[i - 1][j] != 0:
                                        if (
                                            route[i - 1][j][0] == "Intersection"
                                            and traffic[i - 1][j - 1][-1] == 0
                                        ):
                                            res.append([i, j, i - 1, j])
                                    else:
                                        res.append([i, j, i - 1, j])
                                else:
                                     res.append([i, j, i - 1, j])

                    """Pour les priorités suivant la direction il faut :"""
                    """Si le choix de la desico, implique de couper 1 seule route alors il faut qu'il n'y est personne sur la voie coupé"""
                    """On estime qu'une voie est libre si il y a 3 emplacement vacants"""
                    """Si le choix implique de couper """
                    if route[i][j][0] == "Priorite":
                        sens_prio = route[i][j][1]
                        dir_prio = direction[i][j][1]
                        """Cas 1 voie coupé """
                        if dir_prio == (sens_prio + 1) % 4:
                            if sens_prio == 0:
                                if (
                                    0 <= i + 1 <= len(route)
                                    and 0 <= i + 2 <= len(route)
                                    and 0 <= j - 1 <= len(route[i])
                                ):
                                    if (
                                        traffic[i + 1][j - 1][-1] == 0
                                        and traffic[i + 2][j - 1][-1] == 0
                                        and traffic[i + 2][j - 1][-2] == 0
                                    ):  # ATTENTION NE MARCHE QUE POUR NOTRE CAS A MODIFIER SI GENERALISATION
                                        res.append([i, j, i, j - 1])
                            elif sens_prio == 1:
                                if (
                                    0 <= i + 1 <= len(route)
                                    and 0 <= j + 1 <= len(route)
                                    and 0 <= j + 2 <= len(route[i])
                                ):
                                    if (
                                        traffic[i + 1][j + 1][-1] == 0
                                        and traffic[i + 1][j + 2][-1] == 0
                                        and traffic[i + 1][j + 2][-2] == 0
                                    ):  # ATTENTION NE MARCHE QUE POUR NOTRE CAS A MODIFIER SI GENERALISATION
                                        res.append([i, j, i + 1, j])
                            elif sens_prio == 2:
                                if (
                                    0 <= i - 1 <= len(route)
                                    and 0 <= i - 2 <= len(route)
                                    and 0 <= j + 1 <= len(route[i])
                                ):
                                    if (
                                        traffic[i - 1][j + 1][-1] == 0
                                        and traffic[i - 2][j + 1][-1] == 0
                                        and traffic[i - 2][j + 1][-2] == 0
                                    ):  # ATTENTION NE MARCHE QUE POUR NOTRE CAS A MODIFIER SI GENERALISATION
                                        res.append([i, j, i, j + 1])
                            else:
                                if (
                                    0 <= i - 1 <= len(route)
                                    and 0 <= j - 1 <= len(route)
                                    and 0 <= j - 2 <= len(route[i])
                                ):
                                    if (
                                        traffic[i - 1][j - 1][-1] == 0
                                        and traffic[i - 1][j - 2][-1] == 0
                                        and traffic[i - 1][j - 2][-2] == 0
                                    ):  # ATTENTION NE MARCHE QUE POUR NOTRE CAS A MODIFIER SI GENERALISATION
                                        res.append([i, j, i - 1, j])

    return res

def mouvement(n):

    global temps

    for _ in range(n):

        """Pour rappel la route est une matrice 2x2"""

        update_route()

        ref_traffic = copy.deepcopy(traffic)

        intention = intentions()

        for i in range(len(intention)):
            x = intention[i][0]
            y = intention[i][1]
            nx = intention[i][2]
            ny = intention[i][3]

            # Cas particulier départ autres blocs
            if route[x][y][0] == "Depart":
                if traffic[nx][ny][0] == 0:
                    traffic[nx][ny][0] += 1
                    traffic[x][y][-1] -= 1

            # Cas particulier intersection->intersection
            elif route[nx][ny][0] == "Intersection" and route[x][y][0] == "Intersection":
                if traffic[nx][ny][0] == 0 and ref_traffic[nx][ny][0] == 0:
                    direction[nx][ny] = direction[x][y][1::]
                    direction[x][y] = []
                    traffic[nx][ny][0] += 1
                    traffic[x][y][-1] -= 1

                # Cas particulier non/intersection->intersection
            elif (
                route[nx][ny][0] == "Intersection" and route[x][y][0] != "Intersection"
            ):
                if traffic[nx][ny][0] == 0 and ref_traffic[nx][ny][0] == 0:
                    direction[nx][ny] = chemin_intersection(x, y)
                    traffic[nx][ny][0] += 1
                    traffic[x][y][-1] -= 1

            # Cas particulier intersection->non-intersection
            elif route[nx][ny][0] != "Intersection" and route[x][y][0] == "Intersection":
                if route[nx][ny][0] == 'Fin':
                    direction[x][y] = []
                    traffic[nx][ny][0] += 1
                    traffic[x][y][-1] -= 1
                elif traffic[nx][ny][0] == 0 and ref_traffic[nx][ny][0] == 0:    
                    direction[x][y] = []
                    traffic[nx][ny][0] += 1
                    traffic[x][y][-1] -= 1

                # Cas général
            else:
                if route[nx][ny][0] == 'Fin':
                    traffic[nx][ny][0] += 1
                    traffic[x][y][-1] -= 1
                elif traffic[nx][ny][0] == 0 and ref_traffic[nx][ny][0] == 0:    
                    traffic[nx][ny][0] += 1
                    traffic[x][y][-1] -= 1

        for i in range(len(route)):
            for j in range(len(route[i])):
                if route[i][j] != 0:
                    if route[i][j][0] == "Route":
                        for k in range(2, len(traffic[i][j]) + 1):
                            if (
                                traffic[i][j][-k] == 1
                                and traffic[i][j][-k + 1] == 0
                                and ref_traffic[i][j][-k + 1] == 0
                            ):
                                traffic[i][j][-k + 1] += 1
                                traffic[i][j][-k] -= 1

        temps += 1

# Fonction de simulation
def simulation(frame, ax, traffic_matrix, n_rows, n_cols):
    ax.clear()  # Effacer l'axe pour le prochain frame

    # Parcourir la matrice et ajouter des éléments graphiques
    for i in range(n_rows):
        for j in range(n_cols):
            value = traffic_matrix[i][j]
            
            # Si c'est une case vide (0)
            if value == 0:
                ax.add_patch(patches.Rectangle((j, n_rows - 1 - i), 1, 1, fill=True, color='white'))
            
            # Si c'est une voiture simple (1)
            elif value == [1]:
                ax.add_patch(patches.Rectangle((j, n_rows - 1 - i), 1, 1, fill=True, color='black'))
            
            # Si c'est une route (liste avec plusieurs valeurs)
            elif isinstance(value, list) and len(value) > 1:
                route_len = len(value)
                sub_w = 1 / route_len  # Largeur de la sous-case
                
                # Diviser la case en plusieurs sous-cases pour chaque élément de la route
                for k, sub_value in enumerate(value):
                    sub_x = j + (k * sub_w)  # Position en x de la sous-case
                    color = 'Grey' if sub_value == 1 else 'white'
                    ax.add_patch(patches.Rectangle((sub_x, n_rows - 1 - i), sub_w, 1, fill=True, color=color))
            
            # Si c'est une zone de départ ou fin (nombre > 1)
            elif isinstance(value, list) and value[0] > 1:
                ax.add_patch(patches.Rectangle((j, n_rows - 1 - i), 1, 1, fill=True, color='lightblue'))
                ax.text(j + 0.5, n_rows - 1 - i + 0.5, str(value[0]), color='red', weight='bold', ha='center', va='center')

    # Réglages de la grille
    ax.set_xlim(0, n_cols)
    ax.set_ylim(0, n_rows)
    ax.set_xticks(np.arange(0, n_cols, 1))
    ax.set_yticks(np.arange(0, n_rows, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True)

    ax.set_aspect('equal', adjustable='box')
    ax.set_title("Simulation du traffic au temps : " + str(frame))

# Fonction pour générer une animation en mettant à jour la matrice de trafic
def update(frame,ax):
    # Simuler le mouvement des véhicules (fonction fictive)
    mouvement(1)  # Met à jour la matrice 'traffic'

    # Taille de la matrice
    n_rows = len(traffic)
    n_cols = len(traffic[0])
    
    # Appeler la fonction de simulation pour mettre à jour le graphique
    simulation(frame, ax, traffic, n_rows, n_cols)


# Initialisation de la simulation
fig, ax = plt.subplots()
n_rows = len(traffic)
n_cols = len(traffic[0])

# Créer l'animation
ani = FuncAnimation(fig, update, frames=1000,fargs=(ax,), repeat=False)

# Afficher l'animation
plt.show()