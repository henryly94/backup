# coding=utf-8
import os
import urllib2
import urllib
import re
import sys
sys.path.append('./lib_sjtu_rebuild/')
import login as lg
import cookielib
import captcha3

cookie = cookielib.MozillaCookieJar()
openerL = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(openerL)

content = ""
loginflag = False


def login(id, opener):
    global headers, cookie, loginflag
    if loginflag:
        return
    times = 1
    while times <= 10:
        print u'尝试登陆 第%d次' % times
        demoUrl = "http://studyroom.lib.sjtu.edu.cn/"
        headers = {
         'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Connection':'keep-alive',
         'detail':'anything'
        }

        req = urllib2.Request(demoUrl, None, headers)
        opener.open(req)    # study room
        yzm = "https://jaccount.sjtu.edu.cn/jaccount/captcha"
        res = opener.open(yzm)  # get captcha
        status = res.getcode()
        picData = res.read()
        path = "yzm.jpg"
        if status:
            localPic = open(path, "wb")
            localPic.write(picData)
            localPic.close()
        captcha, possible_data = captcha3.getCap('yzm.jpg')
        login_info = urllib.urlencode([('user', 'henryly94'), ('pass', 'dc2315'), ('captcha', captcha)])
        req3 = urllib2.Request("https://jaccount.sjtu.edu.cn/jaccount/ulogin", login_info, headers)
        c = opener.open(req3)  # login Jaccount
        content = c.read()
        req = urllib2.Request('http://tongqu.me/index.php/auth/jaccount', None, headers)
        a = opener.open(req)  # login Tongqu
        URL = re.findall('URL=(.+?)">', a.read())[0]
        req = urllib2.Request(URL, None, headers)
        opener.open(req)    # open Tongqu login jump page
        req = urllib2.Request("http://tongqu.me/index.php/act/detail/sign/%s" % id, None, headers)
        d = opener.open(req)  # open Tongqu's action page
        content = d.read().decode('utf-8')
        username = re.findall('"user_name":"(.+?)"', content)
        if username:
            if 'henryly94' in username[0]:
                for pdc in range(len(possible_data)):
                    # captcha3.add_into_model(possible_data[pdc], captcha[pdc])
                    pass
                loginflag = True
                print u"登陆成功"
                return
        failcap = open('capture\\failure\\%d.jpg' % len(os.listdir('capture\\failure\\')), 'wb')
        failcap.write(picData)
        failcap.close()
        times += 1
    print u'登陆失败'
    return


def do(id, applist, opener):
    global headers, cookie
    login(id, opener)
    appurl = 'http://tongqu.me/index.php/api/act/sign'
    dic = [
        ("act_id", id),
        ("user_sign_info",
            {
                "info": applist,
                "name": "henryly94",
                "phone": "13162570096",
                "email": "henryly94@sjtu.edu.cn"
            }),
        ("attach_id", 0),
        ("token", "XTTUfoei")
    ]

    # two replace() is experimental solutions
    info2 = urllib.urlencode(dic).replace("%27", "%22").replace("+", "")

    req = urllib2.Request(appurl, info2, headers)
    d = opener.open(req)  # send action application
    f = d.read().decode('unicode-escape')
    e = eval(f.encode("GBK"))
    if e.get('error', 0) == 1:
        if e.get('msg', u'未知') == '已经报名成功，请不要重复报名'.decode('utf-8').encode('gbk'):
            pass
        else:
            print u'报名失败'
            print u'原因', e.get('msg', u'未知')
    else:
        print u'报名成功'


def do_many_time(id):
    do(id, [], openerL)
    do(id, ['0'], openerL)
    do(id, ['0', '0', '0'], openerL)
    do(id, ['0', '0', '0', '0'], openerL)
    do(id, ['0', '0', '0', '0', '0'], openerL)

if __name__ == '__main__':
    do_many_time('10765')
