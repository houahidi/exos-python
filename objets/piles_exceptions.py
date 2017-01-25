"""Exemple Pile"""

class PilePleineException(Exception):
    def __init__(self, message="Erreur : Pile pleine"):
        Exception.__init__(self,message)
    def __str__(self):
        return "PilePleine(message:{0})".format(self.args)

class Pile(object):
    """Pile de type FILO"""
    def __init__(self, taille=10):
        self.__elements = []
        self.__taille = taille

    @property
    def taille(self):
        return self.__taille

    def depiler(self):
        if len(self.__elements) > 0:
            return self.__elements.pop(-1)
        else:
            print "Pile vide"

    def __str__(self):
        return "Pile(taille:{0}, nombre:{1})".format(self.__taille, len(self))
    def __len__(self):
        return len(self.__elements)

    def empiler(self, elem):
        if len(self.__elements) < self.__taille:
            self.__elements.append(elem)
        else: # lever l'exception
            raise PilePleineException("Erreur : Pile pleine taille {0} depasse".format(self.taille))


if __name__ == "__main__":
    TAILLE = int(raw_input("Veuillez saisir la taille :"))
    PILE1 = Pile(TAILLE)
    while True:
        print PILE1
        CHOIX = raw_input("Veuillez saisir 1 : Empiler | 2 empiler | Quitter :")
        if CHOIX == "1":
            ELEM = raw_input("Element a empiler :")
            try: # traiter l'exception
                PILE1.empiler(ELEM)
            except PilePleineException as e:
                print e
        elif CHOIX == "2":
            print "Element depile :", PILE1.depiler()
        else:
            break