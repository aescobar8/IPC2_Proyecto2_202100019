from nodo import Nodo
class Puntos:
    def __init__(self):
        self.primero = None

    def add(self, dato):
        valor1 = Nodo(dato)
        if self.primero == None:
            self.primero = valor1
        else:
            valor1.next = self.primero.next
            self.primero.next = valor1
            
    def ShowData(self):
        valor2 = self.primero
        while valor2 != None:
            print(valor2.dato.name)
            valor2 = valor2.next

    def DeleteData(self):
        pos = self.primero
        if self.primero == None:
            self.primero = pos.next
        else:
            self.primero.next = pos.next
        self.primero = None
        pos = self.primero