class Jeans:
    def __init__(self, waist, len, color):
        self.waist=waist
        self.len=len
        self.color=color
        self.wearing=False

    def put_on(self):
        print(f'Putting on {self.waist} x {self.len} {self.color} jeans')
        self.wearing=True
    
    def take_off(self):
        print(f'Taking off {self.waist} x {self.len} {self.color} jeans')
        self.wearing=False