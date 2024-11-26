# @Autor : Mathis Adinolfi
# @Date of creation : 25/11/2024

# Bibliothèques utilisées
import copy
import random
from Variables import *
from collections import deque

# Fonction qui permet de trouver les chemins à emprunter dans les intersections

# Fonction BFS pour trouver le chemin le plus court
def bfs(route, depart, arrivee):
    """
    Effectue une recherche en largeur (BFS) pour trouver le chemin entre deux points
    dans une grille donnée, tout en minimisant le nombre de virages nécessaires.

    Args:
        route (list[list[tuple]]): Notre route
        depart (tuple): Coordonnées (i, j) de l'intersection de départ.
        arrivee (tuple): Coordonnées (i, j) de l'intersection d'arrivée.

    Returns:
        list[tuple]: Le chemin optimal sous forme d'une liste de coordonnées (i, j),
                     où chaque élément représente une case du chemin.
                     Le chemin minimise le nombre de virages nécessaires.

    Raises:
        TypeError: Si la case de départ ou d'arrivée n'est pas une intersection valide
                   dans la grille.

    Notes:
        - Un virage est compté lorsqu'il y a un changement de direction dans le chemin.
        - Si plusieurs chemins ont le même nombre minimal de virages, un seul est retourné.
        - Le chemin retourné inclut la case de départ et celle d'arrivée.
    """
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

    # Variables
    n, m = len(route), len(route[0])  # Dimensions de la grille
    file = deque([depart])  # File d'attente pour le BFS
    visite = set()  # Ensemble pour marquer les cases visitées
    visite.add(depart)  # Marquer le point de départ
    parents = {depart: ("fin", "fin")}  # Pour reconstruire le chemin
    res = []

    # Dico des directions avec déplacement associé
    directions = {
        3: (-1, 0),  # Haut
        1: (1, 0),  # Bas
        0: (0, -1),  # Gauche
        2: (0, 1),  # Droite
    }

    inverse_directions = {v: k for k, v in directions.items()}

    # Parcourt en largeur
    while file:
        x, y = file.popleft()

        # Si on atteint la case d'arrivée on décompile le chemin et on calcul le nbr de virage
        if (x, y) == arrivee:
            chemin = []
            virage = 0
            chemin.append((x, y))
            x_parent, y_parent = parents[(x, y)]
            # Cas chemin de longeur 1
            if (x_parent, y_parent) == ("fin", "fin"):
                res.append([chemin[::-1],virage])
            # Sinon
            else:
                # On trouve la direction de départ
                dir = inverse_directions[(x_parent - x, y_parent - y)]
                # Tant qu'on est pas à la fin
                while (x_parent, y_parent) != ("fin", "fin"):
                    chemin.append((x_parent, y_parent))
                    x_fils, y_fils = copy.copy((x, y))
                    x_parent, y_parent = parents[(x_parent, y_parent)]
                    # Si on est pas à la fin et on tourne on ajt un virage
                    if (x_parent, y_parent) != ("fin", "fin") and dir != inverse_directions[
                        (x_parent - x_fils, y_parent - y_fils)
                    ]:
                        virage += 1
                        dir = inverse_directions[(x_parent - x_fils, y_parent - y_fils)]
                # Retourne le chemin inversé
                res.append([chemin[::-1], virage])

        # On cherche les directions possibles
        dir = []

        for k, test in enumerate(route[x][y][1]):
            if test:
                dir.append(k)

        # Explorer les voisins accessibles à partir des directions de la case actuelle
        for index in dir:
            dx, dy = directions[index]
            nx, ny = x + dy, y + dy

            if (
                0 <= nx < n
                and 0 <= nx < m
                and route[nx][ny] != 0
                and route[nx][ny][0] == "Intersection"
                and (nx, ny) not in visite
            ):
                visite.add((nx, ny))
                file.append((nx, ny))
                parents[(nx, ny)] = (x, y)  # Garder trace du parent

    # On retourne le chemin avec le premier chemin avec le moins de virage
    # ! Comment différencier deux chemins de même longeur ?
    chemin_final, nbr_virage_min = res[0]

    for chemin, nbr_virage in res:
        if nbr_virage < nbr_virage_min:
            chemin_final = chemin

    return chemin_final

# Faire un focntion taille de l'intersection
def taille_inter(route,num_inter):
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
            if route[i][j] != 0 and route[i][j][0] == 'Intersection' and route[i][j][2] == num_inter:
                coord_i.append(i)
                coord_j.append(j)
    
    l_i = max(coord_i) - min(coord_i) + 1
    l_j = max(coord_j) - min(coord_j) + 1
    
    return [[min(coord_i),min(coord_j)],[max(coord_i),max(coord_j)]]

