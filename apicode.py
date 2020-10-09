from riotwatcher import LolWatcher, ApiError

# golbal variables
api_key = 'RGAPI-e9e4857b-edc4-491c-88bb-9fe2bd27c34d'
watcher = LolWatcher(api_key)
my_region = 'na1'

me = watcher.summoner.by_name(my_region, 'Hay1tsme')
print(me)

my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)