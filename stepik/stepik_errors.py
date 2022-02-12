n = input()
dic_er = {}

for i in range(int(n)):

    x = input().split()
    if ':' in x:
        child = x[0]
        par = x[2:]
        if child in dic_er.keys():
            dic_er[child] += par
        else:
            dic_er.update({x[0]: x[2:]})
    else:
        dic_er.update({x[0]: []})

m = input()
out_ls = []

for _ in range(int(m)):
    out_ls.append(input())

out_ls.reverse()


def perent(child, par):
    if par in dic_er[child]:
        # print('!',child, par)
        return True

    else:
        for i in dic_er[child]:
            # print('@@', i )
            return perent(i, par)

    # return False


a = []
for children in out_ls:

    if children in out_ls[out_ls.index(children) + 1:]:
        if children not in a:
            a.append(children)
            continue
    else:
        for parent in out_ls[out_ls.index(children) + 1:]:
            u = perent(children, parent)
            # print(u)
            if u:
                # print(children)
                a.append(children)
                # print(a)
                break
a.reverse()
for _ in a:
    print(_)
