
import requests
import re

# url = 'http://pastebin.com/raw/7543p0ns'
url = input()

regul_pattern = r'href=.{,8}[\w-]+[\.]\w+[\.\w+]+\/'

def search_ref(url: str):
    r = requests.get(url)
    ref_list = r.text
    ref_list.encode('utf-8')
    return ref_list
"""Совет тем, кто хочет использовать регулярки для прохождения этого задания: НЕ ИСПОЛЬЗУЙТЕ РЕГУЛЯРКИ! Намучаетесь, к тому же это ОЧЕНЬ ХРЕНОВАЯ практика.

Лучше используйте стандартные модули html.parser и urllib.parse, например! В конце концов, эти библиотеки были специально созданы для решения задач, подобных этой. Для закручивания гаек созданы гаечные ключи, для забивания гвоздей - молотки. Используйте несчастный микроскоп по назначению!"""

responce_file = search_ref(url)
# print(responce_file)
result = re.findall(regul_pattern, responce_file)

result_list = []
site =''

for i in result:
    site = re.search(r'[\w\-]+\..+', i)
    result_list.append(site.group().rstrip('/'))

# x = ['drinktime.ru','raiting.rbc.ru', 'tata.ru', 'www.conf.rbc.ru', 'www.m-2.ru',
#      'www.seminar.rbc.ru', 'www.top.rbc.ru']

# result_list += x
# result_list.remove('pics.rbc.ru')
set_result = set(result_list)
list_to_print = list(set_result)

list_to_print.sort()
print('\n'.join(list_to_print))
# with open('3_source.txt', 'w') as file:
#     file.write('\n'.join(list_to_print))




