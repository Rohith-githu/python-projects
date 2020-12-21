first_name = 'Rohith '
print(first_name)
last_name = 'venkata sai'
print(last_name)
full_name = first_name + last_name 
print(full_name)

"""
now lets get the input from users
"""
firstname = input('what is your first name')
lastname = input('what is your last name')
fullname = 'hello {1} {0}'.format(firstname,lastname)
print(fullname)
print(type(firstname))