#!/usr/bin/env python3

#search 
import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
lookfor = input("search for?")
lookwhere= input("search where")

print(find(lookfor, lookwhere))
