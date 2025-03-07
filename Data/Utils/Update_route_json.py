import json
import re

# On crée un fonction qui crée la value de la route à partir d'un element de data
def create_route_value(element):
    # On récupère les infos
    info = element["info"]
    
    return ["Route", info["sens"]]

# On crée un fonction qui crée la value de l'intersection à partir d'un element de data
def create_intersection_value(element):
    # Direction possible et numéro de l'intersection
    return ["Intersection", [True, True, True, True], 0]

# On crée un fonction qui crée la value du feu à partir d'un element de data
def create_feu_value(element):
    # On récupère les infos
    info = element["info"]

    return ["Feu", info["sens"], info["cycle"], info["etat"]]

# On crée un fonction qui crée la value de la priorité à partir d'un element de data
def create_priorite_value(element):
    # On récupère les infos
    info = element["info"]

    return ["Priorité", info["sens"]]

# On crée un fonction qui crée la value du départ à partir d'un element de data
def create_depart_value(element):
    # On récupère les infos
    info = element["info"]

    if info["type"] == "depart_voiture":
        return ["Depart", info["sens"], info["densite"]]
    else:
        return ["Depart_pieton", info["sens"], info["densite"], info["cycle"], info["etat"]]
    
# On crée une fonction qui crée la value du piéton à partir d'un element de data
def create_pieton_value(element):
    # On récupère les infos
    info = element["info"]

    return ["Pieton", info["sens"], [0, 0, 0, 0], [False, False, False, False]]

# On crée une fonction qui crée la value de la fin à partir d'un element de data
def create_arrivee_value(element):
    # On récupère les infos
    info = element["info"]

    return ["Fin", info["sens"]]

# On crée une fonction qui prend un élément et qui crée la value
def create_value(element):
    # On récupère les infos
    info = element["info"]
    type = info["type"]

    if type == "route":
        return create_route_value(element)
    elif type == "intersection":
        return create_intersection_value(element)
    elif type == "feux":
        return create_feu_value(element)
    elif type == "priorité":
        return create_priorite_value(element)
    elif type == "depart_voiture":
        return create_depart_value(element)
    elif type == "piéton":
        return create_pieton_value(element)
    elif type == "depart_pieton":
        return create_depart_value(element)
    elif type == "fin":
        return create_arrivee_value(element)

# On à pour but de créer les json route trafic et direction
def update_route_json():
    with open("./Data/Data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    res = {"route" :[]}

    for item in data["data"]:
        item_id = item["item_id"]
        value = create_value(item)
        res["route"].append({"item_id": item_id, "value": value})
        
    # Sérialisation avec indentation pour une bonne lisibilité
    json_str = json.dumps(res, ensure_ascii=False, indent=4)
    
    # Post-traitement pour remettre en ligne le contenu des tableaux "value"
    # Cette regex cherche le pattern "value": [ ... ] avec des retours à la ligne à l'intérieur
    json_str = re.sub(
        r'("value": )\[\n(.*?)\n\s*\]',
        lambda m: m.group(1) + '[' + re.sub(r'\n\s*', ' ', m.group(2)).strip() + ']',
        json_str,
        flags=re.DOTALL
    )

    with open("./Data/Route.json", "w", encoding="utf-8") as f:
        f.write(json_str)
