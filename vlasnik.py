
class Vlasnik():
    def __init__(self,ime,prezime,pol,jmbg):
        self.ime=ime
        self.prezime=prezime
        self.pol=pol
        self.jmbg=jmbg
    def __str__(self):
        return "Vlasnik "+self.ime+" "+self.prezime+", jmbg: "+str(self.jmbg)
