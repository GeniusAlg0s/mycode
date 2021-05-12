#!/usr/bin/env

def valentryint(number):
    try:
        newnum= int(number)
        return True
    except:
        return False

def valentryfloat(number):
    try:
        newnum= float(number)
        return True
    except:
        return False

def valop(op):
    count = 0
    operators=["x","/","-","+"]
    for x in operators:
        if x == op:
            count= count + 1
            break
    if count != 0:
        return True
    else:
        return False


operators=["x","/","-","+"]
num1=""
num2=""
uoperator=""

while True:
    num1= input("enter a decimal or number value")
    if not valentryint(num1):
        if not valentryfloat(num1):
            print("please retry enter number or valid integer")
    elif valentryint(num1):
        num1= int(num1)
        break
    else:
        num1= float(num1)
        break

while True:
    num2= input("enter a second decimal or number value")
    if not valentryint(num2):
        if not valentryfloat(num2):
            print("please retry enter number or valid integer")
    elif valentryint(num2):
        num2= int(num2)
        break
    else:
        num2= float(num2)
        break

print("you first number is: ", num1, "your second number is: ", num2)

while True:
    uoperator= input("choose x / - or + for some math time")
    if not valop(uoperator):
        print("stop playing not fun")
    else:
        print("your operation to be performed is : ", uoperator)
        break

