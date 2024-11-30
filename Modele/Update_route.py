# @Autor : Mathis Adinolfi
# @Date of creation : 25/11/2024

# Bibliothèque utilisée
import random

# Fonction permettant de update les éléments de la route

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
                # Si l'élément n'est pas un point de fin ou une intersection, on modifie la direction
                if (
                    route[x][y][0] != "Fin"
                    and route[x][y][0] != "Intersection"
                    and route[x][y][0] != "Depart"
                ):
                    # Mise à jour aléatoire de la direction en fonction des poids fournis
                    # direction[x][y][0] contient les probabilités pour chaque direction
                    # k=1 signifie que l'on choisit une seule direction
                    direction[x][y][1] = random.choices(
                        [0, 1, 2, 3], weights=direction[x][y][0], k=1
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

    for x in range(len(route)):
        for y in range(len(route[x])):
            # Vérifie que l'élément de la route est différent de zéro (par exemple, 0 pourrait représenter un espace vide)
            if route[x][y] != 0:
                # Si l'élément est un départ
                if route[x][y][0] == "Depart":
                    # Si on génère un nombre aléatoire et si il est inférieur à débit par seconde alors
                    # On génère une voiture permet de modéliser l'aléatoire du traffic
                    if random.random() <= route[x][y][2] / 60:
                        traffic[x][y][0] += 1

    return traffic

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
                    # Si on arrive à la fin du cycle on change l'état des feux
                    if (temps % route[x][y][2]) == 0:
                        route[x][y][3] = not (route[x][y][3])

    return route

def update_grille(route, direction, traffic, temps):
    """Mise à jour de la grille de simulation, qui met à jour la direction des voitures, 
    génère des voitures sur les cases de départ et met à jour les feux rouges.
    
    Args:
        route (2D list): Liste des élements de notre route
        direction (2D list): Liste des préferences de direction des utilisateur pour chaque élement
        traffic (2D list): Liste resprésentant le traffic de notre route 0 = vide / 1 = voiture
        temps (int): Temps depuis début de la simulation en seconde

    Returns:
        route (2D list): Retourne la route avec les éléments mis à jour
        direction (2D list): Retourne la direction avec les éléments mis à jour
        traffic (2D list): Retourne le traffic avec les éléments mis à jour
    """
    
    # On met à jour les éléments dans l'ordre
    direction = update_direction(route, direction)
    traffic = update_départ(route, traffic)
    route = update_feux_rouges(route, temps)
    
    return route, direction, traffic
