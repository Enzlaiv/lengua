class nombre:

    def __init__(self, nom):
        self.nom=nom
    
    def imprimir(self):
        print(f"\nmi nombre es : " , self.nom, "\n")

a=nombre("daniel")
a.imprimir()
