#!/usr/bin/env python3
"""challenge api tues 05182021"""
import requests


URL="http://api.open-notify.org/astros.json"

def main():
    """run time"""

    req= requests.get(URL)


    noj = req.json()

    print("fingers crossed")
    print(noj)
    print("people in space" , noj['number'])
    for i in noj['people']:
        print(i['name'] , "is on the: ", i['craft'])
    #people = noj['people']
    #print(people)

if __name__ =="__main__":
    main()
