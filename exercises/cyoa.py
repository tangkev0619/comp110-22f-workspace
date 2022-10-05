"""EX06 - Choose Your Own Adventure."""
__author__ = "730578568"

from random import randint


def prologue() -> None:
    """This function is used to tell the user about the prologue of the game."""
    print("This game will be using Pokémon names from the famous Pokémon franchises, but this game is not affiliated or associated with the Pokémon games creators Nintendo, Game Freak, and Creatures. Now after this copyright shit is over, welcome to my game called, Pokémon Dark, Game 1. (P.S. To read the dialogue each line is separated by a enter key, so press the enter key to read the dialogue.)")
    input("")
    print("Prologue: Before I knew it, I was transported to a different world because of that fucking god.")
    input("")
    print("Technically I don't know who he is, but for certain, he has the power of a god, so I'll refer to him as Being Z.")
    input("")
    print("Being Z mistaken me as an atheist, but in reality, I devoted my life to God or whoever that rules and controls the higher powers.") 
    input("")
    print("The reasoning is that I was born into a religious family; my dad was a priest for the temple my family has owned for generations, while my mom was a religious teacher.")
    input("")
    print("From a young age, I was always told that I will be the next head of the temple, but now I lay in the world of Pokémon.")
    input("")
    print("You may ask, how do I know this is the world of Pokémon?")
    input("")
    print("Well, because that Being Z told me that I will be transported to the world of Pokémon, what the fuck is a Pokémon?")
    input("")
    print("The last thing I remember Being Z telling me is 'Deus Vult.'")
    input("")
    print("Well, whatever we can't keep bitching about this situation; let's just find a town and talk to people about this world.")


player: str


def greet() -> None:
    """This function is used to greet the user when they first start the game."""
    global player
    print("You arrived at some town.")
    input("")
    print("Town's Man: Hello, welcome to Nuvema Town.") 
    input("")
    player = input("What is your name? ")
    input("")
    print(f"Town's Man: Oh your name is {player}, what is your business in our town?")
    input("")
    print(f"{player}: I need to find out about this world of Pokémon and how this world works.")
    input("")
    print("Town's Man: Then you need to speak to Professor Oak, he researches about Pokémon.")
    input("")
    print(f"{player}: Okay, can you take me to Professor Oak, then?")
    input("")
    print("Town's Man: Sure follow me.")
    input("")
    print(f"{player} followed Town's Man to the laboratory of Professor Oak.")
    input("")
    print("Town's Man: Professor Oak, I brought a person that needs to speak to you about the world of Pokémon.")
    input("")
    print(f"Town's Man Left The Building Leaving {player} with Professor Oak.")
    input("")
    print(f"{player}: Hello, Professor, my name is {player} and I want to learn about this world of Pokémon.")
    input("")
    print("Professor Oak: Nice to meet you. First, how the hell do you not know about Pokémon?")
    input("")
    print(f"{player} tells Professor Oak about what happened so far.")
    input("")
    print("Professor Oak: Oh, that's weird whoever Being Z is we need to find it, so we can get you back to your home. Well since your hear let me tell you about the world of Pokémon.")
    input("")
    print("Professor Oak: They were beings or better I say creatures that live with us from the dawn of time, you can see them everywhere, they can be in the wild or captured by trainers.")
    input("")
    print("Professor Oak: The important thing is that they live together with humans for the longest, so what I need you to do is go out there and capture Pokémon for me.")
    input("")
    print(f"{player}: Well how do I capture Pokémon then?")
    input("")
    print("Professor Oak: Let me tell you about the capturing device called a Poké Ball.")
    input("")
    print("Professor Oak: The Poké Ball have 50 Percent Chance of capturing the Pokémon you encounter, the Great Ball have 75 Percent Chance of capturing Pokémon, and the Ultra ball have 90 Percent Chance of capturing Pokémon.")
    input("")
    print("Professor Oak: The meaning is that the higher the Poké Ball you have the better the chance you have to catch the Pokémon because when you encounter a wild Pokémon you have one turn to capture it before it runs away. The down side is that buying Great Balls or Ultra Balls cost more compared to buying Poké Ball. The points you earn to buy Poké Balls comes from transfering the Pokémon to me. ")
    input("")
    print(f"{player}: Okay, I understand now.")
    input("")
    print("Professor Oak: Now go out there and capture as many Pokémon for me. But before you go here have a map of the region.")
    input("")
    print(f"{player} recieved a map from Professor Oak and {player} left Professor Oak's Laboratory")
    input("")
    print(f"{player}: Fuck it, I got nothing else to do, so let's just capture Pokémon. Well the map first said I need to go to The Lustful Forest and travel until the Sacred Heaven, and I bet that Being Z is fucking there!!!") 


