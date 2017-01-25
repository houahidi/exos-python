
class Compte(object):
    def __init__(self, numero):
        self.__numero = numero
        self.__solde = 0

    def crediter(self, somme):
        self.__solde += somme

    def debiter(self, somme):
        self.__solde -= somme

    @property
    def numero(self):
        return self.__numero

    @property
    def solde(self):
        return self.__solde

    def __str__(self):
        return "Compte(numero = {0}, solde = {1})".format(self.__numero, self.__solde)

class CompteEpargne(Compte):
    """Compte Epargne"""
    def __init__(self, numero, taux):
        Compte.__init__(self, numero)
        self.__taux = taux

    def afficher(self):
        return "CompteEpargne(taux: {0})".format(self.__taux) + \
               Compte.afficher(self)


if __name__ == "__main__":
    COMPTE1 = CompteEpargne(1, 2.9)
    print COMPTE1
    COMPTE1.crediter(100)
    print COMPTE1
    COMPTE1.debiter(30)
    print COMPTE1
