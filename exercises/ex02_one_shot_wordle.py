"""EX02 - One_Shot Wordle.""" 
__author__ = "730578568"

secret = "python"
user_name: str = input(f"What is your {len(secret)}-letter guess?")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index = 0 
emo_line = ""

while len(user_name) != len(secret):
    user_name: str = input(f"That was not {len(secret)} letters! Try again: ")
    if user_name != secret:
        print("Not quite. Play again soon!")
if user_name == secret:
    print("Woo! You got it!")

while index < len(secret):
    if user_name [index] != secret [index]: 
        contain_char: bool = False
        number_index: int = 0
        while contain_char is False and number_index < len(secret):
            if user_name [index] == secret[number_index] and index != number_index:
                emo_line += YELLOW_BOX 
                # This part is here since if the user name index and the secret number of index is the same and the index doesn't equal number index we add a yellow box.
                contain_char = True
            else: 
                number_index += 1
        if contain_char == False:
            emo_line += WHITE_BOX
            # This part is here since if user input doesn't equal any letters in the secret word it will print out a white box.
    elif user_name [index] == secret [index]:
        emo_line += GREEN_BOX
        # This part is here since if the user's input is equal to the secret input then it will print out a green box. 
    index += 1
print(emo_line)