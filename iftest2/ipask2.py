#!/usr/bin/env python3

ipchk = input("Apply an IP address: ")

if ipchk == "192.168.70.1":
    print("IP gateway was set :", ipchk, "change it dummy")
elif ipchk:
     print("Looks like the IP address was set: " + ipchk)
else:
    print("You did not provide input.")

