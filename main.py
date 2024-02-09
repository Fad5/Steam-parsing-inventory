from def_steam import  is_sell, get_price, get_JSON_inventory_steam, get_price_from_bd, get_price_bd
from def_work_JSON import load_json, save_json
from config import assets, datebase_inv
from time import sleep


def get_from_id(summa:int = 0) -> float:
    # Getting inventory data
    data_reqvests = get_JSON_inventory_steam()
    # Saving data to data.json
    save_json(data_reqvests, 'data')
    # Uploading data from data.json
    data = load_json('data')
    # Getting data by assets key
    items_assets = data.get("assets")
    # Getting the items from the list
    for item_assets in items_assets:
        # Getting the item ID
        item = (item_assets['classid'])
        assets.append(item)
    # Getting items from the description, 
    # since not duplicate items are stored, but also their names
    data_description = (data.get("descriptions"))
    for i in data_description:
        # Checking that the product can be sold
        item_sell = is_sell(i)
        if item_sell == None:
            pass
        else:
            id_ = (get_price(item_sell))
            price = id_[0]
            classid = id_[1]
            sleep(4)
            count = 0
            # Counting the number of items that converge by classid
            for asset in assets:
                if classid == asset:
                    count+=1
            itme_summa = count * price
            summa_all = summa + itme_summa
    return summa_all
        

def get_from_db(datebase:str = datebase_inv, summa=0) -> int:
    """
    The function takes the name of a json file, we tear it off, and through the loop we take count and link,
    we run the link through the get_price_from_bd function (we make requests and take the data). Using the
    key ['median_price'], we process the data through the get_price_bd function, then multiply the number 
    and the price
    """
    data = load_json(datebase)
    for i in data:
        # Получение информации по ключу
        counts_items =  i['cont']
        info_item = get_price_from_bd(i['link'])
        price_item =  get_price_bd(info_item['median_price'])
        summa_item = int(counts_items) * int(price_item)
        summa = summa_item + summa
        sleep(8)
    return summa


if __name__ == '__main__': 
   # Getting from data from bd.json is all you need to keep in memory  
   summa_db = get_from_db()
   # Getting the inventory from the link and getting the price
   summa_from_id = get_from_id()
   summa = summa_db + summa_from_id
   print(summa)