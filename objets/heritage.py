

class Mere1 :
    def __init__(self , param):
        self.attribut1 = param
    def methode1(self):
        print "mere1" , self.attribut1

class Mere2 :
    def __init__(self , param):
        self.attribut1 = param
    def methode1(self):
        print "mere2", self.attribut1

class Fille(Mere1, Mere2):
    def __init__(self, param1,param2):
        Mere1.__init__(self, param1)
        self.attribut2 = param2
    def methode2(self):
        print self.attribut2
    def methode1(self):
        Mere2.methode1(self)

F1 = Fille("val1","val2")
F1.methode1()
F1.methode2()
