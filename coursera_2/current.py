from contracts import contract
# change operatorPrecedence to infix_notation for work with contract


@contract(x='str | >=0')
def main(x):
    print(x+x)



if __name__ == '__main__':
    main('-5')

