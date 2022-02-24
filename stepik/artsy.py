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

art_dict = {}

with open('1.txt','r') as f:
    artists_code = []
    artists_code = f.read().split()
# artists_code = ['4d8b92b34eb68a1b2c0003f4','537def3c139b21353f0006a6','4e2ed576477cc70001006f99']

def request_art(art_code):
    for i in art_code:
        art_url = 'https://api.artsy.net/api/artists/' + i
        r = requests.get(art_url, headers=headers)
        r.encoding = 'utf-8'
        j = json.loads(r.text)

        # print(j.keys()) # dict_keys(['id', 'slug', 'created_at', 'updated_at', 'name', 'sortable_name', 'gender', 'biography',
                        # 'birthday', 'deathday', 'hometown', 'location', 'nationality', 'target_supply', 'image_versions', '_links'])
        art_dict[j['sortable_name']] = j['birthday']
    return art_dict

# request_art(artists_code)
# test_list = [['Andy Warhol', '1928'], ['Mary Abbott', '1921'],['Hamra Abbas', '1976'],['Aamra RRRRR', '1976']]

def sort_art(dict_a:dict):
    x = sorted(dict_a.items(), key=lambda x: (x[1],x[0]))
    return x

y = request_art(artists_code)

x = sort_art(y)


with open('2.txt','w', encoding='utf-8') as f:
    for i, val in enumerate(x):
        print(val)
        f.write(val[0] + '\n')