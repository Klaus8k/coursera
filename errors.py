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
    # print(dic_er)
    x = input().split()
    if len(x) != 1:
        # y = {x[2]:x[:1]}
        if x[2] in dic_er.keys():
            r = {x[0]:x[2]}
            dic_er.update(r)
        else:
            dic_er[x[0]].add(x[2])
    else:
        x = {x[0]: ()}
        dic_er.update(x)

# print(dic_er)

m = input()
out_ls = []

for _ in range(int(m)):
    out_ls.append(input())

for item in out_ls:
    x = out_ls.pop()
    if dic_er[x] in out_ls:
        print(x)








