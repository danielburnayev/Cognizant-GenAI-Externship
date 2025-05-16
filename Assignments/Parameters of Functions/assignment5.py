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