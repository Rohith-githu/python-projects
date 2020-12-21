
import requests

ip = requests.get('http://ipinfo.io')

print(ip.text)

input('Is this helpfull for you?')
