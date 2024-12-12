# @Autor : Mathis Adinolfi
# @Date of creation : 12/12/2024

# Parce que créer des dictionnaires tout le temps c'est pas beau !

repere = {
        3: (-1, 0),  # Haut
        1: (1, 0),   # Bas
        0: (0, -1),  # Gauche
        2: (0, 1),   # Droite
    }

inverse_repere = {
        (-1, 0): 3,  # Haut
        (1, 0): 1,   # Bas
        (0, -1): 0,   # Gauche
        (0, 1): 2,  # Droite
    }
