from inheritClass import *

objectCar = Car("Grey","VolksWagen")
objectBike = Bike("Red","Honda Active")

objectCar.drive()
objectCar.drive()
objectCar.drive()
objectCar.drive()
objectCar.drive() # it preserve the state of variable of the object

objectCar.music()
objectCar.window()
objectBike.helmet()

objectEC=ElectricCar("Black", "Tesla")

objectEC.drive()
print(f'The Electic Car class can still access the variable gas {objectEC.gas}')

