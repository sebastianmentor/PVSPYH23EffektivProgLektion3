def log_function_call(func):
    def wrapper():
        print(f"Funktionen {func.__name__} körs.")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hej!")

say_hello()


def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Funktionen {func.__name__} körs med argumenten: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def add(x, y):
    return x + y

result = add(3, 5)
print(result)



def first_decorator(func):
    def wrapper():
        print("Första dekoratorn")
        return func()
    return wrapper

def second_decorator(func):
    def wrapper():
        print("Andra dekoratorn")
        return func()
    return wrapper

@first_decorator
@second_decorator
def say_hello():
    print("Hej!")

say_hello()