# coding=utf-8
import tongqu1
import tongqu2
import re

# scan first 2 pages
tongqu1.do(5)

fd = open('tongqures2.txt')
content = fd.read()
actions = re.findall('<action>(.+?)</action>', content, re.S)
for each in actions:

    name = re.findall('<name>(.+?)</name>', each, re.S)

    if u'讲坛' in name[0].decode('GBK') or "Voice" in name[0] or u'实习' in name[0].decode('GBK') or u'高校' in name[0].decode('GBK'):
        print name[0].decode('GBK').strip('\n').strip('\t').strip(' ')
        actid = re.findall('<actid>(.+?)</actid>', each, re.S)[0]#.strip('\n').strip('\t').strip(' ')
        tongqu2.do_many_time(str(int(actid)))



