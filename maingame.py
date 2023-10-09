""" Print game introduction and explain the setting of the game, using print statements. The user is being prompted to to input whether they want to start the game or not.
Other various functions from other modules are being imported, like the role selection, the challenges and the overall point system, which decides the outcome of the game.
The purpose of this module is, to have a neat module, where you can run the game."""

#Print Game introduction

print("Welcome to BUS STOP.")
print("After a long day as a student, you try to go home by bus like always.")
print("However on this foggy winter day, something is different.")
print("Waiting for your bus, you feel observed. There's something looking at you.")
print("Can you trust your intuition and make the right choices to escape this situation?")

#Prompt user for input to decide whether they want to start the game or not

startGame = (input("Do you want to start the game? Answer with Yes or No : "))

if startGame.lower() == ("yes"):
    print("Great. You can choose between two characters.")
elif startGame.lower() == ("no"):
    print("Comeback another time!")

#Allow User to choose between two characters

from role import roleselection    #import roleselection function

from app import challengeOne #import the first challenge 'challengeOne' from the app.py module

from app import challengeTwoIfWin #import the second challenge 'challengeTwoIfWin' from the app.py module

from app import challengeThree #import the third challenge 'challengeThree' from the app.py module

from game import overallPoints #import the Win/Loss system 'pointsOverall' from the game.py