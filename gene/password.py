import random
import string

print('hi welcome to password generator version 1.0')
if __name__ == "__main__":
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    passlen = int(input('pls enter the password length :'))
    s = [ ]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    # print(s)
    random.shuffle(s)
    # print(s)
if passlen == 0 :
        print('we cant print 0 length password')
else: 
        print('here\'s your password')
        

print("".join(s[0:passlen]))

 