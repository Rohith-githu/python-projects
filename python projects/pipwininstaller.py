import os
package_name = input('Enter the package name >>>')
try :
	os.system(f'pipwin install {package_name}')
except Exception as e :
	inp = input('not found')