def last_dialogue() -> None:
    """This function is the dialogue for the ending of the game."""
    global player, points 
    print(f"{player}: I tried to captured all the Pokémon in the biomes Professor Oak told me too, I even finished the biome The Sacred Heaven, where the hell is Being Z?")
    input("")
    print(f"{player} felt a cold aura surround the room the user was in like some kind of Being that shouldn't be messed with.")
    input("")
    print(f"{player}: Fuck why is it so fucking cold, but this presence is something so familiar. It's like when Being Z transported me to this world.")
    input("")
    print(f"{player} was right about that Being Z following the user.")
    input("")
    print(f"{player}: !!!")
    input("")
    print(f"Being Z: Oh hello again {player}. How are you feeling in the world I transported you in? Have you finally developed faith in the real God?")
    input("")
    print(f"{player}: You finally fucking show up now, Being Z, what do you mean by the real God?")
    input("")
    print("Being Z: Oh you still don't know about the real God, no wonder the real God our lord and savior has lost hope with humanity which he created.")
    input("")
    print(f"{player}: Well can you at least answer the question?")
    input("")
    print("Being Z: Well fine, I am a apostle of the real God, and a God of the world you know as Pokémon, so technically your in the realm that I rule over.")
    input("")
    print("Being Z reveals that he is the God and Creator of all Pokémon it's name is called Arceus.")
    input("")
    print("Arceus: Now, you know who I am why don't you respect me by bowing down to me, as the apostle to the real God.")
    input("")
    print(f"{player}: Well fuck you I don't bow down to you, I only bow when the true God and ruler of the universe shows up.")
    input("")
    print("Arecus: Keke, sure you won't bow down to me now, but when you suffer the punishment I'm about the give you, you be pleading to me like crazy.")
    input("")
    print(f"{player}: ???")
    input("")
    print("Arecus: Oh, so you don't know what wrong you have done?")
    input("")
    print("Arecus: You fucking imbecile, how dear you sell my creations you humans called Pokémon to that professor you call Professor Oak for points?")
    input("")
    print(f"{player}: Well how the hell do I know not to do that, you didn't even tell me.")
    input("")
    print("Arecus: WTF, what are you trying to say? That when you were walking into Professor Oak's lab didn't see bags of blood and odd looking bones that belong to Pokémon?")
    input("")
    print(f"{player}: No, I didn't see that, he probably cleaned it up before I got there, and why do you need to punish me and not the professor?")
    input("")
    print("Arecus: Well I will punish him after I kill you.")
    input("")
    print(f"{player} thought that the Ultra Ball in the item bag can be used to capture Arecus.")
    input("")
    print(f"{player} threw a Ultra Ball at Arecus capturing it in the device.")
    input("")
    points -= 30 
    print(f"{player} let out a sigh of relief: I finally got the thing that transported me to this world.")
    input("")
    print(f"{player} then felt a cold pinch in the middle of the user's stomach, when {player} looked down there was something white stuck in the middle of the user's stomach.")
    input("")
    print(f"{player} then saw the white thing move out from the stomach then a gush of blood came out of the stomach.")
    input("")
    print(f"{player} choking on blood: What the fuck happened, what was that thing in my stomach? Cough, cough, cough.")
    input("")
    print(f"{player} kept coughing up blood even time the user spoke.")
    input("")
    print(f"Arecus: {player} you really thing that puny device you call the Ultra Ball can catch me. That may work for my creations, but you forgot that I was a God of this world, stuff like that won't work, as I was the creator of these Pokémon catching device.")
    input("")
    print(f"{player}: What the fuck you mean? You created the devices to catch your own creations?")
    input("")
    print("Arecus: That's what it sounds like when my creations aren't obedient to me there creator, I will just use the capturing device to catch them.")
    input("")
    print("Arecus: You still haven't seen my prized collection 'The Master Ball,' it has the chance to catch all Pokémon with 100 Percent catching rate. Hahahahahahahaha.")
    input("")
    print(f"{player} now in shock from the blood and the news: What!!! I though the Professor Oak said 'The Master Ball' is only of legends.")
    input("")
    print("Arecus: Well it is since I'm the only one that can create it and use it, so nothing I create will be insubordinate to me because they will be loyal to me and do what I command them to do. Hehehehe.")
    input("")
    print("Arecus: Now you know about it you will pay by dying because I'm the only one that can use my creations to do my tasks. If you bow down to me I might reconsider it.")
    input("")
    print(f"{player}: FUCK YOU, YOU SCUMBAG I DON'T BOW DOWN TO YOU, I BOW DOWN TO THE REAL GOD, AND YOU WILL ONE DAY FACE THE REAL GOD'S JUDGEMENT DAY.")
    input("")
    print("Arecus: Well fuck you too, because I will have fun killing you. Hahahahahahahahaha.")
    input("")
    print(f"{player} was brutally injured by Arecus. After that Arecus went back to his palace.")
    input("")
    print(f"{player} on the brink of death: Oh how I feel so cold, such a cruel world, I was just trying to survive in the world of Pokémon, but now I'm dying. Well I can't do anything but lay in the puddle of my blood, so good bye cruel world, I knew it was going to end like this.") 
    input("")
    print(f"{player}: Oh how my body feels like I'm in a voidless cold ocean without anyone trying to save me.....({player} heart stopped).")
    input("")
    print("YOU DIED!!!(Insert Dark Soul Meme Here) GAME OVER!!!")
    print("You have", {check_points(points)}, "points!!!")


