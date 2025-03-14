# @Autor : Mathis Adinolfi
# @Date of creation : 25/11/2024

# Bibliothèques utilisées
from .Intersections import trouve_arrivee
from .Repere import *
import copy

# Obejctif : définir une fonction qui cherche les voitures qui veulent changer des blocs et retourne leur
# pos avant aprés si elle respecte le code de la route

def est_dans_la_grille(route, x, y):
    """
    Vérifie si une position (x, y) est à l'intérieur de la grille 'route'.

    Args:
        route (2D list): Grille représentant la route.
        x (int): Coordonnée x de la position à vérifier.
        y (int): Coordonnée y de la position à vérifier.

    Returns:
        bool: True si la position est dans la grille, sinon False.
    """
    # Obtenir les dimensions de la grille
    n, m = len(route), len(route[0])
    
    # Vérifier si (x, y) est dans la plage des indices valides
    return 0 <= x < n and 0 <= y < m

def regle_route_depart(route, x, y):
    """
    Cette fonction permet de respecter le code de la route pour un utilisateur.

    Args:
        route (2D list): Liste des élements de notre route
        x (int): Indique la position en x de la voiture
        y (int): Indique la position en y de la voiture

    Returns:
        res (1D list): Retourne l'ensemble des changement de blocs en indiquant le point de départ et l'arrivée
    """

    # On trouve la direction 
    dir_route = route[x][y][1]
    
    # Pour la route et les départ la voiture voudra toujour suivre la direction
    # aucune perturbation n'est à prévoir
    dx, dy = repere[dir_route]
    nx, ny = x + dx, y + dy
    
    return [x, y, nx, ny]


def regle_pieton(direction, x, y):
    
    # On trouve la direction de la voiture
    dir_route = direction[x][y][1]
    
    # Pour les passages pieton la voiture voudra toujour suivre la direction
    # aucune perturbation n'est à prévoir
    dx, dy = repere[dir_route]
    nx, ny = x + dx, y + dy
    
    return [x, y, nx, ny]

def regle_intersection(route, direction, trafic, x, y):
    """
    Cette fonction permet de respecter les règles de la route pour un utilisateur sur une intersection.

    Args:
        route (2D list): Liste des élements de notre route
        direction (2D list): Liste des préferences de direction des utilisateur pour chaque élement et la direction
        trafic (2D list): Liste des préferences de direction des utilisateur pour chaque élement et la direction
        x (int): Indique la position en x de la voiture
        y (int): Indique la position en y de la voiture

    Returns:
        res (1D list): Retourne l'ensemble des changement de blocs en indiquant le point de départ et l'arrivée
    """
    
    # On trouve la direction
    dir_voiture = direction[x][y][0]
    
    # On définit une variable res
    res = None
    
    # Pour les intersections ca se complique en effet il faut faire attention aux priorités à droite
    # La priorité à droite s'applique si le bloc à droite de la destination est une route occupée
    # De ce fait sur une intersection on peut avancer si le bloc à droite de la destination n'est pas une route
    # Ou alors c'est une route non occupée
    # Attention la "droite" dépend de la direction
    # ! La priorité à droite ne concerne que les routes, pour les feux rouges on considérera que il laisse passer

    # Gauche
    if dir_voiture == 0:
        # On se déplace sur le bon bloc à tester
        x_dest , y_dest = x - 1, y - 1

        if est_dans_la_grille(route, x_dest, y_dest):
            if route[x_dest][y_dest] != 0:
                if route[x_dest][y_dest][0] != "Route" or trafic[x_dest][y_dest][-1] == 0:
                    res = [x, y, x, y - 1]
            else:
                res = [x, y, x, y - 1]
        else:
            res = [x, y, x, y - 1]

    # Bas
    elif dir_voiture == 1:
        # On se déplace sur le bon bloc à tester
        x_dest , y_dest = x + 1, y - 1
        
        if est_dans_la_grille(route, x_dest, y_dest):
            if route[x_dest][y_dest] != 0:
                if route[x_dest][y_dest][0] != "Route" or trafic[x_dest][y_dest][-1] == 0:
                    res = [x, y, x + 1, y]
            else:
                res = [x, y, x + 1, y]
        else:
            res = [x, y, x + 1, y]

    # Droite
    elif dir_voiture == 2:
        # On se déplace sur le bon bloc à tester
        x_dest , y_dest = x + 1, y + 1

        if est_dans_la_grille(route, x_dest, y_dest):
            if route[x_dest][y_dest] != 0:
                if route[x_dest][y_dest][0] != "Route" or trafic[x_dest][y_dest][-1] == 0:
                    res = [x, y, x, y + 1]
            else:
                res = [x, y, x, y + 1]
        else:
            res = [x, y, x, y + 1]

    # Haut
    elif dir_voiture == 3:
        # On se déplace sur le bon bloc à tester
        x_dest , y_dest = x - 1, y + 1

        if est_dans_la_grille(route, x_dest, y_dest):
            if route[x_dest][y_dest] != 0:
                if route[x_dest][y_dest][0] != "Route" or trafic[x_dest][y_dest][-1] == 0:
                    res = [x, y, x - 1, y]
            else:
                res = [x, y, x - 1, y]
        else:
            res = [x, y, x - 1, y]

    # Si pas none on retourn res
    if res is not None:
        return res

