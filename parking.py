
class Parking():
    def __init__(self,jed_br_parkinga,grad,ulica,zona,broj_mjesta):
        self.jed_br_parkinga=jed_br_parkinga
        self.grad=grad
        self.ulica=ulica
        self.zona=zona
        self.br_mjesta=broj_mjesta
    def __str__(self):
        return "Parking "+str(self.jed_br_parkinga)+" u gradu: "+self.grad+",ulica: "+self.ulica+" je "+str(self.zona)+" zona i ima "+str(self.br_mjesta)+" mjesta."


