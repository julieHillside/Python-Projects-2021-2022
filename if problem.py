message = input("enter a word, 'north, 'south', 'east', 'west'")

while True:
    if message == 'east':
        message = input('choose a new topic')
    elif message == 'west':
        message= input('you typed West, now tell me y or n')
        if message == 'y':
            print('you typed Y')
        elif message == 'n':
            print('you typed N')
        else:
            message = input('You did not type y or n, do you wish to choose a direction?')
    elif message == 'north':
        print('you typed North')
    elif message == 'south':
        message = input('you typed South')
        
    else:
        message = input('you need to type a direction')
    