def regle_feu(route, trafic, x, y):
    """
    Cette fonction permet de respecter le code de la route pour un feu.

    Args:
        route (2D list): Liste des éléments de notre route
        trafic (2D list): Liste des éléments de notre trafic
        x (int): Indique la position en x de la voiture
        y (int): Indique la position en y de la voiture

    Returns:
        res (1D list): Retourne l'ensemble des changements de blocs en indiquant le point de départ et l'arrivée
    """
    
    # Le feu doit etre au vert
    if route[x][y][-1] == False:
        return None
     
    # On définit la direction de la route
    dir_route = route[x][y][1]
    
    # On définit une variable res
    res = None
    
    # Feux rouges : pour les feux rouges il va dans la direction si le feu est vert
    # Attention execption si le feu rouge est relier à une intersection
    # Et que celle-ci est pleine (voiture sur la gauche) alors on le laisse passer = évite les blocages"""
    
    # Gauche
    if dir_route == 0:    
        if route[x][y - 1][0] == "Intersection":
            # On test si la route est libre
            if est_dans_la_grille(route, x + 1, y - 1):
                if trafic[x + 1][y - 1][-1] == 0:
                    res = [x, y, x, y - 1]
        else:
            res = [x, y, x, y - 1]
            
    # Bas
    elif dir_route == 1:
        if route[x + 1][y][0] == "Intersection":
            # On test si la route est libre
            if est_dans_la_grille(route, x + 1, y + 1):
                if trafic[x + 1][y + 1][-1] == 0:
                    res = [x, y, x + 1, y]
        else:
            res = [x, y, x + 1, y]

    # Droite
    elif dir_route == 2:
        if route[x][y + 1][0] == "Intersection":
            # On test si la route est libre
            if est_dans_la_grille(route, x - 1, y + 1):
                if trafic[x - 1][y + 1][-1] == 0:
                    res = [x, y, x, y + 1]
        else:
            res = [x, y, x, y + 1]

    # Haut
    elif dir_route == 3:
        if route[x - 1][y][0] == "Intersection":
            # On test si la route est libre
            if est_dans_la_grille(route, x - 1, y - 1):
                if trafic[x - 1][y - 1][-1] == 0:
                    res = [x, y, x - 1, y]
        else:
            res = [x, y, x - 1, y]

    # Si pas none on retourne res
    if res is not None:
        return res

def voie_libre(route, trafic, nbr_case_libre_necessaire, dir_route, x, y):
    """
    Fonction qui permet de savoir si il y a une place pour avancer.
    
    Args:
        route (2D list): Liste des élements de notre route
        trafic (2D list): Liste des préferences de direction des utilisateur pour chaque élement et la direction
        nbr_case_libre_necessaire (int): Nombre de case qu'il faut avoir pour avancer
        dir_route (int): Direction de la route
        x (int): Indique la position en x de la voiture
        y (int): Indique la position en y de la voiture
        
    Returns:
        bool: True si il y a la place, False sinon
    """
        
    # On s'assure que le x,y est dans la grille est bien un élément
    if not est_dans_la_grille(route,x,y) or route[x][y] == 0:
        raise IndexError("La positon n'est pas dans la grille ou n'est pas un élément" + str(x,y))
    
    # On trouve la direction dans laquelle il faut tester
    if route[x][y][0] == "Intersection":
        # Si dir_route dans 0,2 il faut regarder si dans l'inter on peut aller en 1 ou en 3
        if dir_route in [0, 2]:
            dir_test = [dir for dir, flag in enumerate(route[x][y][1][1:4:2]) if flag]
        else:
            dir_test = [dir for dir, flag in enumerate(route[x][y][1][0:3:2]) if flag]
    else:
        dir_test = [route[x][y][1]]  
    
    # On crée une liste avec les trafics de toutes les directions
    test = []
    
    for d in dir_test:
        trafic_dir = []
        while est_dans_la_grille(route, x, y) and route[x][y] != 0:
            trafic_dir = trafic[x][y] + trafic_dir
            x, y = x + repere[d][0], y + repere[d][1]
        
        test.append(trafic_dir)
        
    # On vérifie si on a la place
    for index in range(len(test)):
        for k in range(1, nbr_case_libre_necessaire + 1):
            if test[index][-k] != 0:
                return False
    
    return True
        
