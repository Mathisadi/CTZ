# @Autor : Mathis Adinolfi
# @Date of creation : 02/10/2024

# Bibliothèques utilisées

import copy
from Modele import *


# Objectif définir une fonction qui déplace les voitures et met à jour le trafic

def mouvement(route, direction, trafic, temps):
    """Cette fonction a pour but de faire avancer les voitures et de mettre à jour le trafic,
    1 itération correspond à 1 seconde.

    Args:
        route (2D list): Liste des élements de notre route
        direction (2D list): Liste des préferences de direction des utilisateur pour chaque élement et la direction choisie
        trafic (2D list): Liste resprésentant le trafic de notre route 0 = vide / 1 = voiture
        temps (int): Temps depuis début de la simulation en seconde

    Returns:
        route (2D list): Element de la route mis à jour à t = temps
        trafic (2D list): trafic mis à jour aprés mouvement des voitures
        direction (2D list): Mise à jour des directions dans les intersections
    """

    # Update des éléments
    route, direction, trafic = update_grille(route, direction, trafic, temps)
    
    # On garde en copie le trafic
    ref_trafic = copy.deepcopy(trafic)
    
    # Dans un premier temps on fait déplacer les voitures entre les blocs
    deplacement_entre_bloc = changement_bloc(route, direction, trafic)

    # On vient regarder si chaque déplacement entre les blocs est possible
    for k in range(len(deplacement_entre_bloc)):
        # On trouve les nouvelles positions
        x, y, x_dest, y_dest = deplacement_entre_bloc[k]

        # Cas particulier départ autres blocs
        if route[x][y][0] == "Depart":
            if trafic[x_dest][y_dest][0] == 0:
                trafic[x_dest][y_dest][0] += 1
                trafic[x][y][-1] -= 1

        # Cas particulier intersection->intersection
        elif route[x_dest][y_dest][0] == "Intersection" and route[x][y][0] == "Intersection":
            if trafic[x_dest][y_dest][0] == 0 and ref_trafic[x_dest][y_dest][0] == 0:
                direction[x_dest][y_dest] = direction[x][y][1::]
                direction[x][y] = []
                trafic[x_dest][y_dest][0] += 1
                trafic[x][y][-1] -= 1

            # Cas particulier non/intersection->intersection
        elif route[x_dest][y_dest][0] == "Intersection" and route[x][y][0] != "Intersection":
            if trafic[x_dest][y_dest][0] == 0 and ref_trafic[x_dest][y_dest][0] == 0:
                direction[x_dest][y_dest] = chemin_intersection(route, direction, (x, y))
                trafic[x_dest][y_dest][0] += 1
                trafic[x][y][-1] -= 1

        # Cas particulier intersection->non-intersection
        elif route[x_dest][y_dest][0] != "Intersection" and route[x][y][0] == "Intersection":
            if route[x_dest][y_dest][0] == "Fin":
                direction[x][y] = []
                trafic[x_dest][y_dest][0] += 1
                trafic[x][y][-1] -= 1
            elif trafic[x_dest][y_dest][0] == 0 and ref_trafic[x_dest][y_dest][0] == 0:
                direction[x][y] = []
                trafic[x_dest][y_dest][0] += 1
                trafic[x][y][-1] -= 1

        # Cas général
        else:
            if route[x_dest][y_dest][0] == "Fin":
                trafic[x_dest][y_dest][0] += 1
                trafic[x][y][-1] -= 1
            elif trafic[x_dest][y_dest][0] == 0 and ref_trafic[x_dest][y_dest][0] == 0:
                trafic[x_dest][y_dest][0] += 1
                trafic[x][y][-1] -= 1                

    # Dans un second temps on fait déplacer les voitures à l'intérieur des blocs seul les routes sont concernées
    n, m = len(route), len(route[0])
    
    # On test tous les bloc de la grille
    for x in range(n):
        for y in range(m):
            if route[x][y] != 0:
                if route[x][y][0] == "Route":
                    for k in range(2, len(trafic[x][y]) + 1):
                        if (
                            trafic[x][y][-k] == 1
                            and trafic[x][y][-k + 1] == 0
                            and ref_trafic[x][y][-k + 1] == 0
                        ):
                            trafic[x][y][-k + 1] += 1
                            trafic[x][y][-k] -= 1

    return route, direction, trafic
