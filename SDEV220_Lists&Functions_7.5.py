things = ["mozzarella", "cinderella", "salmonella"]

# Find the index of the element referring to a person ("cinderella")
person_index = things.index("cinderella")

# Capitalize the element at the person_index
things[person_index] = things[person_index].capitalize()

# Print the modified list
print(things)