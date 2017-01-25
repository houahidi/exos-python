""" Gestion des rectangles"""

from objets import points as p
from objets.formes import Forme

class Rectangle(Forme):
    """ Rectangle avec 2D"""
    def __init__(self, origine, longueur=0, largeur=0):
        Forme.__init__(self,origine)
        self.longueur = longueur
        self.largeur = largeur
    def __str__(self):
        """ afficher le  rectangle"""
        return "Rectangle(rayon : {0}, largeur:{1}) \n \t".format(self.longueur, self.largeur) \
               + Forme.__str__(self)

    def perimetre(self):
        "calculer le perimetre"
        return 2 * (self.longueur + self.largeur)

    def surface(self):
        "calculer la surface"
        return self.longueur * self.largeur

if __name__ == "__main__":
    ORIGINE = p.Point(2, 5)
    RECT1 = Rectangle(ORIGINE, 3, 5)
    print RECT1
    print "Surface : ", RECT1.surface()
    print "Perimetre : ", RECT1.perimetre()
