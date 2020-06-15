#Encapsulacion

class Cliente:
  def __init__(self):
    self.__codigo = 1234

  def __cuenta(self):
    print('cuenta de procesamiento')
  
  def getcodigo(self):
    return self.__codigo

persona = Cliente()
#objeto._nombredelaclase_nombre atribujo
print(persona._Cliente__codigo)
print(persona.getcodigo())
print(persona._Cliente__cuenta())
