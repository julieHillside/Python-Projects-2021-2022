
def start():
    message = input("You can choose East, West, South, or North")
    first_choice(message)

def East_choices(choice):
    if choice == 'Y':
        print('You chose Y')
    elif choice == 'N':
        print('You chose N')
    else:
        choice = input('you need to chose something else')
    return choice

def first_choice(direction):
    if direction == "East":
        choice = input('Chose Y or N')
        East_choices(choice)
    elif direction == "West":
        print('You chose WEst')
    elif direction == "North":
        print('You chose North')
    elif direction == "South":
        print('You chose South')
    else:
        print('You did not chose a direction, try again')

