operat = input('enter the operation(+,-,*,/)')
firstnum = float(input('enter the first number'))
secondnum = float(input('enter the second number'))

if operat == '+':
    print(firstnum + secondnum)
elif operat == '-':
    print(firstnum - secondnum)
elif operat == '*' :
    print(firstnum * secondnum)
elif operat == '/' :
    print(firstnum / secondnum)
else :
    print('pls check the input and try again')
