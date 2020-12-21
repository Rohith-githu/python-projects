#hi letsnow print functions

def greet(task):
 return task.upper()

gree = greet('rohith')
print(gree)

name = 'rohith'

def init(name):
    initial = name[0:3]
    return initial

fname = input('your first name')

initial = init(fname)
print(initial.upper())