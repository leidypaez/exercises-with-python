class Week:
  def __init__(self):
    self.lunes = 1
    self.martes = 2
    self.miercoles = 3
    self.jueves = 4
    self.viernes = 5
    self.sabado = 6
    self.domingo = 7
  
  def days(self):
    number_day = int(input("Hola: digita un numero del 1 al 7 para conocer el dia de la semana"))
    if number_day == 1:
      print("El numero que pusiste corresponde a LUNES")
    elif number_day == 2:
      print("El numero que pusiste corresponde a MARTES")
    elif number_day == 3:
      print("El numero que pusiste corresponde a MIERCOLES")
    elif number_day == 4:
      print("El numero que pusiste corresponde a JUEVES")
    elif number_day == 5:
      print("El numero que pusiste corresponde a VIERNES")
    elif number_day == 6:
      print("El numero que pusiste corresponde a SABADO")
    elif number_day == 7:
      print("El numero que pusiste corresponde a DOMIGO")
    else: 
      print("A ocurrido un error: solo puedes digitar los numeros indicados")

day_of_week = Week()
day_of_week.days()