# Fonction qui trouve les sorties possibles
def trouve_sorti(route,direction,depart):
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
    # Def variable local
    x_depart, y_depart = depart
    n, m = len(route), len(route[0])  # Dimensions de la route
    dir_route = route[x_depart][y_depart][1]
    dir_voiture = direction[x_depart][y_depart][1]

    # Dictionnaire avec toute les directions
    directions = {
        0: (0, -1),  # Gauche
        1: (1, 0),  # Bas
        2: (0, 1),  # Droite
        3: (-1, 0),  # Haut
    }
    
    # On se décale sur l'intersection et on note le num de l'inter
    dx, dy = directions[dir_route]
    nx, ny = x_sorti + dx, y_sorti + dy
    num_inter = route[nx][ny][2]
    
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
                dx_sorti, dy_sorti = directions[dir_voiture]
                x_sorti, y_sorti= x + dx_sorti, y + dy_sorti
                
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
def trouve_entre(route,direction,depart):
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
    # Def variable local
    x_depart, y_depart = depart
    n, m = len(route), len(route[0])  # Dimensions de la route
    dir_route = route[x_depart][y_depart][1]

    # Dictionnaire avec toute les directions
    directions = {
        0: (0, -1),  # Gauche
        1: (1, 0),  # Bas
        2: (0, 1),  # Droite
        3: (-1, 0),  # Haut
    }

    # Num intersection
    dx, dy = directions[dir_route]
    nx, ny = x_depart + dx, y_depart + dy
    num_inter = route[nx][ny][2]
    
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
                dx_adj, dy_adj = directions[dir_opp]
                x_adj, y_adj = x + dx_adj, y + dy_adj
                
                # On test les bloc adj
                if (
                    0 <= x_adj < n
                    and 0 <= y_adj < m
                    and route[x_adj][y_adj] != 0
                    and route[x_adj][y_adj][0] != "Intersection"
                    and route[x_adj][y_adj][1] == dir_route
                ):
                    route_adj.append((x_adj, y_adj))

    return route_adj
                    


