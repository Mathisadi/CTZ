# @Autor : Mathis Adinolfi
# @Date of creation : 02/10/2024

# Bibliothèques utilisées

import copy
import time
import random
from Variables import *

# Modéle Traffic


def update_direction(route, direction):
    """Cette fonction modifie les choix de trajet des utilisateurs de manière aléatoire afin de respecter les
    probas observées sur le terrain

    Args:
        route (2D list): Liste des élements de notre route
        direction (2D list): Liste des préferences de direction des utilisateur pour chaque élement et la direction choisie

    Returns:
        direction (2D list): Retourne la liste des direction modifiée
    """

    for i in range(len(route)):
        for j in range(len(route[i])):
            if route[i][j] != 0:
                if route[i][j][0] != "Fin" and route[i][j][0] != "Intersection":
                    direction[i][j][1] = random.choices(
                        [0, 1, 2, 3], weights=direction[i][j][0], k=1
                    )[0]

    return direction


def update_départ(route, traffic):
    """Cette fonction permet de générer des voitures dans les cases départ de manière aléatoire,
    tout en respectant le débit d'entrée

    Args:
        route (2D list): Liste des élements de notre route
        traffic (2D list): Liste resprésentant le traffic de notre route 0 = vide / 1 = voiture

    Returns:
        traffic (2D list): Ajoute les voitures générées sur les cases départs
    """

    for i in range(len(route)):
        for j in range(len(route[i])):
            if route[i][j] != 0:
                if route[i][j][0] == "Depart":
                    if random.random() <= route[i][j][2] / 60:
                        traffic[i][j][0] += 1

    return traffic


def update_feux_rouges(route, temps):
    """Cette fonction permet de mettre à jour les feux rouges de notre route

    Args:
        route (2D list): Liste des élements de notre route
        temps (int): Temps depuis début de la simulation en seconde

    Returns:
        route (2D list): Retourne la route avec les feux rouges modifiés
    """
    for i in range(len(route)):
        for j in range(len(route[i])):
            if route[i][j] != 0:
                if route[i][j][0] == "Feu":
                    if (temps % route[i][j][2]) == 0:
                        route[i][j][3] = not (route[i][j][3])

    return route


# TODO : Modifer la fonction pour prendre en compte toutes les intersection


def dfs(route, pos_i, pos_j, visited, inter):

    n, m = len(route), len(route[0])
    pile = [(pos_i, pos_j)]
    r = []

    while pile:
        i, j = pile.pop()

        if visited[i][j]:
            continue

        visited[i][j] = True
        r.append((i, j))

        dir = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

        for x, y in dir:
            if (
                0 <= x < n
                and 0 <= y < m
                and route[i][j] != 0
                and route[x][y][0] == "Intersection"
                and not visited[x][y]
            ):
                pile.append((x, y))

    inter.append(r)

    return visited, inter


def trouve_intersection(route):
    """Cette fonction à pour but de trouver les ensemble d'intersection et retourne une liste ou l'on voit clairement les intersections.

    Args:
        route (2D list): Liste des élements de notre route

    Returns:
        res (2D list): Map des intersections numérotées
    """

    compt = 1
    inter = []
    visited = [[False for _ in range(len(route[0]))] for _ in range(len(route))]

    for i in range(len(route)):
        for j in range(len(route[i])):
            if (
                not visited[i][j]
                and route[i][j] != 0
                and route[i][j][0] == "Intersection"
            ):
                visited, inter = dfs(route, i, j, visited, inter)

    return inter


def trouve_direction_case(route, pos_i, pos_j):

    if route[pos_i][pos_j] == 0:
        raise AssertionError("L'élément choisi n'est pas une intersection")
    elif route[pos_i][pos_j][0] != "Intersection":
        raise AssertionError("L'élément choisi n'est pas une intersection")

    n, m = len(route), len(route[0])
    res = [False, False, False, False]
    dir = [
        (pos_i, pos_j - 1),
        (pos_i + 1, pos_j),
        (pos_i, pos_j + 1),
        (pos_i - 1, pos_j),
    ]

    for index, (i, j) in enumerate(dir):

        if route[i][j] != 0 and 0 <= i < n and 0 <= j < m:
            if route[i][j][0] == "Fin":
                res[index] = True
            elif route[i][j][0] == "Intersection":
                if route_etude[i][j][1][(index + 2) % 4] == True:
                    res[(index + 2) % 4] = True
            else:
                if route[i][j][1] == index or route[i][j][1] == (index + 2) % 4:
                    res[route[i][j][1]] = True

    return res

