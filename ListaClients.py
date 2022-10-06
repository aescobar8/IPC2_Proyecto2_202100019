from nodo import Nodo

class ListClientes:
    def __init__(self):
        self.frente = None
        self.final = None

    def addCliente(self, dato):
        valor1 = Nodo(dato)
        valor1.next = None
        if self.frente	== None:
            self.final = valor1
        else:
            self.final.next = valor1
        self.final = valor1

    def ShowData(self, valor2):
        valor2 = self.frente
        while valor2 != None:
            print(valor2.dato)
            valor2 = valor2.sig

    def DeleteData(self):
        if self.vacia():
            print("Esta vacia")
        else:
            self.frente = self.frente.sig
            if self.frente == None:
                self.final = None
    
    def empty(self):
        return self.frente == None