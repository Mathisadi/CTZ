# Modéle des différents éléments :

## Route

Route = ["Route", 1 = direction de la route]
Trafic = [0,0,0,0,0,0,0] la len de la liste = len de la route en m / 4 m
Direction = [[0,0,1,0] = les directions possibles et les probas associées, 2 = la direction choisie]

---

## Intersection

Route = ["Intersection", [True, True, True, True] = les directions possibles depuis l'intersection, 0 = numéro de l'intersection]
Trafic = [0] len = 1
Direction = [] liste dynamique qui sera remplie en fonction des directions de la voiture sur l'intersection

---

## Feu

Route = ["Feu", 1 = direction de la route, [34] = temps du cyle du feu, True = état du feu]
Trafic = [0] len = 1
Direction = [[0,0,1,0] = les directions possibles et les probas associées, 2 = la direction choisie]

---

## Priorité

Route = ["Priorite", 1 = direction de la route]
Trafic = [0] len = 1
Direction = [[0,0,1,0] = les directions possibles et les probas associées, 2 = la direction choisie]

---

## Depart

Route = ["Depart", 1 = direction de la route, 10 = densité de voiture V/min]
Trafic = [12] le nombre de voiture présent sur le départ
Direction = [[0,0,1,0] = les directions possibles et les probas associées, 2 = la direction choisie]

---

## Pieton

Route = ["Pieton", 1 = direction du piéton, 4 = temps restant pour traverser, True = piéton présent] : parametres piétons
Trafic = [0] len = 1 : paramètres voitures
Direction = [[0,0,1,0] = les directions possibles et les probas associées, 2 = la direction choisie] : paramètres voitures

---

## Depart piéton

Route = ["Depart_pieton", 0 = direction de la route, 5 = densité de piéton en fonction des directions P/min, 30 = temps du cycle, True = état du passage piéton]
Trafic = [0] = piéton présent ?
Direction = []

---

## Fin

Route = ["Fin", 1 = direction de la route]
Trafic = [21] = nbr de voiture sur le bloc de fin
Direction = []

