# @Autor : Mathis Adinolfi
# @Date of creation : 25/11/2024

# Bibliothèques utilisées
import copy
import random
from collections import deque
from .Repere import *

# Objectif : Fonction qui permet de trouver les chemins à emprunter dans les intersections

# Fonction BFS pour trouver le chemin le plus court
def bfs(route, depart, arrivee):
    """
    Cherche le chemin le plus court entre deux intersections dans une route.

    Parameters
    ----------
    route : 2D list
        Route à étudier.
    depart : tuple
        Coordonnées de l'intersection de départ.
    arrivee : tuple
        Coordonnées de l'intersection d'arrivée.

    Returns
    -------
    list
        Chemin le plus court entre les deux intersections, sous forme de
        liste de tuples (x, y) représentant les coordonnées des intersections
        successives. La liste est vide si il n'y a pas de chemin possible.

    Raises
    ------
    TypeError
        Si les coordonnées de départ ou d'arrivée ne sont pas valides (hors
        route, non-intersection, etc.).
    """
    
    # Vérification des points de départ et d'arrivée
    if (
        route[depart[0]][depart[1]] == 0
        or route[depart[0]][depart[1]][0] != "Intersection"
    ):
        raise TypeError("Départ n'est pas une intersection valide")
    if (
        route[arrivee[0]][arrivee[1]] == 0
        or route[arrivee[0]][arrivee[1]][0] != "Intersection"
    ):
        raise TypeError("Arrivée n'est pas une intersection valide")
    
    n, m = len(route), len(route[0])  # Dimensions de la grille
    file = deque([depart])  # File pour BFS
    visite = set()  # Cases visitées
    visite.add(depart)
    parents = {depart: ("fin", "fin")}  # Pour reconstruire le chemin
    res = []
    
    # Parcours BFS
    while file:
        x, y = file.popleft()

        # Si on atteint la destination
        if (x, y) == arrivee:
            chemin = []
            virages = 0
            chemin.append((x, y))
            x_parent, y_parent = parents[(x, y)]

            # Reconstruction du chemin
            if (x_parent, y_parent) == ("fin", "fin"):
                res.append([chemin[::-1], virages])
            else:
                direction = inverse_repere[(x_parent - x, y_parent - y)]
                while (x_parent, y_parent) != ("fin", "fin"):
                    chemin.append((x_parent, y_parent))
                    x_fils, y_fils = copy.copy((x_parent, y_parent))
                    x_parent, y_parent = parents[(x_parent, y_parent)]

                    # Compter les virages
                    if (x_parent, y_parent) != ("fin", "fin") and direction != inverse_repere[(x_parent - x_fils, y_parent - y_fils)]:
                        virages += 1
                        direction = inverse_repere[(x_parent - x_fils, y_parent - y_fils)]

                res.append([chemin[::-1], virages])

        # Vérifier les directions possibles
        for index, test in enumerate(route[x][y][1]):
            if test:  # Direction disponible
                dx, dy = repere[index]
                nx, ny = x + dx, y + dy

                # Vérifier si la case voisine est valide
                if (
                    0 <= nx < n and 0 <= ny < m and
                    route[nx][ny] != 0 and
                    route[nx][ny][0] == "Intersection" and
                    (nx, ny) not in visite
                ):
                    visite.add((nx, ny))
                    file.append((nx, ny))
                    parents[(nx, ny)] = (x, y)
    
    # On retourne le chemin avec le premier chemin avec le moins de virage
    # ! Comment différencier deux chemins de même longeur ?
    chemin_final, nbr_virage_min = res[0]

    for chemin, nbr_virage in res:
        if nbr_virage < nbr_virage_min:
            chemin_final = chemin

    return chemin_final

