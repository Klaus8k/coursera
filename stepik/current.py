import json

sample = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
data = json.loads(sample)


x = []
for i in data:
    x.append(i["name"])

parent = dict.fromkeys(x, [])

for elem_d in data:
    print(elem_d)
    for par in elem_d['parents']:
        print(par, ' par')
        print(elem_d['name'], 'elem name')
        print(parent[par], 'par[par]')
        parent[par].extend(elem_d['name'])
        print(parent)


print(parent)

def search_parent():
    pass



# Попробовать так:
# Наполняем словарь ( класс : дети )
# потом поиск потомков.
# Проверяем есть ли в списках у детей детей и тд. новые классы. Их прибавляем к потомкам.
# Считаем выводим сортировано лексографически