import math
def calculate(diameter_cm, price):
    diameter_m = diameter_cm / 100
    radius = diameter_m / 2
    area = math.pi * ( radius **2)
    unit_price = price / area
    return unit_price
print("Pizza_1")
d1 = float(input("Enter a diameter for pizza_1(cm):"))
p1 = float(input("Enter a price for pizza_1(USD):"))
print("Pizza_2")
d2 = float(input("Enter a diameter for pizza_2(cm):"))
p2 = float(input("Enter a price for pizza_2(USD):"))
unit_price1 = calculate(d1, p1)
unit_price2 = calculate(d2, p2)
print(f"Unit price of pizza 1: {unit_price1:.2f} USD/m^2")
print(f"Unit price of pizza 2: {unit_price2:.2f} USD/m^2")
if unit_price1 < unit_price2:
    print("\n=> pizza 1 has a better value (cheaper per square meter)!")
elif unit_price2 < unit_price1:
    print("\n=> pizza 2 has a better value (cheaper per square meter)!")
else:
    print("\n=> both pizzas have the same value!")


