#!/usr/bin evn python3

#open the file
dnsfile =open("dnsservers.txt", "r")

#list of file lines
dnslist= dnsfile.readlines()

#loop over line list
for svr in dnslist:
    #print w/o new line
    print(svr, end="")

#close file
dnsfile.close()
