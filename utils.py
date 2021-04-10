def Random_Word():
    #επιστρέφει μία τυχαία λέξη από προκαθορισμένο λεξικό 50 λέξεων
    import random
    words = ["ΚΛΟΥΒΙ", "ΚΛΕΙΔΙ", "ΨΥΧΟΦΘΟΡΟΣ", "ΚΑΛΟΚΑΙΡΙ", "ΑΚΡΟΓΥΑΛΙΑ", "ΡΥΑΚΙ", 
        "ΑΥΤΟΚΙΝΗΤΟ", "ΘΑΛΑΣΣΑ", "ΓΑΣΤΡΕΝΤΕΡΙΤΙΔΑ", "ΔΙΑΜΟΝΗ", "ΣΚΟΠΕΛΟΣ",
        "ΔΡΑΜΑ", "ΜΥΘΙΣΤΟΡΗΜΑ", "ΠΕΡΙΠΕΤΕΙΑ", "ΑΡΚΟΥΔΑ", "ΟΘΟΝΗ",
        "ΨΥΧΟΛΟΓΙΑ", "ΛΕΦΤΑ", "ΑΠΟΓΡΑΦΗ", "ΟΓΚΟΣ", "ΓΛΕΙΦΥΤΖΟΥΡΙ", "ΜΟΥΣΙΚΗ",
        "ΦΟΙΝΙΚΑΣ", "ΣΤΟΧΟΣ", "ΚΙΝΗΤΟ", "ΚΑΛΟΥΠΙ", "ΘΗΣΑΥΡΟΣ", "ΤΡΟΦΗ",
        "ΒΙΑ", "ΧΑΡΑ", "ΠΕΡΙΠΑΤΟΣ", "ΤΡΑΜΠΟΥΚΟΣ", "ΠΑΣΤΑ", "ΔΥΝΑΜΗ", "ΖΑΡΙ",
        "ΛΑΟΣ", "ΠΑΡΟΙΜΙΑ", "ΓΕΡΟΝΤΟΚΟΡΗ", "ΡΑΦΙ", "ΤΟΡΝΑΔΟΡΟΣ", "ΖΥΘΟΣ",
        "ΚΟΥΜΠΑΡΑΣ", "ΠΡΟΝΟΜΙΟ", "ΜΝΗΜΗ", "ΖΩΓΡΑΦΙΑ", "ΤΕΡΨΗ", "ΜΗΧΑΝΟΡΡΑΦΩ",
        "ΦΑΚΟΣ", "ΔΡΑΚΟΣ", "ΙΠΠΟΚΑΜΠΟΣ"]
    #τυχαία θέση της λέξης στη λίστα-λεξικό
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

