# Variables

Route_02 = ["Fin"]
Route_03 = ["Intersection", [False, False, False, False]]
Route_04 = ["Intersection", [False, False, False, False]]
Route_05 = ["Feu", 0, 34, True]
Route_06 = ["Route", 0]
Route_07 = ["Depart", 0, 10]
Route_10 = ["Depart", 2, 10]
Route_11 = ["Route", 2]
Route_12 = ["Feu", 2, 34, True]
Route_13 = ["Intersection", [False, False, False, False]]
Route_14 = ["Intersection", [False, False, False, False]]
Route_15 = ["Fin"]
Route_23 = ["Fin"]
Route_24 = ["Feu", 3, 34, False]
Route_34 = ["Route", 3]
Route_44 = ["Depart", 3, 10]

Traffic_02 = [0]
Traffic_03 = [0]
Traffic_04 = [0]
Traffic_05 = [0]
Traffic_06 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Traffic_07 = [0]
Traffic_10 = [0]
Traffic_11 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Traffic_12 = [0]
Traffic_13 = [0]
Traffic_14 = [0]
Traffic_15 = [0]
Traffic_23 = [0]
Traffic_24 = [0]
Traffic_34 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Traffic_44 = [0]

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
Direction_23 = []
Direction_24 = [[0.5, 0, 0.5, 0], 0]
Direction_34 = [[0, 0, 0, 1], 0]
Direction_44 = [[0, 0, 0, 1], 0]

route_etude = [
    [0, 0, Route_02, Route_03, Route_04, Route_05, Route_06, Route_07],
    [Route_10, Route_11, Route_12, Route_13, Route_14, Route_15, 0, 0],
    [0, 0, 0, Route_23, Route_24, 0, 0, 0],
    [0, 0, 0, 0, Route_34, 0, 0, 0],
    [0, 0, 0, 0, Route_44, 0, 0, 0],
]

traffic_etude = [
    [0, 0, Traffic_02, Traffic_03, Traffic_04, Traffic_05, Traffic_06, Traffic_07],
    [Traffic_10, Traffic_11, Traffic_12, Traffic_13, Traffic_14, Traffic_15, 0, 0],
    [0, 0, 0, Traffic_23, Traffic_24, 0, 0, 0],
    [0, 0, 0, 0, Traffic_34, 0, 0, 0],
    [0, 0, 0, 0, Traffic_44, 0, 0, 0],
]

direction_etude = [
    [
        0,
        0,
        Direction_02,
        Direction_03,
        Direction_04,
        Direction_05,
        Direction_06,
        Direction_07,
    ],
    [
        Direction_10,
        Direction_11,
        Direction_12,
        Direction_13,
        Direction_14,
        Direction_15,
        0,
        0,
    ],
    [0, 0, 0, Direction_23, Direction_24, 0, 0, 0],
    [0, 0, 0, 0, Direction_34, 0, 0, 0],
    [0, 0, 0, 0, Direction_44, 0, 0, 0],
]

duree = 1000
