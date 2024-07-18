'''
Name: Akash Lakshmanan
Date: 2021-09-20
Title: Coding Unit Assignment - ROCK, PAPER, SCISSORS, SPOCK and LIZARD
Description: This program will allow the users to play the Rock/Paper/Scissor game with computer for 5 rounds per game. Also, will allow them to continue playing until they want to quit.
Last Modified: 2021-09-26
'''

import time
#Import time is the delay after the results load up
import random
#Import random is for generating random numbers and various other functions

#General instructions about the GAME
print("This game is called ROCK, PAPER, SCISSOR, LIZARD and SPOCK")
print("")
print("This game will have 5 rounds (First to reach 3 wins will be declared a WINNER)")
print("")
#Listing all the possible options that user can input
print("ROCK=(r), PAPER=(p), SCISSOR=(s),SPOCK=(o), LIZARD(l) - THESE SHOULD BE YOUR CHOICES FOR THE ENTIRE GAME")
#Assigning values to Variable names
ROCK='r'
#Variable name= ROCK. This is a string that lets the user choose their input in this game
PAPER='p'
#Variable name= PAPER. This is a string that lets the user choose their input in this game
SCISSOR='s'
#Variable name= SCISSOR. This is a string that lets the user choose their input in this game
SPOCK='o'
#Variable name= SPOCK. This is a string that lets the user choose their input in this game
LIZARD='l'
#Variable name= LIZARD. This is a string that lets the user choose their input in this game

computerSelect=0
#Variable name=computerSelect. This is an integer variable that allows the program to keep track of random select
computerScore=0
#Variable name=computerScore. This is an interger variable that allows the program to keep track of computer score
userSelect=0
#Variable name=userSelect. This is an integer variable that allows the program to keep track of user select
userScore = 0
#Variable name=userScore. This is an interger variable that allows the program to keep track of user score

print("")
print("The Game will begin Right Now")

