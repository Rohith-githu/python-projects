import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

s = []
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
# print(s)

length = int(input('enter the password length'))

random.shuffle(s)

print(''.join(s[0:length]))
input('press the enterkey to exit')