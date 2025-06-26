# Assignment: Exploring Python Concepts, done by Daniel Burnayev

# Task 1:
name = "Daniel"
age = 20
height = 6.3

print("Hey y'all, this is " + name + " here, " + str(age) + " years old and " + str(height) + " feet tall.")


# Task 2:
num1 = 9
num2 = 10
print("The sum of " + str(num1) + " and " + str(num2) + " is: ", num1 + num2, "\n")
print("The difference of " + str(num1) + " and " + str(num2) + " is: ", num1 - num2, "\n")
print("The product of " + str(num1) + " and " + str(num2) + " is: ", num1 * num2, "\n")
print("The quotient of " + str(num1) + " and " + str(num2) + " is: ", num1 / num2, "\n")


# Task 3:
given_num = input("Type in a number, any number!\n")
num = int(given_num)
if num > 0:
    print("This number is positive. Awesome!")
elif num < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")