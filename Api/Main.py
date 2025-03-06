from typing import Union
import json

from fastapi import FastAPI

app = FastAPI()




@app.post("/build/{item_id}/route")
def build_route(item_id: int, item_type: str, data: DataModel):
    chemin_fichier = "./Var/Variables.json"

    # On ouvre les données
    info = data.model_dump()

    # On crée le header
    info = {"type": item_type, **info}

    # On crée les données à afficher
    donnee = {"item_id": item_id, "info":info}

    try:
        # On copie les valeurs existantes
        with open(chemin_fichier, "r", encoding="utf-8") as f:
            donnee_existante = json.load(f)

        # On ajoute les nouvelles données
        donnee_existante["element"].append(donnee)

        # On sauvegarde
        with open(chemin_fichier, "w", encoding="utf-8") as f:
            json.dump(donnee_existante, f, ensure_ascii=False, indent=4)
        print("ok")

    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier JSON : {e}")

    # Par exemple, vous pouvez les enregistrer en base de données ou effectuer d'autres traitements
    return {
        "status": "succès",
        "message": "Données traitées avec succès",
        "data": data.model_dump(),
    }
