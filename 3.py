class libro():
    def _init_(self):
        self.libros = {} #diccionario vacio
    def add(self):
        insert = True
        while insert:
            nombre = input("Ingresar nombre: ")    
            autor = input("Ingrese autor: ")
            self.libros[nombre] = autor # Agrega el elemento al diccionario
            print()
            if (input("Registrar otro libro? S/N: ")).lower() == "n":
                insert = False

    def mostrar(self):
        print()
        for nombre, autor in self.libros.items(): # .items() funciona en Python 3.x
            print("----")
            print("Nombre: {} - Autor: {}".format(nombre, autor))

obj = libro()
obj.add()
obj.mostrar()