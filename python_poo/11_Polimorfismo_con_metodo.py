#Polimorfismo con metodo

# Se utiliza con mas de dos metodos 

class Guatemala:
  def capital(self):
    print('Guatemala')
  def idioma(self):
    print('Espanol')

class Alemania:
  def capital(self):
    print('Berlin')
  def idioma(self):
    print('Aleman')

guatemala = Guatemala()
aleman = Alemania()

for pais in (guatemala,aleman):
  pais.capital()
  pais.idioma()