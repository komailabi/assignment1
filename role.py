"""This module contains a function called roleselection() that allows the user to select a role between "Jerome" and "Hafid". 
Depending on the user's selection, the function assigns values to the variables intelligence, strength, intuition, and health.
It also prints out the selected role's stats.
The intelligence, strength, intuition, and health variables are initially set to 0, but after a role is selected, the function updates the values based on the chosen role.
If the user enters and invalid selection, other then the mentioned roles, an error message is being displayed.""" 

#Define Roles and the attributes, Max amount of overall attributes are 15. Lowest amount of overall attributes are 0.

intelligence = 0
strength = 0
intuition = 0
health = 10
pointsOverall = intelligence + strength + intuition + health

#Function to prompt user, to choose between two roles, using if-statements
def roleselection():
    print('Select your role')
    print("The two roles available, are 'Jerome' and 'Hafid'. Both of them are students. 'Jerome' is more intelligent, but physically weak. 'Hafid' shines through physical strength and intuition.")
    print("His weakness is his intelligence. Choose wisely.")
    selection = input("Do you want to play 'Jerome' or 'Hafid'? : ")
    if selection.lower() == "jerome": #If 'Jerome' is selected the stats are getting updated to the values underneath
        intelligence = 2
        strength = -1
        intuition = 1
        health = 10
        print("You have selected Jerome... These are his stats...") #Displaying 'Jeromes' stats after selection, using print statement
        print("Intelligence:", intelligence)
        print("Strength:", strength)
        print("Intuition:", intuition)
        print("Health:" , health)
      
    
    elif selection.lower() == "hafid": #If 'Hafid' is selected the stats are getting updated to the values underneath
        intelligence = -1
        strength = 1
        intuition = 2
        health = 10
        print("You have selected Hafid... These are his stats...") #Displaying 'Hafids' stats after selection, using print statement
        print("Intelligence:", intelligence)
        print("Strength:", strength)
        print("Intuition:", intuition)
        print("Health:" , health)
        
    
    else:
        print("Only enter 'Jerome' or 'Hafid'") #Displaying error message, if an invalid selection is entered
        
roleselection()