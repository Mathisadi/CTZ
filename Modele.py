# @Autor : Mathis Adinolfi
# @Date of creation : 02/10/2024

# Bibliothèques utilisées

import copy
import time
import random
from Variables import *
from collections import deque

# Modéle Traffic

# TODO : Commenter le code avec ChatGPT


def update_direction(route, direction):
    """Cette fonction modifie les choix de trajet des utilisateurs de manière aléatoire afin de respecter les
    probabilités observées sur le terrain.

    Args:
        route (2D list): Liste en 2D représentant les éléments de la route. Chaque élément peut contenir des informations
                         sur un emplacement, comme "Fin" (point de fin de route) ou "Intersection".
        direction (2D list): Liste en 2D des préférences de direction pour chaque emplacement sur la route. Chaque entrée
                             comprend une liste de probabilités pour chaque direction (0, 1, 2, 3) et une valeur actuelle de direction.

    Returns:
        direction (2D list): Liste en 2D des directions mises à jour après modification aléatoire en fonction des probabilités.
    """

    # Parcours de chaque élément de la route
    for i in range(len(route)):
        for j in range(len(route[i])):
            # Vérifie que l'élément de la route est différent de zéro (par exemple, 0 pourrait représenter un espace vide)
            if route[i][j] != 0:
                # Si l'élément n'est pas un point de fin ou une intersection, on modifie la direction
                if (
                    route[i][j][0] != "Fin"
                    and route[i][j][0] != "Intersection"
                    and route[i][j][0] != "Depart"
                ):
                    # Mise à jour aléatoire de la direction en fonction des poids fournis
                    # direction[i][j][0] contient les probabilités pour chaque direction
                    # k=1 signifie que l'on choisit une seule direction
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


# TODO : Refract code for compatibility bfs, grille ?


# Fonction BFS pour trouver le chemin le plus court
def bfs(route, depart, arrivee):
    # TODO : Mettre un poids pour tenir trier les parcours équivalents
    # Départ et arrivée sont des intersections
    if (
        route[depart[0]][depart[1]] == 0
        or route[depart[0]][depart[1]][0] != "Intersection"
    ):
        raise TypeError("Départ n'est pas une intersection")
    if (
        route[arrivee[0]][arrivee[1]] == 0
        or route[arrivee[0]][arrivee[1]][0] != "Intersection"
    ):
        raise TypeError("Arrivee n'est pas une intersection")

    n, m = len(route), len(route[0])  # Dimensions de la grille
    file = deque([depart])  # File d'attente pour le BFS
    visite = set()  # Ensemble pour marquer les cases visitées
    visite.add(depart)  # Marquer le point de départ
    parents = {depart: ("fin", "fin")}  # Pour reconstruire le chemin
    res = []

    # Directions avec déplacement associé
    directions = {
        3: (-1, 0),  # Haut
        1: (1, 0),  # Bas
        0: (0, -1),  # Gauche
        2: (0, 1),  # Droite
    }

    inverse_directions = {v: k for k, v in directions.items()}

    while file:
        i, j = file.popleft()

        # Si on atteint la case d'arrivée on décompile le chemin et on calcul le nbr de virage
        if (i, j) == arrivee:
            chemin = []
            virage = 0
            chemin.append((i, j))
            x, y = parents[(i, j)]
            # Cas chemin de longeur 1
            if (x, y) == ("fin", "fin"):
                res.append([chemin[::-1],virage])
            # Sinon
            else:
                dir = inverse_directions[(x - i, y - j)]
                while (x, y) != ("fin", "fin"):
                    chemin.append((x, y))
                    ox, oy = copy.copy((x, y))
                    x, y = parents[(x, y)]
                    if (x, y) != ("fin", "fin") and dir != inverse_directions[
                        (x - ox, y - oy)
                    ]:
                        virage += 1
                        dir = inverse_directions[(x - ox, y - oy)]
                res.append([chemin[::-1], virage])  # Retourne le chemin inversé

        # On cherche les directions possibles
        dir = []

        for k, test in enumerate(route[i][j][1]):
            if test:
                dir.append(k)

        # Explorer les voisins accessibles à partir des directions de la case actuelle
        for index in dir:
            di, dj = directions[index]
            ni, nj = i + di, j + dj

            if (
                0 <= ni < n
                and 0 <= nj < m
                and route[ni][nj] != 0
                and route[ni][nj][0] == "Intersection"
                and (ni, nj) not in visite
            ):
                visite.add((ni, nj))
                file.append((ni, nj))
                parents[(ni, nj)] = (i, j)  # Garder trace du parent

    # On retourne le chemin avec le moins de virage
    chemin_final, nbr_virage_min = res[0]

    for chemin, nbr_virage in res:
        if nbr_virage < nbr_virage_min:
            chemin_final = chemin

    return chemin_final


