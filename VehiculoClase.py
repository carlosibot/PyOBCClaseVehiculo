class vehiculo:
    color = "Rojo"
    ruedas = 4
    puertas = 2

class coche(vehiculo):
    velocidad = 180.80
    cilindrada = 6

Coche = coche()
print("Cilindrada del coche: ",Coche.cilindrada)
print("Velocidad del coche: ",Coche.velocidad)
print("Color del coche: ",Coche.color)
print("Numero de ruedas del coche: ",Coche.ruedas)
print("Numero de puertas del coche: ",Coche.puertas)