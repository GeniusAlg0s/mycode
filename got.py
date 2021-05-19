#!/usr/bin/python3
import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)
        print(got_dj['name'])
        allegiances_url = got_dj['allegiances']
        print(type(allegiances_url))

        alleresp = requests.get(allegiances_url[0])
        allign = alleresp.json()
        pprint.pprint(allign['name'])

if __name__ == "__main__":
        main()