while True:
 for roundcounter in range (5):
   #This is a for loop.  This is used to change the amount of rounds the user can play. I have set it to 5 Rounds.
   print("**********************","\t\n        ROUND "+str(roundcounter+1))
   print("**********************")
   
   #Letting user pick the choice
   while True:
     #While loop to be excuted until user picks the right choice. Break command is for not letting the program crash
     userSelect=input("Your Choice     : ")
     if (userSelect==ROCK) or (userSelect==PAPER) or (userSelect==SCISSOR) or (userSelect==LIZARD) or (userSelect==SPOCK):
       break
     else:
       print("Error, WRONG INPUT (PLEASE READ THE INSTRUCTIONS ONCE AGAIN)")
       #error message of wrong input
   
   #Letting computer pick the choice
   computerSelect = random.choice("rpsol")
   print("Computer choice : "+ computerSelect)

   #Apply rules of the GAME to decide on the winner (21 different combinations, including DRAW)
   #Checking for Draw between User & Computer choices
   if userSelect == computerSelect:
     print("Oops. You DREW with computer. Try hard to beat the computer.")

   #First set of rules while userSelect = ROCK
   elif userSelect == ROCK and computerSelect == PAPER:
     computerScore=computerScore+1
     print("Computer Won this round. NEVER GIVE UP. Try again.")

   elif userSelect == ROCK and computerSelect == SCISSOR:
     userScore=userScore+1
     print("This is your day. You WON the round. Keep going.")

   elif userSelect == ROCK and computerSelect == SPOCK:
     computerScore=computerScore+1
     print("Computer Won this round. NEVER GIVE UP. Try again.")

   elif userSelect == ROCK and computerSelect == LIZARD:
     userScore=userScore+1
     print("This is your day. You WON the round. Keep going.")

   #First set of rules while userSelect = PAPER
   elif userSelect == PAPER and computerSelect == ROCK:
     userScore=userScore+1
     print("This is your day. You WON the round. Keep going.")

   elif userSelect == PAPER and computerSelect == SCISSOR:
     computerScore=computerScore+1
     print("Computer Won this round. NEVER GIVE UP. Try again.")

   elif userSelect == PAPER and computerSelect == SPOCK:
     userScore=userScore+1
     print("This is your day. You WON the round. Keep going.")
     
   elif userSelect == PAPER and computerSelect == LIZARD:
     computerScore=computerScore+1
     print("Computer Won this round. NEVER GIVE UP. Try again.")

    #First set of rules while userSelect = SCISSOR
   elif userSelect == SCISSOR and computerSelect == ROCK:
     computerScore=computerScore+1
     print("Computer Won this round. NEVER GIVE UP. Try again.")

   elif userSelect == SCISSOR and computerSelect == PAPER:
     userScore=userScore+1
     print("This is your day. You WON the round. Keep going.")

   elif userSelect == SCISSOR and computerSelect == SPOCK:
     computerScore=computerScore+1
     print("Computer Won this round. NEVER GIVE UP. Try again.")

   elif userSelect == SCISSOR and computerSelect == LIZARD:
     userScore=userScore+1
     print("This is your day. You WON the round. Keep going.")

    #First set of rules while userSelect = SPOCK
   elif userSelect == SPOCK and computerSelect == ROCK:
     userScore=userScore+1
     print("This is your day. You WON the round. Keep going.")

   elif userSelect == SPOCK and computerSelect == PAPER:
     computerScore=computerScore+1
     print("Computer Won this round. NEVER GIVE UP. Try again.")

   elif userSelect == SPOCK and computerSelect == SCISSOR:
     userScore=userScore+1
     print("This is your day. You WON the round. Keep going.")
  
   elif userSelect == SPOCK and computerSelect == LIZARD:
     computerScore=computerScore+1
     print("Computer Won this round. NEVER GIVE UP. Try again.")

    #First set of rules while userSelect = LIZARD
   elif userSelect == LIZARD and computerSelect == ROCK:
     computerScore=computerScore+1
     print("Computer Won this round. NEVER GIVE UP. Try again.")

   elif userSelect == LIZARD and computerSelect == PAPER:
     userScore=userScore+1
     print("This is your day. You WON the round. Keep going.")

   elif userSelect == LIZARD and computerSelect == SCISSOR:
     computerScore=computerScore+1
     print("Computer Won this round. NEVER GIVE UP. Try again.")

   elif userSelect == LIZARD and computerSelect == SPOCK:
     userScore=userScore+1
     print("This is your day. You WON the round. Keep going.")
     
   if userScore == 3 or computerScore == 3:
      break
 print("************************")
 print("")
 print("")
 print("THE GAME HAS ENDED\t Results loading up")
 #printing the Results after tha game and setting up the time delay option
 time.sleep(2)
 print("")

 #Comparing the User and Computer score to declare the winner
 if userScore > computerScore:
   print("Good News. Congrats YOU WON the GAME.")
   print("")
   print(f"FINAL SCORE     :    comp - {computerScore}, player - {userScore}")
   print("")
   print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
   print("")
   reset = input("If you would like to play again, KEY in (y)YES,n(NO): ")
   #If the user would like to play again

 elif userScore < computerScore :
   #elif statement
   print("Sorry, You lost. GOOD LUCK next time")
   print(f"FINAL SCORE     :    comp - {computerScore}, player - {userScore}")
   print("")
   print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
   print("")
   reset = input("If you would like to play again, KEY in (y)YES,n(NO): ")
   
 else:
   print("Close Game. You DREW the game with Computer.")
   #Very rare option, if choices between User & Computer were the same atleast in 1 round
   print("")
   print(f"FINAL SCORE     :    comp - {computerScore}, player - {userScore}")
   print("")
   print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
   print("")
   reset = input("If you would like to play again, KEY in (y)YES,n(NO): ")

#Following lines of code would allow the user to reset the game counter and continue playing
 if reset == "y":
   #If user wants to play again than they press y
   #resetting the userscore and computerscore variables
   computerScore = 0
   userScore = 0
   print("")
   continue

 elif reset == "n":
   #If user does not want to play again they input the letter n
   print("")
   print("Thank you for playing the Game. Hope to see you soon.")
   break

  #Will ask the user to keep inputing until he keys in y or n 
 else:
   while reset != "y" and reset != "n":
      print("")
      print("You Have Entered A Wrong Letter, PLEASE TRY AGAIN.")
      reset = input("If you would like to play again, KEY in (y)YES,n(NO): ")
   #If user enters a incorrect letter, the program tells them they have entered a wrong letter
   #resetting the userscore and computerscore variables
   computerScore = 0
   userScore = 0
   continue
   #END OF THE PROGRAM