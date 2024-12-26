# @Autor : Mathis Adinolfi
# @Date of creation : 30/11/2024

from .Variables import route_etude, trafic_etude, direction_etude, duree

# Si vous voulez limiter ce qui est exporté lorsque quelqu'un fait "from Modele import *"
__all__ = [
    "route_etude",
    "trafic_etude",
    "direction_etude",
    "duree",
]
