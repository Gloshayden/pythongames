def getname():
    def firstnamecheck():
        print("what is your name? (max of 20 characters)")
        name = str(input("First name:"))
        name = name.lower()
        return name
    def lastnamecheck():
        print("what is your last name? (max of 20 characters)")
        lname = str(input("Last name:"))
        lname = lname.upper()
        return lname
    name = firstnamecheck()
    lname = lastnamecheck()
    if len(name) > 20 and len(lname) > 20:
        print("invalid name")
        return "false"
    else:
        fname = f"{name} {lname}"
        return fname
def getage():
    def agecheck():
        print("what is your age? (min of 20 and max of 80)")
        age = int(input("Age:"))
        return age
    age = agecheck()
    if age < 20 or age > 80:
        print("invalid age")
        return 0
    else:
        return age

fname = getname()
while fname == "false":
    fname = getname()
age = getage()
while age == 0:
    age = getage()
print(f"Your name is {fname} and your age is {age}")