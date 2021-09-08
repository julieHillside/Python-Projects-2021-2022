# number = 4
# 
# print(number==4)
# 
# # Boolean is a True or False value
# 
# cars = ['audi', 'bmw', 'subaru', 'toyota']
# 
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
        
# animal = 'squirrel'
# print(animal == 'Squirrel')
# 
# requested_pizza_topping = 'mushrooms'
# 
# if requested_pizza_topping != 'anchovies':
#     print("Hold the Anchovies!")
#     
# 
# answer1 = int(17)
# while True:
#     answer = int(input("Enter a guess for the age"))
#     if answer != answer1:
#         print("That is not the correct answer.  Please try again.")
#     else:
#         print("Good job, you guessed it!")
#         break
# 
# var1 = int(2)
# var2 = 2.0
# 
# print(var1 == var2)

# use if/else statements and input to create a choose your own adventure game.

story = input("You are in a dark forest, which way do you go (N, E, S, W)")
if story == 'N':
    story1 = input("You chose North, you see a stream ahead, do you cross it? Y N")
    if story1 == 'Y':
        print("You chose to cross the Stream")
    elif story1 == 'N':
        print("You did not cross the stream")
    else:
        print("please enter a valid response")
elif story == 'E':
    print("you went East")
elif story == 'S':
    print("you went South")
elif story == 'W':
    print("you went West")
else:
    print("Please enter a valid response")