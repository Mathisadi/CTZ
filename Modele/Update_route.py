# @Autor : Mathis Adinolfi
# @Date of creation : 25/11/2024

# Bibliothèque utilisée
import random

# Objectif : update les éléments de la route

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
    for x in range(len(route)):
        for y in range(len(route[x])):
            # Vérifie que l'élément de la route est différent de zéro (par exemple, 0 pourrait représenter un espace vide)
            if route[x][y] != 0:
                # Si l'élément n'est pas une extremité ou une intersection, on modifie la direction
                if (
                    route[x][y][0] != "Fin"
                    and route[x][y][0] != "Intersection"
                    and route[x][y][0] != "Depart"
                    and route[x][y][0] != "Depart_pieton"
                ):
                    # Mise à jour aléatoire de la direction en fonction des poids fournis
                    # direction[x][y][0] contient les probabilités pour chaque direction
                    # k=1 signifie que l'on choisit une seule direction
                    direction[x][y][1] = random.choices(
                        [0, 1, 2, 3], weights=direction[x][y][0], k=1
                    )[0]

    return direction

def update_depart(route, trafic):
    """Cette fonction permet de générer des voitures dans les cases départ de manière aléatoire,
    tout en respectant le débit d'entrée

    Args:
        route (2D list): Liste des élements de notre route
        trafic (2D list): Liste resprésentant le trafic de notre route 0 = vide / 1 = voiture

    Returns:
        trafic (2D list): Ajoute les voitures générées sur les cases départs
    """

    for x in range(len(route)):
        for y in range(len(route[x])):
            # Vérifie que l'élément de la route est différent de zéro (par exemple, 0 pourrait représenter un espace vide)
            if route[x][y] != 0:
                # Si l'élément est un départ
                if route[x][y][0] == "Depart":
                    # Si on génère un nombre aléatoire et si il est inférieur à débit par seconde alors
                    # On génère une voiture permet de modéliser l'aléatoire du trafic
                    if random.random() <= route[x][y][2] / 60:
                        trafic[x][y][0] += 1

    return trafic

# ! - A mettrre à jour afin de pouvoir gérer les cycles de feux rouges complexe
def update_feux_rouges(route, temps):
    """Cette fonction permet de mettre à jour les feux rouges de notre route

    Args:
        route (2D list): Liste des élements de notre route
        temps (int): Temps depuis début de la simulation en seconde

    Returns:
        route (2D list): Retourne la route avec les feux rouges modifiés
    """
    for x in range(len(route)):
        for y in range(len(route[x])):
            # Vérifie que l'élément de la route est différent de zéro (par exemple, 0 pourrait représenter un espace vide)
            if route[x][y] != 0:
                # Si l'élément est un feu
                if route[x][y][0] == "Feu":
                    temps_tot = sum(route[x][y][2])
                    temps_cumule = [sum(route[x][y][2][:i]) for i in range(len(route[x][y][2]))]
                    # Si on arrive à la fin du cycle on change l'état des feux
                    if (temps % temps_tot) in temps_cumule:
                        route[x][y][3] = not (route[x][y][3])

    return route

def update_pieton(route):
    """Met à jour les piétons en réduisant le temps restant pour traverser
    si il y a un piéton sur la route. Si le temps restant est à 0 et qu'il y a
    un piéton sur la route, on retire le piéton. Si le temps restant est à 0
    et qu'il n'y a pas de piéton sur la route, on ne fait rien.

    Args:
        route (2D list): Liste des élements de notre route

    Returns:
        route (2D list): Retourne la route avec les piétons mis à jour
    """
    
    for x in range(len(route)):
        for y in range(len(route[x])):
            # Vérifie que l'élément de la route est différent de zéro (par exemple, 0 pourrait représenter un espace vide)
            if route[x][y] != 0:
                # Si l'élément est un passage piéton
                if route[x][y][0] == "Pieton":
                    for k in route[x][y][1]:
                        # Si piéton sur le passage  
                        route[x][y][2][k] -= 1 if route[x][y][2][k]!= 0 else 0

    return route

# ! - A mettrre à jour afin de pouvoir gérer les cycles de feux rouges complexe
def update_depart_pieton(route, trafic, temps):
    """
    Met à jour le trafic piétonnier sur les cases de départ piéton et gère l'alternance des passages piétons.

    Args:
        route (2D list): Liste des éléments de la route où chaque élément peut contenir des informations 
                         sur un emplacement, comme "Depart_pieton".
        trafic (2D list): Liste représentant le trafic de la route, avec 0 pour vide et 1 pour piéton présent.
        temps (int): Temps écoulé depuis le début de la simulation en secondes.

    Returns:
        tuple: Retourne la route mise à jour et le trafic mis à jour.
    """
    
    for x in range(len(route)):
        for y in range(len(route[x])):
            # Vérifie que l'élément de la route est différent de zéro (par exemple, 0 pourrait représenter un espace vide)
            if route[x][y] != 0:
                # Si l'élément est un départ de piéton
                if route[x][y][0] == "Depart_pieton":
                    # Si on génère un nombre aléatoire et si il est inférieur à débit par seconde alors
                    # On génère un piéton permet de modéliser l'aléatoire du trafic
                    if random.random() <= route[x][y][2] / 60:
                        trafic[x][y][0] = 1
                    
                    # Si passage avec alternance et on arrive à la fin du cycle
                    if route[x][y][3] != [0]:
                        temps_tot = sum(route[x][y][3])
                        temps_cumule = [sum(route[x][y][3][:i]) for i in range(len(route[x][y][3]))]
                        # Si on arrive à la fin du cycle on change l'état des feux
                        if (temps % temps_tot) in temps_cumule:
                            route[x][y][4] = not (route[x][y][4])
                        
    return route, trafic

def update_grille(route, direction, trafic, temps):
    """
    Met à jour la grille de simulation en fonction des conditions actuelles des routes, des directions,
    et du trafic pour un instant donné.

    Args:
        route (2D list): Liste des éléments de la route, représentant l'état de chaque cellule.
        direction (2D list): Liste des préférences de direction pour chaque élément de la route.
        trafic (2D list): Représentation du trafic sur la route, indiquant la présence de voitures et piétons.
        temps (int): Temps écoulé depuis le début de la simulation en secondes.

    Returns:
        tuple: Retourne la route mise à jour, les directions mises à jour, et le trafic mis à jour après le traitement des piétons, des voitures, et des feux rouges.
    """
    
    # On met à jour les éléments dans l'ordre
    # On commence par les piétons car prioritaire
    route, trafic = update_depart_pieton(route,trafic,temps)
    route = update_pieton(route)
    
    # Puis les voitures
    direction = update_direction(route, direction)
    trafic = update_depart(route, trafic)
    route = update_feux_rouges(route, temps)
    
    return route, direction, trafic

