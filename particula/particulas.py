from .particula import Particula
from .algoritmos import distancia_euclidiana
import json

class Particulas:
    def __init__(self):
        self.__particulas = []
    
    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__particulas
        ) 

    def __len__(self):
        return len(self.__particulas)

    def __iter__(self):
        self.cont = 0
        
        return self
    
    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                print(lista)
                json.dump(lista, archivo, indent = 5)
            return 1
        except:
            return 0

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0       

# p01 = Particula(id= 1, origen_x= 7, origen_y= 4, destino_x= 5, destino_y= 1, velocidad= 100, red= 50, green= 75, blue= 100, distancia= distancia_euclidiana)
# p02 = Particula(id= 2, origen_x= 500, origen_y= 200, destino_x= 500, destino_y= 200, velocidad= 100, red= 50, green= 75, blue= 100, distancia= distancia_euclidiana)
# particulas = Particulas()
# particulas.agregar_final(p01)
# particulas.agregar_inicio(p02)
# particulas.agregar_inicio(p01)
# particulas.mostrar()

