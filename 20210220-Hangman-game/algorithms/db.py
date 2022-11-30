#importing modules
import algorithms.hangman  as data
import mysql.connector
from mysql.connector import Error

 #Exception handling
try:
    conn=mysql.connector.connect(host="localhost",user="root",password='')

except Error as e:
    print("SERVER_ERROR ")
    print(e)

def write_db():
    "Inserting data into database"
    #Open database connection with a dictionary
    conDict={'host':'localhost','database':'Hangman_records','user':'root','password':''}
    db=mysql.connector.connect(**conDict)

    #Prepare a cursor object using cursor() method
    cursor=db.cursor()

    #Execute SQL query using execute () method 
    mySQLText="INSERT INTO final_results  VALUES (%s, %s, %s, %s);"
    mySQLvalues=[(data.user_name,data.win_count,data.loss_count,data.game_count)]
    cursor.executemany(mySQLText,mySQLvalues)
    
    for i in range(data.game_count):
        mySQLText="INSERT INTO game_results  VALUES (%s, %s, %s, %s, %s);"
        mySQLvalues=[((i+1),data.word_given[i],data.turns_given[i],data.turns_used[i],data.game_outcome[i])]
        cursor.executemany(mySQLText,mySQLvalues)


    #Commit the change
    db.commit()

    #disconnect from server
    db.close()

