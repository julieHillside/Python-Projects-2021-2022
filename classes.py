## understanding classes from Crash Course Python

"""Make a class called Restaurant.  The __init__() methodfor Restaurant should have
two attributes
a restaurant_name, and a cuisine_type Make a method called describe_restaurant()
that prints these
two pieces of info
and a method called open_restaurant() that prints a message indicating the restaurant
is open.
Make an instance called restaurant from your class.  Print the two attributes
individually, then
call both """



class Dog:
    """a simple attempt to model a dog"""
    def __init__(self, name, age):
        """initialize name and attributes"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name + " is now sitting")
        
    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(self.name + " rolled over")
        
my_dog = Dog('Willie', 6)
my_dog.roll_over()
'''Start with your class you just made, create 3 different instances of your class and call
describe_restaurant() for each instance'''
your_dog = Dog("fluffy", 3)

# def print_dog(instance):
#     print("My dog's name is " + instance.name)
#     print("My dog is " + str(instance.age) + " years old")
# 
#     instance.sit()
#     instance.roll_over()
#         
# # print_dog(my_dog)
# # print_dog(your_dog)
# 
# third_dog = Dog("Piper", 17)
# print_dog(third_dog)

