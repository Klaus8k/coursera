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
        self.result = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.result.append(attrs)


def write_to_file(file_name, data):
    with open(file_name, 'a') as file:
        if isinstance(data, list):
            for i in data:
                file.write(str(i[0][1]) + '\n')
        else:
            file.write(data)


def search_ref(url: str):
    r = requests.get(url)
    responce = r.text

    responce.encode('utf-8')
    write_to_file('sourse.txt', responce)
    return responce


# responce = search_ref(url)
with open('sourse.txt', 'r') as file:
    responce = file.read()

links = ''

parc = MyParce()
parc.feed(responce)
gen = (i[0][1] for i in parc.result)


for i in gen:
    x = re.findall(r'',i)
    links += x + '\n'

write_to_file('2.txt', links)

# for p in responce.splitlines():
#     parc.result_m = None
#     parc.feed(p)
#     if parc.result_m and 'href' in parc.result_m[0]:
#         x = parc.result_m[0][1]
#         result_list.append(x)

# write_to_file(result_list)

# Не все чистится. Попробовать сначала из файла 2. Или чистить поэтапно разными регулярками, но послего корректного отбора парсером.

# x = re.findall(r'([\w]+://)([\w\.-]+)/', result_list)


# for p in result_list:
#     x = re.search(r'([\w]+://)([\w\.-]+)/',p)
#     write_to_file(x.group(2))
# site =''
#
#
# set_result = set(result_list)
# list_to_print = list(set_result)
#
# list_to_print.sort()
# print('\n'.join(list_to_print))
