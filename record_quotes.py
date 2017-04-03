# encoding=utf8  

import sys
import json
import dataset

database_name = sys.argv[1] #'predictit.db'
file_name = 'data.xml'

print("Writing %s to %s" % ( file_name, database_name))

with open(file_name) as f:
    data = f.readlines()[0]


y=json.loads(data)

db = dataset.connect('sqlite:///%s' % database_name) 
if True:
    quote_table = db['quotes']
    market_table = db['markets']
    for marketdata in y['Markets']:
        for values in marketdata['Contracts']:
            values['market_id'] = values['ID']
            values['timestamp'] = marketdata['TimeStamp']
            keys = 'market_id LastTradePrice  BestBuyYesCost  BestBuyNoCost  BestSellYesCost  BestSellNoCost  LastClosePrice timestamp'.split()
            record = dict([(k.lower(), values[k]) for k in keys])
            quote_table.insert(record)

            keys = 'ID  Name TickerSymbol DateEnd'.split()
            record = dict([(k.lower(), values[k]) for k in keys])
            market_table.insert_ignore(record, keys=['id'])

