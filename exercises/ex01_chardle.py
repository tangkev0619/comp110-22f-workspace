"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730578568"

user_name: str = input("Enter a 5-character word:")
if len(user_name) < 5 or len(user_name) > 5:
    print("Error: Word must contain 5 characters") 
    exit()
user_char: str = input("Enter a single character:")
if len(user_char) < 1 or len(user_char) > 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + user_char + " in " + user_name)
counter: int = 0
if user_char == user_name[0]:
    print(user_char + " found at index 0")
    counter += 1
if user_char == user_name[1]:
    print(user_char + " found at index 1")
    counter += 1
if user_char == user_name[2]:
    print(user_char + " found at index 2")
    counter += 1
if user_char == user_name[3]:
    print(user_char + " found at index 3")
    counter += 1
if user_char == user_name[4]:
    print(user_char + " found at index 4")
    counter += 1
if counter == 0:
    print("No instances of " + user_char + " found in " + user_name)
elif counter == 1:
    print("1 instance of " + user_char + " found in " + user_name)
else: 
    print(str(counter) + " instances of " + user_char + " found in " + user_name)