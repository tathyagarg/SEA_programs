# Program to conduct various operations on a list
items = ['Apple', 'Banana', 'Orangee']
print(items)

# Operation a: insertion
items.insert(1, "Grapes")  # We use index 1 since indecies start at 0, making 1 the second index
print(items)

# Operation b: deletion
items.remove("Banana")
print(items)

# Operation c & d: appending
items.append("Mango")
print(items)

items.append("Kiwi")
print(items)

# Operation e: editing
items[0] = "Pineapple"  # We know the apple is at first position, i.e., index 0
print(items)
