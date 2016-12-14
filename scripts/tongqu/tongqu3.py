# coding=utf-8
import tongqu1
import tongqu2
import re

#tongqu1.do(3)
fd = open('tongqures2.txt', 'r')
acts = re.findall('<action>(.+?)</action>', fd.read(), re.S)
actions = []
for each in acts:
    tmpdic = {}
  #  for every in re.findall()

