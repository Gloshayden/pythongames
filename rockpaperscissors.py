import random
import time

rps = ['rock', 'paper', 'scissors']
creds = 20
debug = False
print("welcome to rock paper scissors")
while creds > 0 and debug == False:
    x = random.choice(rps)
    print("you have", creds,"credits")
    print("what will you choose rock paper or scissors")
    y = str(input())
    if x == y:
        creds = creds + 1
        print("well done you won +1 credits")
        time.sleep(2)
        print(chr(27) + "[2J")
    elif x != y:
        creds = creds - 1
        print("you lost -1 credits")
        time.sleep(2)
        print(chr(27) + "[2J")
while creds <= 0:
    print("you ran out of credits, thank you for playing")
    time.sleep(120)
while creds > 0 and debug == True:
    x = random.choice(rps)
    creds = 999999999999
    print("Debug mode enabled, Answer revieled and unlimited creds")
    print("Answer:", x)
    y = str(input())
    if x == y:
        creds = creds + 1
        print("well done you won +1 credits")
    elif x != y:
        creds = creds - 1
        print("you lost -1 credits")