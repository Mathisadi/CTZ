import json
from fastapi import APIRouter
from Model import *
from Utils import *

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