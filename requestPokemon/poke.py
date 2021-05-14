#!/usr/bin/env python3

import requests
#import wget

def valint(num):
    try:
        num = int(num)
        return True
    except:
        return False

url = "https://pokeapi.co/api/v2/pokemon/143"

url2 = "https://pokeapi.co/api/v2/pokemon/"

respons = requests.get(url)
respons2 = requests.get(url2)

def main():

    while True:
        usrsrch= input("enter number to search for pokemon")
        if not valint(usrsrch):
            print("try again only numbers")
        else:
            uurl= url2 + usrsrch
            print(uurl)
            break
    usrres = requests.get(uurl)

#print(respons.json())
#print(response.json())

    upokedex = usrres.json()

    print(upokedex)
#pokedex = respons.json()

    for x in upokedex["moves"]:
        print(x["move"]["name"])
    print(upokedex["sprites"]["front_default"])

    imgfile= upokedex["sprites"]["front_default"]


    count = 0
    for x in upokedex["game_indices"]:
         count = count +1
    print(count)
    print(upokedex["name"])
#dfile= wget.download(imgfile)
main()

