print("Задание 1: цитаты, в которых менее 10-ти слов:")
print(" ")

import codecs

with codecs.open('new  1.txt','r','utf-8') as f:
    for line in f:
        if (len(line.split('—')[0].split()) < 10):
            print(line.split('—')[0])      
rcount = 0
with codecs.open('new  1.txt','r','utf-8') as f:
    for line in f:
        if ("Разум" in line.split('—')[0].split()):
            rcount = rcount + 1

print(" ")
print(" ")
print(" ")
print("Задание 2: в скольких цитатах есть слово «Разум», источники этих цитат:")
print(" ")
print("ЦИТАТ СО СЛОВОМ «РАЗУМ»:", rcount)
print(" ")

with codecs.open('new  1.txt','r','utf-8') as f:
    for line in f:
        if ("Разум" in line.split('—')[0].split()):
            print(line.split('—')[1])

print(" ")
print(" ")
print(" ")
print("Задание 3: Вводите слова, и после пустого слова программа покажет Вам само это слово и все цитаты, в которых оно встречается")
print(" ")

inp = []
while True:
    word = str(input("введите слово: "))
    if len(word) == 0:
        break
    else:
        inp.append(word)

rcount = 0

for w in inp:
    print(w)
    with codecs.open('new  1.txt','r','utf-8') as f:
        for line in f:
            if (w in line.split('—')[0].split()):
                print(line.split('—')[0]) 
                rcount = rcount + 1
    if (rcount == 0):
        print("Цитат нет")
    rcount = 0
