class CircuitBreaker:
    def __init__(self, maxLimit):
        self.capacity=maxLimit
        self.load=0
    
    def connect(self, amps):
        if self.load + amps > self.capacity:
            raise Exception("There is going to be too much load")
        elif self.load + amps < 0:
            raise Exception("Connection will cause negative amps")
        else:
            self.load += amps
            print(f'The load is {self.load}')

