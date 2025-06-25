import random
def add_one(n):
    pass

def power(base, exponent):
    #solve with iteration
    for _ in range(exponent):
        result *= base
    return result

def say_something(name):
    greetings = ['Hello', 'Nice to meet you!', 'How are you']
    greeting = random.choice(greetings)

    return f"{greeting} {name}"