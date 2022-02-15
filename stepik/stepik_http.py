import requests
import re

url = 'http://pastebin.com/raw/7543p0ns'
# url = input()

regul_pattern = r'\w+[\.]\w+[\.\w+]+\b'

def search_ref(url: str):
    r = requests.get(url)
    ref_list = r.text
    ref_list.encode('utf-8')
    return ref_list
    # with open('1.txt', 'w+') as file:
    #
    #     file.write(ref_list)
    #     r_file = file.read()
    #     print(r_file)
    #
    # return r_file




# with open('1.txt', 'r') as url:
#     r = url.read()
#
#     result = re.findall(regul_pattern, r)
#     result.sort()
#     for i in result:
#         print(i)

responce_file = search_ref(url)
print(responce_file)
result = re.findall(regul_pattern, responce_file)
result.sort()
for i in result:
    print(i)