def ending() -> None:
    """This is the ending dialogue for the game."""
    global player 
    print(f"{player} woke up in Professor Oak's lab in a tank split by glass when {player} looked down at the human body the user once had some of it was replaced by parts of Pokémon {player} caught.")
    input("")
    print("Professor Oak: Hahahaha. This will be my weapon to fight Arecus, my masterpiece, my creation that will make everything and everyone obey me, and I will gain the power of God. Hahahahaha, I can't wait to face Arecus with my human Pokémon hybrid.")
    input("")
    print(f"{player}: FUCK!!!")
    input("")
    print("A quote that will be a main idea of the next game (if users want one), 'The worst enemy you can meet will always be yourself' by Friedrich Nietzsche.")
    input("")
    print("Hello, it's your game dev here, I want to say I hope your enjoyed this game, and if you didn't understand the previous lines, there could be a sequel if you keep supporting me.")
    input("")
    print("Additionally, there is a extended version of this game which would have 196 lines more to this game, so if you want it, tell me.")
    input("")
    print("On top of that, today's game is sponsored by the beautiful COMP 110 class that made it possible for me to learn how to code.")
    input("")
    print("That's it from your game dev, good bye have a nice day.")


points: int = 100 


def check_points(p: int) -> int:
    """This tells the user how many points they have."""
    return p


def Poké_Ball() -> bool:
    """This is the percentage for capturing Pokémon with the Poké Ball."""
    i: int = randint(0, 1)
    if i == 0:
        print("The wild Pokémon ran away.")
        return False
    else: 
        print("You have sucessfully captured the wild Pokémon!!!")
        return True


def Great_Ball() -> bool:
    """This is the percentage for capturing Pokémon with the Great Ball."""
    i: int = randint(0, 3)
    if i < 1:
        print("The wild Pokémon ran away.")
        return False
    else: 
        print("You have sucessfully captured the wild Pokémon!!!")
        return True


def Ultra_Ball() -> bool:
    """This is the percentage for capturing Pokémon with the Ultra Ball."""
    i: int = randint(0, 9)
    if i > 1:
        print("You have sucessfully captured the wild Pokémon!!!")
        return True
    else:
        print("The wild Pokémon ran away.")
        return False


FB_Emojis: str = "\U0001F332\U0001F940\U0001F494\U0001F332\U0001F940\U0001F494\U0001F332\U0001F940\U0001F494\U0001F332\U0001F940\U0001F494\U0001F332\U0001F940\U0001F494\U0001F332\U0001F940\U0001F494\U0001F332"


