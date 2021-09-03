## Returning a simple value, from Python Crash Course

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

artist = get_formatted_name('frida', 'calou')
print(artist)