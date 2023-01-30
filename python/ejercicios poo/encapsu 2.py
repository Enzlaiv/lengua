class ahorros:
    def __init__(self):
        self.__dinero=100

    def __usuario(self):
        print("usuario activo")
    
    def getdinero(self):
        return self.__dinero

persona=ahorros()
print(f"su dinero actual es ", persona._ahorros__dinero, "soles \n")
 
 #objeto,_clase,__def
 
persona._ahorros__usuario()