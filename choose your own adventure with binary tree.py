text001 = "You are a hero on an ancient quest.  Your quest is to go to the land of the elves and ask them for help with your kingdom.  your kingdom is experiencing crop failure and you need their magical healing power to help you.  The elves are very shy, and will require payment.  You don't have very much money.  You wish to go about getting more money.  Do you A) start a fundraiser hosted by the king in order to earn more money, or B) work really hard and ask your relatives and friends for money?"

text002A = "You decide to host a fundraiser with the king's help.  The king was rather broke too because there have been a number of bad years of grain crops.  The king is starting to worry that the barbarians will come and overrun the kingdom.  The king and you ask the northern neighbors for help and hold a gala ball in order to sway them.  The gala is going well and the northern neighbors pledge their support.  You get the money you need and go to the elves.  When you get to them, you find that their kingdom has been sacked by the Barbarians.  Do you A) send word to the king and ask for help or B) try to find help yourself? "

text002B = "You work very hard in the fields all day, since you are a farmer, working in the hot sun.  This is a bad year for grain though, and you do very poorly.  At the end of the summer you have very little to show for your efforts.  You have barely enough for your family.  Do you A) save your food and carefully try to get through the winter on what you have or B) Try to go out and learn another trade to get more money for your family?"

text003A = "You send word to the King asking for help.  Your best messenger is a pegasus that you find tethered inside the burned out elven castle.  the Pegasus carries you high into the sky.  You also find a little bit of money in the castle, which you put inside your wallet.  On the way to find the king, you see a band of elves who escaped the barbarians on the ground.  You go to them and find that they are in need of help.  You offer to help them in exchange for some healing magic on your fields.  Do you A) fly home right away and work on your fields with their help or B) explore further in case you find more elves?"

text003B = "text3B"
text004A = "You decide to save your little bit of food and your family barely scrapes by the winter.  It is also a very cold winter.  One day, in the middle of the winter you are out in the forest and you see a magical elk wandering about.  Do you A) hunt and kill the elk for food, or B) try to follow the elk and see where it lives?"

text004B = "You decide to become a blacksmith, and start learning the trade from the local blacksmith in town.  You give him lots of free labor in exchange for learning how to make cool things out of metal.  You learn how to make swords and axes, and shields and plows, and all your useful iron age swag.  As you are learning the skills, a witch comes into town one day wanting to offer you a shortcut, she will give you 3 wishes if you will only steal the best sword from your friend the blacksmith.  You feel very loyal to the blacksmith, he has been kind to you, but 3 wishes would be marvelous and could help you out of your financial troubles. Do you A) steal from the blacksmith to get the wishes from the witch, or B) tell the witch thanks but no thanks and carry on?"

text005A = "You decide to fly home right away, you are carrying two elven children who are very skilled in earth healing magic.  They come to your field and begin the chanting and dancing and soon the fields are growing before your eyes, full to the brim with delicious food.  You take the elf children home to their parents and keep the Pegasus.  Your fields now produce so much food that you have a great surplus.  Do you A) hog all the food for yourself, or B) share with your hungry neighbors?"

text005B = "You decide to fly back and help the elves, they are very grateful, and you fly many of them back to your kingdom.  After explaining to your fellow countrypeople that these elves have healing magical qualities, many of your friends decide to take them in and help them in return for some magic.  Fun things start happening all over the  countryside, elves are playing tricks and having fun and everyone is laughing. Choose A or B to continue"

text006A = "text6A"
text006B = "text6B"
text007A = "text7A"
text007B = "text7B"
text008A = "text8A"
text008B = "text8B"

text009A = "You decide to hog all the food for yourself.  You are very selfish, and your neighbors start sneaking into your fields at night to take some.  After a time, you become known as a miser, and your neighbors despise you.  Eventually they shun you and won't trade with you and you are impoverished, but not hungry.  Press A or B to continue."

text009B = "You are very generous indeed and share with your neighbors.  People from all over the land come to share in your wealth and you hold a great banquet.  You become known as a great person, giving out so much to those who need it.  Eventually, you go back and help the elves some more and they continue helping people all over the kingdom.  Press A or B to continue"



#I wrote all this, and then realized I should use classes.
#I'll use classes later.  

def validate(val, a,b):
    while not (val == a or val == b):
        val = input("Invalid entry, choose " + a + " or " + b + ": ")
    return val

#add an option to go back.  
def choice(text):
    print(text)
    val1 = input("Choose A or B : ")
    val1 = validate(val1, "A", "B")
    #val1 is either A or B
    return val1
        
def direction(storyID, newAorB):
    #slice next choice into either A or B
    AorB = storyID[7:]
    #slice next choice into the integer indicating the next step,
    #right now only deals with single digits
    nextInt = storyID[4:7]
    if AorB == "A":
        #the A portion of the binary tree has doubled but odd integer next up
        fork = 2*int(nextInt)-1
    else:
        #the B portion of the binary tree has doubled integers up. 
        fork = 2*int(nextInt)
    #this gives the next story id text to the next part.  
    if fork < 9:
        newStoryID = "text" + "00" + str(fork) + newAorB
    elif fork >9 <20:
        newStoryID = "text" + "0" + str(fork) + newAorB
    else:
        newStoryID = "text" + str(fork) + newAorB
    return newStoryID


def story():
    AorB = choice(text001)
    newStoryID = "text002" + AorB
    
    while newStoryID in globals():
        AorB2 =choice(globals()[newStoryID])
        newStoryID = direction(newStoryID, AorB2)
        
    
    #plotnext =choice(globals()[nextchoice])

    print("The End")