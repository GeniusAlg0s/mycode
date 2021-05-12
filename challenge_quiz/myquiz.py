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

response = ["we guess you may not like too many people","you be bored with out people","try again","please dont be dumbe enter the right stuff","you should live in a farming community","middle of no where is good for you","do you cummute by bus or car?","you should live in a inner city","suburbs should be fine"]

age_response =[{"few":{"farm>=50":"maybe get free corn", "farm<50":"find a field hand job", "wood>=50":"your age this easy living should great", "wood<50": "yeah the boredum is strong with this one"},"loads":{"bus>=50":"you may need a med shuttle","bus<50":"your spry walk","car>=50":"smooth sailing","car<50":"watch the road for old people"}}]
#highest level
people_pref =""

#few path
corn_pref =""

#loads pth
travel_pref=""

print("you are ", age)

if age >=50:
    print(response[0])

if age <50:
    print(response[1])

while people_pref == "":
    people_pref = input("do you perfer loads of people or few? ")
    if people_pref != "few":
        if people_pref != "loads":
         print(response[2])
         people_pref = ""


if people_pref == "few":
    while corn_pref == "":
        corn_pref = input("do you perfer farm land or woodland? ")
        if corn_pref != "farm":
            if corn_pref != "woodland":
                print(response[3])
                corn_pref =""
        if corn_pref == "farm":
            if age >=50:
                print(response[4],age_response[0]["few"]["farm>=50"] )
            if age <50:
                print(response[4], age_response[0]["few"]["farm<50"])
        if corn_pref == "woodland":
            if age >=50:
                print(response[5],age_response[0]["few"]["wood>=50"])
            if age <50:
                print(response[5],age_response[0]["few"]["wood<50"])

if people_pref == "loads":
    while travel_pref == "":
        travel_pref = input(response[6])
        if travel_pref != "bus":
            if travel_pref != "car":
                print(response[3])
                corn_pref =""
        if travel_pref == "bus":
            if age>=50:
                print(response[7],age_response[0]["loads"]["bus>=50"])
            if age<50:
                print(response[7],age_response[0]["loads"]["bus<50"])
        if travel_pref == "car":
            if age>=50:
                print(response[8],age_response[0]["loads"]["car>=50"])
            if age<50:
                print(response[8],age_response[0]["loads"]["car<50"])
        
