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