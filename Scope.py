def inp ():
    while True:
        x = input()
        x.lower()
        mes = x.split()
        if len(mes) != 3:
            continue
        if len(mes[1]) > 10 or len(mes[2]) > 10:
            continue
        else:
            return mes


def add(scope, nmsp, v):
    if len(scope) == 0:
        new_d = dict({'namespace': nmsp, 'parent': None, 'var': []})
        new_d['var'].append(v)
        scope.append(new_d)
        return scope
    else:
        for i, di in enumerate(scope):
            if scope[i]['namespace'] == nmsp:
                scope[i]['var'].append(v)
                return scope

    return None


def get( nmsp, v):
    for i in scope:
        if i['namespace'] == nmsp:
            if v in i['var']:
                return nmsp
            else:
                if i['parent']:
                    return get( i['parent'], v)
                else:
                    return None
    return None




scope =[]
x = input()

while 100 <= int(x) <= 1:
    x = input()

for i in range(int(x)):

    mes = inp()
    if mes[0] == 'create':
        if len(scope) == 0:
            scope.append(dict({'namespace': mes[1], 'parent': mes[2], 'var': []}))
            scope.append(dict({'namespace': mes[2], 'parent': None, 'var': []}))
        else:
            scope.append(dict({'namespace': mes[1], 'parent': mes[2], 'var': []}))
    elif mes[0] == 'add':
        add(scope, mes[1],mes[2])
        # print(scope)
    elif mes[0] == 'get':
        print(get( mes[1], mes[2]))
    else: continue

