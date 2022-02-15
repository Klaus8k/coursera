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


responce_file = search_ref(url)
# print(responce_file)
result = re.findall(regul_pattern, responce_file)

result_list = []
site =''

for i in result:
    site = re.search(r'[\w\-]+\..+', i)
    result_list.append(site.group().rstrip('/'))

set_result = set(result_list)
list_to_print = list(set_result)

list_to_print.sort()
print('\n'.join(list_to_print))












