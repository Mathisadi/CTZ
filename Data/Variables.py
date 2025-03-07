# @Autor : Mathis Adinolfi
# @Date of creation : 02/10/2024

Route_02 = ["Fin", 0]
Route_03 = ["Intersection", [True, True, False, False], 0]
Route_04 = ["Intersection", [True, False, False, False], 0]
Route_05 = ["Feu", 0, [30,10], True]
Route_06 = ["Route", 0]
Route_07 = ["Depart", 0, 10]
Route_10 = ["Depart", 2, 10]
Route_11 = ["Route", 2]
Route_12 = ["Feu", 2, [30,10], True]
Route_13 = ["Intersection", [False, True, True, False], 0]
Route_14 = ["Intersection", [False, False, True, True], 0]
Route_15 = ["Fin", 2]
Route_23 = ["Route", 1]
Route_24 = ["Feu", 3, [30,10], False]
Route_33 = ["Route", 1]
Route_34 = ["Route", 3]
Route_42 = ["Depart_pieton", 2, 5, [0], True]
Route_43 = ["Pieton", [0, 2], [0, 0, 0, 0], [False, False, False, False]]
Route_44 = ["Pieton", [0, 2], [0, 0, 0, 0], [False, False, False, False]]
Route_45 = ["Depart_pieton", 0, 2, [0], True]
Route_53 = ["Fin", 1]
Route_54 = ["Depart", 3, 10]

Trafic_02 = [0]
Trafic_03 = [0]
Trafic_04 = [0]
Trafic_05 = [0]
Trafic_06 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Trafic_07 = [0]
Trafic_10 = [0]
Trafic_11 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Trafic_12 = [0]
Trafic_13 = [0]
Trafic_14 = [0]
Trafic_15 = [0]
Trafic_23 = [0]
Trafic_24 = [0]
Trafic_33 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Trafic_34 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Trafic_42 = [0]
Trafic_43 = [0]
Trafic_44 = [0]
Trafic_45 = [0]
Trafic_53 = [0]
Trafic_54 = [0]

Direction_02 = []
Direction_03 = []
Direction_04 = []
Direction_05 = [[0.5, 0.5, 0, 0], 0]
Direction_06 = [[1, 0, 0, 0], 0]
Direction_07 = [[1, 0, 0, 0], 0]
Direction_10 = [[0, 0, 1, 0], 0]
Direction_11 = [[0, 0, 1, 0], 0]
Direction_12 = [[0, 0.5, 0.5, 0], 0]
Direction_13 = []
Direction_14 = []
Direction_15 = []
Direction_23 = [[0, 1, 0, 0], 0]
Direction_24 = [[0.5, 0, 0.5, 0], 0]
Direction_33 = [[0, 1, 0, 0], 0]
Direction_34 = [[0, 0, 0, 1], 0]
Direction_42 = []
Direction_43 = [[0, 1, 0, 0], 0]
Direction_44 = [[0, 0, 0, 1], 0]
Direction_45 = []
Direction_53 = []
Direction_54 = [[0, 0, 0, 1], 0]

route_etude = [
    [0       , 0       , Route_02, Route_03, Route_04, Route_05, Route_06, Route_07],
    [Route_10, Route_11, Route_12, Route_13, Route_14, Route_15, 0       , 0       ],
    [0       , 0       , 0       , Route_23, Route_24, 0       , 0       , 0       ],
    [0       , 0       , 0       , Route_33, Route_34, 0       , 0       , 0       ],
    [0       , 0       , Route_42, Route_43, Route_44, Route_45, 0       , 0       ],
    [0       , 0       , 0       , Route_53, Route_54, 0       , 0       , 0       ],
]

trafic_etude = [
    [0        , 0        , Trafic_02, Trafic_03, Trafic_04, Trafic_05, Trafic_06, Trafic_07],
    [Trafic_10, Trafic_11, Trafic_12, Trafic_13, Trafic_14, Trafic_15, 0        , 0        ],
    [0        , 0        , 0        , Trafic_23, Trafic_24, 0        , 0        , 0        ],
    [0        , 0        , 0        , Trafic_33, Trafic_34, 0        , 0        , 0        ],
    [0        , 0        , Trafic_42, Trafic_43, Trafic_44, Trafic_45, 0        , 0        ],
    [0        , 0        , 0        , Trafic_53, Trafic_54, 0        , 0        , 0        ],
]

direction_etude = [
    [0           , 0           , Direction_02, Direction_03, Direction_04, Direction_05, Direction_06, Direction_07],
    [Direction_10, Direction_11, Direction_12, Direction_13, Direction_14, Direction_15, 0           , 0           ],
    [0           , 0           , 0           , Direction_23, Direction_24, 0           , 0           , 0           ],
    [0           , 0           , 0           , Direction_33, Direction_34, 0           , 0           , 0           ],
    [0           , 0           , Direction_42, Direction_43, Direction_44, Direction_45, 0           , 0           ],
    [0           , 0           , 0           , Direction_53, Direction_54, 0           , 0           , 0           ],
]

# Temps de calcul
duree = 1000
