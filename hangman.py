import random, json

def getWord():
    print("Loading words...")
    with open("words.json", "r") as f:
        words = json.load(f)
    words = words["words"]
    test = words[random.randint(0,len(words)-1)]
    return test

word = getWord()
print("Welcome to hangman! \n Whats your name?")
name = input("Enter name here: ")
print(f"Hello {name} lets get started\n")
