#Call functions
from algorithms.word_list import Word_list
from algorithms.hangman import get_word
from algorithms.hangman import hangman
from algorithms.hangman import get_name
from algorithms.hangman import get_results
from algorithms.print_results import make_html
from algorithms.db import write_db

#Execute functions
get_name()
re_try="Y"
while re_try=="Y":
    get_word(Word_list)
    hangman()
    
#Chose to try again or exit game
    re_try=input("If you wish to try again, press Y else press N : ").upper()   

#Getting results
get_results()

#Printing results to txt,html and database 
make_html()
write_db()

