class raza():
    def __init__(self, animal, domestico, salvaje):
        self.animal=animal
        self.domestico=domestico
        self.salvaje=salvaje
    
    def caracter(self):

        print("el nombre del animal es : ", self.animal,"\n es domestico? ", self.domestico, "\n es salvaje? ", self.salvaje)


class tigre(raza):
    Gafilidas=""
    def garras(self):
        self.Gafilidas="es peligroso domesticar a un tigre"
    
    def caracter(self):

        print("el nombre del animal es : ", self.animal,"\n es domestico? ", self.domestico, "\n es salvaje? ", self.salvaje, "\n", self.Gafilidas)
    
class perro(raza):
    pass

ser=tigre("tigre", "no", "si")
ser.garras()

ser.caracter()



ser=perro("perro", "si", "no")
ser.caracter()
