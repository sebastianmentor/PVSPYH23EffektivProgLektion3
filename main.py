from faker import Faker
from typing import Callable
from collections import abc

class player:
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age

    
    def __str__(self) -> str:
        return f"Spelare {self.name} är ålder {self.age}"



fake = Faker()

list_of_players = []
# for _ in range(100_000_000_000_000_000):
#     list_of_players.append(player(fake.name(), fake.random_int(min=18, max=99)))


def get_oldest_player(list_of_players:list[player]) -> player|None:
    if not list_of_players: return None

    oldest = list_of_players[0]

    for player in list_of_players:
        if oldest.age < player.age:
            oldest = player

    return oldest



def get_youngest_player(list_of_players:list[player]) -> player|None:
    if not list_of_players: return None

    youngest = list_of_players[0]

    for player in list_of_players:
        if youngest.age > player.age:
            youngest = player

    return youngest


def get_oldest_and_youngest_player(list_of_players:list[player]) -> player|None:

    if not list_of_players: return None, None

    oldest = list_of_players[0]
    youngest = list_of_players[0]

    for player in list_of_players:

        if oldest.age < player.age:
            oldest = player

        if youngest.age > player.age:
            youngest = player

    return oldest, youngest


def calculate_total_sum(*args) -> None:
    total_sum = 0
    print(type(args), args)
    for number in args:
        total_sum += number
    
    print(total_sum)


def greet_me(**kwargs) -> None:
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# greet_me(name1 = "Sebastian", name2 = "Kalle")

def run_func(func:abc.Callable, **kwargs):
    return func(**kwargs)


# run_func(greet_me, key = "value")
# skriv_ut_på_skärmen = print
# skriv_ut_på_skärmen('Hejsan 123')

import time

def tidtagning(funktion):
    def wrapper(*args, **kwargs):
        start = time.time()
        resultat = funktion(*args, **kwargs)
        slut = time.time()
        print(f"Funktionen {funktion.__name__} tog {slut - start:.4f} sekunder. args={args}")
        return resultat
    return wrapper

def print_decorator_true(func:abc.Callable):
    def wrapper():
        print("Start function", func)
        value = func()
        print("Ending it all")
        return value
    return wrapper

@print_decorator_true
def calculate_salary():
    print('Start calculating salary....')
    # beräkning...
    return 100

def calculate_what_ever():
    # beräkning
    print('Calculating a lot of shit!!')
    x = 200
    print('Done calculating')
    return x

def dummy_func(func):
    def dum(): return True
    def wrapper():
        return dum()

    return wrapper

@dummy_func
def some_func():
    print('Hello from some_func')

def print_decorator(func:abc.Callable):
    print("Start function", func)
    func()
    print("Ending it all")

# print(some_func())

# salary = calculate_salary()
# print(salary)
# salary = print_decorator(calculate_salary)
# whatever = print_decorator(calculate_what_ever)

# base ** exponent -> base = 4, exponent = 2 == 4^2 
def generate_power_func(exponent:int) -> abc.Callable:
    def power(base):
        return base ** exponent
    return power

def pure_to_the_power_of_4(base):
    return base ** 4

to_the_power_of_4 = generate_power_func(4)
# print(to_the_power_of_4)
# print(to_the_power_of_4(2))
square_func = generate_power_func(2) # base^2
cube_func = generate_power_func(3)# base^3

# calculate_total_sum(1,2,3,12,3,3,3,1,2,3,3,4,23,4,1234,12,34)

# print(get_oldest_player(list_of_players=list_of_players))
# print(get_youngest_player(list_of_players=list_of_players))
# oldest, youngest = get_oldest_and_youngest_player(list_of_players=list_of_players)
# print(oldest, youngest)
 
# 0, 1, 1, 2, 3, 5, 8, 13, ...
from functools import cache

@cache
def fib(n):
    match n:
        case 1: return 0
        case 2: return 1
        case _: return fib(n-2) + fib(n-1)

#  print(fib(1000))


def log_function_call (func):
    def wrapper ():
        print(f"Funktionen {func.__name__} körs.")
        return func ()
    return wrapper

@log_function_call
def say_hello ():
    print("Hej!")

# say_hello ()

def log_function_call_counter(func):
    counter = 0
    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1 
        print(f"Funktionen {func.__name__} körs och har körts {counter} och args{args}.")
        return func (*args, **kwargs)
    return wrapper

# @log_function_call_counter
def fib_v2(n):
    match n:
        case 1: return 0
        case 2: return 1
        case _: return fib_v2(n-2) + fib_v2(n-1)

# print(fib_v2(15))


def first_decorator (func ):
    def wrapper ():
        print("Första dekoratorn")
        return func ()
    return wrapper
def second_decorator (func ):
    def wrapper ():
        print("Andra dekoratorn")
        return func ()
    return wrapper

@first_decorator
@second_decorator
def say_hello ():
    print("Hej!")   

# say_hello ()


sträng1 = "((434((2(442(32(3(5(23(5))))))))))"
# sträng2 = "())())((()))()"

def control_parent(sträng:str):
    stack = []
    for p in sträng:
        if p == '(':
            stack.append('(')
        elif p == ')':
            stack.pop(-1)
    
    return False if stack else True

# print(control_parent(sträng1))
# print(control_parent(sträng2))


from functools import lru_cache

@tidtagning
@lru_cache(3)
def fib_v3(n):
    match n:
        case 1: return 0
        case 2: return 1
        case _: return fib_v3(n-2) + fib_v3(n-1)

# print(fib_v2(35))
print(fib_v3(40))