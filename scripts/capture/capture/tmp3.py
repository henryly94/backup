# coding=utf-8

str = ''
for i in range(31):
    tmp = raw_input('%d' % i)
    str += tmp
    str += ','

fd = open('trainresult.txt', 'w')
fd.write(str[:-1])