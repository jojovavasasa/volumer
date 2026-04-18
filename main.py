import math
import time

unit = input("Welke eenheid ga je gebruiken? ")
shape = input("Welke vorm wil je berekenen?\n(A): Piramide\n(B): Balk\n(C): Kubus\n(D): Bol\n(E): Kegel\n")
shape = shape.lower()
if shape == "a":
    length = float(input(f"Wat is de lengte in {unit}? "))
    width = float(input(f"Wat is de breedte in {unit}? "))
    height = float(input(f"Wat is de hoogte in {unit}? "))
    volume = (length * width * height) / 3
elif shape == "b":
    length = float(input(f"Wat is de lengte in {unit}? "))
    width = float(input(f"Wat is de breedte in {unit}? "))
    height = float(input(f"Wat is de hoogte in {unit}? "))
    volume = length * width * height
elif shape == "c":
    length = float(input(f"Wat is de lengte in {unit}? "))
    volume = length * length * length
elif shape == "d":
    radius = float(input(f"Wat is de straal in {unit}? "))
    volume = (4/3) * math.pi * (radius * radius * radius)
elif shape == "e":
    radius = float(input(f"Wat is de straal in {unit}? "))
    height = float(input(f"Wat is de hoogte in {unit}? "))
    volume = (1/3) * math.pi * (radius * radius) * height

print()
print(f"{volume} {unit}³")
print(f"{round(volume)} {unit}³ afgerond")
time.sleep(5)