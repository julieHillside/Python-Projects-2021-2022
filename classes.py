## understanding classes from Crash Course Python

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

print("My dog's name is " + my_dog.name)
print("My dog is " + str(my_dog.age) + " years old")

my_dog.sit()
my_dog.roll_over()

        