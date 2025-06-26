# task 1
init_string = "Python is amazing!"

first_six = init_string[0:6]
amazing_part = init_string[10:len(init_string) - 1]
reverse_string = init_string[::-1]

print("First 6 characters:", first_six + "\n", "Amazing part:", amazing_part + "\n", "Reversed string:", reverse_string)


# task 2
og_str = " hello, python world! "

print("\nOriginal string: \" hello, python world! \"\n\
Stripped string: \"" + og_str.strip() + "\"\n\
Capitalized string: \"" + og_str.capitalize() + "\"\n\
Replaced string: \"" + og_str.replace("world", "universe") + "\"\n\
Uppercase string: \"" + og_str.upper() + "\"")


# task 3
given_str = input("\nGive me a string, any string: ")
backwards_str = given_str[::-1]
if given_str == backwards_str:
    print("Yes,", "\'" + given_str + "\'", "is a palindrome!")
else:
    print("No,", "\'" + given_str + "\'", "is not a palindrome.")
