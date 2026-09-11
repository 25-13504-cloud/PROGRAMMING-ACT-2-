# Name = Punzalan, Aljon E.
# Section = BMET 2101
# Task 3 = leap year test

name = input("enter your name")
print("hello, " + name)

year = int(input("Enter a year: "))
print("Is it a leap year?", (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))
