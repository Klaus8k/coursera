def inp ():
    mes = input('?').split(' ')
    # print(mes)
    return mes

# scope = {'nm': 'global', 'pr' : None, 'v' : []}
scope =[]


def create(nmsp,pr = None):
    scope.append(dict({'nm': nmsp, 'pr' : pr, 'v':[]}))
    return scope

def add(nmsp, v):
    if len(scope) == 0:
        new_d = dict({'nm': nmsp, 'pr': None, 'v': []})
        new_d['v'].append(v)
        scope.append(new_d)
        return scope

    for i in scope:
        if i['nm'] == nmsp:
            i['v'].append(v)
            return i
        else:
            return None


def get(nmsp, v):
    for item in scope:
        if nmsp in item:
            if v in item:
                return nmsp
            elif item[1]:
                get(item[1])
            else:
                return None

for i in range(100):
    mes = inp()
    if mes[0] == 'c':
        res = create(mes[1],mes[2])
        print(res)
    elif mes[0] == 'a':
        res = add(mes[1],mes[2])
        print(res)
    else:
        res = get(mes[1],mes[2])
        print(res)
