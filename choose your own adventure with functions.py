
def start():
    message = input("You can choose East, West, South, or North")
    first_choice(message)
    
def one(info1):
    if info1 = 'a':
        infoA = input('you chose a, ')
    
def Y_choice(pick):
    if pick == 1:
        info1= input('you chose 1 now pick a letter, a, b, c')
        one(info1)
    elif pick == 2:
        two(info)
    elif pick == 3:
        three(info)
    else:
        info = input("please chose a valid response, 1,2,3")
        Y_choice(info)
        
def East_choices(choice):
    if choice == 'Y':
        info1 = input("You chose Yes, now which do you choose, 1, 2,3")
        Y_choice(info1)
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

start()