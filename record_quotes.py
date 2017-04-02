import json
import dataset

database_name = 'predictit.db'
file_name = 'data.xml'

with open(file_name) as f:
    data = f.readlines()[0]


y=json.loads(data)

db = dataset.connect('sqlite:///%s' % database_name)
table = db['quotes']
for marketdata in y['Markets']:
    for values in marketdata['Contracts']:
        values['market_id'] = values['ID']
        values['timestamp'] = marketdata['TimeStamp']
        del values['ID']    
        table.insert(values)
