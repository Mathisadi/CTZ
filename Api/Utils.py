# Ce fichier à pour but de répertorier toute les fonctions utiles pour le main
import json
import os




# Fonction qui vérifie que l'on a pas déjà l'élément dans le fichier json
def test_est_dans_data(item_id, chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data["data"]:
        if item["item_id"] == item_id:
            return True

    return False


# Fonction qui édite le fichier data.json
def update_data(item_id, info):
    # Obtenir le dossier courant du fichier
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construire le chemin absolu vers le fichier Variables.json situé dans Data
    chemin_fichier = os.path.abspath(os.path.join(current_dir, "..", "Data", "Data.json"))
    
    # Si l'élément est dans le fichier json on le modifie
    if test_est_dans_data(item_id, chemin_fichier):
        with open(chemin_fichier, "r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data["data"]:
            if item["item_id"] == item_id:
                item["info"] = info

        with open(chemin_fichier, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # Sinon on l'ajoute
    else:
        with open(chemin_fichier, "r", encoding="utf-8") as f:
            data = json.load(f)

        data["data"].append({"item_id": item_id, "info": info})

        with open(chemin_fichier, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            
    print("ok")
