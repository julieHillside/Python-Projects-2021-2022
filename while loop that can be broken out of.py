## from Crash course in Python

prompt = "\n Tell me something, and I will repeat it back to you"
prompt += "\n Enter 'quit' to end the program."

message = ""

while message != 'quit':
    message = input(prompt)
    print(message)