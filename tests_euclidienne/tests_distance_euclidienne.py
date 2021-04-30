# Créé par theog, le 30/04/2021 en Python 3.7
import numpy as np
from projet import distance_euclidienne
from random import randint

Bilan = True

point_a =  np.array((randint(0,10000),randint(0,10000)))
point_b =  np.array((randint(0,10000),randint(0,10000)))
point_c =  np.array((randint(0,10000),randint(0,10000)))
if distance_euclidienne(point_a,point_a) == 0:
    Bilan = True
else :
    Bilan = False
if Bilan == False:
    print("echec du test")


if distance_euclidienne(point_b,point_b) == 0:
    Bilan = True
else :
    Bilan = False
if Bilan == False:
    print("echec du test")

if distance_euclidienne(point_a,point_b) == 0 or distance_euclidienne(point_a,point_b) > 0:
    Bilan = True
else :
    Bilan = False
if Bilan == False:
    print("echec du test")

ab = distance_euclidienne(point_a,point_b)
ac = distance_euclidienne(point_a,point_c)
bc = distance_euclidienne(point_b,point_c)
somme = ab + bc
if ac < somme or ac == somme :
    Bilan = True
else :
    Bilan = False
if Bilan == False:
    print("echec du test")
