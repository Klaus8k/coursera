n = input()

# input_list = ['ArithmeticError', 'ZeroDivisionError : ArithmeticError', 'OSError', 'FileNotFoundError : OSError',
#               'dghjghjgdj : OSError']
# exept_list = ['ZeroDivisionError', 'OSError', 'ArithmeticError', 'FileNotFoundError']


# def graf(child):
#     print(child)
#     for item in out_ls:
#
#         if child in dic_er[item]:
#             print(item)
#             graf(item)
#         else:
#             return False


dic_er = {}
for i in range(int(n)):
    x = input().split()
    if ':' in x:
        child = x[0]
        par = x[2:]
        if child in dic_er.keys():
            dic_er[child]+=par
        else:
            dic_er.update({x[0]:x[2:]})

    else:
        dic_er.update({x[0]:[]})
    print(dic_er)





    # if len(x) != 1:
    #
    #     if x[0] in dic_er.keys():
    #         dic_er[x[0]]+=x[2:]
    #     else:
    #         dic_er.update({x[0]:[]})
    # else:
    #     dic_er.update({x[0]:[]})
    # print(dic_er)

# print(dic_er)

m = input()
out_ls = []
for _ in range(int(m)):
    out_ls.append(input())

out_ls.reverse()

def perent(child, par):
    print('par', par)
    if par in dic_er[child]:
        print(child)
        return '1'
    else:
        for i in dic_er[child]:
            perent(i,par)


    return False

for children in out_ls:
    for parent in out_ls[out_ls.index(children) + 1:]:

        if perent(children,parent)  == '1':
            print(children,'!')
            break











