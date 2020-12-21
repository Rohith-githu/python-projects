dig1 = int(input('please enter the first number'))
dig = str(input('pls enter the operator'))
dig2 = int(input('please enter the second number'))

if dig == '+':
    print(float(dig1 + dig2))
elif dig == '-':
    print(float(dig1 - dig2))
elif dig == '*':
    print(float(dig1 * dig2))
elif dig == '/':
    print(float(dig1 / dig2))
else:
    print('pls enter a valid input')
    input('press enter to close the file')