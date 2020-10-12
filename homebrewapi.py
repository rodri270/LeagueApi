## this will use all the get commands offered by the riot docs 
## pip instal requests
## api = RGAPI-e9e4857b-edc4-491c-88bb-9fe2bd27c34d
## install requests library 

import requests
import json

#request input for who they wanna search up 
SummonerName = input("Please enter summoner name: ")

#varioable for the api key
apikey ='RGAPI-e9e4857b-edc4-491c-88bb-9fe2bd27c34d'

#get request for pulling the general user info 
UserRequest = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}".format(SummonerName, apikey))

#assigned the request to a value in text
TextValue = UserRequest.text

#convert value to string (not sure if this is needed)
str(TextValue)

#print string but only characters between 215 and 230 
print(TextValue[215:230])

#next step is to figure out a way to have it automatically  pull the info needed without having to manually tell it where the text is 
#OR figure out how to get the request to show up in json and then parse the info that way 
