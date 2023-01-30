class animal():
    def nombreIngresado(self,nom):
        self.nom=nom

    def obtener (self):
        return self.nom

a=animal()

a.nombreIngresado("\n ----> perro \n")
print(a.obtener())