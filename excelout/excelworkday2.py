#!/usr/bin/env python3

import pandas as pd
import json 


def get_ip_data():
    input_ip = input("\nWhat is the IP address? ")
    input_driver = input("What is the driver associated with this device? ")
    state = input("location")
    needs = input("need fast or slow")
    d = {"IP": input_ip, "driver": input_driver, "state": state, "needs":needs}
    return d
mylistdict = []  # this will be our list we turn into a *.xls file

print("Hello! This program will make you a *.xls file")

while(True):
    mylistdict.append(get_ip_data())
    keep_going = input("\nWould you like to add another value? Enter to continue, or \
    enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break

### patDF= pandas.read_dict?(mylistdict)
patJson = json.dumps(mylistdict)
patdf =pd.read_json(patJson)
print(type(patJson))
### patDF.to_excel("pat_did_this.xls")

filename = input("\nWhat is the name of the *.xls file? ")

#pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')

#patdf.to_json("pat_did_this.json")
#patdf.to_excel("pat_made_this_too")
print("The file " + filename + ".xls should be in your local directory")
