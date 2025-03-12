import json
import os

from fastapi import APIRouter
from .Model import *
from .Utils import *
from Modele import *
from Data import *
from Simulation import *

router = APIRouter()


@router.post("/build/{item_id}/route")
def build_route(item_id: int, data: RouteModel):
    # On récupère les infos du front
    info = data.model_dump()

    # On ajoute ou modifie l'element dans data
    update_data(item_id, info)

    return {"status": "ok"}


@router.post("/build/{item_id}/intersection")
def build_intersection(item_id: int, data: IntersectionModel):
    # On récupère les infos du front
    info = data.model_dump()

    # On ajoute ou modifie l'element dans data
    update_data(item_id, info)

    return {"status": "ok"}


@router.post("/build/{item_id}/feu")
def build_feu(item_id: int, data: FeuModel):
    # On récupère les infos du front
    info = data.model_dump()

    # On ajoute ou modifie l'element dans data
    update_data(item_id, info)

    return {"status": "ok"}


@router.post("/build/{item_id}/priorite")
def build_priorite(item_id: int, data: PrioriteModel):
    # On récupère les infos du front
    info = data.model_dump()

    # On ajoute ou modifie l'element dans data
    update_data(item_id, info)

    return {"status": "ok"}


@router.post("/build/{item_id}/pieton")
def build_pieton(item_id: int, data: PietonModel):
    # On récupère les infos du front
    info = data.model_dump()

    # On ajoute ou modifie l'element dans data
    update_data(item_id, info)

    return {"status": "ok"}


@router.post("/build/{item_id}/depart")
def build_depart(item_id: int, data: DepartModel):
    # On récupère les infos du front
    info = data.model_dump()

    # On ajoute ou modifie l'element dans data
    update_data(item_id, info)

    return {"status": "ok"}


@router.post("/build/{item_id}/departPieton")
def build_depart_pieton(item_id: int, data: DepartPietonModel):
    # On récupère les infos du front
    info = data.model_dump()

    # On ajoute ou modifie l'element dans data
    update_data(item_id, info)

    return {"status": "ok"}


@router.post("/build/{item_id}/fin")
def build_fin(item_id: int, data: FinModel):
    # On récupère les infos du front
    info = data.model_dump()

    # On ajoute ou modifie l'element dans data
    update_data(item_id, info)

    return {"status": "ok"}


@router.get("/isSimu")
def is_simu():
    # Obtenir le dossier courant du fichier
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construire le chemin absolu vers le fichier Variables.json situé dans Data
    json_path = os.path.join(current_dir, "..", "Data", "Variables.json")

    with open(json_path, "r") as f:
        data = json.load(f)

    try:
        if data["isSimu"] == True:
            return {"isSimu": True}
        else:
            return {"isSimu": False}
    except:
        return {"isSimu": False}


@router.post("/simulation/launch")
def launch_simu():
    # On lit les datas
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.abspath(os.path.join(current_dir, "..", "Data", "Data.json"))
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # On crée le json Variable
    init_variables_json(data)

    # On lit les datas pour les remettre à jour
    # Construire le chemin absolu vers le fichier Variables.json situé dans Data
    variables_path = os.path.abspath(
        os.path.join(current_dir, "..", "Data", "Variables.json")
    )

    with open(variables_path, "r") as f:
        variables = json.load(f)

    route_etude = variables["variables"]["route"]
    trafic_etude = variables["variables"]["trafic"]
    direction_etude = variables["variables"]["direction"]

    # On enregistre la simu
    create_animation(route_etude, direction_etude, trafic_etude, 300)

    # On modifie la variable isSimu
    # Obtenir le dossier courant du fichier
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construire le chemin absolu vers le fichier Variables.json situé dans Data
    variable_path = os.path.abspath(
        os.path.join(current_dir, "..", "Data", "Variables.json")
    )

    with open(variable_path, "r") as f:
        data = json.load(f)["variables"]

    res = {
        "variables": {
            "route": data["route"],
            "trafic": data["trafic"],
            "direction": data["direction"],
            "isSimu": True,
        }
    }

    formatted_json = custom_json_dumps(res, current_indent=0, indent_step=4)

    with open(variable_path, "w", encoding="utf-8") as f:
        f.write(formatted_json)

    return {"status": "ok"}


@router.post("/clearData")
def clear_data_back():
    # On lance la fonction
    clear_data()

    return {"status": "ok"}
