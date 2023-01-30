
class raza():
    def __init__(self, animal, domestico, salvaje):
        self.animal=animal
        self.domestico=domestico
        self.salvaje=salvaje
    
    def caracter(self):

        print("el nombre del animal es : ", self.animal,"\n es domestico? ", self.domestico, "\n es salvaje? ", self.salvaje)


class tigre(raza):
    pass

ser=tigre("tigre", "no", "si")
ser.caracter()

