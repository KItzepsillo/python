#Herencia
class Pokemon:
  def __init__(self,nombre,tipo):
    self.nombre = nombre
    self.tipo = tipo
  
  def descripcion(self):
    return '{} es un pokemon de tipo {}'.format(self.nombre,self.tipo)

class pikachu (Pokemon):
  def ataque(self,tipoataque):
    return '{} tipo de ataque: {}'.format(self.nombre, tipoataque)

class charmander (Pokemon):
  def ataque(self,tipoataque):
    return '{} tipo de ataque: {}'.format(self.nombre, tipoataque)

nuevoPokemon = pikachu('Juan','electrico')
print(nuevoPokemon.descripcion())
print(nuevoPokemon.ataque('tira pedos'))