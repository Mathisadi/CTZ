import json
import re


# On crée une fonction qui prend un élément et qui crée la value
def create_value(element):
    # On récupère les infos
    info = element["info"]
    type = info["type"]

    if type == "route":
        return [0] * round(info["len"] / 4)
    else:
        return [0]


# On à pour but de créer les json route trafic et direction
def update_trafic_json():
    with open("./Data/Data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    res = {"route": []}

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

    with open("./Data/Trafic.json", "w", encoding="utf-8") as f:
        f.write(json_str)
    
update_trafic_json()
