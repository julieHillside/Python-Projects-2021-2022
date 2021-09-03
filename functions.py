# functions from Crash course in Python

def greet_user(username):
    print("Hello " + username)
    


## create a function called favorite_book() that accepts one parameter, title.
## the function should print a message, such as "one of my favorite books is
## Alice in Wonderland", Call the function, making sure to include a book title
## as an argument in the function call.
    
def describe_pet(animal_type, pet_name):
    print("I have an " + animal_type)
    print("My " + animal_type + "'s name is " + pet_name.title())
    
animals = {'rabbit': 'Sarah', 'gerbil':'George', 'chinchilla': 'Chuck'}

for animal_type, animal_name in animals.items():
    describe_pet(animal_type, animal_name)