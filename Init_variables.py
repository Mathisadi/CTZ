# Fichier avec toutes les fonction qui définiront la variable peut etre mettre en place des classes
# Pour l'instant juste recopier les valueurs dans la variable*

from Variables import *
import copy

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
                and route[x][y] != 0
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
        visited = set()
        compt = 0

        while coin_droit not in visited and coin_droit in inter:

            for pos in inter:
                # Barre haute
                if (
                    pos[0] == min_i
                    and min_j <= pos[1] <= max_j
                    and pos[1] - 1 >= 0
                    and route[pos[0]][pos[1] - 1] != 0
                ):
                    route[pos[0]][pos[1]][1][0] = True
                    visited.add(pos)
                # Barre droite
                if (
                    pos[1] == max_j
                    and min_i <= pos[0] <= max_i
                    and pos[0] - 1 >= 0
                    and route[pos[0] - 1][pos[1]] != 0
                ):
                    route[pos[0]][pos[1]][1][3] = True
                    visited.add(pos)
                # Barre bas
                if (
                    pos[0] == max_i
                    and min_j <= pos[1] <= max_j
                    and pos[1] + 1 < len(route[0])
                    and route[pos[0]][pos[1] + 1] != 0
                ):
                    route[pos[0]][pos[1]][1][2] = True
                    visited.add(pos)
                # Barre gauche
                if (
                    pos[1] == min_j
                    and min_i <= pos[0] <= max_i
                    and pos[0] + 1 < len(route)
                    and route[pos[0] + 1][pos[1]] != 0
                ):
                    route[pos[0]][pos[1]][1][1] = True
                    visited.add(pos)

            # On repositionne le coin droit
            min_i += 1
            max_i -= 1
            min_j += 1
            max_j -= 1

            coin_droit = (min_i, max_j)

    return route

print(initialisation_direction_intersection_antihoraire(route_etude))

def trouve_direction_case(route, pos_i, pos_j):

    if route[pos_i][pos_j] == 0:
        raise AssertionError("L'élément choisi n'est pas une intersection")
    elif route[pos_i][pos_j][0] != "Intersection":
        raise AssertionError("L'élément choisi n'est pas une intersection")

    n, m = len(route), len(route[0])
    res = route[pos_i][pos_j][1]
    dir = [
        (pos_i, pos_j - 1),
        (pos_i + 1, pos_j),
        (pos_i, pos_j + 1),
        (pos_i - 1, pos_j),
    ]

    # On prend les directions adjacentes sans regarder si les directions sont possibles
    for index, (i, j) in enumerate(dir):

        if route[i][j] != 0 and 0 <= i < n and 0 <= j < m:
            if route[i][j][0] == "Fin":
                res[index] = True
            elif route[i][j][0] == "Intersection":
                if route[i][j][1][(index + 2) % 4] == True:
                    res[(index + 2) % 4] = True
            else:
                if route[i][j][1] == index or route[i][j][1] == (index + 2) % 4:
                    res[route[i][j][1]] = True
                    
    # On corrige les directions et supprime celle impossible
    for index, (i, j) in enumerate(dir):

        if route[i][j] == 0 or not 0 <= i < n or not 0 <= j < m:
            if res[index] == True:
                res[index] = False

    route[pos_i][pos_j][1] == res

    return route

def direction_intersection(route):

    # On initialise les directions des intersections
    route = initialisation_direction_intersection_antihoraire(route)

    # On ajoute les directions des cases adjacentes
    tab = trouve_intersection(route)

    # Pour chaque intersections on effectue tous les changements et si tout est parail on passe à la suivante
    for index,inter in enumerate(tab):
        # On initialise les variables
        route_ref = copy.deepcopy(route)
        ite = 1
        
        # On test si notre route de réf est la même que la route aprés modif
        while route != route_ref or ite == 1:
            route_ref = copy.deepcopy(route)
            for pos in inter:
                trouve_direction_case(route, pos[0], pos[1])
                route[pos[0]][pos[1]][2] = index
            ite += 1
            
    return route

def affiche_inter(route_etude):
    route = direction_intersection(route_etude)
    res = []
    for i in range(len(route)):
        for j in range(len(route[i])):
            if route[i][j] != 0 and route[i][j][0] == "Intersection":
                res.append([(i, j), route[i][j][1]])

    return res

print(affiche_inter(route_etude))