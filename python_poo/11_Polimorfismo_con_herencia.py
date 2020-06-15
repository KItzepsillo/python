#Polimorfismo con herencia

class Aves:
  def volar(self):
    print('Puede volar la mayoria')

class Aguila(Aves):
  def volar(self):
    print('Las aguilas pueden volar')

class Gallina(Aves):
  def volar(self):
    print('La gallina no puede volar')


ob_ave = Aves()
aguila = Aguila()
gallina = Gallina()

ob_ave.volar()
aguila.volar()
gallina.volar()