""" Demo encapsulation"""

class MaClasse(object):
    """MaClasse"""
    def __init__(self, param):
        self.attribut = param

    def __str__(self):
        return "Maclasse({0})".format(self.__attribut)

    def set_attribut(self, value):
        self.attribut = value

    def get_attribut(self):
        return self.attribut

    attribut = property(get_attribut, set_attribut,None, "Attribut publique")

if __name__ == "__main__":
    INST1 = MaClasse("valeur")
    print INST1
    INST1.attribut = "new Value"
    print INST1
    print INST1.attribut
    INST1.set_attribut("set new value")
    print INST1