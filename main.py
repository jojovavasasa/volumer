unit = input("welke eenheid ga je gebruiken? ")

length = float(input(f"wat is de lengte in {unit}? "))
breadth = float(input(f"wat is de breedte in {unit}? "))
height = float(input(f"wat is de hoogte in {unit}? "))

volume = (length * breadth * height) / 3
print(f"{volume} {unit}³")