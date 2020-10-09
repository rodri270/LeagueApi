## this will use all the get commands offered by the riot docs 
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

print (UserRequest.json)