def arrivee(route, direction, depart):
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
    route_adj = []

    for x in range(n):
        for y in range(m):
            if (
                route[x][y] != 0
                and route[x][y][0] == "Intersection"
                and route[x][y][2] == num_inter
            ):
                # On regarde que dans le sens de la voiture pour les sortie
                dx_sorti, dy_sorti = directions[dir_voiture]
                x_sorti, y_sorti= x + dx_sorti, y + dy_sorti
                
                # On regarde que dans le sens inverse de la direction de la voiture pour les routes adj
                dir_opp = (dir_route + 2) % 4
                dx_adj, dy_adj = directions[dir_opp]
                x_adj, y_adj = x + dx_adj, y + dy_adj
                
                # On test les sortie                
                if (
                    0 <= x_sorti < n
                    and 0 <= y_sorti < m
                    and route[x_sorti][y_sorti] != 0
                    and route[x_sorti][y_sorti][0] != "Intersection"
                    and route[x_sorti][y_sorti][1] == dir_voiture
                ):
                    route_arv.append(
                        (x_sorti, y_sorti)
                    )  # Affiche les coordonées des routes empruntables
                
                # On test les bloc adj
                if (
                    0 <= x_adj < n
                    and 0 <= y_adj < m
                    and route[x_adj][y_adj] != 0
                    and route[x_adj][y_adj][0] != "Intersection"
                    and route[x_adj][y_adj][1] == dir_route
                ):
                    route_adj.append(
                        (x_adj, y_adj)
                    )  # Affiche les coordonées des routes empruntables

                    

    # Maintenant on définit une loi normale en fonction de la position de la sortie
    # Pic situé sur le bloc le plus proche du départ
    # Puis écart type de 1 car on veut que les valeurs soit autour de ce pic
    # ! pos en face dir_voiture = dir_route et que dir_route = [0,2] on garde le i sion j
    # ! pos en haut dir_voiture = dir_route + 1 % 4 
    # ! pos en bas dir_voiture = dir_route - 1 % 4 
    
    if dir_voiture in [0, 2]:
        max_limite = taille_inter(route,num_inter)[1][0] - taille_inter(route,num_inter)[0][0] # Taille i inter
        coord_sorti = [x for x, y in route_arv]
        coord_sorti.sort()
    else:
        max_limite = taille_inter(route,num_inter)[1][1] - taille_inter(route,num_inter)[0][1] # Taille j inter
        coord_sorti = [y for x, y in route_arv]
        coord_sorti.sort()

    if dir_route in [0, 2]:
        coord_adj = [x for x, y in route_adj]
        pos_depart = i
        coord_adj.sort()
    else:
        coord_adj = [y for x, y in route_adj]
        pos_depart = j
        coord_adj.sort()
    
    # On crée une liste avec l'ensemble des bloc de sortie possible la longeur - 1 = le nbr de sortie possible
    min_sorti = [coord_sorti[0]]
    max_sorti = []
        
    for k in range(len(coord_sorti) - 1):
        if coord_sorti[k + 1] != coord_sorti[k] + 1:
            max_sorti.append(coord_sorti[k])
            min_sorti.append(coord_sorti[k+1])

    max_sorti.append(coord_sorti[-1])
    
    # On charche les positions 
    
    min_adj_liste = [coord_adj[0]]
    max_adj_liste = []
        
    for k in range(len(coord_adj) - 1):
        if coord_adj[k + 1] != coord_adj[k] + 1:
            max_adj_liste.append(coord_adj[k])
            min_adj_liste.append(coord_adj[k+1])
    
    max_adj_liste.append(coord_adj[-1])
    
    for k in range(len(max_adj_liste)):
        if min_adj_liste[k] <= pos_depart <= max_adj_liste[k]:
            min_adj = min_adj_liste[k]
            max_adj = max_adj_liste[k]
            
    # On cherche mtn à positionner selon nous l'endroit de sorti idéal pour les voitures 
    # Si plusiseur sorites alors plusieur point idéaux mais sinon un seul
    
    pos = []
    
    for k in range(len(max_sorti)):
        if dir_route == 0:
            if dir_voiture == 0:
                pos.append(pos_depart)                
            elif dir_voiture == 1:
                pos_projete = max_sorti[k] - abs(max_adj - pos_depart) 
                if pos_projete >= taille_inter(route,num_inter)[0][1]: # Min j inter
                    pos.append(pos_projete)
                else:
                    pos.append(taille_inter(route,num_inter)[0][1]) # Min j inter
            elif dir_voiture == 3:
                pos_projete = max_sorti[k] - abs(min_adj - pos_depart)
                if pos_projete >= taille_inter(route,num_inter)[0][1]:
                    pos.append(pos_projete)
                else:
                    pos.append(taille_inter(route,num_inter)[0][1]) # Min j inter            
        elif dir_route == 1:
            if dir_voiture == 0:
                pos_projete = min_sorti[k] + abs(min_adj - pos_depart)
                if pos_projete <= taille_inter(route,num_inter)[1][0]: # Max i inter
                    pos.append(pos_projete)
                else:
                    pos.append(taille_inter(route,num_inter)[1][0]) # Max i inter
            elif dir_voiture == 1:
                pos.append(pos_depart)
            elif dir_voiture == 2:
                pos_projete =  min_sorti[k] + abs(max_adj - pos_depart)
                if pos_projete <= taille_inter(route,num_inter)[1][0]: # Max i inter
                    pos.append(pos_projete)
                else:
                    pos.append(taille_inter(route,num_inter)[1][0]) # Max i inter
        elif dir_route == 2:
            if dir_voiture == 1:
                pos_projete = min_sorti[k] + abs(max_adj - pos_depart)
                if pos_projete <= taille_inter(route,num_inter)[1][1]: # Max j inter
                    pos.append(pos_projete)
                else:
                    pos.append(taille_inter(route,num_inter)[1][1]) # Max j inter
            elif dir_voiture == 2:
                pos.append(pos_depart)
            elif dir_voiture == 3:
                pos_projete = min_sorti[k] + abs(min_adj - pos_depart)
                if pos_projete <= taille_inter(route,num_inter)[1][1]: # Max j inter
                    pos.append(pos_projete)
                else:
                    pos.append(taille_inter(route,num_inter)[1][1]) # Max j inter
        else:
            if dir_voiture == 0:
                pos_projete = max_sorti[k] - abs(min_adj - pos_depart)
                if pos_projete >= taille_inter(route,num_inter)[0][0]: # Min i inter
                    pos.append(pos_projete)
                else:
                    pos.append(taille_inter(route,num_inter)[0][0]) # Min i inter
            elif dir_voiture == 2:
                pos_projete = max_sorti[k] - abs(max_adj - pos_depart)
                if pos_projete >= taille_inter(route,num_inter)[0][0]: # Min i inter
                    pos.append(pos_projete)
                else:
                    pos.append(taille_inter(route,num_inter)[0][0]) # Min i inter
            elif dir_voiture == 3:
                pos.append(pos_depart)    
    
    # Si aucune pos trouvé on leve une exception
    # Si une seule sortie
    moy_gauss = []
    for k in range(len(pos)):
        if min_sorti[k] <= pos[k] <= max_sorti[k]:
            moy_gauss.append(pos[k])
        else:
            if abs(min_sorti[k] - pos[k]) <= abs(max_sorti[k] - pos[k]):
                moy_gauss.append(min_sorti[k]) 
            else:
                moy_gauss.append(max_sorti[k]) 

    # On génère la sortie sélectionner en respectant les distribution gaussienne

    choix = random.randint(0, len(moy_gauss) - 1)
    arrivee = round(random.gauss(moy_gauss[choix], 1))
    min_gauss = min_sorti[choix]
    max_gauss = max_sorti[choix]
    
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