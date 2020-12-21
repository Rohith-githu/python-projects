from random_words import RandomWords
dicton = RandomWords()
d2 = dicton.random_words()
# print(d2)
inp = int(input('how many words should i generate'))
print(''.join(d2[0:inp]))