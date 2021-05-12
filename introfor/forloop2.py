#!/usr/bin/env python3
#list of str

vendors =["cisco","juniper","big_ip","f5", "arista", "alta3", "zach", "stuart"]
approved_vendors = ["cisco", "juniper", "big_ip"]
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# loop across the list called vendors
for x in vendors:
    print("\nthe vendor is",x,end="")
    if x not in approved_vendors:
        print("UNAUTHORIZED VENDOR!", end="")
print("\nend of loop")
#for x in farms:
   # print(x,end="")

for values  in farms:
    if values["name"]=="NE Farm":
        print(values["agriculture"])
   

farm_pick =input("pick NE Farm, SE Farm, or W Farm")

for values in farms:
    if values["name"]== farm_pick:
        print(values["agriculture"])


bad_list =["carrots","veggies", "celery"]
farm_pick2 =input("pick NE Farm, SE Farm, or W Farm")

for values in farms:
    if values["name"] == farm_pick2:
        for x in values["agriculture"]:
            if x not in bad_list:
                 print(x)


    
    
