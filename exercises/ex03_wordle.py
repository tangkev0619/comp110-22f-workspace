"""EX03 - Wordle."""
__author__ = "730578568"

"""This function checks whether or not letter is contained in word."""

def contains_char (word: str, letter: str) -> bool:
    assert len(letter) == 1
    index=0
    while index < len(word):
        if letter == word[index]:
            return True 
        index +=1
    return False

def emojified (guess: str, secret: str) -> str:
    """This function assigns and returns the white, green, and yellow boxes based on the position of the letters in the word by using the contains char to see if it true or false."""
    assert len(guess) == len(secret)
    emo_box = ""
    index: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while index < len(secret):
        if secret[index] == guess[index]:
            emo_box += GREEN_BOX
        elif contains_char(secret, guess[index]):
            emo_box += YELLOW_BOX
        else:
            emo_box += WHITE_BOX
        index +=1
    return emo_box 

def input_guess (expectedlen: int) -> str:
    """This function checks the user's input and checks it with the expected length and if it's incorrect it will say that wasn't this number try again, if it's correct it will return user input."""
    user_name: str = input(f"Enter a {expectedlen} character word: ")
    while len(user_name) != expectedlen:
         user_name = input(f"That wasn't {expectedlen}! Try again: ")
    if len(user_name) == expectedlen:
        return user_name 

def main ( ) -> None:
    """The entrypoint of the program and main game loop."""
    turns = 1
    won: bool = False
    secret = "codes"
    while turns < 7 and won is False:
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess (len(secret))
        print(emojified (guess, secret))
        if guess == secret: 
            won = True 
            print(f"You won in {turns}/6 turns!")
        turns += 1
    if won == False: 
        print("X/6 - Sorry, try again tomorrow!")