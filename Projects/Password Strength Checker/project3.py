special_chars = {"~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "[", "]", "{", "}", "|", "\\", ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/"}

while True:
    password_input = input("Put in your password\nIt should be at least 8 characters long, have one uppercase and lowercase character, one numerical digit, and one special character\nPassword: ")
    if len(password_input) < 8:
        print("The password needs to be at least 8 characters long!\n")
        continue
    
    upper_check = False
    lower_check = False
    num_check = False
    special_check = False
    requirements = 4
    for char in password_input:
        if upper_check is False and char.isupper():
            upper_check = True
            requirements -= 1
        elif lower_check is False and char.islower():
            lower_check = True
            requirements -= 1
        elif num_check is False and char.isdigit():
            num_check = True
            requirements -= 1
        elif special_check is False and char in special_chars:
            special_check = True
            requirements -= 1
    
    if upper_check and lower_check and num_check and special_check:
        print("Your password is strong! 💪")
        break

    require_copy = requirements
    error_msg = "To make your password secure, it needs at least "
    error_list = ["" if upper_check else "one uppercase character", 
                  "" if lower_check else "one lowercase character", 
                  "" if num_check else "one numerical digit",
                  "" if special_check else "one special character"]
    for index, error in enumerate(error_list):
        error_msg += "and " if requirements > 2 and require_copy == 1 and error != "" else ""
        error_list[index] += ", " if require_copy > 1 and error != "" else ""
        error_msg += error_list[index]
        if error != "":
            require_copy -= 1
    print(error_msg + "\n")






