""" Gestion des points 2D en objet"""
import math

class Point:
    """ Point en 2D"""
    def __init__(self, abscisse = 0, ordonnee = 0):
        """initialiser les cordonnees du point"""
        self.abscisse = abscisse
        self.ordonnee = ordonnee

    def deplacer(self, deplx, deply):
        """ deplacer le point"""
        self.abscisse += deplx
        self.ordonnee += deply

    def __str__(self):
        """ afficher le point"""
        return "Point(x={0},y={1})".format(self.abscisse, self.ordonnee)

    def calculer_distance(self, point):
        """ calculer la distance entre 2 points"""
        diffx = math.pow(self.abscisse - point.abscisse, 2)
        diffy = math.pow(self.ordonnee - point.ordonnee, 2)
        return math.sqrt(diffx + diffy)

    def __sub__(self, point):
        """ calculer la distance entre 2 points"""
        return self.calculer_distance(point)

if __name__ == "__main__":
    print "definir Point1"
    POINT1 = Point(1,4)
    print POINT1
    print "deplacer Point1 avec deplx: 3 et deply:5"
    POINT1.deplacer(3, 5)
    print POINT1
    print "definir Point2"
    POINT2 = Point(3, 5)
    print POINT2
    print "distance : ", POINT1.calculer_distance(POINT2)
    print "distance : ", POINT1 - POINT2