# Faire un focntion taille de l'intersection
def taille_inter(route, num_inter):
    """
    Calcule les coordonnées des limites rectangulaires de l'intersection spécifiée dans une grille.

    Cette fonction parcourt une grille donnée sous forme de liste de listes (représentant un réseau routier)
    pour trouver l'intersection correspondant au numéro `num_inter`. Une intersection est identifiée
    par une cellule contenant un tuple dont le premier élément est la chaîne "Intersection" et
    le troisième élément est égal à `num_inter`. La fonction retourne les coordonnées des coins
    supérieur gauche et inférieur droit du rectangle englobant cette intersection.

    Args:
        route (list[list]): Notre route
        num_inter (int): Le numéro de l'intersection à localiser.

    Returns:
        list[list[int]]: Une liste de deux sous-listes représentant les coordonnées des coins
                         supérieur gauche et inférieur droit de la zone englobante de l'intersection.
                         Format : [[i_min, j_min], [i_max, j_max]], où (i_min, j_min) est le coin supérieur
                         gauche et (i_max, j_max) est le coin inférieur droit.
    """
    coord_i = []
    coord_j = []

    for i in range(len(route)):
        for j in range(len(route[i])):
            if (
                route[i][j] != 0
                and route[i][j][0] == "Intersection"
                and route[i][j][2] == num_inter
            ):
                coord_i.append(i)
                coord_j.append(j)

    return [[min(coord_i), min(coord_j)], [max(coord_i), max(coord_j)]]

# Fonction qui trouve les sorties possibles
def trouve_sorti(route, dir_voiture, num_inter):
    """
    Trouve les routes accessibles à partir d'une intersection en fonction de la direction initiale.

    Cette fonction identifie toutes les routes adjacentes à une intersection donnée, à partir
    de laquelle une voiture peut sortir dans une direction spécifiée. Elle prend en compte les
    orientations des routes et des intersections pour déterminer les sorties valides.

    Args:
        route (list[list]): Notre route
        direction (list[list]): Une grille représentant la direction des véhicules dans chaque cellule.
        depart (tuple[int, int]): Les coordonnées (x, y) de la cellule de départ dans la grille.

    Returns:
        list[tuple[int, int]]: Une liste de tuples représentant les coordonnées des sorties valides
                               accessibles depuis l'intersection spécifiée.

    Notes:
        - Les directions possibles sont codées comme suit :
            0 : gauche
            1 : bas
            2 : droite
            3 : haut
    """
    # Dimensions de la route
    n, m = len(route), len(route[0]) 

    # On définit une liste rés
    route_arv = []

    # On parcourt tous les élemnents de la route et on cherche ceux qui sont collés à l'intersection et
    # dont la direction permet la sorti de la route dir = dir_route
    for x in range(n):
        for y in range(m):
            if (
                route[x][y] != 0
                and route[x][y][0] == "Intersection"
                and route[x][y][2] == num_inter
            ):
                # On regarde que dans le sens de la voiture pour les sortie
                dx_sorti, dy_sorti = repere[dir_voiture]
                x_sorti, y_sorti = x + dx_sorti, y + dy_sorti

                # On test les sorties
                if (
                    0 <= x_sorti < n
                    and 0 <= y_sorti < m
                    and route[x_sorti][y_sorti] != 0
                    and route[x_sorti][y_sorti][0] != "Intersection"
                    and route[x_sorti][y_sorti][1] == dir_voiture
                ):
                    route_arv.append((x_sorti, y_sorti))

    return route_arv

# Fonction qui trouve les entrées possibles
def trouve_entre(route, dir_route, num_inter):
    """
    Identifie les routes adjacentes à une intersection, dont la direction est la direction initiale
    et la route collée à une intersection.

    Args:
        route (list[list]): Notre route
        depart (tuple[int, int]): Les coordonnées (i, j) de la cellule de départ dans la grille.

    Returns:
        list[tuple[int, int]]: Une liste de tuples représentant les coordonnées des routes adjacentes
                               valides connectées à l'intersection.

    Notes:
        - Les directions possibles sont codées comme suit :
            0 : gauche
            1 : bas
            2 : droite
            3 : haut
    """
    # Dimensions de la route
    n, m = len(route), len(route[0]) 

    # On définit le res
    route_adj = []

    # On test tous les blocs pour trouver ceux collés à l'intersection concernée
    for x in range(n):
        for y in range(m):
            if (
                route[x][y] != 0
                and route[x][y][0] == "Intersection"
                and route[x][y][2] == num_inter
            ):

                # On regarde que dans le sens inverse de la direction de la voiture pour les routes adj
                dir_opp = (dir_route + 2) % 4
                dx_ent, dy_ent = repere[dir_opp]
                x_ent, y_ent = x + dx_ent, y + dy_ent

                # On test les bloc adj
                if (
                    0 <= x_ent < n
                    and 0 <= y_ent < m
                    and route[x_ent][y_ent] != 0
                    and route[x_ent][y_ent][0] != "Intersection"
                    and route[x_ent][y_ent][1] == dir_route
                ):
                    route_adj.append((x_ent, y_ent))

    return route_adj

