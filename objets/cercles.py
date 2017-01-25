""" Gestion des rectangles"""

import math
from objets import points as p
from formes import  Forme

class Cercle(Forme):
    """ Cercle avec 2D"""
    def __init__(self, origine, rayon=0):
        """ init le cercle"""
        Forme.__init__(self,origine)
        self.rayon = rayon

    def __str__(self):
        """ afficher le  cercle"""
        return "Cercle(rayon : {0}) \n \t".format(self.rayon) + Forme.__str__(self)

    def perimetre(self):
        "calculer le perimetre"
        return 2 * math.pi * self.rayon

    def surface(self):
        "calculer la surface"
        return math.pi * math.pow(self.rayon, 2)

if __name__ == "__main__":
    ORIGINE = p.Point(2, 5)
    CERC1 = Cercle(ORIGINE, 3)
    print CERC1
    print "Surface : ", CERC1.surface()
    print "Perimetre : ", CERC1.perimetre()
