class aracnidos:
    def numPatas(self):
        print(" el numero de patas es de 8")

class crustaceos:
    def numPatas(self):
        print(" el numero de patas es de 10")

class miriapodos:
    def numPatas(self):
        print(" el numero de patas es más de 10 ")

def PatasTotales(servivo):
    servivo.numPatas()

servivo=crustaceos()

PatasTotales(servivo)
