import collections


def long_word():
    text = str(input("Введите предложение!: "))
    word = text.split()
    counter = collections.Counter(word)
    common = counter.most_common()[0]
    long = max(word, key=len)
    return long, common


print(long_word())