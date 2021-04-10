from utils import *

total_players = int(input("Πόσα άτομα θα παίξουν;"))
#κατασκευή λίστας με τα ονόματα των παικτών
players = ()
for i in range(total_players):
    name = input("Δώσε το όνομά σου:")
    players += (name,)

#γράμματα της αλφαβήτου που θα χρησιμοποιηθούν
alpabeth = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"

round = 0 #μέτρηση των γύρων του παιχνιδιού
copy_players = list(players)
while len(copy_players) > 0:
    #κατασκευή λίστας με τις λέξεις που έχουν χρησιμοποιηθεί σε αυτόν και στον επόμενο γύρο, θα διαγράφονται τα στοιχεία ανά 2 γύρους
    if (round % 2) == 0:
        used_words = []
    #επανάληψη του παιχνιδιού για κάθε παίχτη στον τρέχων γύρο
    for play in players:
        if play in copy_players:
            print(36*"*")
            print(play, "έχεις περιθώριο να μαντέψεις 5 λάθος γράμματα. Η έκτη αποτυχία θα σε αποκλείσει από το παιχνίδι.")
            word = Random_Word()
            #έλεγχος εάν η τυχαία λέξη έχει χρησιμοποιηθεί ή όχι ώστε να επιλεγεί άλλη αν χρειάζεται
            while (word in used_words) == True:
                word = Random_Word()
            used_words += [word]
            simplist = list(len(word)*"_")
            print("Η λέξη που πρέπει να μαντέψεις είνα:", " ".join(simplist))
            found = False
            lives = 5
            #ο παίκτης μαντεύει γράμματα μέχρι να του τελειώσουν οι ζωές ή να κερδίσει
            while lives > 0 and found == False:
                guess = input("Δώσε γράμμα:")
                #έλεγχος εάν το γράμμα δεν περιέχεται στο αλφάβητο επιστρέφει μήνυμα
                while guess not in alpabeth:
                    guess = input("Ο χαρακτήρας που έδωσες δεν ανήκει στο αλφάβητο. Δώσε κεφαλαίο ελληνικό γράμμα:")
                #έλεγχος εάν ο χρήστης μάντεψε σωστά το γράμμα κι εμφανισή του
                if guess in word:
                    for i in range(len(word)):
                        if word[i]== guess:
                            simplist[i]= guess
                    if  "".join(simplist)== word:
                        print("Συγχαρητήρια! Βρήκες τη λέξη:", word)
                        found = True
                    else:
                        print("Η λέξη που πρέπει  να μαντέψεις είναι:", " ".join(simplist))
                else: 
                    #εάν δε μάντεψε σωστά αφαιρείται μία ζωή και εμφανίζεται η κρεμάλα
                    stickman_draw(lives)
                    lives -= 1
                    print("Η λέξη που πρέπει να μαντέψεις είναι:", " ".join(simplist))
                    print("Έχεις ακόμα", lives, "ζωές.")
            #γίνεται έλεγχος εάν τελικά έχασε, εφόσον ναι εκτυπώνεται ολόκληρο το ανθρωπάκι και μήνυμα αποτυχίας
            if lives == 0:
                stickman_draw(0)
                print("Δυστυχώς δε κατάφερες να μαντέψεις τη λέξη:", word, "για αυτό αποκλείστηκες από το παιχνίδι παίκτη:", play)
                copy_players.remove(play)
    #αύξηση των αριθμών των γύρων κατά 1
    round +=1
    if len(copy_players) == 1:
        print("Παίκτη:", copy_players[0], "είσαι ο νικητής!")
        break

if len(copy_players) == 0:
    print("Το παιχνίδι τελείωσε χωρίς κανένα νικητή.")        
