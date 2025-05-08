'''
Decorator with Arguments
def my_decorator(func):
    def wrapper(name):
        print('before running function')
        func(name)
        print('after running function')
    return wrapper

@my_decorator
def hello(name):
    print(f'hello {name}')

hello("vignesh")
'''



def my_decorator(func):
    def wrapper(n):
        result = func(n)
        return result *10
    return wrapper

@my_decorator
def add_five(n):
    return n + 5 

print(add_five(6))