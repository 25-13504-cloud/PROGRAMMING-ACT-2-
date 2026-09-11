# Name = Punzalan, Aljon E.
# Section = BMET 2101
# Task 4 = temperature check

name = input("enter your name")
print("hello, " + name)

celsius = float(input("Enter temperature in °C: "))
fahrenheit = celsius * 9/5 + 32
in_range = 20 <= celsius <= 30

print("Fahrenheit:", fahrenheit)
print("Between 20 and 30 °C:", in_range)