def forest_biome() -> None: 
    """This function gives the user 5 different random Pokémon from the forest biome to catch."""
    global player, points, FB_Emojis 
    caught: bool
    choices: str
    FB_Pokémon: list[str] = ["Celebi", "Shedinja", "Heracross", "Altaria", "Slaking"]
    list1: list[int] = []
    for x in range(len(FB_Pokémon)):
        list1.append(x)
    print("You Have Arrived At: The Lustful Forest.")
    print(f"{FB_Emojis}")
    print(f"{player}: Let's start capturing Pokémon.")
    while len(FB_Pokémon) > 0:
        number = randint(0, len(FB_Pokémon) - 1)
        print("A wild", FB_Pokémon.pop(number), "has appeared.") 
        choices_for_balls: int = int(input("Do you want to use the Poké Ball type 1, Great Ball type 2, and Ultra Ball type 3? "))
        if choices_for_balls == 1:
            caught = Poké_Ball()
            points -= 10
            if caught is True:
                choices = input("Transfer Pokémon to Profess Oak (Yes or No): ")
                if choices == "yes" or choices == "Yes":
                    points += 50 
                    print("50 Points Have Been Added.")
                else:
                    print("Pokémon you just caught has been released back into the wild.")
        if choices_for_balls == 2:
            caught = Great_Ball()
            points -= 20
            if caught is True:
                choices = input("Transfer Pokémon to Profess Oak (Yes or No): ")
                if choices == "yes" or choices == "Yes":
                    points += 50 
                    print("50 Points Have Been Added.")
                else:
                    print("Pokémon you just caught has been released back into the wild.")
        if choices_for_balls == 3:
            caught = Ultra_Ball()
            points -= 30
            if caught is True:
                choices = input("Transfer Pokémon to Profess Oak (Yes or No): ")
                if choices == "yes" or choices == "Yes":
                    points += 50 
                    print("50 Points Have Been Added.")
                else:
                    print("Pokémon you just caught has been released back into the wild.")
    print(f"{player}: I think I have captured all the Pokémon and finished exploring The Lustful Forest.")
    print("You have", {check_points(points)}, "points!!!")


SB_Emojis: str = "\U0001F30A\U0001F6A2\U0001F198\U0001F30A\U0001F6A2\U0001F198\U0001F30A\U0001F6A2\U0001F198\U0001F30A\U0001F6A2\U0001F198\U0001F30A\U0001F6A2\U0001F198\U0001F30A\U0001F6A2\U0001F198\U0001F30A"


def sea_biome() -> None:
    """This function gives the user 5 different random Pokémon from the sea biome to catch."""
    global player, points 
    caught: bool
    choices: str 
    SB_Pokémon: list[str] = ["Kyogre", "Lapras", "Kabutops", "Kingdra", "Wailord"]
    list1: list[int] = []
    for x in range(len(SB_Pokémon)):
        list1.append(x)
    print("You Have Step Into: The Sea of Despair.")
    print(f"{SB_Emojis}")
    print(f"{player}: Let's start capturing Pokémon.")
    while len(SB_Pokémon) > 0:
        number = randint(0, len(SB_Pokémon) - 1)
        print("A wild", SB_Pokémon.pop(number), "has appeared.")
        choices_for_balls: int = int(input("Do you want to use the Poké Ball type 1, Great Ball type 2, and Ultra Ball type 3? "))
        if choices_for_balls == 1:
            caught = Poké_Ball()
            points -= 10
            if caught is True:
                choices = input("Transfer Pokémon to Profess Oak (Yes or No): ")
                if choices == "yes" or choices == "Yes":
                    points += 50 
                    print("50 Points Have Been Added.")
                else:
                    print("Pokémon you just caught has been released back into the wild.")
        if choices_for_balls == 2:
            caught = Great_Ball()
            points -= 20
            if caught is True:
                choices = input("Transfer Pokémon to Profess Oak (Yes or No): ")
                if choices == "yes" or choices == "Yes":
                    points += 50 
                    print("50 Points Have Been Added.")
                else:
                    print("Pokémon you just caught has been released back into the wild.")
        if choices_for_balls == 3:
            caught = Ultra_Ball()
            points -= 30
            if caught is True:
                choices = input("Transfer Pokémon to Profess Oak (Yes or No): ")
                if choices == "yes" or choices == "Yes":
                    points += 50 
                    print("50 Points Have Been Added.")
                else:
                    print("Pokémon you just caught has been released back into the wild.")
    print(f"{player}: I think I have captured all the Pokémon and finished exploring The Sea of Despair.")
    print("You have", {check_points(points)}, "points!!!")


