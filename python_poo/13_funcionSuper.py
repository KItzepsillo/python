# Funcion super
# Se utiliza para llamar metodos definidos 

class Mamifero:
  def __init__(self,nombre):
    print(nombre,' es una animal caliente')

class Leon(Mamifero):
  def __init__(self):
    print('El leon tiene cuatro patas')
    super().__init__('Simba')
    #Mamifero.__init__(self,'Tigre')

nuevo = Leon()
