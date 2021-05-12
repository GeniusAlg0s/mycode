#!usr/bin/env python3

#open and read file

with open("dnsservers.txt","r") as dnsfile:
    #line list
    dnslist =dnsfile.readlines()
    #loop lines
    for svr in dnslist:
        print(svr, end="")

        #auto closed
