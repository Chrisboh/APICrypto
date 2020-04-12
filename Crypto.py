#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:18:39 2020

@author: hassanramez
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 10:24:10 2020

@author: hassanramez
"""

import requests
import json




#getting API and storing in a variable 

api_request=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=22866a19-1ca6-43e5-8e3b-f150b1885397")


#using Json to get a parsable data  and #deliver content of API req
api=json.loads(api_request.content)   

coins=[
       {"symbol":"BTC",
       "amount_owned":2,
       "price_per_coin":3200
       },
        {"symbol":"EOS",
       "amount_owned":100,
       "price_per_coin":2.05
       },
        {"symbol":"XTZ",
       "amount_owned":100,
       "price_per_coin":2.05
       },
        ]


for i in range(0,10):
    for coin in coins:
        
        if api["data"][i]["symbol"]==coin["symbol"]:
           
            totalpaid=coin["amount_owned"]*coin["price_per_coin"]
            currentvalue=api["data"][i]["quote"]["USD"]["price"]*coin["amount_owned"]
            profit=currentvalue-totalpaid
            
            pl_percoin=api["data"][i]["quote"]["USD"]["price"]-coin["price_per_coin"]
            total_pl_coin=pl_percoin*coin["amount_owned"]
       
            print (api["data"][i]["name"]+"--"+api["data"][i]["symbol"])
            
            print ("price---{0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print ("numer of coins", coin["amount_owned"])
            print ("total paid:","${0:.2f}".format(totalpaid))
            print ("current value :","${0:.2f}".format(currentvalue))
            print ("profit loss per coin :","${0:.2f}".format(pl_percoin))
            
          
            print ("total profit or loss:","${0:.2f}".format(profit))
            print ("---------------------------------------")

