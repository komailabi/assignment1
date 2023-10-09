""" This module defines two functions related : a dice roll system and a overall attribute points system , which defines if the character looses or wins.
The dice roll system, allows the player to roll two regular dices, and adds a bonus parameter based on the used attribute. 
The overallPoints function checks the overall attribute points of the player.
If the pointsOverall attribute is greater than or equal to 10, it prints a message indicating that the player has won. 
Otherwise, it prints a message indicating that the player has lost.
The purpose of the module is to implement and keep track of the game data and logic."""


import random
import role
#Function for a Dice Roll system, which determines the outcome of challenges
def diceRoll(bonus):
    while True:
        roll = input("Enter 'roll' to roll the dice: ")
        if roll.lower() == "roll":
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)

            total = dice1 + dice2

            print("You have rolled the two dice and your result is:", total , bonus)
            break
        else:
            print("Type roll")
            continue
    total += bonus #This adds the attribute to the total
    if total >= 2 and total <= 3:
        print("Critical Loss: Challenge is lost and the attribute based on is decreased.")
        role.health -= 3  # deduct 3 health points
        print("You lost and your health is now:", role.health)
    elif total >= 4 and total <= 7:
        print("Loss: Challenge is lost, no change in the character's attributes.")
        role.health -= 1  # deduct 1 health point
        print("You lost and your health is now:", role.health)
    elif total >= 8 and total <= 10:
        print("Win: Challenge is won, no change in the character's attributes.")
    elif total >= 11 and total <= 12:
        print("Critical Win: Challenge is won and the attribute based on increases.")

#Print message based on overall attribute points if the player won or lost
def overallPoints():
    if role.pointsOverall >= 10:
        print("You were able to hold the creature long enough in the sun and he starts to burn and vanish. You saved the humanity. Congratulations : You Won!")
    else:
        print("After an hard fought battle, you do not have enough energy to survive it's final attack. The creature kills you. You Lost!:")