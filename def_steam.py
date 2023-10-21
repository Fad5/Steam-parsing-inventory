import requests
from variables import  headers, url_steam_profil, game_id
from time import sleep


# Получеие JSON с ивинтаря
def get_JSON_inventory_steam():
    """
    Фунцкция вызывает requests(url_steam_profil - ссылка на профиль)
    результат преоброзовывают в json формат, если результат None
    функция повторяется через 60 секунд
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


# Проверка то что товар можно продать 
def is_sell(item):
        if item['marketable'] == 1:
            return item


#Подучение информации о предмете 
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


#Получние цены и преобразование str в float
def get_price(item):
    sleep(10)
    get_info_items = get_info_item(item)
    item_id = str(get_info_items[1])
    item_price = str((get_info_items[0])['lowest_price'])
    item_price_list = item_price.split(' ')
    price = float(item_price_list[0].replace(',','.'))
    return price, item_id

def get_price_from_bd(url:str):
    resource = requests.get(url=url, headers=headers)
    data = resource.json()
    if data['success'] == False:
            print('False')
            sleep(20)
            get_price_from_bd(url=url)
    return data
     
def get_price_bd(item_price:str):
    """
    Форматирование цены 10,10 руб -> ('10,10','руб') -> 10.10
    """
    item_price_list = item_price.split(' ')
    price = float(item_price_list[0].replace(',','.'))
    return price