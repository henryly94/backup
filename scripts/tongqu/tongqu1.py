# coding=utf-8
import urllib
import re


def do(amt):
    url1 = "http://tongqu.me/index.php/act/type?type=2&status=0&order=hotvalue"
    url2 = "http://tongqu.me/index.php/api/act/type?type=2&status=0&offset=%d&number=10&oder=hotvalue&desc=true"
    a = urllib.urlopen(url1)
    content = a.read().decode("utf-8")


    # 扫描讲座类前5页的活动并记录在tongqu.txt中
    fd2 = open("info.txt", 'w')
    cnt = 0
    for i in range(0, amt * 10, 10):
        a = urllib.urlopen(url2 % i)
        content = a.read()
        acts = re.findall('\{(.+?)}', re.findall('"acts":\[(.+?)\]', content)[0])
        for each in acts:
            fd2.write("<action>\n")
            cnt += 1
            for every in each.split(','):
                # print every
                one = every.split(':')
                if len(one) == 3:
                    one[1] = one[1].strip('"').strip() + one[2].strip('"').strip()
                fd2.write("\t<" + one[0].strip('"').strip() + ">\n")
                try:
                    txt = one[1].strip('"').decode("unicode-escape").encode("GBK").replace('\/', '\\').strip()
                except UnicodeError:
                    txt = one[1].strip('"').replace('\/', '\\').strip()
                fd2.write('\t\t' + txt)
                fd2.write("\t</" + one[0].strip('"').strip() + ">\n")
            fd2.write('</action>\n')

if __name__ == '__main__':
    do(5)
# for each in re.findall("(.+?):(.+?)", b):
#     print each[0], ":", each[1]


# 信息获取
# fd = open("tongqures2.txt", 'w')
# for each in re.findall('<script>(.+?)</script>', content, re.S):
#     if "var g_all_act_types" in each.strip():
#         for every in re.findall('\{(.+?)\}', each):
#             tmp = every.split(",")
#             fd.write("<action>\n")
#             for one in tmp:
#                 tmp2 = one.split(":")
#                 tmp2[0] = tmp2[0].strip('"')
#                 tmp2[1] = tmp2[1].strip('"')
#
#                 # 有数据
#                 if len(tmp2) == 2:
#                     if '\u' in tmp2[1]:
#                         tmp2[1] = tmp2[1].decode("unicode-escape")
#                 # 是网址
#                 elif len(tmp2) == 3:
#                     tmp2[1] += tmp2[2].strip('"')
#                 fd.write('\t<'+tmp2[0]+'>\n\t\t')
#                 fd.write(tmp2[1].encode('GBK'))
#                 fd.write('</' + tmp2[0] + ">\n")



                    # print tmp2[0], "", tmp2[1]
        # for every in re.findall('(.+?):(.+?)', each):
        #     print e

# print content

# fd = open("1.txt", "w")
# fd.write(content)

