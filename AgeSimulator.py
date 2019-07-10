import time
import sys

#creates a custom error message
def my_except_hook(exctype, value, traceback):
        print('Sorry, please try again. Insert another value.')
        exit()


sys.excepthook = my_except_hook


def start():    #initializes the game and gets the three user inputs that will be used throughout the game
    print("Welcome to age simulator. Here I will magically reveal your age from months down to seconds!!!")

    name = str(input("Please Enter Your Name Here:"))

    x = int(input("Enter your age in years here:")) #age in years

    y = int(input("Enter how many months it has been since your most recent birthday:"))

    # age + months, more accurate representation of age

    if y >=12: #sets some limits.
        print("Sorry please try again. Insert a lower number this time.")
        start()
    else:
        first_step(x, y, name)


def first_step(agey, agem, playername):
    # calculates age in months by taking the age in years and multiplying it by twelve + the remaining months old
    print(playername + ", you are:")
    z =((agey*12) + agem)
    z = str(z)
    print((z) + " months old")
    z = float(z)                 #conversions of type so that the age can be calculated, rounded, then printed
    z = round(z)
    z = int(z)
    time.sleep(2)   #delays the process so the user has time to understand what they are looking at
    return second_step(z, playername)    #returns the age in months so the age in weeks can be calculated

#second through sixth steps very similar to the first step, but different calculation for units of time
def second_step(agemonths, playername_two):
    q = (agemonths * 4.34524)
    q = round(q)
    q = str(q)
    print(playername_two + ", you are:")
    print(q + " weeks old")
    q = float(q)
    q = round(q)
    q = int(q)
    time.sleep(2)
    return third_step(q, playername_two)


def third_step(ageweeks, playername_three):
    c = (ageweeks * 7)
    c = str(c)
    print(playername_three + ", you are:")
    print(c + " days old")
    c = float(c)
    c = round(c)
    c = int(c)
    time.sleep(2)
    return fourth_step(c, playername_three)


def fourth_step(agedays, playername_four):
    h = (agedays * 24)
    h = str(h)
    print(playername_four + ", you are:")
    print(h + " hours old")
    h = float(h)
    h = round(h)
    h = int(h)
    time.sleep(2)
    return fifth_step(h, playername_four)


def fifth_step(agehours, playername_five):
    m = (agehours * 60)
    m = str(m)
    print( playername_five+ ", you are:")
    print(m + " minutes old")
    m = float(m)
    m = round(m)
    m = int(m)
    time.sleep(2)
    return sixth_step(m, playername_five)


def sixth_step(agemin, playername_six):
    sec = (agemin * 60)
    print(playername_six + ", you are:")
    sec = float(sec)
    sec = round(sec)
    sec = int(sec)
    sec = sec + 90  #adds seconds to the age because the seconds count increases each time ou run the program :)
    sec = str(sec)
    print(sec + " seconds old")
    return last_step()

#asks the user if they want to quit or play again.
def last_step():
    print("Thanks for playing! To exit type QUIT, to keep playing type PLAY:")
    end = input("")
    if end == "QUIT":
        exit()
    elif end == "PLAY":
        start()

#starts the program
start()