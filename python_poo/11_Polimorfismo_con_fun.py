#Polimorfismo Funciones 

class Tomate:
  def tipo(self):
    print("vegetal")
  
  def color(self):
    print('rojo')

class Manzana:
  def tipo(self):
    print('fruta')
  
  def color(self):
    print('verde')

def funcion(ob):
  ob.tipo()
  ob.color()

nuevo = Tomate()
funcion(nuevo)

nuevo1 = Manzana()
funcion(nuevo1)
