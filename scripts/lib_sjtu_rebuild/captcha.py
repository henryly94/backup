# coding=utf-8
import os
import Image

# path = 'C:\Users\Administrator\Desktop\Python\captcha\\'
# files = os.listdir(path)
cut = []
count = 0
result = []


# add new data when recognition success
def add_into_model(new_data, new_result):
    new_data_transformed = []
    for every in new_data:
        for one in every:
            if one !='\n':
                new_data_transformed.append(float(one))
    fd_add = open('capture\\training\data.txt', 'r')
    key = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    dic = {}
    cnt = {}
    res = new_result

    # read original model data in
    for each in fd_add.readlines():
        tmp = each.strip('\n').split(':')
        cnt[tmp[0]] = int(tmp[2])
        dic[tmp[0]] = []
        for every in tmp[1].split(','):
            dic[tmp[0]].append(float(every))
    fd_add.close()

    # add new Data into old model
    atmp = []
    for ai in range(300):
        atmp.append(float(float(dic[res][ai]*cnt[res] + new_data_transformed[ai])/float(cnt[res]+1)))
    dic[res] = atmp
    cnt[res] += 1

    # write back new model
    fd_add_wb = open('capture\\training\data.txt', 'w')
    for each in key:
        fd_add_wb.write(each + ':')
        tmpstr = ""
        for every in dic[each]:
            tmpstr += '%.5f,' % every
        fd_add_wb.write(tmpstr[:-1])
        fd_add_wb.write(':')
        fd_add_wb.write('%d\n' % cnt[each])
    fd_add_wb.close()


def horizon(fd):
    global result
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

        result.append(str)
        # number = open('capture\cap%d\\%d.txt' % (Cap, No), 'w')
        # number.writelines(str)
        # number.close()
        # tmp2.save('capture\cap%d\\f%d.jpg' % (i, j+1))


# 前期处理
def vertical(cappath):  # k
    # fd = Image.open(path + '%d.jpg' % k)
    # fd.save('capture\\test\%d.jpg' % k)
    fd = Image.open(cappath)
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
        tmp2 = fd.crop((newcut[q], 0, newcut[q+1], 39)).copy()
        horizon(tmp2)

def get_model():
    fd = open("D:\\workspace\\capture\\training\data.txt", 'r')
    dic = {}
    for each in fd.readlines():
        content = each.strip('\n')
        terms = content.split(':')
        dic[terms[0]] = []
        for every in terms[1].split(','):
            if every:
                dic[terms[0]].append(float(every))
    return dic

def get_distance(a, b):
    if len(a) != len(b):
        return -1
    sum = 0
    for i in range(len(a)):
        sum += pow((a[i]-b[i]), 2)
    return sum


def getCap(cpath):
    global result
    str2 = ""
    vertical(cpath)
    model = get_model()
    for each in result:
        tmp = []
        # format
        for every in each:
            for one in every:
                if one != '\n':
                    tmp.append(float(one))
        res = '0'
        dis = 10000
        for each2 in model:
            if get_distance(model[each2], tmp) < dis:
                dis = get_distance(model[each2], tmp)
                res = each2
        str2 += res
    t_result = result
    result = []
    return str2, t_result
if __name__ == '__main__':
    print getCap('C:\Users\Administrator\Desktop\captcha\\1.jpg')

