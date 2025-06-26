# task 1
def greet_user(name):
    print("Hello,", name + "!", "Welcome aboard.")
    
def add_numbers(num1, num2):
    return num1 + num2

name_input = input("What is your name? ")
nums_input = input("Give me two numbers, each one seperated by a space. ")
given_nums = nums_input.split()

greet_user(name_input)
print(int(given_nums[0]), "+", int(given_nums[1]), "=", add_numbers(int(given_nums[0]), int(given_nums[1])))


# task 2
def describe_pet(pet_name: str, animal_type: str = "dog"):
    print("I have a", animal_type, "named", pet_name + ".")

dog_name = input("\nGive a dog name. ")
animal_name = input("Now, what is the name of the animal of your choice? ")
animal_type = input("What type of animal is " + animal_name + "? ")
describe_pet(dog_name)
describe_pet(animal_name, animal_type)


# task 3
def make_sandwich(*args):
    print("Making a sandwich with the following ingredients:")
    for ingredient in args:
        print("\t- ", ingredient)

ingredients_input = input("Welcome to the snadwich maker! To start, list all the ingredients you want in your sandwich. Make sure to seperate every ingredient with a comma.")
ingredients = ingredients_input.split(",")
ingredients = list(map(lambda param: param.strip(), ingredients))
make_sandwich(*ingredients)


# task 4
def factorial(num: int):
    if type(num) != int or num < 0:
        return None
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
def fibonacci(nth_num: int):
    if type(nth_num) != int or nth_num < 0:
        return None
    elif nth_num == 0:
        return 0
    elif nth_num == 1:
        return 1
    else:
        return fibonacci(nth_num - 2) + fibonacci(nth_num - 1)

print("Factorial of", 4, "is", factorial(4))
print("Factorial of", -4, "is", factorial(-4), "since it cannot be calculated.")
print("Factorial of", 4.5, "is", factorial(4.5), "since this function only calcuates factorials of integers.\n")

print("The 6th fibonacci number is", fibonacci(6))
print("The -6th fibonacci number is", fibonacci(-6), "since that cannot be determined.")
print("The 6.5th fibonacci number is", fibonacci(6.5), "since that cannot be determined.")