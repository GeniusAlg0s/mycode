#!/usr/bin/env python3


def validAge(input):
    try:
        num_age = int(input)
        return True
    except:
        return False

while True:
    age = input("how old are you")
    if not validAge(age):
       print("enter a valid age")
    else:
       break

#highest level
people_pref =""

#few path
corn_pref =""

#loads pth
travel_pref=""




while people_pref == "":
    people_pref = input("do you perfer loads of people or few? ")
    if people_pref != "few":
        if people_pref != "loads":
         print("try again")
         people_pref = ""


if people_pref == "few":
    while corn_pref == "":
        corn_pref = input("do you perfer farm land or woodland ")
    #if


