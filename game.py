from utils import *

total_players = int(input("How many people want to play?\n"))
#create a list containing the name of each player
players = ()
for i in range(total_players):
    name = input("What's your name, player %d?\n" % (i+1))
    players += (name,)

#the letters of the alphabet
alpabeth = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

round = 0 #counting rounds
copy_players = list(players)
while len(copy_players) > 0:
    #make a list containing the words that have been used during the 2 latest rounds
    #and clean it every 2 rounds
    if (round % 2) == 0:
        used_words = []
    #for every active player
    for play in players:
        if play in copy_players:
            print(36*"*")
            print(play, "you have only 5 mistakes to make, while guessing letters. After that, you won't be able to play.")
            word = Random_Word()
            #check if the word picked by chance hase already been used in this game; if so, we randomly pick another one
            while (word in used_words) == True:
                word = Random_Word()
            used_words += [word]
            simplist = list(len(word)*"_")
            print("Your word is:", " ".join(simplist))
            found = False
            lives = 5
            #the current player gusses letters till he has no lives left or he founds the word
            while lives > 0 and found == False:
                guess = input("Guess a letter:")
                #check if the input is a valid capital letter of the english alphabet
                while guess not in alpabeth:
                    guess = input("Invalid input detected. Please, try again with a valid capital letter of the english alphabet:\n")
                #check if the word contains the guess
                if guess in word:
                    for i in range(len(word)):
                        if word[i]== guess:
                            simplist[i]= guess
                    if  "".join(simplist)== word:
                        print("Congratulations! You found the hidden word:", word)
                        found = True
                    else:
                        print("The word you have tou find is:", " ".join(simplist))
                else: 
                    #in case of a wrong guess, remove one from his remaining lives
                    stickman_draw(lives)
                    lives -= 1
                    print("Your word is:", " ".join(simplist))
                    print("You have", lives, "more lives.")
            #check if the player has lost
            if lives == 0:
                stickman_draw(0)
                print("Unfortunately, you did not manage to find the word: ", word, ".\nAs a result, the game is over for you, player:", play)
                copy_players.remove(play)
    #increse the number of round by 1
    round +=1
    if len(copy_players) == 1:
        print("Player:", copy_players[0], "you are the winner!")
        break

if len(copy_players) == 0:
    print("The game is over and no winner has been spotted :( ")