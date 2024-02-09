import requests
from config import  headers, url_steam_profil, game_id
from time import sleep


# Getting JSON from inventory
def get_JSON_inventory_steam():
    """
    The function calls requests(url_steam_profil - link to the profile)
    the result is converted to json format, if the result is None
    the function repeats after 60 seconds
    """
    resource = requests.get(url=url_steam_profil, headers=headers)
    data = resource.json()
    print(data)
    if data == None:
        sleep(60)
        print('Response: None. Timeout: 60 sec')
        get_JSON_inventory_steam()
        
    else:
        return data


# Checking that the product can be sold
def is_sell(item):
        if item['marketable'] == 1:
            return item


# Getting information about the subject
def get_info_item(item):
    if item == None:
          pass
    else:
        name_item = item["market_hash_name"]
        print(name_item)
        class_id = item.get("classid")
        url_steam_item = (f'https://steamcommunity.com/market/priceoverview/?market_hash_name={name_item}&appid={game_id}&currency=5')
        resource = requests.get(url=url_steam_item, headers=headers)
        data = resource.json()
        if data['success'] == False:
                print('False')
                sleep(20)
                get_info_item(item)
        else:
            return data, class_id


# Getting the price and converting str to float
def get_price(item):
    sleep(10)
    get_info_items = get_info_item(item)
    item_id = str(get_info_items[1])
    item_price = str((get_info_items[0])['lowest_price'])
    item_price_list = item_price.split(' ')
    price = float(item_price_list[0].replace(',','.'))
    return price, item_id


# Getting the price from the db.json file
def get_price_from_bd(url:str):
    resource = requests.get(url=url, headers=headers)
    data = resource.json()
    if data['success'] == False:
            print('False')
            sleep(20)
            get_price_from_bd(url=url)
    return data
     

def get_price_bd(item_price:str)->float:
    """
    Formatting the price of 10.10 rubles -> ('10.10','rub') -> 10.10
    """
    item_price_list = item_price.split(' ')
    price = float(item_price_list[0].replace(',','.'))
    return price