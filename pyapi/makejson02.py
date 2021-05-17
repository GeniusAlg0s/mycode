#!/usr/bin/env python3
"""json.dumps() creat json string"""

import json

def main():
    """run time"""
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, {"name": "Arthur Dent", "species": "Human"}]

    print(hitchhikers)

    jsonstring = json.dumps(hitchhikers)

    print(jsonstring)

if __name__ =="__main__":
    main()
