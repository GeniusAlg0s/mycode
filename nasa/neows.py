#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()
    date= input("using yyyy-mm-dd format enter date")
    #date2=input("using yyyy-mm-dd format enter date")
    ## update the date below, if you like
    startdate = "start_date="+date
    #enddate   ="end_date"+date2

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&"+ nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    #print(neodata)
    count=0
    for x in neodata['near_earth_objects']:
        for i in neodata['near_earth_objects'][x]:
            #print(i['name'])
            if i["is_potentially_hazardous_asteroid"] == True:
                print(i['name'])


    
if __name__ == "__main__":
    main()

