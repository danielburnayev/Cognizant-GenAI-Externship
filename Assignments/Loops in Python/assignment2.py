# task 1
count = int(input("Provide a positive integer: "))
while count > 0:
    print(count, end=" ")
    count -= 1

if count == 0:
    print("\nBlast off!")
else:
    print("\nUmmmmm, blast off already happened. Maybe start from a postivie integer instead of a negative one")


# task 2
multiplier = int(input("Give a number, any number: "))
for multiplicand in range(1, 11): # multiplying from 1 to 10
    print(multiplier, " X ", multiplicand, " = ", multiplier * multiplicand)