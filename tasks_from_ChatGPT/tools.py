import random

def random_greeting():
    greetings = ["Hello", "Hi", "Welcome", "Good day", "Hey"]
    return random.choice(greetings)

print(random_greeting())
