"""This module contains various functions, which represent challenges for the game. The function "challengeOne" prompts the user to make a decision at the bus stop. 
The function "showMonster" presents the user with options to either run or fight a creature. 
The function "challengeTwoIfWin" prompts the user to choose between two paths. 
The function "challengeThree" asks the user if they want to save themselves or fight the creature. 
After completing these challenges, the function "overallPoints" calculates and displays the overall points of the characters in the game and decides if the player won or lost."""


#Import required modules such as diceRoll for the dice rolling system , role to access the attributes of the roles, game to access the overall points of the characters
from game import diceRoll
from game import overallPoints
import role

#Prompt user to start the game or exit it


""" This module contains the function "challengeOne" which presents the first challenge of the game. 
The function prompts the user to make a choice: whether to leave the bus stop or wait for the bus to come. The function then enters a loop where it repeatedly asks the user for a direction (left, right, or stay).
Regardless of the choice, the function calls the "showMonster" function and breaks out of the loop.
The "showMonster" function displays a message saying "that something was actually observing the user and a black creature is coming towards them." 
It then enters a loop where it asks the user if they want to run or fight. 
If the user chooses to run or fight, the function uses the ability "strength" for a dice roll, and presents the results."""

#Create while loop which prompts user to make a decision for the first challenge
def challengeOne():
    print("You are at the bus stop. You feel like something is observing you. It is time to make a choice: Do you want to leave the bus stop or wait for the bus to come?")
    
    while True:
        print("Your options: left / right / stay")
        userInput = input("Pick a direction: ")
        
        if userInput.lower() == "left":
            showMonster()
            break
        if userInput.lower() == "right":
            showMonster()
            break
        if userInput.lower() == "stay":
            showMonster()
            break
        else:
            print("Pick one of the options:")
            continue
#Create while loop which prompts user to decide whether to fight the monster or not after it appears for the first time
def showMonster():
    print("Oh No! Something was actually observing you. A black creature is coming towards you!")
    
    while True:
        print("Your options: run / fight")
        userInput = input('Do you want to run or fight? :')
        
        if userInput.lower() == "run":
            print("You chose to run away!")
            print("The creature is considerably faster than you, it lashes out and you have to try to block the hit")
            print("The ability 'strength' is going to get used for that. Roll the dice to complete this action")
            diceRoll(role.strength) #Bonus Parameter for the dice roll system
            print("There are two ways. You can either run on the wide main road or go through the dense forest.")
            break
            
        if userInput.lower() == "fight":
            print("You chose to fight!")
            print("You try to hit the creature.")
            print("The ability 'strength' is going to get used for that. Roll the dice to complete this action")
            diceRoll(role.strength) #Bonus Parameter for the dice roll system
            print("After a long battle. There is the opportunity to run away. ")
            break
            
        else:
            print("Pick one of the options")
            continue
            

challengeOne()

""" This module contains the function "challengeTwo" which presents the second challenge of the game. 
The function prompts the user to make a choice: whether to enter the main road or forest. The function then enters a loop where it repeatedly asks the user for a choice (main road / forest).
Regardless of the choice, the function calls the "showMonster" function and breaks out of the loop. 
If the user chooses the main road or the forest, the function uses the ability "intelligence" for a dice roll, and presents the results."""

#Create while loop which prompts user to make a decision for the second challenge
def challengeTwoIfWin():
        print("Your options: main road / forest ")
        while True:
            userInput = input("Which way are you using? : ")
            if userInput.lower() == "main road":
                print("You chose the main road!")
                print("The wide area of the main road might be beneficial for the fast creature, but there is only one way to find out.")
                print("The ability 'intelligence' is going to get used for that. Roll the dice to complete this action")
                diceRoll(role.intelligence) #Bonus Parameter for the dice roll system
                break
            
            elif userInput.lower() == "forest":
                print("You chose the forest!")
                print("The dense forest makes it hard for the creature to see you, but you don't know if it can sense your presence")
                print("There is only one way to find out.")
                print("The ability 'intelligence' is going to get used for that. Roll the dice to complete this action")
                diceRoll(role.intelligence) #Bonus Parameter for the dice roll system
                break
            
        
            else:
                print("Pick one of the options:")
                continue
            

challengeTwoIfWin()


""" This module contains the function "challengeThree" which presents the third and final challenge of the game. 
The function prompts the user to make a choice: whether to safe yourself or fight the creature. The function then enters a loop where it repeatedly asks the user for a choice (safe yourself, fight it ).
After making the choice, the loop breaks.
If the user chooses to safe yourself or fight it, the function uses the ability "intuition" for a dice roll, and presents the results."""

#Create while loop which prompts user to make a decision for the third challenge
def challengeThree():
        print("The creature stands right in front of you. The sun is about to rise. ")
        print("He starts burning, once the sunrays hit him. He is about to flee.")
        print("Do you want to save yourself and let him flee, or try to stop him so the sun burns him and no other human has to ever face it? ")
        print("Be aware! Attacking him could save humanity but cost your own life! But saving yourself could end up in an unexpected attack!")
        print("Your options: safe yourself / fight it ")
        userInput = input("What are you deciding to do? : ")
        
        while True:
            if userInput.lower() == "safe yourself":
                print("You chose to safe yourself!")
                print("You gave the creature the opportunity to launch an final attack, before he flees back to the shadows! ")
                print("The ability 'intuition' is going to get used for that. Roll the dice to complete this action")
                diceRoll(role.intuition) #Bonus Parameter for the dice roll system
                break
                
            elif userInput.lower() == "fight it":
                print("You chose to fight it!")
                print("You jump on him! You try everthing to prevent him from moving and the sun keeps on burning him!")
                print("Are you able to hold him for long enough?")
                print("The ability 'intuition' is going to get used for that. Roll the dice to complete this action")
                diceRoll(role.intuition) #Bonus Parameter for the dice roll system
                break
                
            
            else:
                print("Pick one of the options:")
                continue
        

challengeThree()
overallPoints()