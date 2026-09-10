# Name = Punzalan, Aljon E.
# Section = BMET 2101
# Task 1 = change calculator

name = input("enter your name")
print("hello, " + name)

amount = int(input("Enter amount in pesos: "))

p100 = amount // 100
amount = amount % 100

p20 = amount // 20
amount = amount % 20

p5 = amount // 5
amount = amount % 5

p1 = amount // 1

print("100 pesos:", p100)
print("20 pesos:", p20)
print("5 pesos:", p5)
print("1 peso:", p1)