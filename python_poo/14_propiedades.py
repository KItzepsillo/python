#Propiedades
class Empleado:
  def __init__(self,nombre,salario):
    self.__nombre = nombre
    self.__salario = salario
  
  def __getnombre(self):
    return self.__nombre
  
  def __getsalario(self):
    return self.__salario
  
  #Modificar
  def __setnombre(self, nombre):
    self.__nombre = nombre
  
  def __setsalario(self, salario):
    self.__salario = salario
  
  #Eliminacion
  def __delnombre(self):
    del self.__nombre
  
  def __delsalario(self):
    del self.__salario

  nombre = property(
    fget = __getnombre,
    fset = __setnombre,
    fdel = __delnombre,
    doc = "Propiedad del 'nombre'"
  )
  
  salario = property(
    fget = __getsalario
  )

empleado2 = Empleado('Victor',3000)
empleado2.nombre = "Peter"
print(empleado2.nombre,empleado2.salario)
help(empleado2)
  #fget -> obtener
  #fset -> establecer
  #fdel -> eliminar 


"""
empleado1 = Empleado('Victor',2000)
print(empleado1.getnombre(),',',empleado1.getsalario())
empleado1.setnombre('Juan')
print(empleado1.getnombre(),',',empleado1.getsalario())
"""