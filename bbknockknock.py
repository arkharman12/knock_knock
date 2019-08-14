import datetime
now = datetime.datetime.now()           #importing datetime module
hour = now.hour

if 5 <= hour < 12:
    wishing = "Good morning!"
elif hour < 18:
    wishing = "Good afternoon!"         #greeting the user according to the current time
else:
    wishing = "Good evening!"


print("Welcome to My Super Magical Joke Generator\n")           #printing to the screen

def get_name():
    while True:
        global name                                                     #global variable is accessible from anywhere
        name = input("{} What is your name: ".format(wishing))          #using the .format() to greet the user

        if len(name) <= 2:
            print("Please enter a valid name.")                         #this whole function decides whether the user input is at least 3 letters long
            continue

        elif len(name) >= 3:
            return name
            continue
get_name()                                                      #calling the function

def access_name():                                              #defining a new function
  print("Here's a joke for you, {} \n".format(name))            #Accessing the gloabl variable here
access_name()                                                   #calling the function

whos_there = input("KNOCK, KNOCK: ")                            #getting user's input and storing in a variable
print("Boo")
whos_luke = input()                                                 #getting user input one more time
print("Gosh, don't cry it's just a knock knock joke. ;) \n\n\n")
print("Goodbye, {}!".format(name))                                  #printing goodbye to the screen with user's name

