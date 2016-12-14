# coding=utf-8
import re

fd = open('../4.txt','r')

content = fd.read()


a = re.findall('var g_all_act_types = (.+)', content)
print a
b = re.findall('\{(.+?)}', a[0])
for each in b:
    print each
