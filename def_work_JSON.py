import json
from typing import List


#Saving in JSON
def save_json(file, name_file:str='db', encoding:str='utf-8'):  
    with open(f'{name_file}.json', 'w', encoding=encoding) as f: 
        json.dump(file, f, indent=4, ensure_ascii=False)
        print('Ok')


#Uploading a JSON file
def load_json( name_file='db', encoding='utf-8') -> List:
    with open(f'{name_file}.json', 'r', encoding=encoding) as f: 
        data = json.load(f)
        return data