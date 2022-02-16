import requests
import re
import urllib.parse as urlpars
import html.parser

# url = 'http://pastebin.com/raw/7543p0ns'
url = input()

# regul_pattern = r'href=.{,8}[\w-]+[\.]\w+[\.\w+]+\/'

def search_ref(url: str):
    r = requests.get(url)
    ref_list = r.text
    ref_list.encode('utf-8')
    return ref_list
https://docs.python.org/3.9/library/html.parser.html

responce_file = search_ref(url)
result_list = []

for i in responce_file.splitlines():
    list_ref = re.search(r'\<a href=(.+)\b', i)
    if list_ref:
        x = (urlpars.urlsplit(list_ref.group(1)[1:]))
        result_list.append(re.sub(r'[\"\'\:].+','',x.netloc))


# result = re.findall(regul_pattern, responce_file)

site =''

# for i in result:
#     site = re.search(r'[\w\-]+\..+', i)
#     result_list.append(site.group().rstrip('/'))

set_result = set(result_list)
list_to_print = list(set_result)

list_to_print.sort()
print('\n'.join(list_to_print))