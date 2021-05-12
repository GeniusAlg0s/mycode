#!/usr/bin/python3

#pare keystone.common.wsgi  number of failed logins
loginfail =0 #counts fails

#open and read file
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")
# turn the file into a list of lines in memory
keystone_file_lines=keystone_file.readlines()

#loop over the lines
for line in keystone_file_lines:
    #if fail pattern appears
    if"- - - - -] Authorization failed" in line:
        loginfail += 1
print("The number of failed log in attempts is", loginfail)
keystone_file.close() # close the open file