# Fonction test qui s'assure que tous les critères sont bons pour la fonction arrivee
def test_situation_ok(route, depart):
    """
    Vérifie si la situation de départ est ok pour une voiture.
    
    Args:
        route (list[list]): Notre route
        depart (tuple[int, int]): Les coordonnées (i, j) de la cellule de départ dans la grille.
    
    Returns:
        bool: True si la situation est ok, sinon False.
    
    Notes:
        - On vérifie que le bloc de départ n'est pas un bloc de fin ou 0.
        - On se déplace sur l'intersection en fonction de la direction du bloc de départ.
        - On vérifie que le bloc pointé est bien une intersection.
    """
    
    # Pos de départ
    x, y = depart

    # On test si le bloc de départ n'est pas un bloc de fin ou 0
    if route[x][y] == 0 or route[x][y][0] == "Fin":
        return False

    # Direction
    dir_route = route[x][y][1]

    # On se déplace sur l'intersection
    dx, dy = repere[dir_route]
    x, y = x + dx, y + dy

    # On test si le bloc pointé est bien une intersection
    if route[x][y] == 0 or route[x][y][0] != "Intersection":
        return False

    # Si tous les test ok
    return True

# Fonction qui retourne le numéro de l'intersection adjacente
def num_intersection_adj(route, depart):
    """
    Fonction qui retourne le numéro de l'intersection adjacente
    dans la direction de la route

    Args:
        route (2D list): Liste des élements de notre route
        depart (tuple[int, int]): Les coordonnées (x, y) de la cellule de départ dans la grille

    Returns:
        int: Le numéro de l'intersection adjacent
    """
    
    # Pos de départ
    x, y = depart

    # Direction
    dir_route = route[x][y][1]

    # On se déplace sur l'intersection
    dx, dy = repere[dir_route]
    x, y = x + dx, y + dy

    return route[x][y][2]

# Fonction qui prend en entrée les coordonnes des sorties et cherche à regrouper les sorties
# qui sont collées entres elles et retourne un intervalle qui spécifie les positions des groupes
def intervalle_sorti(route_arv, dir):
    """
    Prend en entrée les coordonnes des sorties et cherche à regrouper les sorties
    qui sont collées entres elles et retourne un intervalle qui spécifie les positions
    des groupes.

    Args:
        route_arv (list[tuple[int, int]]): Les coordonnées (x, y) des sorties
        dir (int): La direction dans laquelle on sort de l'intersection

    Returns:
        tuple[list[int], list[int]]: Un tuple contenant deux listes, la première
        correspond aux valeurs minimales des intervalles, la seconde aux valeurs maximales
    """
    
    if dir in [0, 2]:
        coord = [x for x, y in route_arv]
        coord.sort()
    else:
        coord = [y for x, y in route_arv]
        coord.sort()

    # On crée une liste avec l'ensemble des bloc de sortie possible la longeur - 1 = le nbr de sortie possible
    min_list = [coord[0]]
    max_list = []

    for k in range(len(coord) - 1):
        if coord[k + 1] != coord[k] + 1:
            max_list.append(coord[k])
            min_list.append(coord[k + 1])

    max_list.append(coord[-1])

    return min_list, max_list

# Fonction qui prend en entrée les coord des entrées et trouve le max et min de la route d'entrée
def intervalle_entre(route_ent, dir, pos_depart):
    """
    Prend en entrée les coordonnes des entrées et la direction de l'intersection
    et cherche à regrouper les entrées qui sont collées entres elles et
    retourne un intervalle qui spécifie la position de la route d'entrée
    dans laquelle on se trouve.

    Args:
        route_ent (list[tuple[int, int]]): Les coordonnées (x, y) des entrées
        dir (int): La direction dans laquelle on entre dans l'intersection
        pos_depart (int): La position de départ

    Returns:
        tuple[int, int]: Un tuple contenant deux entiers, le premier
        correspond au minimum de l'intervalle, le second au maximum
    """
    
    if dir in [0, 2]:
        coord = [x for x, y in route_ent]
        coord.sort()
    else:
        coord = [y for x, y in route_ent]
        coord.sort()

    # On crée une liste avec l'ensemble des bloc d'entrée possible la longeur - 1 = le nbr d'entrée possible
    min_list = [coord[0]]
    max_list = []

    for k in range(len(coord) - 1):
        if coord[k + 1] != coord[k] + 1:
            max_list.append(coord[k])
            min_list.append(coord[k + 1])

    max_list.append(coord[-1])

    # On cherche le bloc d'entrée où notre départ est situé
    for k in range(len(max_list)):
        if min_list[k] <= pos_depart <= max_list[k]:
            min_ent = min_list[k]
            max_ent = max_list[k]

    return min_ent, max_ent

