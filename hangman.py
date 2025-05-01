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

print("Welcome to hangman! \nWhats your name?")
name = input("Enter name here: ")
print(f"Hello {name} lets get started\n")
loop = True
while loop:
    answer = getWord()
    word = list(answer)
    for i in range(len(word)):
        word[i] = "_"
    print(word)
    while "_" in word:
        print("What letter do you guess?")
        guess = input("Enter letter here: ")
        for i in range(len(answer)):
            if answer[i] == guess:
                word[i] = guess
        print(word)
    print(f"Congrats {name} you won!")
    print(f"The word was {answer}")
    print("Do you want to play again? y/n")
    again = input().lower()
    if again == "y": loop = True
    elif again == "n": loop = False