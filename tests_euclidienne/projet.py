# Créé par theog, le 29/04/2021 en Python 3.7
import numpy as np
point_a = np.array((0,0))
point_b = np.array((1,1))

def distance_euclidienne(a,b):
    distance = np.linalg.norm(a-b)
    return distance

print(distance_euclidienne(point_a,point_b))