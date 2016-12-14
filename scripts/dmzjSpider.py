# coding=utf-8
import urllib
import urllib2
import os
import sys
import re
import json
from lxml import etree
import time
import socket
import signal
from tmp6 import trans
timeout = 10
socket.setdefaulttimeout(timeout)


class BlablaError(Exception):
    def __init__(self):
        Exception.__init__(self)


def handler(signum, frame):
    raise AssertionError


def callbackfunc(blocknum, blocksize, totalsize):
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    if percent < 0:
        raise BlablaError
    sys.stdout.write("%.2f%%\r"% percent)


def download(url, path, episode, cnt):
    url = 'http://manhua.dmzj.com%s' % url
    i = 10
    while i != 0:
        try:
            a = urllib2.urlopen(url, timeout=100)
        except socket.timeout:
            print 'Timeout, try again'
            i -= 1
            continue
        finally:
            break
    print i
    if not i:
        print 'jump'
        raise BlablaError
        return
    content = a.read()

    # print content
    a = re.findall("eval.+\[(.+?)]", content)[0].split(',')
    b = re.findall("'([A-Za-z\d_\|]+?)'.split", content)[0].split('|')
    # for each in a:
    #     print a.index(each), each
    # print '**********'
    # for each in b:
    #     print b.index(each), each
    urls = trans(a, b)
    print episode
    for each in urls:
        print urls.index(each), each
    for each_url in urls:
        local = "%s%04d_%s_%03d.jpg" % (path, cnt, episode, urls.index(each_url) + 1)
        time_out_counter = 0
        while True:
            try:
                urllib.urlretrieve(each_url, local, callbackfunc)
                time.sleep(0.1)
            except socket.timeout:
                if time_out_counter <= 10:
                    print "Timeout, Try again"
                    time_out_counter += 1
                else:
                    print "Error, jump to next"
                    break
            finally:
                break


def matchlp(s):
    spos = []
    res = []
    for i in range(0, len(s)):
        if s[i] == '{':
            spos.append(i)
            continue
        if s[i] == '}' and spos:
            ts = s[spos[-1]: i+1]
            spos.pop()
            if not spos:
                res.append(ts)
    return res


def search():
    """
    :param None:
    :return infos: urls of search result and its title
    """
    a = urllib.urlopen('http://s.acg.178.com/comicsum/search.php?s=%s' % urllib.quote(raw_input(">>").decode('gbk').encode('utf8')))
    content = a.read()
    infos = []
    for json_string in matchlp(content):
        # print json_string
        json_string = json_string
        dic = json.loads(json_string)
        infos.append((dic['name'], dic["comic_url_raw"]))
    return infos


def access(url):
    """
    :param url:
    :return pages: the download url and its title
            lens: the length of pages
    """
    a = urllib.urlopen(url)
    content = a.read().replace('‧', '')
    selector = etree.HTML(content)
    path = '/html/body/div[3]/div[2]/div[1]/div/ul/li/a/text()'
    path2 = '/html/body/div[3]/div[2]/div[1]/div/ul/li/a/@href'
    urls = selector.xpath(path2)
    names = selector.xpath(path)
    pages = []
    for i in range(len(urls)):
        pages.append((names[i], urls[i]))
    return pages, len(urls)


def path_create(title):
    if title in os.listdir('D:\Manga\\'):
        return 'D:\Manga\%s\\' % title
    else:
        try:
            os.mkdir('D:\Manga\%s\\' % title)
        except WindowsError:
            print 'MB'
            return 'D:\Manga\Error\\'
        finally:
            return 'D:\Manga\%s\\' % title


def suffix_change(url, num):
    print 'suf', url
    if url[-5:] == 'shtml':
        return '%s-%d.shtml' % (url[:-6], num)
    else:
        if url[-4] == 'html':
            return '%s-%d.html' % (url[:-5], num)


def do():
    """
    Main Function
    """
    method = raw_input('Url or Title')
    while not (method == 'Url' or method == 'Title'):
        method = raw_input('Url or Title')
    if method == 'Url':  # input url to download
        page, amount = access(raw_input('url plz>>'))
    else:
        info = search()
        if not info:
            print "No such Manga"
        else:
            for each in info:
                print info.index(each), each[0].encode('gbk')
            num = raw_input('Choose one')
            while not num.isdigit or not (len(info) >= int(num) >= 0):
                num = raw_input("Wrong choice, choose again")
            num = int(num)
            title = info[num][0].encode('gbk')
            url = info[num][1]
            path = path_create(title)
            eachpage, amount = access(url)
            i = 0
            t_str = ''
            for each in eachpage:
                t_str += '%d.%-10s' % (eachpage.index(each), each[0])
                i += 1
                if i == 10:
                    print t_str
                    t_str = ''
                    i = 0
            begin, end = raw_input('range from?').split(',')
            episode = int(begin)
            while episode <= int(end):
                try:
                    download(eachpage[episode][1], path, eachpage[episode][0].encode('gbk'), episode)
                except BlablaError:
                    pass
                finally:
                    episode += 1


if __name__ == '__main__':
    do()

    # access()
    # search()

    """
    后续思路：
        获取每一章节页面后，读取前几张图片地址，下载，根据固定格式访问之后几张的页面（非图片，网页），注意检查尾部
        bullshit
    """