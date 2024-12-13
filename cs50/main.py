import random
import math

name =" Djomy LalaLaO "


class User:
    def __meta__(self):
        return type(self)

    def __init__(self, first_name, last_name, age = 0):
        self.first_name = first_name
        self.last_name = last_name

        try:
            self.age = int(age)
        except ValueError:
            self.age = 0

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old"
    
    def __repr__(self):
        return f"{self.first_name} ({self.age})"

    def say_hello(self):
        print(f"hello.........{self.first_name.strip().title()}")

    def run(self, steps=10):
        for i in range(steps):
            print(f"{self.first_name} is running")


def main():
    user = User("Oury", "Diallo")

    while user.age is None:
        try:
            x = int(input("Enter a number: "))
            print(f"x is {x}")
        except ValueError:
            print("Invalid input")
        else:
            user.age = x
    
    user.say_hello()
    print(user)
    print(random.choice(10))
    math.acosh(user.age)
    # user.run(3)

main()