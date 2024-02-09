headers = {
   'user-agent': 'user-agent',
   'accept': '* / *'
}

# id game in steam
game_id = 730

# id steam profile
steamID = 'ID'

# link to get information about the inventory
url_steam_profil = (f'https://steamcommunity.com/inventory/{steamID}/{game_id}/2?l=language&count=1000&format=json')
assets = []
count = 0

# naming the file with information about the items in the repository
datebase_inv = 'bd'