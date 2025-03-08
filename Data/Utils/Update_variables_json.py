import json
import re

def trouve_pos_index(data):
    
    # Liste avec tous les index
    index = [data["data"][i]["item_id"] for i in range(len(data["data"]))]
    
    # On crée un dico qui pour un index retourne la pos
    res = {}
    for val in index:
        row = val // 101
        col = val % 101 
        res[val] = [row, col]
    
    # On trouve le min row et le max row
    min_row = min(res.values(), key=lambda x: x[0])[0]
    min_col = min(res.values(), key=lambda x: x[1])[1]
    
    # On soustrait à toutes les valeurs le min row et le min col
    for key in res.keys():
        res[key][0] -= min_row
        res[key][1] -= min_col

    return res

# On écrit une fonction qui trouve la largeur et la hauteur de la route
def trouve_dimension(dict):

    largeur = max(dict.values(), key=lambda x: x[1])[1] + 1
    hauteur = max(dict.values(), key=lambda x: x[0])[0] + 1
    
    return largeur, hauteur

# On écrit une fonction qui crée la matrice de la route
def create_matrice(data):
    # On lit les datas de la route
    with open("./Data/Route.json", "r", encoding="utf-8") as f:
        data_route = json.load(f)
    
    # On lit les datas du trafic
    with open("./Data/Trafic.json", "r", encoding="utf-8") as f:
        data_trafic = json.load(f)
    
    # On lit les datas de la direction
    with open("./Data/Direction.json", "r", encoding="utf-8") as f:
        data_direction = json.load(f)      
    
    # On trouve les pos des index
    pos = trouve_pos_index(data)
    
    # On trouve la largeur et la hauteur
    largeur, hauteur = trouve_dimension(pos)
    
    # On crée la matrice vide
    route = [[0 for _ in range(largeur)] for _ in range(hauteur)]
    trafic = [[0 for _ in range(largeur)] for _ in range(hauteur)]
    direction = [[0 for _ in range(largeur)] for _ in range(hauteur)]
     
    # On remplit la matrice avec les valeurs
    for key in pos.keys():
        # Je veux la value de l'item id = key
        for elm in data_route["route"]:
            if elm["item_id"] == key:
                route[pos[key][0]][pos[key][1]] = elm["value"]

        for elm in data_trafic["route"]:
            if elm["item_id"] == key:
                trafic[pos[key][0]][pos[key][1]] = elm["value"]

        for elm in data_direction["route"]:
            if elm["item_id"] == key:
                direction[pos[key][0]][pos[key][1]] = elm["value"]
             
    return route, trafic, direction

def is_simple_list(lst):
    """
    Renvoie True si lst est une liste dont tous les éléments sont simples.
    Un élément est considéré simple s'il n'est pas un dictionnaire et, s'il s'agit d'une liste,
    tous ses éléments sont eux-mêmes simples (récursivement).
    """
    if not isinstance(lst, list):
        return False
    for x in lst:
        if isinstance(x, dict):
            return False
        if isinstance(x, list) and not is_simple_list(x):
            return False
    return True

def custom_json_dumps(obj, current_indent=0, indent_step=4):
    sp = " " * current_indent
    if isinstance(obj, dict):
        items = []
        for key, value in obj.items():
            formatted_value = custom_json_dumps(value, current_indent + indent_step, indent_step)
            items.append(" " * (current_indent + indent_step) + json.dumps(key) + ": " + formatted_value)
        return "{\n" + ",\n".join(items) + "\n" + sp + "}"
    elif isinstance(obj, list):
        # Si c'est une "matrice" : chaque élément est une liste simple
        if all(isinstance(item, list) and is_simple_list(item) for item in obj):
            lines = []
            for row in obj:
                # Formatage de la ligne avec un espace après chaque virgule
                row_str = json.dumps(row, separators=(', ', ':'))
                lines.append(" " * (current_indent + indent_step) + row_str)
            return "[\n" + ",\n".join(lines) + "\n" + sp + "]"
        # Si la liste elle-même est simple (pas de sous-listes complexes), on la dump compactement
        elif is_simple_list(obj):
            return json.dumps(obj, separators=(', ', ':'))
        else:
            items = []
            for item in obj:
                items.append(custom_json_dumps(item, current_indent + indent_step, indent_step))
            return "[\n" + ",\n".join(" " * (current_indent + indent_step) + i for i in items) + "\n" + sp + "]"
    else:
        return json.dumps(obj)

def update_variables_json():
    with open("./Data/Data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # La fonction create_matrice doit retourner trois matrices : route, trafic, direction
    route, trafic, direction = create_matrice(data)
    res = {"variables": {"route": route, "trafic": trafic, "direction": direction}}

    formatted_json = custom_json_dumps(res, current_indent=0, indent_step=4)

    with open("./Data/Variables.json", "w", encoding="utf-8") as f:
        f.write(formatted_json)


update_variables_json()
