#!/usr/bin/env python 3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

noth = nightmare[0]["d"]
print(f"my {challenge[2][1]}! the {challenge[2][0]} do {challenge[3]}")
print(f"my {trial[2]['goggles']}! the {trial[2]['eyes']} do {trial[3]}")
#print(f"my {nightmare['user']['name']['first']}! the {nightmare['kumquat]} do {noth}")
eyes= nightmare[0]["user"]["name"]["first"]
goggles= nightmare[0]["kumquat"]
nothing= nightmare[0]["d"]
print(f"My {eyes}! The {goggles} do {nothing}!")

