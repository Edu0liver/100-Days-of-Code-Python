import tkinter
import turtle

window = tkinter.Tk()
window.title("My first GUI program!")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

tim = turtle.Turtle()
tim.write("Hello")

# window.mainloop()

def add(*args):
    total = 0
    for n in args:
        total += n
    return total

print(add(3, 5, 6, 7))

def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)

calculate(add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT-R")

print(my_car.model)
