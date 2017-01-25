class Etudiant(object):
    def __init__(self, name, note):
        self.note = note
        self.name = name
    def __cmp__(self, other):
        #print cmp(self.note, other.note),self.note,other.note
        return cmp(self.note,other.note)

    def __str__(self):
        return "Etudiant({0},{1})".format(self.note, self.name)

    def __repr__(self):
        return str(self)

    def __radd__(self, total):
        return self.note + total

if __name__ == "__main__":
    etudiants = []
    for i in range(4):
        etudiants.append(Etudiant("name"+str(i),i) )
    etudiants.append(Etudiant("-1 name",-1))
    print etudiants
    print "etudiant ayant la meileure note", max( etudiants )
    print "etudiant ayant la mauvaise note", min(etudiants)
    print "la note moyenne =", float(sum(etudiants)) / len(etudiants)
    etudiants.sort()
    print etudiants
    etudiants.reverse()
    print etudiants




    #liste = [ Etudiant("name"+str(i),-i) for i in range(4)]
    #print "liste non triee",liste
    #liste.sort()
    #print "liste triee",etudiants


