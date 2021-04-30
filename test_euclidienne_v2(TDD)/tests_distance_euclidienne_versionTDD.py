# Créé par theog, le 30/04/2021 en Python 3.7
import numpy as np
import math
from projet import distance_euclidienne
from random import randint
import unittest
class test_distance_euclidienne(unittest.TestCase):
    def setUp(self):
        point_a =  np.array((randint(0,10000),randint(0,10000)))
        point_b =  np.array((randint(0,10000),randint(0,10000)))
        point_c =  np.array((randint(0,10000),randint(0,10000)))
    def PermierTest(self):
        self.assertEqual( 0,distance_euclidienne(point_a,point_a))
    def DeuxièmeTest(self):
        self.assertGreaterEqual(distance_euclidienne(point_a,point_b),0)
    def TroisèmeTest(self):
        self.assertEqual(distance_euclidienne(point_a,point_b),distance_euclidienne(point_b,point_a))
    def QuatrièmeTest(self):
        ab = distance_euclidienne(point_a,point_b)
        ac = distance_euclidienne(point_a,point_c)
        bc = distance_euclidienne(point_b,point_c)
        somme = ab + bc
        self.assertLessEqual(ac,somme)
    def Derniertest(self):
        self.assertAlmostEqual(distance_euclidienne((0,1)(1,0)),sqrt(2))
if __name__ == '__main__':
unittest.main()
