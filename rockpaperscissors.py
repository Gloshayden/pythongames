import random
import time

rps = ['rock', 'paper', 'scissors']
creds = 20
debug = False
print("welcome to rock paper scissors")
while creds > 0:
  if debug == True: creds = 999999999
  x = random.choice(rps)
  print(f"you have {creds} credits")
  print("what will you choose rock paper or scissors")
  if debug == True: print(f"Answer: {x}")
  y = str(input())
  y = y.lower()
  if x == y:
    creds = creds + 1
    print("well done you won +1 credits")
    time.sleep(2)
    print("")
  elif x != y:
    creds = creds - 1
    print("you lost -1 credits")
    time.sleep(2)
    print("")
while creds <= 0:
    print("you ran out of credits, thank you for playing")
    time.sleep(10)