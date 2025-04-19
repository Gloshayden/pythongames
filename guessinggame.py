import time as t
import random as r

def Gameinp():
  inputloop = True
  while inputloop == True:
    try:
      y = int(input())
      inputloop = False
      return y
    except:
      print("please enter an integer")

def wrong_input():
    print("you didn't enter a number between 1-6")
    print("please re-enter your number")
    return Gameinp()

debug = True
creds = 20
while creds >= 0:
  if debug == True: creds = 9999999
  print(f"you have {creds} credits")
  print("win/lose credits compared to the dice number")
  x = r.randint(1,6)
  print("please enter a number between 1-6")
  if debug == True: print(f"answer: {x}")
  y = Gameinp()
  while y >= 7:
    y = wrong_input()
  if x == y:
    creds = creds + x
    print(f"you win {x} credits")
    t.sleep(2)
    print("")
  elif x != y:
    creds = creds - x
    print(f"you lose {x} credits")
    t.sleep(2)
    print("")
if creds <= 0:
    print("thank you for playing come back next time to try again")