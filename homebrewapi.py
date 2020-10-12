## this will use all the get commands offered by the riot docs 
## pip instal requests
## pip instal pandas 
## api = RGAPI-e9e4857b-edc4-491c-88bb-9fe2bd27c34d
## install requests library 

import requests
import json


#request input for who they wanna search up 
SummonerName = input("Please enter summoner name: ")

#varioable for the api key
apikey ='RGAPI-5de70cb1-7458-4726-b4ba-3f3480c23160'

#get request for pulling the general user info 
UserRequest = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}".format(SummonerName, apikey))


#this will print in just raw text 
#print (UserRequest.text)

#this sets the resquest output as text and to the json_object_string
json_object_string = UserRequest.text

#this lets you take the output from the top variable and load the data into a json dictionary 
json_object = json.loads(json_object_string)

#this lets you call the value from above, pick a certain value and assign it to a new variable 
Summonerid = (json_object["id"])

#New get request for the ranked aspect of the user 
UserRankedRequest = requests.get("https://na1.api.riotgames.com//lol/league/v4/entries/by-summoner/{}?api_key={}".format(Summonerid, apikey))

#prints everything in a raw string
#print (UserRankedRequest.text)

json_object_string2 = UserRankedRequest.text
json_object2 = json.loads(json_object_string2)

UserInformation = (json_object2["summonerName"])
print (UserInformation)