# Fonction qui projete la position des entree sur la sorti en fonction de la taille de l'intersection
def projete_entre_sorti(taille, pos_depart, dir_route, dir_voiture, min_entre, max_entre, min_sorti, max_sorti):
    """
    Fonction qui projete la position des entree sur la sorti en fonction de la taille de l'intersection
    et de la direction de la route et de la voiture.

    Args:
        taille (list[tuple[int, int]]): La taille de l'intersection
        pos_depart (int): La position de départ
        dir_route (int): La direction de la route
        dir_voiture (int): La direction de la voiture
        min_entre (int): La position minimale de l'entrée
        max_entre (int): La position maximale de l'entrée
        min_sorti (list[int]): La liste des positions minimales des sorties
        max_sorti (list[int]): La liste des positions maximales des sorties

    Returns:
        list[int]: La liste des positions projetées sur la sortie
    """
    
    # On définit le rés
    pos = []

    for k in range(len(max_sorti)):
        if dir_route == 0:
            if dir_voiture == 0:
                pos.append(pos_depart)
            elif dir_voiture == 1:
                pos_projete = max_sorti[k] - abs(max_entre - pos_depart)
                if pos_projete >= taille[0][1]:  # Min j inter
                    pos.append(pos_projete)
                else:
                    pos.append(taille[0][1])  # Min j inter
            elif dir_voiture == 3:
                pos_projete = max_sorti[k] - abs(min_entre - pos_depart)
                if pos_projete >= taille[0][1]:
                    pos.append(pos_projete)
                else:
                    pos.append(taille[0][1])  # Min j inter
        elif dir_route == 1:
            if dir_voiture == 0:
                pos_projete = min_sorti[k] + abs(min_entre - pos_depart)
                if pos_projete <= taille[1][0]:  # Max i inter
                    pos.append(pos_projete)
                else:
                    pos.append(taille[1][0])  # Max i inter
            elif dir_voiture == 1:
                pos.append(pos_depart)
            elif dir_voiture == 2:
                pos_projete = min_sorti[k] + abs(max_entre - pos_depart)
                if pos_projete <= taille[1][0]:  # Max i inter
                    pos.append(pos_projete)
                else:
                    pos.append(taille[1][0])  # Max i inter
        elif dir_route == 2:
            if dir_voiture == 1:
                pos_projete = min_sorti[k] + abs(max_entre - pos_depart)
                if pos_projete <= taille[1][1]:  # Max j inter
                    pos.append(pos_projete)
                else:
                    pos.append(taille[1][1])  # Max j inter
            elif dir_voiture == 2:
                pos.append(pos_depart)
            elif dir_voiture == 3:
                pos_projete = min_sorti[k] + abs(min_entre - pos_depart)
                if pos_projete <= taille[1][1]:  # Max j inter
                    pos.append(pos_projete)
                else:
                    pos.append(taille[1][1])  # Max j inter
        else:
            if dir_voiture == 0:
                pos_projete = max_sorti[k] - abs(min_entre - pos_depart)
                if pos_projete >= taille[0][0]:  # Min i inter
                    pos.append(pos_projete)
                else:
                    pos.append(taille[0][0])  # Min i inter
            elif dir_voiture == 2:
                pos_projete = max_sorti[k] - abs(max_entre - pos_depart)
                if pos_projete >= taille[0][0]:  # Min i inter
                    pos.append(pos_projete)
                else:
                    pos.append(taille[0][0])  # Min i inter
            elif dir_voiture == 3:
                pos.append(pos_depart)

    return pos

# Fonction qui trouve la position de la moy de gauss
def pos_moy_gauss(proj, min_sorti, max_sorti):
    
    # On définit notre rés
    moy_gauss = []
    
    for k in range(len(proj)):
        if min_sorti[k] <= proj[k] <= max_sorti[k]:
            moy_gauss.append(proj[k])
        else:
            if abs(min_sorti[k] - proj[k]) <= abs(max_sorti[k] - proj[k]):
                moy_gauss.append(min_sorti[k])
            else:
                moy_gauss.append(max_sorti[k])
    
    return moy_gauss