MB_Emojis: str = "\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4\U0001F3D4"


def moutain_biome() -> None:
    """This function gives the user 5 different random Pokémon from the moutain biome to catch."""
    global player, points
    caught: bool 
    choices: str
    MB_Pokémon: list[str] = ["Jirachi", "Charizard", "Aggron", "Tyranitar", "Snorlax"]
    list1: list[int] = []
    for x in range(len(MB_Pokémon)):
        list1.append(x)
    print("You Have Step Into: The Moutain of Vainglory.")
    print(f"{MB_Emojis}")
    print(f"{player}: Let's start capturing Pokémon!")
    while len(MB_Pokémon) > 0:
        number = randint(0, len(MB_Pokémon) - 1)
        print("A wild", MB_Pokémon.pop(number), "has appeared.")
        choices_for_balls: int = int(input("Do you want to use the Poké Ball type 1, Great Ball type 2, and Ultra Ball type 3? "))
        if choices_for_balls == 1:
            caught = Poké_Ball()
            points -= 10
            if caught is True:
                choices = input("Transfer Pokémon to Profess Oak (Yes or No): ")
                if choices == "yes" or choices == "Yes":
                    points += 50 
                    print("50 Points Have Been Added.")
                else:
                    print("Pokémon you just caught has been released back into the wild.")
        if choices_for_balls == 2:
            caught = Great_Ball()
            points -= 20 
            if caught is True:
                choices = input("Transfer Pokémon to Profess Oak (Yes or No): ")
                if choices == "yes" or choices == "Yes":
                    points += 50 
                    print("50 Points Have Been Added.")
                else:
                    print("Pokémon you just caught has been released back into the wild.")
        if choices_for_balls == 3:
            caught = Ultra_Ball()
            points -= 30
            if caught is True:
                choices = input("Transfer Pokémon to Profess Oak (Yes or No): ")
                if choices == "yes" or choices == "Yes":
                    points += 50 
                    print("50 Points Have Been Added.")
                else:
                    print("Pokémon you just caught has been released back into the wild.")
    print(f"{player}: I think I have captured all the Pokémon and finished exploring The Moutain of Vainglory.")
    print("You have", {check_points(points)}, "points!!!")


FTB_Emojis: str = "\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B\U0001F30B"


def rough_terrian_biome() -> None:
    """This function gives the user 5 different random Pokémon from the rough-terrian biome to catch."""
    global player, points
    caught: bool
    choices: str
    RTB_Pokémon: list[str] = ["Groudon", "Metagross", "Salamence", "Flygon", "Donphan", "Garachop"]
    list1: list[int] = []
    for x in range(len(RTB_Pokémon)):
        list1.append(x)
    print("You Have Step Into: The Infuriated Stony Cliff.")
    print(f"{FTB_Emojis}")
    print(f"{player}: Let's start capturing Pokémon!")
    while len(RTB_Pokémon) > 0:
        number = randint(0, len(RTB_Pokémon) - 1)
        print("A wild", RTB_Pokémon.pop(number), "has appeared.")
        choices_for_balls: int = int(input("Do you want to use the Poké Ball type 1, Great Ball type 2, and Ultra Ball type 3? "))
        if choices_for_balls == 1:
            caught = Poké_Ball()
            points -= 10
            if caught is True:
                choices = input("Transfer Pokémon to Profess Oak (Yes or No): ")
                if choices == "yes" or choices == "Yes":
                    points += 50 
                    print("50 Points Have Been Added.")
                else:
                    print("Pokémon you just caught has been released back into the wild.")
        if choices_for_balls == 2:
            caught = Great_Ball()
            points -= 20
            if caught is True:
                choices = input("Transfer Pokémon to Profess Oak (Yes or No): ")
                if choices == "yes" or choices == "Yes":
                    points += 50 
                    print("50 Points Have Been Added.")
                else:
                    print("Pokémon you just caught has been released back into the wild.")
        if choices_for_balls == 3:
            caught = Ultra_Ball()
            points -= 30
            if caught is True:
                choices = input("Transfer Pokémon to Profess Oak (Yes or No): ")
                if choices == "yes" or choices == "Yes":
                    points += 50 
                    print("50 Points Have Been Added.")
                else:
                    print("Pokémon you just caught has been released back into the wild.")
    print(f"{player}: I think I have captured all the Pokémon and finished exploring The Infuriated Stony Cliff.")
    print("You have", {check_points(points)}, "points!!!")


