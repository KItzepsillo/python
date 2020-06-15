class Pastel:
  def __init__(self,ingredientes):
    self.ingredientes = ingredientes
  
  def __repr__(self):
    return f'pastel({self.ingredientes !r})'
  
  @classmethod
  def Pastel_chocolate(cls):
    return cls(['Harina','Leche','Chocolate'])
  
  @classmethod
  def Pastel_vainilla(cls):
    return cls(['Harina','Leche','Vainilla'])


print(Pastel.Pastel_chocolate())

import  math

class Pastel1:
  def __init__(self,ingredientes,tamano):
    self.ingredientes = ingredientes
    self.tamano = tamano

  def __repr__(self):
    return (f'Pastel({self.ingredientes},'f'{self.tamano})')
  
  def area(self):
    return self.tamano_area(self.tamano)
  
  @staticmethod
  def tamano_area(A):
    return A**2*math.pi

nuevo_pastel = Pastel1(['Harina','Azucar','Crema'],4)
print(nuevo_pastel.tamano_area(10))