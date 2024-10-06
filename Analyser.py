import Modele
from Variables import *
import csv
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import time

# Idée de test 1 : nbr de voiture total sur la route hors fin


def test_1(route, direction, traffic, temps_min, temps_max, duree_test):

    compt = []

    for duree in tqdm(range(temps_min, temps_max + 1)):

        for i in range(len(route)):
            for j in range(len(route[i])):
                if route[i][j] != 0 and route[i][j][0] == "Feu":
                    route[i][j][2] = duree

        l = []

        for temps in range(duree_test):

            route, direction, traffic = Modele.mouvement(route, direction, traffic, temps)

            res = 0

            for i in range(len(traffic)):
                for j in range(len(traffic[i])):
                    if isinstance(traffic[i][j], list):
                        if route[i][j] != 0 and route[i][j][0] == "Route":
                            res += traffic[i][j].count(1)
                        elif route[i][j] != 0 and route[i][j][0] != "Fin":
                            res += traffic[i][j][0]

            l.append(res)

        compt.append(l)
        
    return compt

r = test_1(route_etude, direction_etude, traffic_etude, 5, 60, 1000)
s = [sum(r[i]) for i in range(len(r))]
index = sorted(range(len(s)), key=lambda i: s[i])[:1]

fig, ax = plt.subplots()
l = np.linspace(0,1000,1000)
for i in index:
    ax.plot(l,r[i], label=str(i))
ax.legend()
plt.show()
