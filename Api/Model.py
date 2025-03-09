from pydantic import BaseModel

class RouteModel(BaseModel):
    type: str
    nom: str
    sens: int
    proba_g: float
    proba_d: float
    proba_b: float
    proba_h: float
    len: float

class IntersectionModel(BaseModel):
    type: str
    nom: str
    len: float
    
class FeuModel(BaseModel):
    type: str
    nom: str
    sens: int
    proba_g: float
    proba_d: float
    proba_b: float
    proba_h: float
    cycle: str
    etat: bool

class PrioriteModel(BaseModel):
    type: str
    nom: str
    sens: int
    proba_g: float
    proba_d: float
    proba_b: float
    proba_h: float
    len: float

class PietonModel(BaseModel):
    type: str
    nom: str
    sens: list
    len: float

class DepartModel(BaseModel):
    type: str
    nom: str
    sens: int
    densite: float
    proba_g: float
    proba_d: float
    proba_b: float
    proba_h: float
    len: float

class DepartPietonModel(BaseModel):
    type: str
    nom: str
    sens: int
    densite: float
    cycle: str
    etat: bool
    len: float

class FinModel(BaseModel):
    type: str
    nom: str
    sens: int
    len: float
