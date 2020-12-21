# hi we are going to build an input calculator with python
# varibles
firstnum = int(input('pls enter a first number'))
operator = str(input('pls enter an operator'))
secondnum = int(input('pls enter a second number'))

# conditions , statements
if operator == '+':
  print(floatfirstnum + secondnum))
elif operator == '-':
    print(floatfirstnum - secondnum))
elif operator in('*','x'):
    print(floatfirstnum * secondnum))
elif operator == '/':
    print(floatfirstnum/secondnum))
else:
    print('error occoured')