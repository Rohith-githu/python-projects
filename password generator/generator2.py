import string
import random

if __name__ == "__main__":
    set1 = string.ascii_uppercase
    # print(set1)
    set2 = string.ascii_lowercase
    # print(set2)
    set3 = string.digits
    # print(set3)
    set4 = string.punctuation
    # print(set4)
    passlen = int(input('pls enter the password length'))
    passset = []
    passset.extend(set1)
    passset.extend(set2)
    passset.extend(set3)
    passset.extend(set4)
    # print(passset)
    random.shuffle(passset)
    # print(passset)
    print(''.join(passset[0:passlen]))
