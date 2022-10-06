from nodo import Nodo
class ListCompany:
    def __init__(self):
        self.frente = None
        self.final = None

    def AddCompany(self, dato):
        valor1 = Nodo(dato)
        valor1.sig = None
        if self.final == None:
            self.frente = valor1
        else:
            self.final.sig = valor1
        self.final = valor1

    def ShowData(self):
        valor2 = self.frente
        while valor2 != None:
            print(valor2.dato.name)
            valor2 = valor2.sig

    def ReturnData(self):
        data = []
        valor3 = self.frente
        while valor3 != None:
            data.append(valor3.dato.name)
            valor3 = valor3.sig
        return data

    def DeleteData(self):
        if self.vacia():
            print("Esta vacia")
        else:
            self.frente = self.frente.sig
            if self.frente == None:
                self.final = None
    
    def empty(self):
        return self.frente == None