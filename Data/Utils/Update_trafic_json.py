import json
import re
import os

# On crée une fonction qui prend un élément et qui crée la value
def create_value(element):
    # On récupère les infos
    info = element["info"]
    type = info["type"]

    if type == "Route":
        return [0] * round(info["len"] / 4)
    else:
        return [0]


# On à pour but de créer les json route trafic et direction
def update_trafic_json():
    # Obtenir le dossier courant du fichier
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construire le chemin absolu vers le fichier Variables.json situé dans Data
    data_path = os.path.abspath(os.path.join(current_dir, "..", "Data.json"))
    trafic_path = os.path.abspath(os.path.join(current_dir, "..", "Trafic.json"))

    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    res = {"trafic": []}

    for item in data["data"]:
        item_id = item["item_id"]
        value = create_value(item)
        res["trafic"].append({"item_id": item_id, "value": value})
        
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

    with open(trafic_path, "w", encoding="utf-8") as f:
        f.write(json_str)
