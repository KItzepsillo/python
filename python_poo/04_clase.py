class Persona:
  #atributos
  pass
  #construcctor
  def __init__(self,nombre, edad):
    #atributos
    self.nombre = nombre
    self.edad = edad
  #metodo
  
  def descripcion(self):
    return '{} tiene {}'.format(self.nombre,self.edad)

  def comentario(self, frase):
    return ' {} dice {} '.format(self.nombre,frase)

mecanico = Persona('Juan',26)
#print(mecanico.descripcion())
#print(mecanico.comentario('como estas '))

## MODIFICAR UN ATRIBUTO

class Email:
  def __init__(self):
    self.enviado = False
  
  def enviarCorreo(self):
    self.enviado = True

mi_correo = Email()
print(mi_correo.enviado)
mi_correo.enviarCorreo()
print(mi_correo.enviado)