DB_Emojis: str = "\U000026EA\U0001F54C\U0001F6D5\U0001F54D\U000026E9\U0001F54B\U000026EA\U0001F54C\U0001F6D5\U0001F54D\U000026E9\U0001F54B\U000026EA\U0001F54C\U0001F6D5\U0001F54D\U000026E9\U0001F54B\U000026EA\U000026E9"


def divine_biome() -> None:
    """This function gives the user 5 different random Pokémon from the divine biome to catch."""
    global player, points
    caught: bool
    choices: str
    DB_Pokémon: list[str] = ["Mewtwo", "Deoxys", "Rayquaza", "Ho-Oh", "Articuno", "Lugia"]
    list1: list[int] = []
    for x in range(len(DB_Pokémon)):
        list1.append(x)
    print("You Have Step Into: The Sacred Heaven.")
    print(f"{DB_Emojis}")
    print(f"{player}: The last fucking biome, let's start capturing the Pokémon here!")
    while len(DB_Pokémon) > 0:
        number = randint(0, len(DB_Pokémon) - 1)
        print("A wild", DB_Pokémon.pop(number), "has appeared.")
        choices_for_balls: int = int(input("Do you want to use the Poké Ball type 1, Great Ball type 2, and Ultra Ball type 3? "))
        if choices_for_balls == 1:
            caught = Poké_Ball()
            points -= 10
            if caught is True:
                choices = input("Transfer Pokémon to Profess Oak (Yes or No): ")
                if choices == "yes" or choices == "Yes":
                    points += 50 
                    print("50 Points Have Been Added.")
                else:
                    print("Pokémon you just caught has been released back into the wild.")
        if choices_for_balls == 2:
            caught = Great_Ball()
            points -= 20
            if caught is True:
                choices = input("Transfer Pokémon to Profess Oak (Yes or No): ")
                if choices == "yes" or choices == "Yes":
                    points += 50 
                    print("50 Points Have Been Added.")
                else:
                    print("Pokémon you just caught has been released back into the wild.")
        if choices_for_balls == 3:
            caught = Ultra_Ball()
            points -= 30
            if caught is True:
                choices = input("Transfer Pokémon to Profess Oak (Yes or No): ")
                if choices == "yes" or choices == "Yes":
                    points += 50 
                    print("50 Points Have Been Added.")
                else:
                    print("Pokémon you just caught has been released back into the wild.")
    print(f"{player}: I think I have captured all the Pokémon and finished exploring The Sacred Heaven.")
    print("You have", {check_points(points)}, "points!!!")


def complements_or_criticism() -> str:
    """This functions complements or critics the user based on the points they have."""
    global player, points
    if points < 100:
        return "Haha, you can't even break even, I gave you 100 points and look at you in debt like the college student you are."
    elif points >= 200:
        return "Wow, your fucking amazing to get all those points with them Pokémon catching balls."
    elif points >= 100 or points < 200:
        return "Your just mid bro, nothing is special about you, KEKW."
    return ""


def main() -> None:
    """This functtion is used to run all the other functions I have writing, in summary this function is used to run the game."""
    prologue()
    input("")
    greet()
    input("")
    forest_biome()
    input("")
    sea_biome()
    input("")
    moutain_biome()
    input("")
    divine_biome()
    input("")
    last_dialogue()
    input("")
    print(complements_or_criticism())
    input("")
    ending()


if __name__ == "__main__":
    main()