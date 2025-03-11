import os
import json

# Fonction qui clear les données
def clear_data():
    # Path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.abspath(os.path.join(current_dir, "..", "Data.json"))
    direction_path = os.path.abspath(os.path.join(current_dir, "..", "Direction.json"))
    route_path = os.path.abspath(os.path.join(current_dir, "..", "Route.json"))
    trafic_path = os.path.abspath(os.path.join(current_dir, "..", "Trafic.json"))
    variable_path  = os.path.abspath(os.path.join(current_dir, "..", "Variables.json"))
    
    # Pour chaque json on crée le fichier initiale
    init_data = {"data" : []}
    init_route = {"route" : []}
    init_trafic = {"trafic" : []}
    init_direction = {"direction" : []}
    init_variable = {"variables" : {"route":[],"trafic":[],"direction":[]}}
    
    # On écrit ça dans chaque JSON
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(init_data, f, ensure_ascii=False, indent=4)
        
    with open(route_path, "w", encoding="utf-8") as f:
        json.dump(init_route, f, ensure_ascii=False, indent=4)
    
    with open(trafic_path, "w", encoding="utf-8") as f:
        json.dump(init_trafic, f, ensure_ascii=False, indent=4)
    
    with open(direction_path, "w", encoding="utf-8") as f:
        json.dump(init_direction, f, ensure_ascii=False, indent=4)
    
    with open(variable_path, "w", encoding="utf-8") as f:
        json.dump(init_variable, f, ensure_ascii=False, indent=4)
        
# On supprimer la simulation si existante
def clear_res():
    # Path res
    current_dir = os.path.dirname(os.path.abspath(__file__))
    res_path = os.path.abspath(os.path.join(current_dir, "..", "..", "Interface", "src", "res", "animation.mp4"))
    
    if os.path.exists(res_path):
        os.remove(res_path)

        
clear_data()
clear_res()