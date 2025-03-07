# On à pour but de créer les json route trafic et direction
def update_route_json():
    


# Fonction qui sélectionne dans les infos que ce qui nous intéresse
def slicer_info(info):
    # On choisit les infos utiles en fonction du type de route
    type = info["type"]

    # Pour les routes
    if type == "route":
        liste_route = ["type", "nom", "sens"]
        liste_direction = []

    # Pour les intersection
    elif type == "intersection":
        liste_route = ["type", "nom"]
        liste_direction = []

    # Pour les feux
    elif type == "feux":
        liste_route = ["type", "nom", "sens", "cycle"]
        liste_direction = ["proba_g","proba_b", "proba_d", "proba_h"]

    # Pour les priorités
    elif type == "priorité":
        liste_route = ["type", "nom", "sens"]
        liste_direction = ["proba_g","proba_b", "proba_d", "proba_h"]

    # Pour les piétons
    elif type == "piéton":
        liste_route = ["type", "nom", "sens"]
        liste_direction = []

    # Pour les départs voiture
    elif type == "depart_voiture":
        liste_route = ["type", "nom", "sens", "densite"]
        liste_direction = []

    # Pour les départ piéton
    elif type == "depart_pieton":
        liste_route = ["type", "nom", "sens", "densite", "cycle"]
        liste_direction = []

    # Pour les arrivée
    elif type == "arrivee":
        liste_route = ["type", "nom"]
        liste_direction = []
    # Pour les arrivée

    return liste_route, liste_direction


# Fonction qui génère les données à rentrer dans le fichier route
def route_info(liste_route, info):

    # On ajoute les infos de la liste
    info_route = {elm: info[elm] for elm in info if elm in liste_route}

    # On ajoute les infos qui ne sont pas dans la liste
    type = info["type"]

    # Si intersection on rajoute les directions possible
    if type == "intersection":
        # Liste des directions possible
        t = [0, 0, 0, 0]
        t[info["sens"]] = 1

        # On ajoute les infos
        info_route["direction"] = t
        info_route["Id_inter"] = 0

    elif type == "feux":
        # On ajoute l'état du feu
        info_route["etat"] = True

    elif type == "pieton":
        # On ajoute l'état du piéton
        info_route["presence"] = True

    elif type == "depart_pieton":
        # On ajoute l'état du feu
        info_route["etat"] = True

    return info_route


# Fonction qui génère les données à rentrer dans le fichier trafic
def trafic_info(info):
    return {"value": [0] * info["len"]}


# Fonction qui génère les données à rentrer dans le fichier direction
def direction_info(liste_direction, info):
    # Si vide
    if liste_direction == []:
        return {}
    # Sinon
    else:
        []
        
        
update_data(4, {"type": "route", "nom": "route", "sens": 1})