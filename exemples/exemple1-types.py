"""
 modul doc
"""

print locals()

def moyenne(liste):
    """ calculer la moyenne """
    print ( locals())
    print ( globals())
    return  sum(liste)/len(liste)

print (" python")
import math

print(math.pi)

print( __doc__)
moyenne([1])
