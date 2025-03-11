import json
import re
import os

# On crée une fonction qui prend un élément et qui crée la value
def create_value(element):
    # On récupère les infos
    info = element["info"]
    type = info["type"]

    if type in ["Route", "Priorite", "Feu", "Depart"]:
        t = [
            info["proba_g"],
            info["proba_b"],
            info["proba_d"],
            info["proba_h"],
        ]
        
        return [t, 0]
    else:
        return []


# On à pour but de créer les json route trafic et direction
def update_direction_json():
    # Path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.abspath(os.path.join(current_dir, "..", "Data.json"))
    direction_path = os.path.abspath(os.path.join(current_dir, "..", "Direction.json"))
    
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    res = {"direction": []}

    for item in data["data"]:
        item_id = item["item_id"]
        value = create_value(item)
        res["direction"].append({"item_id": item_id, "value": value})

    # Sérialiser avec indentation
    json_str = json.dumps(res, ensure_ascii=False, indent=4)
    
    # Expression régulière pour cibler le format spécifique de "value"
    # Cette regex recherche un bloc du type :
    # "value": [  [ ... ],  ...  ]
    pattern = re.compile(
        r'("value":\s*)\[\s*\[(.*?)\],\s*(.*?)\s*\]', 
        re.DOTALL
    )
    
    def repl(match):
        # match.group(1) => "value": (avec les espaces éventuels)
        # match.group(2) => contenu du premier tableau
        # match.group(3) => contenu du second élément
        part1 = re.sub(r'\s+', ' ', match.group(2).strip())
        part2 = re.sub(r'\s+', ' ', match.group(3).strip())
        return f'{match.group(1)}[[{part1}], {part2}]'
    
    # Appliquer le remplacement sur l'ensemble du JSON sérialisé
    json_str = pattern.sub(repl, json_str)
    
    with open(direction_path, "w", encoding="utf-8") as f:
        f.write(json_str)
