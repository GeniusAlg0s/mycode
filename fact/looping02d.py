#!/usr/bin/env python3

#open and read file
with open("dnsservers.txt", "r") as dnsfile:
    for svr in dnsfile:
        svr = svr.rstrip('\n')
        if svr.endswith('org'):
            with open("org-domian.txt", "a") as srvfile:
                srvfile.write(svr + "\n")
        elif svr.endswith('com'):
            with open("com-domian.txt","a") as svrfile:
                svrfile.write(svr +"\n")
