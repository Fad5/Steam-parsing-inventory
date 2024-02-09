# Why did I write this?

**I started investing in 2017, I had a small inventory from the beginning, it was easy to look at and
calculate the amount, but every year the inventory grew and grew. The first attempt to automate somehow was
the use of third-party sites to calculate the amount of inventory, I did not like their inaccuracy. Subsequently, I used Exel, but this method was very slow**

# What language is the project written in?
 - Python 3.11

# Which libraries were used when writing the project?
 - time
 - json
 - requests

# How do I start using the project?

## 1.Installing Libraries 

Installing the library under the name requests
```python
pip install requests
```

## 2. Entering variables to work with
 File "config.py":
 - game_id = id game in steam, exemle 730
 - steamID = exemle 76561197960287999
 - datebase_inv = name name of the json file in the folder
```json
[
  {"name": "Капсула с автографами чемпионов PGL Major Stockholm 2021","link":"https://steamcommunity.com/market/priceoverview/?market_hash_name=Stockholm%202021%20Champions%20Autograph%20Capsule&appid=730&currency=5", "cont": 20},
{"name": "Легенды РМР 2020","link":"https://steamcommunity.com/market/priceoverview/?market_hash_name=2020%20RMR%20Legends&appid=730&currency=5", "cont": 30}]
```
