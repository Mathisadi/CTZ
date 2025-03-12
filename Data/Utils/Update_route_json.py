import json
import os
import re

# On crée un fonction qui crée la value de la route à partir d'un element de data
def create_route_value(element):
    # On récupère les infos
    info = element["info"]
    
    return ["Route", info["sens"]]

# On crée un fonction qui crée la value de l'intersection à partir d'un element de data
def create_intersection_value(element):
    # Direction possible et numéro de l'intersection
    return ["Intersection", [False, False, False, False], 0]

# On crée un fonction qui crée la value du feu à partir d'un element de data
def create_feu_value(element):
    # On récupère les infos
    info = element["info"]
    
    # On crée le cycle
    cycle = info["cycle"]
    cycle = [int(x) for x in cycle.split("/")]

    return ["Feu", info["sens"], cycle, info["etat"]]

# On crée un fonction qui crée la value de la priorité à partir d'un element de data
def create_priorite_value(element):
    # On récupère les infos
    info = element["info"]

    return ["Priorite", info["sens"]]

# On crée un fonction qui crée la value du départ à partir d'un element de data
def create_depart_value(element):
    # On récupère les infos
    info = element["info"]

    if info["type"] == "Depart":
        return ["Depart", info["sens"], info["densite"]]
    else:
        # On crée le cycle
        cycle = info["cycle"]
        cycle = [int(x) for x in cycle.split("/")]
        
        return ["Depart_pieton", info["sens"], info["densite"], cycle, info["etat"]]
    
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

    if type == "Route":
        return create_route_value(element)
    elif type == "Intersection":
        return create_intersection_value(element)
    elif type == "Feu":
        return create_feu_value(element)
    elif type == "Priorite":
        return create_priorite_value(element)
    elif type == "Depart":
        return create_depart_value(element)
    elif type == "Pieton":
        return create_pieton_value(element)
    elif type == "Depart_pieton":
        return create_depart_value(element)
    elif type == "Fin":
        return create_arrivee_value(element)

# On à pour but de créer les json route trafic et direction
def update_route_json(data):
    # Obtenir le dossier courant du fichier
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construire le chemin absolu vers le fichier Variables.json situé dans Data
    route_path = os.path.abspath(os.path.join(current_dir, "..", "Route.json"))

    
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

    with open(route_path, "w", encoding="utf-8") as f:
        f.write(json_str)
