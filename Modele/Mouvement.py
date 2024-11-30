# @Autor : Mathis Adinolfi
# @Date of creation : 02/10/2024

# Bibliothèques utilisées

import copy
from Modele import *


# Objectif définir une fonction qui déplace les voitures et met à jour le traffic

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
    route, direction, traffic = update_grille(route, direction, traffic, temps)
    
    # On garde en copie le traffic
    ref_traffic = copy.deepcopy(traffic)
    
    # Dans un premier temps on fait déplacer les voitures entre les blocs
    deplacement_entre_bloc = changement_bloc(route, direction, traffic)

    # On vient regarder si chaque déplacement entre les blocs est possible
    for k in range(len(deplacement_entre_bloc)):
        # On trouve les nouvelles positions
        x, y, x_dest, y_dest = deplacement_entre_bloc[k]

        # Cas particulier départ autres blocs
        if route[x][y][0] == "Depart":
            if traffic[x_dest][y_dest][0] == 0:
                traffic[x_dest][y_dest][0] += 1
                traffic[x][y][-1] -= 1

        # Cas particulier intersection->intersection
        elif route[x_dest][y_dest][0] == "Intersection" and route[x][y][0] == "Intersection":
            if traffic[x_dest][y_dest][0] == 0 and ref_traffic[x_dest][y_dest][0] == 0:
                direction[x_dest][y_dest] = direction[x][y][1::]
                direction[x][y] = []
                traffic[x_dest][y_dest][0] += 1
                traffic[x][y][-1] -= 1

            # Cas particulier non/intersection->intersection
        elif route[x_dest][y_dest][0] == "Intersection" and route[x][y][0] != "Intersection":
            if traffic[x_dest][y_dest][0] == 0 and ref_traffic[x_dest][y_dest][0] == 0:
                direction[x_dest][y_dest] = chemin_intersection(route, direction, (x, y))
                traffic[x_dest][y_dest][0] += 1
                traffic[x][y][-1] -= 1

        # Cas particulier intersection->non-intersection
        elif route[x_dest][y_dest][0] != "Intersection" and route[x][y][0] == "Intersection":
            if route[x_dest][y_dest][0] == "Fin":
                direction[x][y] = []
                traffic[x_dest][y_dest][0] += 1
                traffic[x][y][-1] -= 1
            elif traffic[x_dest][y_dest][0] == 0 and ref_traffic[x_dest][y_dest][0] == 0:
                direction[x][y] = []
                traffic[x_dest][y_dest][0] += 1
                traffic[x][y][-1] -= 1

        # Cas général
        else:
            if route[x_dest][y_dest][0] == "Fin":
                traffic[x_dest][y_dest][0] += 1
                traffic[x][y][-1] -= 1
            elif traffic[x_dest][y_dest][0] == 0 and ref_traffic[x_dest][y_dest][0] == 0:
                traffic[x_dest][y_dest][0] += 1
                traffic[x][y][-1] -= 1                

    # Dans un second temps on fait déplacer les voitures à l'intérieur des blocs seul les routes sont concernées
    n, m = len(route), len(route[0])
    
    # On test tous les bloc de la grille
    for x in range(n):
        for y in range(m):
            if route[x][y] != 0:
                if route[x][y][0] == "Route":
                    for k in range(2, len(traffic[x][y]) + 1):
                        if (
                            traffic[x][y][-k] == 1
                            and traffic[x][y][-k + 1] == 0
                            and ref_traffic[x][y][-k + 1] == 0
                        ):
                            traffic[x][y][-k + 1] += 1
                            traffic[x][y][-k] -= 1

    return route, direction, traffic
