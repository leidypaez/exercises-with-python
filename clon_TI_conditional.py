class Segip:
  def __init__(self):
    self.persons = {"Jose": 51764525, "Miguel": 25463784, "Andy": 12345678}
    self.name = input("Ingresa el nombre de la persona a agregar: ")
    self.ci = int(input("Ingresa el documento de la persona a agregar: "))

  def add_person(self):
    if self.ci in self.persons.values():
      print("El carnet es un duplicado, digite el numero de nuevo correctamente")
    else:
      print(self.persons.update({self.name: self.ci}))

result_add_person = Segip()
result_add_person.add_person()
print(result_add_person.persons)

segip = Segip()

segip.add_person("Andy", 12345678)
## No debe agregar a sofia ya que es duplicado
segip.add_person("Sofia", 12345678)