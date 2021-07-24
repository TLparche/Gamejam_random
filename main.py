'''import random

read = open('제시어.txt', 'r', encoding='utf-8').read()
list = []
list = read.split(" ")
print(list)

for i in range(1, 7, 1):
    print(i, "조의 제시어는", end=' ')
    for i in range(3):
        data = list.pop(random.randrange(0, len(list)))
        print(data, end=' ')
    print("입니다.")'''

import random

read = open('멘토.txt', 'r', encoding='utf-8').read()
list = []
list = read.split("\n")
print(list)

for i in range(1, 7, 1):
    print(i, "조의 담당 멘토는 ", end=' ')
    data = list.pop(random.randrange(0, len(list)))
    print("입니다.")