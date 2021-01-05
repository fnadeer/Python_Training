birthdays = {'Alice': 'March 11','Firoz':'March 16','Leo': 'December 19','Jad': 'January 26'}
while True:
    print("Enter the name: (blank to quit)")
    name = input()
    if name == "":
        break
    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
        break
    else:
        print("oh no! " + name + " is not in your birthday calender, if you want to add type Y or N")
        conscent = input()
        if conscent == 'Y':
            print("Please enter the birth date")
            bday = input()
            birthdays[name] = bday
            print("The database is updated")
            break
        else:
            break
