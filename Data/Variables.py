import json

def lecture_variables():
    with open("Data/Variables.json", "r") as f:
        variables = json.load(f)
    
    route_etude = variables["variables"]["route"]
    trafic_etude = variables["variables"]["trafic"]
    direction_etude = variables["variables"]["direction"]
    
    return route_etude, trafic_etude, direction_etude

# Variables globales
route_etude, trafic_etude, direction_etude = lecture_variables()

duree = 300