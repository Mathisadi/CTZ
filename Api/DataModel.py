from pydantic import BaseModel

# Définition du modèle de données correspondant aux informations envoyées
class RouteModel(BaseModel):
    nom: str
    sens: str
    proba_g: float
    proba_d: float
    proba_b: float
    proba_h: float
    len: float

