#Importing functions/modules
from os import system#Needed to interact with relevant file directories
import random 
import string
from algorithms.word_list import Word_list #Getting word list

#Defining variables
word=0
word_letters=0
lettters=0
guessed_letters=0
limbs=0
guessed_list=0
user_input=0
game_outcome=[]
turns_used=[]
turns_given=[]
word_given=[]
user_name=""
win_count=0
loss_count=0
game_count=0

#Defining functions
def get_word(Word_list):
    "Choosing random word from list"
    global word
    word=random.choice(Word_list)
    return word

def get_name():
    "Get user name"
    global user_name
    user_name=input("Enter user name here: ")
    return user_name

def get_results():
    "Get game results"
    global turns_used,turns_given,word_given,user_name,game_outcome,win_count,loss_count,game_count
    print( "Result for this game: ",game_outcome)
    print("You have won ",win_count," time/times")
    print("You have lost ",loss_count," time/times")
    print("You have played",game_count,"game/games")


def hangman():
    "Start main game function"
    global word,turns_used,turns_given,word_given,turns_given,turns_used,user_name,game_outcome,win_count,loss_count,game_count
    word_given.append(word)
    word_letters=set(word)
    lettters=set(string.ascii_uppercase)
    guessed_letters=set()

    limbs=len(word)#Determines no of tries user gets depending on length of the word

    #Reading inputs
    while len(word_letters) > 0 and limbs > 0:
        print("You have", limbs,"tries left") 

        #Letters left to guess currently
        guessed_list=(letter if letter in guessed_letters else "_" for letter in word )
        print("Current word: ", " ".join(guessed_list))

        #Taking user input
        user_input=input("Guess a letter : ").upper()
        if user_input in lettters - guessed_letters:
            guessed_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)

            else:
                limbs=limbs-1
                print("Incorrect guess, lives remaining: ",limbs)

        elif user_input in guessed_letters:
            print("LETTER HAS ALREADY BEEN GUESSED, TRY AGAIN!")

        else:
            print("INVALID INPUT")
        

    #Comes here when len(word_letters)==0 OR when limbs==0
    if limbs==0:
        print("YOU LOST!The word was",word)
        game_outcome.append("LOST")
    else:
        print("You guessed the word",word,"correctly!!","with",limbs,"tries remaining")
        game_outcome.append("WON")

    game_count=game_count+1
    win_count=game_outcome.count("WON")
    loss_count=game_outcome.count("LOST")
    
    print("You were wrong",len(word)-limbs,"times")

    turns_used.append(len(word)-limbs)#Append tries given and tries used
    turns_given.append(len(word))


    
    

   

                                                         
