"""Gestion des points 2D avec des fonctions"""
import  math

def init(coordx=None, coordy=None):
    """initialser les coordonnees du point"""
    if coordx is None:
        coordx = int(raw_input("Veuillez saisir x :"))
    if coordy is None:
        coordy = int(raw_input("Veuillez saisir y :"))

    return {'x':coordx, 'y':coordy}

def afficher(point):
    """afficher les coordonnees du point"""
    print "Point(x={0}, y={1})".format(point['x'], point['y'])

def deplacer(point, deplx, deply):
    """modifier les coordonnees du point"""
    point['x'] += deplx
    point['y'] += deply

def calculer_distance(point1, point2):
    """calculer la distance entre les 2 points"""
    diffx = math.pow(point1['x'] - point2['x'], 2)
    diffy = math.pow(point1['y'] - point2['y'], 2)
    return math.sqrt(diffx + diffy)

if __name__ == "__main__":
    POINT1 = init()
    afficher(POINT1)
    deplacer(POINT1, 3, 5)
    POINT2 = init(3, 5)
    afficher(POINT2)
    print "distance : ", calculer_distance(POINT1, POINT2)
