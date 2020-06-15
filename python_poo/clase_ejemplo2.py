class Jugadores:
  # Atributos
  j1 = 'Juan'
  j2 = 'Mateo'

#print(Jugadores.j1)

class Jugador_A:
  j1 = 'Juan2'
  j2 = 'Mateo2'

#print(Jugador_A.j1)

class Nombre:
  pass

victor = Nombre()
maria = Nombre()

#Objeto.atributo = valor

victor.edad = 30
victor.sexo = 'M'
victor.pais = 'Guatemala'

maria.edad = 45
maria.sexo = 'F'
maria.pais = 'Italia'

print(victor.edad)
print(maria.edad)
