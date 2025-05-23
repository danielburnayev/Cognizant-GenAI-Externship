acceptable_options = ["I", "R", "C", "S", "Q", "V"]
inventory = {
    "apple": (10, 2.5),
    "banana": (20, 1.2)
}
inventory_contents = ""

print("Welcome to the Inventory Manager!")

while True:
    for pair in inventory.items():
        inventory_contents += f"\tItem: {pair[0]}, Quantity: {pair[1][0]}, Price: ${pair[1][1]:.2f}\n"
    print("Current inventory:\n" + inventory_contents)
    inventory_contents = ""

    input_str = input("Select one of the options below:\n\
\tInsert new item (I)\n\
\tRemove current item (R)\n\
\tChange item's quantity and price (C)\n\
\tSee current inventory (S)\n\
\tEvaluate the value of the items (V)\n\
\tQuit this applicaiton (Q)\n").upper()

    if input_str not in acceptable_options:
        print(input_str, "is not a valid option to select from. Try again.\n")
        continue
    if input_str == "Q":
        break
    if input_str == "S":
        for pair in inventory.items():
            inventory_contents += f"Item: {pair[0]}, Quantity: {pair[1][0]}, Price: {pair[1][1]:.2f}\n"
        print(inventory_contents)
        inventory_contents = ""
        continue
    if input_str == "V":
        total_value = 0
        for value in inventory.values():
            total_value += value[0] * value[1]
        print(f"The whole inventory has a value of ${total_value:.2f}\n")
        continue
    
    the_item = input("Type an item name: ")
    if input_str == "R" and inventory.get(the_item) != None:
        inventory.pop(the_item)
    if input_str == "I" or (input_str == "C" and inventory.get(the_item)) != None:
        new_quantity = int(input("Quantity: "))
        new_price = float(input("Price: "))
        inventory[the_item] = (new_quantity, new_price)