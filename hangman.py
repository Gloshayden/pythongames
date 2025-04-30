import random, json, os

def getWord():
    print("Loading words...")
    with open("words.json", "r") as f:
        words = json.load(f)
    words = words["words"]
    test = words[random.randint(0,len(words)-1)]
    return test

# first time startup
if not os.path.exists("words.json"):
    print("No saved words found. Generating file")
    with open("words.json", "w") as f:
        structure = {"words":["enter", "words", "here"]}
        json.dump(structure, f)
    print("Made words file please enter in words there. \n" \
    "Or you can use the premade file with the words: 'enter','words','here'")
    input("Please edit the file then come back and press enter.")

word = getWord()
print("Welcome to hangman! \nWhats your name?")
name = input("Enter name here: ")
print(f"Hello {name} lets get started\n")