def regle_priorite(route, direction, x, y):
    """
    Vérifie si l'on peut s'engager dans une intersection depuis une priorité.
    Lorsqu'on est sur une priorité on le s'engage que lorsqu'il n'y a personne sur l'ensemble
    des voies que l'on coupent. Ainsi savoir si l'on peut s'engager dans une intersection depuis une priorité
    implique de connaitre la destination et la voies de sorti. On suppose que l'on peut s'engager si
    les voies coupées sont vide de (nbr d'intersection coupées) bloc vides.
    
    Parameters:
    route (list[list]): Notre route
    direction (list[list]): Une grille représentant la direction des véhicules dans chaque cellule.
    x (int): Coordonnée x de la cellule de départ.
    y (int): Coordonnée y de la cellule de départ.
    
    Returns:
    list[int, int, int, int] : Une liste de 4 éléments qui sont les coordonnées (x, y) de départ et d'arrivée
    si l'on peut s'engager, None sinon.
    """
    
    # On crée une copie des coordonnées de départ
    x_start, y_start = copy.copy(x), copy.copy(y)
    
    # On trouve les directions
    dir_route = route[x][y][1]

    # Lorsqu'on est sur une priorité on le s'engage que lorsqu'il n'y a personne sur l'ensemble
    # des voies que l'on coupent. Ainsi savoir si l'on peut s'engager dans une intersection depuis une priorité
    # implique de connaitre la destination et la voies de sorti. On suppose que l'on peut s'engager si
    # les voies coupées sont vide de (nbr d'intersection coupées) bloc vides.
    # ! Les blocs priorités sont toujours collé à un bloc intersection
    
    # On trouve la sortie
    x_arv, y_arv = trouve_arrivee(route, direction, (x, y))
    
    # On cherche à vérifier si chaque voeis coupées est libre
    if dir_route in [0, 2]:
        compt = 2
        while y != y_arv and (x != x_arv or y != y_arv):
            if not voie_libre(route, direction, compt, dir_route, x, y):                
                return None
            else:
                y = y + repere[dir_route][1]
                compt += 1
    
    elif dir_route in [1, 3]:
        compt = 2
        while x != x_arv and (x != x_arv or y != y_arv):
            if not voie_libre(route, direction, compt, dir_route, x, y):
                return None
            else:
                x = x + repere[dir_route][0]
                compt += 1
                
    # On retourne l'arrivée si on est passé
    return [x_start, y_start, x, y]

def regle_circulation(route, direction, trafic, x, y):
    """
    Applique la règle de circulation pour le bloc de coordonnée (x, y) de la route.
    
    Parameters:
    route (list[list]): La route.
    x (int): Coordonnée x du bloc.
    y (int): Coordonnée y du bloc.
    
    Returns:
    list[int, int, int, int]: Une liste de 4 éléments qui sont les coordonnées (x, y) de départ et d'arrivée
    si le mouvement est autorisé, None sinon.
    """
    # On définit le type de la route
    type_route = route[x][y][0]
    
    # On attribue à chaque élément la bonne fonction
    if type_route == "Route" or type_route == "Depart":
        return regle_route_depart(route, x, y)
    elif type_route == "Pieton":
        return regle_pieton(direction, x, y)
    elif type_route == "Intersection":
        return regle_intersection(route, direction, trafic, x, y)
    elif type_route == "Feu":
        return regle_feu(route, trafic, x, y)
    elif type_route == "Priorite":
        return regle_priorite(route, direction, x, y)

def changement_bloc(route, direction, trafic):
    """
    Calcule les changements de blocs sur la grille en respectant les règles de circulation.

    Pour chaque bloc de la grille, si celui-ci n'est pas vide et qu'il y a du trafic,
    applique les règles de circulation pour déterminer si un changement de bloc est possible.

    Args:
        route (2D list): Liste des éléments de la route.
        direction (2D list): Liste des directions préférées des utilisateurs pour chaque élément.
        trafic (2D list): Représentation du trafic sur la route : 0 = vide, 1 = voiture présente.

    Returns:
        list[list[int, int, int, int]]: Liste des changements de blocs autorisés sous forme 
        de coordonnées de départ et d'arrivée.
    """
    
    # On défnit la taille de la grille
    n, m = len(route), len(route[0])
    
    # On définit le résultat
    res = []
    
    # On test chaque bloc de la grille
    for x in range(n):
        for y in range(m):    
            if route[x][y] != 0:
                if trafic[x][y][-1] >= 1:
                    change = regle_circulation(route, direction, trafic, x, y)
                    if change is not None:
                        res.append(change)
                        
    return res
   