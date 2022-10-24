from random import randint
def grassland_biome() -> None:
    """This function gives the user 5 different random Pokémon from the grassland biome to catch."""
    global user_name
    GLB_Pokémon = ["Raikou", "Entei", "Suicune", "Arcanine", "Nidoking"]
    list1 = []
    for x in range(len(GLB_Pokémon)):
        list1.append(x)
    print("You Have Step Into: The Lazy Grasslands.")
    print("\U0001F331\U0001F332\U0001F331\U0001F333\U0001F331\U0001F332\U0001F331\U0001F333\U0001F331\U0001F332\U0001F331\U0001F333\U0001F331\U0001F332\U0001F331\U0001F333\U0001F331\U0001F332\U0001F331\U0001F333")
    print(f"{user_name}: Let's start capturing Pokémon.")
    while len(GLB_Pokémon) > 0:
        number = randint(0, len(GLB_Pokémon)-1 )
        print("A wild", GLB_Pokémon.pop(number), "has appeared.")
    print(f"{user_name}: I think I have captured all the Pokémon and finished exploring The Lazy Grasslands.")


def waters_edge_biome() -> None:
    """This function gives the user 5 different random Pokémon from the water's-edge biome to catch."""
    global user_name
    WEB_Pokémon = ["Gyarados", "Milotic", "Latios", "Feraligator", "Dragonite"]
    list1 = []
    for x in range(len(WEB_Pokémon)):
        list1.append(x)
    print("You Have Step Into: The Ravenousness Water's-Edge.")
    print("\U0001F30A\U0001F300\U0001F30A\U0001F300\U0001F30A\U0001F300\U0001F30A\U0001F300\U0001F30A\U0001F300\U0001F30A\U0001F300\U0001F30A\U0001F300\U0001F30A\U0001F300\U0001F30A\U0001F300\U0001F30A\U0001F300\U0001F30A\U0001F300\U0001F30A\U0001F300\U0001F30A")
    print(f"{user_name}: Let's start capturing Pokémon.")
    while len(WEB_Pokémon) > 0:
        number = randint(0, len(WEB_Pokémon)-1 )
        print("A wild", WEB_Pokémon.pop(number), "has appeared.")
    print(f"{user_name}: I think I have captured all the Pokémon and finished exploring The Ravenousness Water's-Edge.")


def cave_biome() -> None:
    """This function gives the user 5 different random Pokémon from the cave biome to catch."""
    global user_name 
    CB_Pokémon = ["Crobat", "Gengar", "Regirock", "Regice", "Registeel"]
    list1 = []
    for x in range(len(CB_Pokémon)):
        list1.append(x)
    print("You Have Step Into: The Greedy Cave.")
    print("\U000026F0\U000026D3\U000026F0\U000026D3\U000026F0\U000026D3\U000026F0\U000026D3\U000026F0\U000026D3\U000026F0\U000026D3\U000026F0\U000026D3\U000026F0\U000026D3\U000026F0\U000026D3\U000026F0\U000026D3\U000026F0\U000026D3\U000026F0\U000026D3\U000026F0\U000026D3\U000026F0\U000026D3\U000026F0\U000026D3\U000026F0\U000026D3\U000026F0\U000026F0\U000026D3")
    print(f"{user_name}: Let's start capturing Pokémon!")
    while len(CB_Pokémon) > 0:
        number = randint(0, len(CB_Pokémon)-1 )
        print("A wild", CB_Pokémon.pop(number), "has appeared.")
    print(f"{user_name}: I think I have captured all the Pokémon and finished exploring The Greedy Cave.")


def urban_biome() -> None:
    """This function gives the user 5 different random Pokémon from the urban biome to catch."""
    global user_name
    UB_Pokémon = ["Alakazam", "Gardevoir", "Magnezone", "Porygon-Z", "Umbreon"]
    list1 = []
    for x in range(len(UB_Pokémon)):
        list1.append(x)
    print("You Have Step Into: The Arrogant City.")
    print("\U0001F3ED\U0001F3EC\U0001F3EB\U0001F3EA\U0001F3E8\U0001F3E6\U0001F3E5\U0001F3E4\U0001F3E2\U0001F3D7\U0001F3DB\U0001F3DF\U0001F3ED\U0001F3EC\U0001F3EB\U0001F3EA\U0001F3E8\U0001F3E6\U0001F3E5\U0001F3E4\U0001F3E2")
    print(f"{user_name}: Let's start capturing Pokémon!")
    while len(UB_Pokémon) > 0:
        number = randint(0, len(UB_Pokémon)-1 )
        print("A wild", UB_Pokémon.pop(number), "has appeared.")
    print(f"{user_name}: I think I have captured all the Pokémon and finished exploring The Arrogant City.")