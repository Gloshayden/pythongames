#!/usr/bin/python
import time as t
import random as r
        
def wrong_input():
    print("you didn't enter a number between 1-6")
    print("please re-enter your number")
    y = int(input())  
    
debug = False
creds = 20
while creds >= 0 and debug == False:
    print("you have", creds,"credits")
    print("win/lose credits compared to the dice number")
    x = r.randint(1,6)
    print("please enter a number between 1-6")
    print("(any letters will cause it to break)")
    y = int(input())
    while y >= 7:
        wrong_input()
    if x == y:
        creds = creds + x
        print("you win", x,"credits")
        t.sleep(2)
        print(chr(27) + "[2J")
    elif x != y:
        creds = creds - x
        print("you lose", x,"credits")
        t.sleep(2)
        print(chr(27) + "[2J")
if creds <= 0:
    print("thank you for playing come back next time to try again")
    
while creds >= 0 and debug == True:
    x = r.randint(1,6)
    creds = 99999999999
    print("debug on inf creds,no refresh,ans revealed")
    print("answer:", x)
    y = int(input())
    while y >= 7:
        wrong_input()
    if x == y:
        creds = creds + x
        print("you win", x,"credits")
    elif x != y:
        creds = creds - x
        print("you lose", x,"credits")