"""
        puto el que lo lea    

"""
from arbol import Arbol

arbol = Arbol("Ruisec")

arbol.agregar("Anubis")
arbol.agregar("FreeMan")
arbol.agregar("IronSage")
arbol.agregar("Macii owo")
arbol.agregar("BlackShell")
arbol.agregar("Papa Rellena")

nombre = input("Ingresa algo para agregar al arbol: ")

arbol.agregar(nombre)
arbol.preorden()
arbol.inorden()
arbol.postorden()

                      # Busqueda

busqueda = input("Busca algo en el arbol: ")
nodo     = arbol.buscar(busqueda)

if nodo is None:
    print(f"{busqueda} no existe")
else:
    print(f"{busqueda} si existe")
    # Aqui tienes en "nodo" toda la informacion del nodo
    # tanto su izquierda, derecha y otros atritibutos que le hayas agregado 

arbol_numeros = Arbol(5)
arbol_numeros.agregar(1984)
arbol_numeros.agregar(60)
arbol_numeros.agregar(10)
arbol_numeros.agregar(20)
arbol_numeros.agregar(10)
arbol_numeros.agregar(25)
arbol_numeros.agregar(59)
arbol_numeros.agregar(64)
arbol_numeros.agregar(10)
arbol_numeros.agregar(19)
arbol_numeros.agregar(23)
arbol_numeros.agregar(18)
arbol_numeros.agregar(1)
arbol_numeros.agregar(2013)
arbol_numeros.preorden()
arbol_numeros.inorden()
arbol_numeros.postorden()

busqueda = int(input("Ingresa un numero para buscar en el arbol: "))
n = arbol_numeros.buscar(busqueda)

if n is None:
    print(f"{busqueda} no existe")
else:
    print(f"{busqueda} si existe")