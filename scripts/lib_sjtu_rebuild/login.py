# coding=utf-8
# Author: Lyy
# Email: henryly94@gmail.com
import urllib
import urllib2
import re
import captcha
import cookielib
import Constant as Const


def login(user):
    print 'haha'
    if Const.my_jaccount.get(user, -1) == -1:
        raise ValueError
    headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Connection': 'keep-alive',
         'detail': 'anything'
    }
    cookie = cookielib.MozillaCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    urllib2.install_opener(opener)
    res = opener.open('http://studyroom.lib.sjtu.edu.cn').read()

    sid = re.findall('%s" value="(.*)">' % 'sid', res)[0]
    se = re.findall('%s" value="(.*)">' % 'se', res)[0]
    returl = re.findall('%s" value="(.*)">' % 'returl', res)[0]
    cap_num = re.findall('img src="captcha\?(.*)" alt', res)[0]
    while True:
        yzm = "https://jaccount.sjtu.edu.cn/jaccount/captcha?%s" % cap_num
        res = opener.open(yzm)  # get captcha
        status = res.getcode()
        pic_data = res.read()
        path = "yzm.jpg"
        if status:
            local_pic = open(path, "wb")
            local_pic.write(pic_data)
            local_pic.close()
        try:
            captcha, possible_data = captcha.getCap('yzm.jpg')
        except:
            continue
        login_info = urllib.urlencode(
            [
                ('user', Const.my_jaccount[user][0]),
                ('pass', Const.my_jaccount[user][1]),
                ('captcha', captcha),
                ('sid', sid),
                ('returl', returl),
                ('se', se),
                ('v', '')
            ]
        )
        req3 = urllib2.Request(
            "https://jaccount.sjtu.edu.cn/jaccount/ulogin",
            login_info,
            headers
        )
        res = opener.open(req3).read()
        url = re.findall('<meta http-equiv="refresh" content="0; url=(.*)"/>', res)
        if url:
            res = opener.open(url[0]).read()
            if not re.findall('img src="captcha\?(.*)" alt', res):
                return opener


if __name__ == '__main__':
    login('lyy')