class Telefono:
  def __init__(self):
    pass

  def llamar(self):
    print('Llamando...')
  
  def ocupado(self):
    print('Ocupado')

class Camara:
  def __init__(self):
    pass

  def fotografia(self):
    print('tomando fotos...')

class Reproduccion:
  def __init__(self):
    pass

  def reproduccion(self):
    print('reproduciendo musica')
  def reproduccionvideo(self):
    print('reproduciendo video')

class smartphone(Telefono,Camara,Reproduccion):
  def __del__(self):
    print('telefonoo apagado')

movil = smartphone()
#print(dir(movil))
print(movil.reproduccion())