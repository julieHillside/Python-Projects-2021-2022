while True:
    message = input("You are on a quest, you have 4 items, a sabre, a potion, bow and arrow, shield which do you use?  A) sabre, B) potion, C) bow and arrow, D) shield")
    if message == 'A':
        message1 = input("Okay, you chose a sabre!  You will slay many enemies, choose option A and B")
        if message1 == 'A':
            print('You chose A')
        else:
            print('You chose something other than A')
    elif message == 'B':
        message2 = input("Okay, you chose a potion, etc...")
    elif message == 'C':
        print('C bow and arrow')
    elif message == 'D':
        print('D shield')
    else:
        print('please enter a valid response needs to be capitalized')
