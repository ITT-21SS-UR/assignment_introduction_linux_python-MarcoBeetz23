#!/usr/bin/python3

import turtle
import sys


print("Skala von 1 bis 10...wie groß willste den Kreis haben? ;-)")

if len(sys.argv) > 1:
    size = sys.argv[1]
else: 
    size = input("Ich will Größe: ")

print(size)

size = float(size)

scaled_size = size*0.2

window = turtle.Screen()
t = turtle.Turtle()
t.speed(0)


t.color("red")
t.pensize(5)

for i in range(1000):
    t.forward(scaled_size)
    t.left(1.15)




