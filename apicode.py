from riotwatcher import LolWatcher, ApiError

# golbal variables
api_key = 'RGAPI-e9e4857b-edc4-491c-88bb-9fe2bd27c34d'
watcher = LolWatcher(api_key)
my_region = 'na1'

me = watcher.summoner.by_name(my_region, 'The Midget Cow')
print(me)

my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)

#this is all code i found online here https://towardsdatascience.com/how-to-use-riot-api-with-python-b93be82dbbd6