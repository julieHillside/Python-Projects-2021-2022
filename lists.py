# lists from Chapter 3 of Python Crash Course

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# print(bicycles[-2])

message = "my first bicycle was a " + bicycles[0].title()
# print(message)

# store a list of names of your friends (can be random names), in a list called
# names.  Print each person's name by accessing each element of the list
# one at a time.

# add to a list
# print(bicycles)
# bicycles.append('dirt bike')
# print(bicycles)
# 
# bicycles.insert(1, 'ducati')
# print(bicycles)
# 
# numbers = []
# for i in range(0, -10, -1):
#     numbers.append(i)
# print(numbers)
# 
# del bicycles[0]
# print(bicycles)

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)
# first_element = bicycles.pop(0)
# print(first_element)
# print(bicycles)

''' Guest list: If you could invite anyone, living or deceased to dinner, who would
you invite?  Make a list that includes at least 3 people you'd like to invite to
dinner.  Then use your list to print a message to each person, inviting them to
dinner'''

guests = ['Albert Einstein', 'Stephen Hawking', 'Abe Lincoln', 'Joe Biden', 'Maya Angelou', 'Kamala Harris', 'Adrienne Rich']

for guest in guests:
    print("hello there, you are invited to dinner " + guest)
    print("this should repeat")
print("this should come at the end and not repeat")
    
# for i in range(0,7):
#     print("You have been summoned " + guests[i])
    
'''Animals: Think of at least three different animals that have a common characteristic
Store the names of these animals in a list, and then use a for loop to print out the
name of each animal:

Modify your program to create a sentence about each animal, such as: "A dog would make
a great pet"

Add a line to the end of your program stating what these animals have in common
You could print a sentence such as, "Any of these animals would make a great pet" '''