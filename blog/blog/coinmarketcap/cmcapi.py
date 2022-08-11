import requests   
import secrets  
from requests import Session
from pprint import pprint as pp
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'f51a6364-20fd-47d1-845d-b0c19e6201ac',
}

r = requests.get(url, headers=headers)
class CMC:
    def __init__(self, token):
        self.apiurl = 'https://api.coinmarketcap.com'
        self.headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': token,}
        self.session = Session()
        self.session.headers.update(headers)

    def getAllCoins(self):
        url = self.apiurl + '/v1/cryptocurrency/map'
        r = self.session.get(url)
        data = r.json()['data']
        return data

cmc = CMC(secrets.API_KEY)

cmc.getAllCoins()