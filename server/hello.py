from cgi import parse_qs, escape
import dataset
import json
#import pandas as pd

database = 'sqlite:////home/pi/predictit/data/predictitquote.%s.sqlite3'
query = 'SELECT * FROM quotes INNER JOIN markets ON quotes.market_id = markets.id WHERE markets.tickersymbol="%s"'

def application(env, start_response):
    parameters = parse_qs(env.get('QUERY_STRING', ''))
    contract = str(escape(parameters['tickersymbol'][0]))
    date = str(escape(parameters['date'][0]))
    response = get_quotes_for(contract, date)
    start_response('200 OK', [('Content-Type','text/plain')])
    return [response]


def get_quotes_for(contract, date):
    db = dataset.connect(database % date)
    q = db.query(query % contract)
    a = list(q)
    return json.dumps(a).encode('utf-8')











