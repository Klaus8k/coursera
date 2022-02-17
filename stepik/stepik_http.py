import requests
import re

url = 'http://pastebin.com/raw/hfMThaGb'
# url = input()


def search_ref(url: str):
    r = requests.get(url)
    responce = r.text
    # responce.encode('utf-8')
    return responce


# with open('sourse.txt', 'r') as file:
#     responce = file.read()

responce = search_ref(url)
result_list = []

for i in responce.splitlines():
    result = re.search(r'<a.+href=(\'|\")(\w+://)?(\w[\w\d\.-]+)', i)

    if result:
        result_list.append(result.group(3))
        # print(result.group(3))
    else: continue

# print(re.search(r'([-\w]+\.\w+[\.\w]+)', result_m))


site = ''

#
# for i in result_m:
#     site = re.search(r'[\w\-]+\..+', i)
#     result_list.append(site.group().rstrip('/'))

set_result = set(result_list)
list_to_print = list(set_result)

list_to_print.sort()
print('\n'.join(list_to_print))

with open('2.txt', 'w') as file:
    file.write('\n'.join(list_to_print))
