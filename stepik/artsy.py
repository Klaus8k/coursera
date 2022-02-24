import requests
import json

url = 'https://api.artsy.net/api/tokens/xapp_token/'
client_id = 'f8fbbe12ac2279b3f247'
client_secret = 'bd9f93e6fa1bfd2bdf7896358723b506'

r = requests.post(url,
                  data={
                    'client_id' : client_id,
                    'client_secret' : client_secret
                  })

j = json.loads(r.text)
token = j['token']
headers = {'X-Xapp-Token' : token}

artists_code = '4d8b92b34eb68a1b2c0003f4'
art_url = 'https://api.artsy.net/api/artists/' + artists_code
r = requests.get(art_url, headers=headers)
j = json.loads(r.text)
print(j)