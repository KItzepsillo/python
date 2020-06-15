class Matematica:
  def suma(self):
    self.n1 = 3
    self.n2 = 4

s = Matematica()
s.suma()
#print(s.n1+s.n2)

class Ropa:
  #Constructor
  def __init__(self):
    self.marca = 'Lapiz'
    self.talla = 'M'
    self.color = 'azul'

camisa = Ropa()
#print(camisa.color)
#print(camisa.marca)

class Calculadora:
  def __init__(self,n1,n2):
    self.suma = n1 + n2
    self.resta = n1 - n2
    self.producto = n1 * n2
    self.division = n1 / n2

operacion = Calculadora(4,5)
print(operacion.producto)