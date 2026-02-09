# https://www.python.org/dev/peps/pep-0318/

def my_decorator(my_target_function):
    def fun_wrapper():
        return "This is a decoration done by wrapper of my_decorator due to call from ==> " + my_target_function()
    return fun_wrapper

@my_decorator
def my_target_function():
    return "this is from target"

print(my_target_function()) #This is a decoration done by wrapper of my_decorator due to call from ==> this is from target



print("\n\n")
