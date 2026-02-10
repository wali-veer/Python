class ElecticalError(Exception):
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem

    def __str__(self):
        return f'The {self.device} is {self.problem}'
    
class PlumbingError(Exception):
    def __init__(self, device, problem):
        self.device=device
        self.problem = problem

    def __str__(self):
        return f'The {self.device} is {self.problem}'
    
def cause_an_error(error_type):
    if error_type == 'elecrical':
        raise ElecticalError('Iron', 'Overload')
    elif error_type == 'plumbing':
        raise PlumbingError('Toilet', 'Leakage')
    else:
        raise Exception('A generic household problem')

try:
    cause_an_error('Yard')
except ElecticalError as e:
    print(e)
    print('I can fix it, dont worry')
except PlumbingError as e:
    print(e)
    print('You need to call Plumber')
except Exception as e:
    print(e)