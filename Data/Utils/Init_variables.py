from .Update_direction_intersection import *
from .Update_trafic_json import *
from .Update_direction_json import * 
from .Update_route_json import *
from .Update_variables_json import *

def init_variables_json():
    # On upadte les fichier route trafic et direction
    update_route_json()
    update_trafic_json()
    update_direction_json()
    
    # On crée le fichier variable
    update_variables_json()
    
    # On trouve les directions des intersections et on modifie le fichier variable
    update_direction_intersection()
