class Auto:
  rueda = 4
  def desplazamiento(self):
    print('Se esta moviendo el carro')

class Moto:
  rueda = 2
  def desplazamiento(self):
    print('Se esta moviendo la moto')

#####
class Animales:
  def __init__(self,nombre):
    self.nombre = nombre
  
  def tipo_animal(self):
    pass

class Leon(Animales):
  def tipo_animal(self):
    print('Animal salvaje')

class Perro(Animales):
  def tipo_animal(self):
    print('animal domestico')

nuevo_animal = Leon('Simba')
nuevo_animal.tipo_animal()

nuevo_animal1 = Perro('Husky')
nuevo_animal.tipo_animal()