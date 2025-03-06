# Ce fichier à pour but de répertorier toute les fonctions utiles pour le main
import json
        
# Fonction qui vérifie que l'on a pas déjà l'élément dans le fichier json
def test_est_dans_json(item_id, nom_fichier, chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for item in data[nom_fichier]:
        if item["item_id"] == item_id:
            return True
        
    return False

# Fonction qui sélectionne dans les infos que ce qui nous intéresse
def selectionner_info(info):
    # On choisit les infos utiles en fonction du type de route
    type = info["type"]
    
    # Pour les routes
    if type == "route":
        liste_route = ["type", "nom", "sens"]
        liste_trafic = ["len"]
        liste_direction = ["proba_g", "proba_d", "proba_b", "proba_h"]
    
    # Pour les intersection
    if type == "intersection":
        liste_route = ["type", "nom"]
        liste_trafic = ["len"]
        liste_direction = []
    
    # Pour les feux
    if type == "feux":
        liste_route = ["type", "nom", "sens", "cycle"]
        liste_trafic = ["len"]
        liste_direction = ["proba_g", "proba_d", "proba_b", "proba_h"]
        
    # Pour les priorités
    if type == "priorité":
        liste_route = ["type", "nom", "sens"]
        liste_trafic = ["len"]
        liste_direction = ["proba_g", "proba_d", "proba_b", "proba_h"]
    
    # Pour les piétons
    if type == "piéton":
        liste_route = ["type", "nom", "sens"]
        liste_trafic = []
        liste_direction = []
        
    # Pour les départs
    if type == "depart" and info["type_depart"] == "Voiture":
        liste_route = ["type", "nom", "sens"]
        liste_trafic = ["len"]
        liste_direction = ["proba_g", "proba_d", "proba_b", "proba_h"]
    
    # On choisit les infos utiles en fonction du type de route
    liste = liste_route + liste_trafic + liste_direction

    info_route = {elm:info[elm] for elm in info if elm in liste}
    return info_route

# Fonction qui ajoute un nouvel élément dans le fichier route json ou modifie si existant
def ajouter_element(item_id, info, chemin_fichier):
    # Dans les infos on sépare les infos pour chaque fichiers
    info_route = selectionner_info(info)
    
    print(info_route)
   
    # Si l'élément est dans le fichier json on le modifie
    if test_est_dans_json(item_id, "route", chemin_fichier):
        with open(chemin_fichier, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        for item in data["route"]:
            if item["item_id"] == item_id:
                item["info"] = info
        
        with open(chemin_fichier, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    
    # Sinon on l'ajoute
    else:
        with open(chemin_fichier, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        data["route"].append({"item_id": item_id, "info": info})
        
        with open(chemin_fichier, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

print(selectionner_info({"pos_x": 0, "pos_y": 0, "type": "route", "nom": "test", "sens": "test", "proba_g": 0.5, "proba_d": 0.5, "proba_b": 0.5, "proba_h": 0.5, "len": 100.0}))