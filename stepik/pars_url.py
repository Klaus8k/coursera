import requests
import re
import urllib.parse as urlpars
from html.parser import HTMLParser

url = 'http://pastebin.com/raw/7543p0ns'
# url = input()

class MyParce(HTMLParser):
    def __init__(self):
        super(MyParce, self).__init__()
        self.reset()
        self.result = None


    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.result = attrs



def search_ref(url: str):
    r = requests.get(url)
    ref_list = r.text
    ref_list.encode('utf-8')
    return ref_list

responce_file = search_ref(url)
result_list = []

parc = MyParce()
for i in responce_file.splitlines():
    parc.result = None
    parc.feed(i)
    if parc.result and 'href' in parc.result[0]:
        x = parc.result[0][1]
        result_list.append(x)

for i in result_list:
    x = re.sub(r'([\w]+://)([\w\.-]+)/',r'\2',i)
    print(x)
# site =''
#
#
# set_result = set(result_list)
# list_to_print = list(set_result)
#
# list_to_print.sort()
# print('\n'.join(list_to_print))