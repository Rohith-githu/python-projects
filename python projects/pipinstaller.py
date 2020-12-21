import os
name = input('Enter the package name >>>')
try :
	os.system(f'pip install {name}')
	input('Enter to exit')
except Exception as e :
	print('Module not found')
	input(' ')