# Fonction qui trouve l'arrivée pour un départ et une direction
def trouve_arrivee(route, direction, depart):
    """
    Trouve l'arrivée pour un départ et une direction.

    On prend en compte les directions des routes et des intersections pour déterminer les sorties valides
    et on positionne les voitures en fonction de la taille de l'intersection et de la direction des routes
    adjacentes.

    Args:
        route (list[list]): Notre route
        direction (list[list]): Une grille représentant la direction des véhicules dans chaque cellule.
        depart (tuple[int, int]): Les coordonnées (x, y) de la cellule de départ dans la grille.

    Returns:
        tuple[int, int]: Les coordonnées (x, y) de la cellule d'arrivée sélectionnée.

    Raises:
        TypeError: si la situation de départ n'est pas valide.

    Notes:
        - Les directions possibles sont codées comme suit :
            0 : gauche
            1 : bas
            2 : droite
            3 : haut
    """
    
    # Test
    if not test_situation_ok(route, depart):
        raise TypeError("Mauvaise situation départ :" + str(depart))

    # Pos de départ
    x, y = depart

    # Direction
    dir_route = route[x][y][1]
    dir_voiture = direction[x][y][1]
    
    # Numéro de l'intersection
    num_inter = num_intersection_adj(route, depart)
    
    # Taille de l'intersection
    taille = taille_inter(route, num_inter)

    # On test tous les blocs pour trouver ceux coller à l'intersection concernée
    route_arv = trouve_sorti(route, dir_voiture, num_inter)
    route_ent = trouve_entre(route, dir_route, num_inter)

    # Sur les deux coordonnees de départ seul une seule varie et nous intéresse
    pos_depart = x if dir_route in [0, 2] else y

    # On cherche les extrémitées des sorties possibles
    # ! Les min et max sont des listes
    min_sorti, max_sorti = intervalle_sorti(route_arv, dir_voiture)

    # On cherche les extrémitées de l'entrée
    # ! Les min et max sont des entiers
    min_entre, max_entre = intervalle_entre(route_ent, dir_route, pos_depart)

    # On cherche mtn à positionner selon nous l'endroit de sorti idéal pour les voitures
    # Pour cela il faut projeter l'entrée sur la sortie en tenant compte de la taille de l'intersection
    proj = projete_entre_sorti(taille,
                               pos_depart,
                               dir_route,
                               dir_voiture,
                               min_entre,
                               max_entre,
                               min_sorti,
                               max_sorti)
    
    # On trouve les postions des moyennes de gauss
    moy_gauss = pos_moy_gauss(proj, min_sorti, max_sorti)
    
    # On génère la sortie sélectionner en respectant les distribution gaussienne
    # On tire au sort une sortie
    choix = random.randint(0, len(moy_gauss) - 1)
    
    # On définit les bornes de notre gaussienne
    min_gauss = min_sorti[choix]
    max_gauss = max_sorti[choix]
    
    # On tire au sort un nombre en respectant les paramètres de la gaussienne
    arrivee = round(random.gauss(moy_gauss[choix], 1))

    # En fonction du résultat on retourne la bonne sortie
    if min_gauss <= arrivee <= max_gauss:
        return (
            (arrivee, route_arv[0][1])
            if dir_voiture in [0, 2]
            else (route_arv[0][0], arrivee)
        )
    elif arrivee < min_gauss:
        return (
            (min_gauss, route_arv[0][1])
            if dir_voiture in [0, 2]
            else (route_arv[0][0], min_gauss)
        )
    elif arrivee > max_gauss:
        return (
            (max_gauss, route_arv[0][1])
            if dir_voiture in [0, 2]
            else (route_arv[0][0], max_gauss)
        )

# Focntion qui pour un départ et une direction trouve le chemin à parcourir dans une intersection
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
    
    if route[depart[0]][depart[1]] == 0:
        raise TypeError("Le départ n'existe pas")

    arrivee = trouve_arrivee(route, direction, depart)

    if route[arrivee[0]][arrivee[1]] == 0:
        raise TypeError("L'arrivée n'existe pas")

    # On modifie les départs et arrivée pour être sur une intersection

    i, j = depart
    dir = route[i][j][1]
    di, dj = repere[dir]
    i, j = i + di, j + dj
    depart = (i, j)

    i, j = arrivee
    dir = (route[i][j][1] + 2) % 4
    di, dj = repere[dir]
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
        deplacement.append(inverse_repere[(i, j)])

    return deplacement
