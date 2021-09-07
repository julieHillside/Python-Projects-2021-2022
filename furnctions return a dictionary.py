## Returning a dictionary from Python Crash Course

## write a while loop that allows users to enter an album's artist and title.
## Once you have that information, call make_album() with the user's input and
## print the dictionary that's created.  Be sure to include a quit value in the
## while loop.

## for Elliot:  Write a while loop that takes information from a function called plant_id(), give
## it two parameters, species and genus of the plant and the common name too.  Make it up, that's okay
## the while loop should take the input from the user, and then return a dictionary with the information
## about the plant.  

def build_person(first_name, last_name):
    person = {'first' : first_name.title(), 'last': last_name.title()}
    return person

musician = build_person('jimi', 'hendrix')
print("There is a musician called " + musician['first'] + " " + musician['last'])

# def get_formatted_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# 
# while True:
#     print("/nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#     
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("Hello " + formatted_name)
#     if f_name or l_name == 'quit':
#         break