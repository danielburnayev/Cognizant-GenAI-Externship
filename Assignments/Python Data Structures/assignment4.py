# task 1
fav_fruits = ["orange", "mandarin", "banana", "mango", "pear"]
print("Original list:", fav_fruits)

fav_fruits.append("apple")
print("After adding a fruit:", fav_fruits)

fav_fruits.remove("mango")
print("After removing a fruit:", fav_fruits)

fav_fruits.reverse()
print("Reversed list:", fav_fruits)


# task 2
dict = {"name": "Daniel Burnayev", "age": "20", "city": "Somewhere in VA"}
dict.update({"favorite color": "blue"})
dict["city"] = "Fairfax"
key_str = "Keys: "
val_str = "Values: "
for pair in dict.items():
    follower = ", " if pair[0] != "favorite color" else ""
    key_str += pair[0] + follower
    val_str += pair[1] + follower
print("\n" + key_str, "\n" + val_str)