def trouve_arrivee(route, direction, depart):
    # TODO : Mettre un test pour savoir si on est sur le bon élément
    # Def variable local
    i, j = depart
    n, m = len(route), len(route[0])  # Dimensions de la route
    dir_route = route[i][j][1]
    dir_voiture = direction[i][j][1]

    # Dictionnaire avec toute les directions
    directions = {
        0: (0, -1),  # Gauche
        1: (1, 0),  # Bas
        2: (0, 1),  # Droite
        3: (-1, 0),  # Haut
    }

    di, dj = directions[dir_route]
    ni, nj = i + di, j + dj

    # On test si le bloc pointé est bien une intersection
    if route[ni][nj] == 0 or route[ni][nj][0] != "Intersection":
        raise TypeError("Le bloc adjacent n'est pas une intersection")

    # On test tous les blocs pour trouver ceux coller à l'intersection concernée
    num_inter = route[ni][nj][2]
    route_arv = []

    for x in range(len(route)):
        for y in range(len(route[x])):
            if (
                route[x][y] != 0
                and route[x][y][0] == "Intersection"
                and route[x][y][2] == num_inter
            ):
                dx, dy = directions[dir_voiture]
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < n
                    and 0 <= ny < m
                    and route[nx][ny] != 0
                    and route[nx][ny][0] != "Intersection"
                    and route[nx][ny][1] == dir_voiture
                ):
                    route_arv.append(
                        (nx, ny)
                    )  # Affiche les coordonées des routes empruntables

    # Maintenant on définit une loi normale en fonction de la position de la sortie
    # Pic situé sur le bloc le plus proche du départ
    # Puis écart type de 1 car on veut que les valeurs soit autour de ce pic
    if dir_route in [0, 2]:
        pos = i
        max_limite = n
        coord = [x for x, y in route_arv]
        coord.sort()
    else:
        pos = j
        max_limite = m
        coord = [y for x, y in route_arv]
        coord.sort()

    nbr_ite = max(pos, max_limite - pos) + 1
    ext = [0]

    for k in range(len(coord) - 1):
        if coord[k + 1] != coord[k] + 1:
            ext.append(k)

    ext.append(len(coord) - 1)

    # Si aucune pos trouvé on leve une exception
    if ext == [0, len(coord) - 1]:
        # ! Ca marche que si on veut aller en face
        for compt in range(nbr_ite):
            if pos - compt in coord and pos + compt not in coord:
                moy_gauss = pos - compt
            elif pos - compt not in coord and pos + compt in coord:
                moy_gauss = pos + compt
            elif pos - compt in coord and pos + compt in coord:
                moy_gauss = pos
    else:
        moy_gauss = []
        for k in range(len(ext) - 1):
            if coord[ext[k]] <= i <= coord[ext[k + 1]]:
                moy_gauss.append(i)
            else:
                res = (
                    coord[ext[k]]
                    if abs(coord[ext[k]] - i) <= abs(coord[ext[k + 1]] - i)
                    else coord[ext[k + 1]]
                )
                moy_gauss.append(res)

    # On génère la sortie sélectionner en respectant les distribution gaussienne
    # Cas 1 une seule gaussienne
    if type(moy_gauss) == int:
        arrivee = round(random.gauss(moy_gauss, 1))
        if arrivee in coord:
            return (
                (arrivee, route_arv[0][1])
                if dir_route in [0, 2]
                else (route_arv[0][0], arrivee)
            )
        elif arrivee < min(coord):
            return (
                (min(coord), route_arv[0][1])
                if dir_route in [0, 2]
                else (route_arv[0][0], min(coord))
            )
        elif arrivee > max(coord):
            return (
                (max(coord), route_arv[0][1])
                if dir_route in [0, 2]
                else (route_arv[0][0], max(coord))
            )
    # Cas 2 plusieur gaussienne ! Pas de destination préférées les gaussiiennnes ont le mm poids
    else:
        choix = random.randint(0, len(moy_gauss) - 1)
        arrivee = round(random.gauss(moy_gauss[choix], 1))
        min_gauss = coord[ext[choix] + 1] if choix != 0 else 0
        max_gauss = coord[ext[choix + 1]]
        if arrivee in coord:
            return (
                (arrivee, route_arv[0][1])
                if dir_route in [0, 2]
                else (route_arv[0][0], arrivee)
            )
        elif arrivee < min_gauss:
            return (
                (min_gauss, route_arv[0][1])
                if dir_route in [0, 2]
                else (route_arv[0][0], min_gauss)
            )
        elif arrivee > max_gauss:
            return (
                (max_gauss, route_arv[0][1])
                if dir_route in [0, 2]
                else (route_arv[0][0], max_gauss)
            )

