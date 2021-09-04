def Random_Word():
    #returns a random word from the following list of 50 words
    import random
    words = ["CAGE", "KEYOARD", "DISASTER", "SUMMER", "BEACH", "RIVER",
        "AUTOMOBILE", "SUBWAY", "IATROGENIC", "RHYTHM", "STYMIED",
        "DRAMA", "AZURE", "ADVENTURE", "BEAR", "JOCKEY",
        "JIUJITSU", "MONEY", "IVY", "TRANSCRIPT", "LUXURY", "MNEMONIC",
        "MATRIX", "MICROWAVE", "PHONE", "ZODIAC", "ZOMBIE", "NUTRITION",
        "VIOLENCE", "FUNNY", "QUIXOTIC", "GOSSIP", "OXYGEN", "POWER", "GLYPH",
        "PEOPLE", "FLUFFINESS", "JAZZ", "BUZZ", "QUIZ", "BEER",
        "BEAR", "AWKWARD", "MEMORY", "DRAWING", "JACKPOT", "BUZZARD",
        "CYCLE", "TRANSPLANT", "VAPORIZE"]
    #pick a random word
    s = random.randint(0,49)
    random_w = words[s]
    return random_w

def stickman_draw(lives): 
    #συνάρτηση που εκτυπώνει για κάθε στάδιο ζωών το αντίστοιχο ανθρωπάκι
    """
    >>> stickman_draw(2)
    |---------|
    |         O
    |        /|\
    |         |
    |       _/ \_
    |
    |

    >>> stickman_draw(0)
    |---------|
    |         O
    |        /|\
    |         |
    |       _/ \_
    |       ## ##
    |       fire

    """ 
    
    parts = ["|---------|", "|         O", "|        /|\ ", "|         |", "|       _/ \_", "|       ## ##", "|       fire"]
    if lives==5:
        print("\n".join(parts[0:2])+("\n|"*5))
    elif lives==4:
        print("\n".join(parts[0:3])+("\n|"*4))
    elif lives==3:
        print("\n".join(parts[0:4])+("\n|"*3))
    elif lives==2:
        print("\n".join(parts[0:5])+("\n|"*2))
    elif lives==1:
        print("\n".join(parts[0:6])+("\n|"*1))
    elif lives==0:
        print("\n".join(parts))