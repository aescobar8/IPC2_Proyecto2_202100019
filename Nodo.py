class Node:
    def __init__(self, dato, next = None):
        self.dato = dato
        self.next = next

class NodeLD:
    def __init__(self, dato, next = None, anterior = None):
        self.dato = dato
        self.next = next
        self.anterior = anterior