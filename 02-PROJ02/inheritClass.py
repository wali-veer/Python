class Vehicle:
    def __init__(self, color, company):
        self.color=color
        self.company=company
        self.gas = 4 #full tank

    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print(f'The {self.color} {self.company} goes on a long drive')
        else:
            print(f'The {self.color} {self.company} is out of fuel')
    
class Car(Vehicle):
    def music(self):
        print("Music has started and its playing bollywood")
    
    def window(self):
        print("Ahhh... cool and fresh air is in")

class Bike(Vehicle):
    def helmet(self):
        print("Helmet is for safty and I wear it")

class ElectricCar(Car):
    def drive(self):
        print(f"The {self.color} by {self.company} goes without noise...ssshhhh")