#format %

dato = 'curso'
print('tutoriales %s'%dato)

nombre = 'victor'
edad = 25
print('Hola soy %s y tengo %s'%(nombre,edad))

#str.format
print('que tal soy {} y mi edad es {}'.format(nombre,edad))

#f-string
print(f"hola soy {nombre} y mi edad es {edad} blabla")


class Estudiante:
  def __init__(self,nombre,apellido,edad):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
  
  def __str__(self):
    return f"Hola que tal soy {self.nombre} {self.apellido} {self.edad}"

nuevo_estudiante = Estudiante('Juan','Lopez',17)
print(f"{nuevo_estudiante}")