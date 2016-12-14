# coding=utf-8
import os
import numpy
import Image
import ImageEnhance

path = 'C:\Users\Administrator\Desktop\captcha\\'
files = os.listdir(path)
anwser = [5, 5, 4, 4, 4, 5, 5, 4, 5, 4, 4, 5, 5, 4, 4, 5, 4, 5, 4, 5, 4, 4, 5, 5, 4, 5, 4, 4]
cut = []
count = 0
print sum(anwser)


def horizon(fd, Cap, No):
    limit = 230
    flag = True
    cnt = 0
    newcut = []
    for k in range(fd.size[1]):
        sum = 0
        for q in range(fd.size[0]):
            sum += fd.getpixel((q, k))
        sum /= fd.size[0]
        if flag:
            if sum < limit:
                flag = False
                cnt += 1
                newcut.append(k)
        else:
            if sum >= 248:
                flag = True
                cnt += 1
                newcut.append(k)
    str = ["" for p in range(20)]
    if cnt == 2:
        tmp = fd.crop((0, newcut[0], fd.size[0], newcut[1])).copy()
        tmp2 = tmp.resize((15, 20))
        for y in range(15):
            for u in range(20):
                if tmp2.getpixel((y, u)) <= 225:
                    tmp2.putpixel((y, u), 0)
                    str[u] += '1'
                else:
                    tmp2.putpixel((y, u), 255)
                    str[u] += '0'
        for u in range(20):
            str[u] += '\n'
        number = open('capture\cap%d\\%d.txt' % (Cap, No), 'w')
        number.writelines(str)
        number.close()
        # tmp2.save('capture\cap%d\\f%d.jpg' % (i, j+1))


# 前期处理
def vertical():
    for k in range(len(anwser)):
        fd = Image.open(path + '%d.jpg' % k)
        fd.save('capture\cap%d\_%d.jpg' % (k, k))
        fd = fd.convert('L')
        flag = True
        limit = 248
        cnt = 0
        newcut = []
        for i in range(100):
            sum = 0
            for j in range(40):
                # sum += fd.getpixel((i, j))[0] + fd.getpixel((i, j))[1] + fd.getpixel((i, j))[2]
                sum += fd.getpixel((i, j))
            # print i, sum/120

            if not flag:
                if sum/40 > limit:
                    newcut.append(i)
                    flag = True
            else:
                if sum/40 <= limit:
                    cnt += 1
                    newcut.append(i)
                    flag = False
        cut.append(newcut)
        for q in range(0, len(newcut), 2):
            tmp = fd.crop((newcut[q], 0, newcut[q+1], 39)).copy()
            horizon(tmp, k, q/2)


if __name__ == '__main__':
    for i in range(len(anwser)):
        try:
            os.mkdir('capture\cap%d' % i)
        except:
            pass
    vertical()


