## Lets make this test one time:

# Calling used libraries
from random import sample # For sampling results
import numpy # To do the if_else statement

# Creating a list with the number of possible options
list_of_doors = [1, 2, 3]
print(list_of_doors)

# Testing the sample function
print(sample(list_of_doors,1))

# Assignment of the prize
prize = int(sample(list_of_doors,1)[0])
print(prize)

# Choose the door
door_choosen = int(sample(list_of_doors,1)[0])
print(door_choosen)

# Open one of the doors you don't choose that don't have the prize
doors_to_remove = [door_choosen, prize]
list_of_doors = list(set(list_of_doors) - set(doors_to_remove))
print(list_of_doors)

# Checking if is better to change the door or not
result = numpy.where(door_choosen == prize, "Dont_change", "Change")
print(result)

## Now let's create a function to help us making this test multiple times
def MontyHall():
    # Creating a list with the number of possible options
    list_of_doors = [1, 2, 3]
    print(list_of_doors)

    # Testing the sample function
    print(sample(list_of_doors,1))

    # Assignment of the prize
    prize = int(sample(list_of_doors,1)[0])
    print(prize)

    # Choose the door
    door_choosen = int(sample(list_of_doors,1)[0])
    print(door_choosen)
    
    # Checking if is better to change the door or not
    result = numpy.where(door_choosen == prize, "Dont_change", "Change")
    return(result)

# Set the number of tries you want to test
number_of_tries = 10

# Count the number of times change the door = win the prize
change_is_win = 0

while True:
    try:
        option = int(input("Press 1 to see all runs or 0 to skip"))
        option in [1,2]
    except ValueError:
        print("Your input is out of parameters")
        continue
    else:
        break    

for i in range(number_of_tries):
    
    MontyHall()

    # Count number of times changing the door let you win
    count = numpy.where(result == 'Change', 1, 0)
    change_is_win = int(change_is_win) + int(count)

    if option == 1 :
        print("Test number " + str(i + 1))
        print("Prize: " + str(prize))
        print("Door Choosen: " + str(door_choosen))
        print("This time you must: " + str(result))

        # Chances of win changing the door
        print("Change door chances: " + str(int(change_is_win) / int(i + 1)))

# Chances of win changing the door
final_chances = str(int(change_is_win) / int(i + 1))
print("Change door chances: " + str(final_chances))

    