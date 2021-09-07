## Using a function with a While Loop

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

# x = 0
# while x < 5:
#     print(x)
#     x += 1

while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
#     if f_name or l_name == 'quit':
#         break
    formatted_name = get_formatted_name(f_name, l_name)
    print("Hello " + formatted_name)
   