print(trouve_arrivee(route_etude,direction_etude,(2,4)))


def chemin_intersection(route, direction, depart):
    """Cette fonction permet de déterminer le chemin à emprunter pour une voiture dans une intersection

    Args:
        route (2D list): Liste des élements de notre route
        direction (2D list): Liste des préferences de direction des utilisateur pour chaque élement et la direction choisie
        pos_x (int): Indique la position en x de la voiture
        pos_y (int): Indique la position en y de la voiture

    Returns:
        res (1D list): Retourne les mouvement à réalisés pour sortir de l'intersection
    """
    # On déf les dico
    direction_position = {
        0: (0, -1),  # Gauche
        1: (1, 0),  # Bas
        2: (0, 1),  # Droite
        3: (-1, 0),  # Haut
    }

    position_direction = {
        (0, -1): 0,  # Gauche
        (1, 0): 1,  # Bas
        (0, 1): 2,  # Droite
        (-1, 0): 3,  # Haut
    }

    if route[depart[0]][depart[1]] == 0:
        raise TypeError("Le départ n'existe pas")

    arrivee = trouve_arrivee(route, direction, depart)

    if route[arrivee[0]][arrivee[1]] == 0:
        raise TypeError("L'arrivée n'existe pas")

    # On modifie les départs et arrivée pour être sur une intersection

    i, j = depart
    dir = route[i][j][1]
    di, dj = direction_position[dir]
    i, j = i + di, j + dj
    depart = (i, j)

    i, j = arrivee
    dir = (route[i][j][1] + 2) % 4
    di, dj = direction_position[dir]
    i, j = i + di, j + dj
    arrivee_inter = (i, j)

    # On trouve le chemin
    chemin = bfs(route, depart, arrivee_inter)
    chemin.append(arrivee)

    # pour chaque étape on détermine le déplacement
    deplacement = []
    for k in range(len(chemin) - 1):
        i = chemin[k + 1][0] - chemin[k][0]
        j = chemin[k + 1][1] - chemin[k][1]
        deplacement.append(position_direction[(i, j)])

    return deplacement


# TODO : Ajouter la condition des piétons
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
                direction[nx][ny] = chemin_intersection(route, direction, (x, y))
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
