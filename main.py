from def_steam import  is_sell, get_price, get_JSON_inventory_steam, get_price_from_bd, get_price_bd
from def_work_JSON import load_json, save_json
from variables import assets, datebase_inv
from time import sleep


def get_from_id(summa:int = 0):
    data_reqvests = get_JSON_inventory_steam()
    save_json(data_reqvests, 'data')
    data = load_json('data')
    items_assets = data.get("assets") 
    for item_assets in items_assets:
        item = (item_assets['classid'])
        assets.append(item)
    data_description = (data.get("descriptions"))
    for i in data_description:
        item_sell = is_sell(i)
        if item_sell == None:
            pass
        else:
            id_ = (get_price(item_sell))
            price = id_[0]
            classid = id_[1]
            sleep(4)
            count = 0
            for asset in assets:
                if classid == asset:
                    count+=1
            itme_summa = count * price
            summa = summa + itme_summa
    return summa
        

def get_from_db(datebase:str = datebase_inv, summa=0) -> int:
    """
    Функция принимает название файла формата json, отрываем, через цикл забираем count и link,
    link прогоняем через функцию get_price_from_bd(делаем requests и забараем данные). Обращаемя по 
    ключу ['median_price'] обрабатываем данные через функцию get_price_bd, дальше умножаем количество 
    и цену
    """
    data = load_json(datebase)
    for i in data:
        counts_items =  i['cont']
        info_item = get_price_from_bd(i['link'])
        price_item =  get_price_bd(info_item['median_price'])
        summa_item = int(counts_items) * int(price_item)
        summa = summa_item + summa
        sleep(8)
    return summa


if __name__ == '__main__':       
   summa_db = get_from_db()
   summa_from_id = get_from_id()
   summa = summa_db + summa_from_id
   print(summa)