
class Automobil():
    def __init__(self,marka,model,br_sjedista,boja,reg_oznake):
        self.marka=marka
        self.model=model
        self.br_sjedista=br_sjedista
        self.boja=boja
        self.reg_oznake=reg_oznake

    def __str__(self):
        return "Automobil "+self.marka+" "+self.model+" registarskih oznaka: "+self.reg_oznake+" "+self.boja+" boja ima "+str(self.br_sjedista)+" sjedista"