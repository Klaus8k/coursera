def match(l1:list,l2:list):
    result = []
    for i in l1:
        if i not in l2:
            print(i)
    return result

def oper_read(name):
    with open(name, 'r') as file:
        return file.read().split()


if __name__ == '__main__':
    x1 = oper_read('1.txt')
    x2 = oper_read('2.txt')
    print(match(x2,x1))