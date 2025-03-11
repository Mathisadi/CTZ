import json
import os

def lecture_variables():
    # Obtenir le dossier courant du fichier
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construire le chemin absolu vers le fichier Variables.json situé dans Data
    variables_path = os.path.abspath(os.path.join(current_dir, "Variables.json"))
    
    with open(variables_path, "r") as f:
        variables = json.load(f)

    route_etude = variables["variables"]["route"]
    trafic_etude = variables["variables"]["trafic"]
    direction_etude = variables["variables"]["direction"]
    
    return route_etude, trafic_etude, direction_etude

# Variables globales
route_etude, trafic_etude, direction_etude = lecture_variables()

duree = 100