""" Gestion des formes"""

import math
from objets import points as p

class Forme:
    """ Forme avec 2D"""
    def __init__(self, origine):
        """ init le cercle"""
        self.origine = origine

    def __str__(self):
        """ afficher la forme"""
        _str = "Forme"
        if self.origine is not None:
            _str += " avec Origine :" + str(self.origine)
        return _str

    def deplacer(self, deplx, deply):
        """ deplacer la forme"""
        if self.origine is not None:
            self.origine.deplacer(deplx, deply)
        else:
            self.origine = p.Point(deplx, deply)

if __name__ == "__main__":
    ORI1 = p.Point(1,5)
    FORME1 = Forme(ORI1)
    print FORME1