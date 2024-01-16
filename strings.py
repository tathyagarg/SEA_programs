# Program to display the length of a string, and each of its characters on a seperate line
text = input("Enter string: ")
print(f"The length is: {len(text)}")
for character in text:
    print(character)