def initialisation_direction_intersection_antihoraire(route):

    tab = trouve_intersection(route)

    for inter in tab:

        # On doit trouver la taille de l'intersection
        min_i, min_j = inter[0]
        max_i, max_j = inter[0]

        for pos in inter:
            min_i = min(min_i, pos[0])
            min_j = min(min_j, pos[1])
            max_i = max(max_i, pos[0])
            max_j = max(max_j, pos[1])

        # On doit trouver le coin droit min i et max j
        coin_droit = (min_i, max_j)

        # Une fois le coin droit trouver on ajoute les directions jusqu'à avoir tout visité
        visited = []
        compt = 0

        while coin_droit not in visited and coin_droit in inter:

            for pos in inter:
                # Barre haute
                if (
                    pos[0] == min_i
                    and min_j <= pos[1] <= max_j
                    and pos[1] - 1 > 0
                    and route[pos[0]][pos[1] - 1] != 0
                ):
                    route[pos[0]][pos[1]][1][0] = True
                    visited.append(pos)
                # Barre droite
                if (
                    pos[1] == max_j
                    and min_j <= pos[1] <= max_j
                    and pos[0] + 1 < len(route)
                    and route[pos[0] + 1][pos[1]] != 0
                ):
                    route[pos[0]][pos[1]][1][3] = True
                    visited.append(pos)
                # Barre bas
                if (
                    pos[0] == max_i
                    and min_j <= pos[1] <= max_j
                    and pos[1] + 1 < len(route[0])
                    and route[pos[0]][pos[1] + 1] != 0
                ):
                    route[pos[0]][pos[1]][1][2] = True
                    visited.append(pos)
                # Barre gauche
                if (
                    pos[1] == min_j
                    and min_i <= pos[0] <= max_i
                    and pos[0] - 1 > 0
                    and route[pos[0] - 1][pos[1]] != 0
                ):
                    route[pos[0]][pos[1]][1][1] = True
                    visited.append(pos)

            # On repositionne le coin droit
            min_i += 1
            max_i -= 1
            min_j += 1
            max_j -= 1
            
            coin_droit = (min_i, max_j)
    
    return route

print(initialisation_direction_intersection_antihoraire(route_etude))


def direction_intersection(route):

    n, m = len(route), len(route[0])
    inter = trouve_intersection(route)
    nbr_inter = max(max(row) for row in inter)

    for i in range(1, max + 1):

        x, y = 0, 0

        # On trouve le coin haut gauche
        while (x != n - 1 or y != m - 1) and inter[x][y] != i:
            if x < n - 1:
                x += 1
            elif x == n - 1 and y != m - 1:
                x = 0
                y += 1

        # Sens route = Anti horaire

        dir = 0

    return route


def chemin_intersection(route, direction, pos_x, pos_y):
    """Cette fonction permet de,determiner le chemin à emprunter pour une voiture dans une intersection

    Args:
        route (2D list): Liste des élements de notre route
        direction (2D list): Liste des préferences de direction des utilisateur pour chaque élement et la direction choisie
        pos_x (int): Indique la position en x de la voiture
        pos_y (int): Indique la position en y de la voiture

    Returns:
        res (1D list): Retourne les mouvement à réalisés pour sortir de l'intersection
    """

    pos = route[pos_x][pos_y][1]
    dir = direction[pos_x][pos_y][1]

    if pos == dir:
        return [pos, pos]

    if pos == (dir + 1) % 4:
        return [dir]

    if dir == (pos + 1) % 4:
        return [pos, dir, dir]


# TODO : Ajouter la condition des piétons
# TODO : Généraliser cette fonction pour des routes à plusieurs voies
# TODO : Prioirité à droite si on est sur une route
# TODO : Reprendre architecture du projet


