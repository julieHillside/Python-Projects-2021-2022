# ## Returning a simple value, from Python Crash Course
# 
# 
# artist = get_formatted_name('frida', 'calou')
# print(artist)
# 
# print("Jimi Hendrix")

## 1) create a simple function called display_message() that prints one sentence telling everyone what
## you are learning about in this chapter.  Call the function, and make sure the message displays
## corrently.
# 
# def display_message(parameter):
#     print("this is a message and you said, " + parameter)
# 
# display_message("argument")
# display_message('something else')
# display_message('another thing')

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

## 2) cities, write a function called describe_city() that accepts the name of a city and its country.
## The function should print a simple sentence, such as Reykjavik is in Iceland.  Call your function
## for 3 different cities in 3 different countries.  