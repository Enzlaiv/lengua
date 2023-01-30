
class carro:
    def numRuedas(self):
        print(" el numero de ruedas del vehiculo es 4")

class mototaxi:
    def numRuedas(self):
        print(" el numero de ruedas del vehiculo es 3")

class bote:
    def numRuedas(self):
        print(" el numero de ruedas del trasporte es 0")

def ruedasVehiculo(vehiculo):
    vehiculo.numRuedas()

vehiculo=mototaxi()

ruedasVehiculo(vehiculo)

