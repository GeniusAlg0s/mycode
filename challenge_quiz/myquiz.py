#!/usr/bin/env python3


def validAge(input):
    try:
        num_age = int(input)
        return True
    except :
        return False

age =""


while True:
    age = input("how old are you? ")
    if not validAge(age):
       print("enter a valid age")
    else:
       age= int(age)
       break


#highest level
people_pref =""

#few path
corn_pref =""

#loads pth
travel_pref=""

print("you are ", age)

if age >=50:
    print("we guess you may not like too many people")

if age <50:
    print("you be bored with out people")

while people_pref == "":
    people_pref = input("do you perfer loads of people or few? ")
    if people_pref != "few":
        if people_pref != "loads":
         print("try again")
         people_pref = ""


if people_pref == "few":
    while corn_pref == "":
        corn_pref = input("do you perfer farm land or woodland? ")
        if corn_pref != "farm":
            if corn_pref != "woodland":
                print("please dont be dumbe enter the right stuff")
                corn_pref =""
        if corn_pref == "farm":
                print("you should live in a farming community")
        if corn_pref == "woodland":
                print("middle of no where is good for you") 

if people_pref == "loads":
    while travel_pref == "":
        travel_pref = input("do you cummute by bus or car?")
        if travel_pref != "bus":
            if travel_pref != "car":
                print("please dont be dumbe enter the right stuff")
                corn_pref =""
        if travel_pref == "bus":
            print("you should live in a inner city")
            break
        if travel_pref == "car":
            print("suburbs should be fine")
            break
