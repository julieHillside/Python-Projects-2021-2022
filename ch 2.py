# from Chapter 2 of Python Crash course

name = 'ada lovelace'
# print(name.title())
# 
# print(name.lower())
# print(name.upper())

# enter the first name
first_name = 'ada'
last_name = 'lovelace'

# full_name = f"Hello there {first_name.title()} {last_name.title()}!"
full_name = "Hello there " + first_name.title() + " " + last_name.title() + "!"
print(full_name)

for i in range(0, 100):
    num = i**100
    print(num)
