import os

os.chdir('main')
print(os.getcwd())
x = os.walk('main')
ans = []

all_file = [i for i in x]
all_file.reverse()
# print(all_file)

for i in all_file:
    m = i[0].split('\\')[-1]
    for j in i[2]:
        if j.split('.')[1] == 'py':
            ans.append(m)

ans = set(ans)
x = list(ans)
print(x.sort())
print(x)

with open('1.txt', 'w') as a:

    ll = '\n'.join(x)
    a.write(ll)

