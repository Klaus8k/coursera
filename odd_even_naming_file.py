# import os
#
#
#
# y = os.listdir()
#
# print(os.path.splitext(y[3])[0])
#
# x = sorted(y, key=lambda y: int(os.path.splitext(y)[0].isdigit()))
# print(x)

for i in range(20):
    x = str(i) + '.jpg'
    with open(x, 'w') as f:
        f.write('i')



