# coding=utf-8
# Knn file
import os

# functions

def get_result():
    fd = open('capture\\trainresult.txt', 'r')
    content = fd.read()
    caps = content.split(',')
    return caps
def addin(adic, acnt, akey, anew):
    count = acnt[akey]
    old = adic[akey]
    atmp = []
    for ai in range(300):
        atmp.append(float(float(old[ai]*count + anew[ai])/float(count+1)))
    adic[akey] = atmp
    acnt[akey] += 1


def train():
    dirlist = os.listdir("capture")

    # initial
    key = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    dic = {}
    cnt = {}
    res = get_result()
    for each in key:
        dic[each] = [0.0 for i in range(15*20)]
        cnt[each] = 0

    for eachdir in dirlist:
        if 'train' in eachdir or 'py' in eachdir:
            continue
        path = 'capture\%s\\' % eachdir  # go through all files
        for eachfile in os.listdir(path):
            if eachfile[-3:] == 'jpg':
                continue
            else:  # target file
                new = res[int(eachdir[3:])][int(eachfile[0])]

                # training
                fd = open(path + eachfile, "r")
                content = fd.read()
                tmp = []
                for value in content:
                    if value == '\n':
                        continue
                    tmp.append(int(value))
                addin(dic, cnt, new, tmp)

    trainfd = open('capture\\training\data.txt', 'w')
    for each in dic:
        trainfd.write(each)
        trainfd.write(':')
        tmpstr = ""
        for every in dic[each]:
            tmpstr += '%.5f,' % every
        trainfd.write(tmpstr[:-1])
        trainfd.write(':%d' % cnt[each])
        trainfd.write('\n')


if __name__ == '__main__':
    train()