def intentions(route, direction, traffic):
    """Cette fonction permet de faire la liste de l'ensemble des mouvement entre les différents éléments de la route
    possible, pour cela les utilisateurs doivents respecter des régles : le code de la route. Ainsi cette fonction
    retranscrit ces règles.

    Args:
        route (2D list): Liste des élements de notre route
        direction (2D list): Liste des préferences de direction des utilisateur pour chaque élement et la direction choisie
        traffic (2D list): Liste resprésentant le traffic de notre route 0 = vide / 1 = voiture

    Returns:
        res (2D list): Retourne l'ensemble des changement de blocs en indiquant le point de départ et l'arrivée
    """

    res = []

    for i in range(len(route)):
        for j in range(len(route[i])):
            if route[i][j] != 0:
                if traffic[i][j][-1] >= 1:
                    # * Pour la route et les départ la voiture voudra toujour suivre la direction aucune perturbation n'est à prévoir
                    # ! Les questions de priorité se pose généralement sur les bloc intersections ou feu rouge ou priorité
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

                    # ! Pour les intersections ca se complique en effet il faut faire attention au priorité à droite
                    # * La prioirité à droite s'applique si le bloc à droite de la destination est une route occupée
                    # * De ce fait sur une intersection on peut avancer si le bloc à droite de la destination n'est pas une route
                    # * Ou alors c'est une route non occupée
                    # * Dépend de la direction et c'est la où c'est plus chaud matrice des chemins
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

                    # * Feux rouges : pour les feux rouges il va dans la direction si le feu est vert
                    # * Attention execption si le feu rouge est relier à une intersection
                    # ! Et que celle-ci est pleine (voiture sur la gauche) alors on le laisse passer = évite les blocages"""
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

                    # * Pour les priorités suivant la direction il faut :
                    # * Si le choix de la desico, implique de couper 1 seule route alors il faut qu'il n'y est personne sur la voie coupé
                    # ! 0n estime qu'une voie est libre si il y a 3 emplacement vacants
                    # * Si le choix implique de couper
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
                                    ):  # ! ATTENTION NE MARCHE QUE POUR NOTRE CAS A MODIFIER SI GENERALISATION
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
                                    ):  # ! ATTENTION NE MARCHE QUE POUR NOTRE CAS A MODIFIER SI GENERALISATION
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
                                    ):  # ! ATTENTION NE MARCHE QUE POUR NOTRE CAS A MODIFIER SI GENERALISATION
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
                                    ):  # ! ATTENTION NE MARCHE QUE POUR NOTRE CAS A MODIFIER SI GENERALISATION
                                        res.append([i, j, i - 1, j])

    return res


def mouvement(route, direction, traffic, temps):
    """Cette fonction a pour but de faire avancer les voitures et de mettre à jour le traffic,
    1 itération correspond à 1 seconde.

    Args:
        route (2D list): Liste des élements de notre route
        direction (2D list): Liste des préferences de direction des utilisateur pour chaque élement et la direction choisie
        traffic (2D list): Liste resprésentant le traffic de notre route 0 = vide / 1 = voiture
        temps (int): Temps depuis début de la simulation en seconde

    Returns:
        route (2D list): Element de la route mis à jour à t = temps
        traffic (2D list): Traffic mis à jour aprés mouvement des voitures
        direction (2D list): Mise à jour des directions dans les intersections
    """

    # Update des éléments
    direction = update_direction(route, direction)
    traffic = update_départ(route, traffic)
    route = update_feux_rouges(route, temps)

    # On garde en copie le traffic
    ref_traffic = copy.deepcopy(traffic)

    intention = intentions(route, direction, traffic)

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
        elif route[nx][ny][0] == "Intersection" and route[x][y][0] != "Intersection":
            if traffic[nx][ny][0] == 0 and ref_traffic[nx][ny][0] == 0:
                direction[nx][ny] = chemin_intersection(route, direction, x, y)
                traffic[nx][ny][0] += 1
                traffic[x][y][-1] -= 1

        # Cas particulier intersection->non-intersection
        elif route[nx][ny][0] != "Intersection" and route[x][y][0] == "Intersection":
            if route[nx][ny][0] == "Fin":
                direction[x][y] = []
                traffic[nx][ny][0] += 1
                traffic[x][y][-1] -= 1
            elif traffic[nx][ny][0] == 0 and ref_traffic[nx][ny][0] == 0:
                direction[x][y] = []
                traffic[nx][ny][0] += 1
                traffic[x][y][-1] -= 1

            # Cas général
        else:
            if route[nx][ny][0] == "Fin":
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

    return route, direction, traffic
