
from nodo import NodoLD

class ListaDP:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def add(self, dato):
        valor1 = NodoLD(dato)
        if self.primero == None:
            self.primero = valor1
            self.ultimo = self.primero
        else:
            valor1.anterior = self.ultimo
            valor1.next = self.ultimo.next
            self.ultimo.next = valor1
            self.ultimo = valor1

    def ShowData(self):
        valor2 = self.primero
        while valor2 != None:
            print(valor2.dato.clients.final.dato.nombre)
            valor2 = valor2.next

    def DeleteData(self):
        pos = self.primero
        if self.primero == None:
            self.primero = pos.next
            self.ultimo = pos.anterior
        else:
            self.ultimo.next = pos.anterior
            self.primero.next = pos.next
        self.ultimo = None
        self.primero = None
        pos = self.primero