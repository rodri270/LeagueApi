## this will use all the get commands offered by the riot docs 
## pip instal requests
## install requests library 

import requests
import json


#request input for who they wanna search up 
SummonerNames = input("Please enter summoner name: ")

#varioable for the api key
apikey ='RGAPI-669a75d1-7044-4010-a8cd-9e01b8fbeb18'

#get request for pulling the general user info 
UserRequest = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}".format(SummonerNames, apikey))


#this will print in just raw text 
#print (UserRequest.text)

#this sets the resquest output as text and to the json_object_string
json_object_string = UserRequest.text

#this lets you take the output from the top variable and load the data into a json dictionary 
json_object = json.loads(json_object_string)

#this lets you call the value from above, pick a certain value and assign it to a new variable 
SummonerNum = (json_object["id"])
#print (SummonerNum)

#New get request for the ranked aspect of the user 
UserRankedRequest = requests.get("https://na1.api.riotgames.com//lol/league/v4/entries/by-summoner/{}?api_key={}".format(SummonerNum, apikey))

json_object_string2 = UserRankedRequest.text
json_object2 = json.loads(json_object_string2)

for s in range(len(json_object2)):
    if json_object2[s]["summonerId"] == SummonerNum:
        print("{} is ranked as {} in {}".format(json_object2[s]["summonerName"], json_object2[s]["tier"], json_object2[s]["queueType"])) 








#prints everything in a raw string
#print (UserRankedRequest.text)



#UserInformation = (json_object2["summonerName"])
#print (UserInformation)