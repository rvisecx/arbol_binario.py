class Nodo:
    def __init__(self, dato):
                               # "dato" puede ser de cualquier tipo, incluso un objeto
                               # si se sobreescriben los operadores de comparacion 
        self.dato      = dato
        self.izquierda = None
        self.derecha   = None