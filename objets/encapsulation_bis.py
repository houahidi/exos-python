""" Demo encapsulation"""

class MaClasse(object):
    """MaClasse"""
    def __init__(self, param):
        self.__attribut = param

    def __str__(self):
        return "Maclasse({0})".format(self.__attribut)

    @property
    def attribut(self):
        return self.__attribut

    @attribut.setter
    def attribut(self, value):
        self.__attribut = value



if __name__ == "__main__":
    INST1 = MaClasse("valeur")
    print INST1
    INST1.attribut = "new Value"
    print INST1
    print INST1.attribut