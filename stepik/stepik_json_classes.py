import json
#
# sample = '[{"name": "A", "parents": ["B", "C", "D"]},\
# {"name": "E", "parents": ["F", "G"]},\
# {"name": "I", "parents": ["E", "F", "Y", "D", "G"]},\
# {"name": "B", "parents": ["I", "Y", "D", "G"]},\
# {"name": "F", "parents": ["D", "Z"]},\
# {"name": "C", "parents": ["Y", "G", "Z"]},\
# {"name": "Y", "parents": []},\
# {"name": "D", "parents": []},\
# {"name": "G", "parents": ["Y", "D"]},\
# {"name": "Z", "parents": ["D", "G"]}]'

sample = input()
data_json = json.loads(sample)
sons_dic = {}

for i in data_json:
    sons_dic[i['name']] = set()


# Наполняем формат в формате "Родитель" : ребенок1, ребенок2...
for i in data_json:
    for j in i['parents']:
        if not i['parents']:
            continue
        else:
            sons_dic[j].add(i['name'])

print(sons_dic)


result = []
count = 0

def recurs_search(name):
    for i in sons_dic[name]:
        result.append(i)
        if i == [] :
            break
        else:

            recurs_search(i)


for i in sorted(sons_dic.keys()):
    recurs_search(i)
    x = set(result)

    print('{} : {}'.format(i,len(x)+1))
    result = []








# Попробовать так:
# Наполняем словарь ( класс : дети )
# потом поиск потомков.
# Проверяем есть ли в списках у детей детей и тд. новые классы. Их прибавляем к потомкам.
# Считаем выводим сортировано лексографически