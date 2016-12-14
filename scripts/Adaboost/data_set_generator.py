# coding=utf-8
# Author: Lyy
# Email: henryly94@gmail.com
import random
import math

def gen(num):
    fd = open('ada_data6', 'w')
    f = [
        [0, 0], [1, 0], [2, 0],
        [0, 1], [1, 1], [2, 1],
        []
    ]
    datas = []
    for i in range(3):
        for j in range(3):
            if [i, j] not in f:
                continue
            if i == 1 and j == 1:
                for k in range(num):
                    datas.append((i * 2 + random.random() * 2, j * 2 + random.random() * 2 + 4, -1))
            else:
                for k in range(num):
                    datas.append((i * 2 + random.random() * 2, j * 2 + random.random() * 2 + 4, 1))
    for each in datas:
        fd.write("%.2f %.2f %d\n" % (each[0], each[1], each[2]))

if __name__ == '__main__':
    gen(40)
