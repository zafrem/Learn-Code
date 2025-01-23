import requests
import json

api_request = requests.get('https://api.binance.com/api/v3/ticker/price')
api = json.loads(api_request.content)

for x in api:
    print(x['symbol'], "${0:.4f}".format(float(x['price'])))
