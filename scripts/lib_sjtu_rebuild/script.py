# coding=gbk
# Author: Lyy
# Email: henryly94@gmail.com
import urllib
import re
import login
import urllib2
import Constant as Const


def reserve_add(user, infos):
    """
    add reservation
    :param user: the Jaccount user
    :param infos: date, begin and end times
    :return:None
    """
    try:
        opener = login.login(user)
        opener.open('http://studyroom.lib.sjtu.edu.cn/index.asp')
        url = 'http://studyroom.lib.sjtu.edu.cn/room_search.asp'
        info = urllib.urlencode(
            [
                ('date_s', infos['date']),
                ('tstart', infos['begin']),
                ('tend', infos['end']),
                ('roomid', 'all'),
                ('location', 'main'),
                ('hasprojector', '0'),
                ('temp', '36')
            ]
        )
        req = urllib2.Request(url, info, Const.my_header)
        b = opener.open(req)
        content = b.read()
        every = re.findall('<tr>(.+?)</tr>', content)
        room_id = '7'
        for each in every:
            temp_room_name = re.findall("<font size='2' color='#000000'>([A-E]\d+)</font></td>", each)
            temp_room_id = re.findall("roomid=(\d+)", each)
            if temp_room_name[0] == infos['room_name']:
                room_id = temp_room_id[0]
        info2 = urllib.urlencode(
            [
                ('groupname', '学习小组'),
                ('topic', '学习会'),
                ('detail', '预习复习课程内容'),
                ('attendcount', '3'),
                ('partake', '0'),
                ('specialneed', '无'),
                ('roomid', room_id),
                ('tstart', '%s %s' % (infos['date'], infos['begin'])),
                ('tend', '%s %s' % (infos['date'], infos['end'])),
                ('action', 'post'),
                ('B1', '提交')
            ]
        )
        url2 = 'http://studyroom.lib.sjtu.edu.cn/reserve_add.asp'
        req2 = urllib2.Request(url2, info2, Const.my_header)
        opener.open(req2)
        # print info2
    except:
        raise Exception


def get_user_reserve_list(user):
    """
    Get a users reserve list
    :param user: the user we get list from
    :return: the list
    """
    opener = login.login(user)
    url = 'http://studyroom.lib.sjtu.edu.cn/user_reserve_list.asp'
    d = opener.open(url)
    content = d.read()
    res = []
    for each in re.findall('<tr>.+?</tr>', content, re.S):
        if len(each) > 7 and each[4:7] == '<td':
            passwd = re.findall("<td><font size='2' color='#000000'>等待加入！\(密码:(\d{6})\)</font></td>", each)
            if passwd:
                applicationid = re.findall("<td><font size='2' color='#000000'>(\d{5})</font></td>", each)
                roomname = re.findall("<td><font size='2' color='#000000'>([A-E]\d+)</font></td>", each)
                res.append(
                    {
                        'application_id': applicationid[0],
                        'password': passwd[0],
                        'room_name': roomname[0]
                    }
                )
    return res


def reserve_plus(user, applications):
    """
    To join the reservation
    :param user: The Jaccount user to login
    :param applications: a list contain the reservation number
    :return:
    """
    opener = login.login(user)
    opener.open('http://studyroom.lib.sjtu.edu.cn/reserve_plus.asp')
    url = 'http://studyroom.lib.sjtu.edu.cn/reserve_plus.asp'
    url2 = 'http://studyroom.lib.sjtu.edu.cn/reserve_plus_ok.asp'
    for each in applications:
        info = urllib.urlencode(
            [
                ('B1', '查询'),
                ('applicationid', each['application_id'])
            ]
        )
        req = urllib2.Request(url, info, Const.my_header)
        infos = re.findall("<input type='hidden' value='(.+?)' name='(.+?)'/>", opener.open(req).read())
        if infos:
            info = urllib.urlencode(
                [
                    ('B1', '加入'),
                    ('applicationid', each['application_id']),
                    ('password', each['password']),
                    ('needusernum', infos[1][0]),
                    ('roomname', infos[2][0])
                ]
            )
            req = urllib2.Request(url2, info, Const.my_header)
            opener.open(req)


def date_apply(dates, room='E310'):
    """
    This function take a list as param, and send applications on those date
    :param dates: a list contain the date you want
    :return: None
    """
    times = [
        '8:00',
        '11:00',
        '14:00',
        '17:00',
        '20:00',
        '22:00'
    ]
    for i in range(len(times) - 1):
        for each in dates:
            info = {
                'date': each,
                'begin': times[i],
                'end': times[i + 1],
                'room_name': room
            }
            try:
                print 'Reserve add ', str(info)
                reserve_add(Const.my_jaccount.keys()[i / 2], info)
            except Exception:
                continue
        if i % 2 or i == 4:
            print 'Reserve plus'
            reserve_plus(Const.my_jaccount.keys()[(i / 2 + 1) % len(Const.my_jaccount.keys())],
                         get_user_reserve_list(Const.my_jaccount.keys()[i / 2])
                         )
            print 1
            reserve_plus(Const.my_jaccount.keys()[(i / 2 + 2) % len(Const.my_jaccount.keys())],
                         get_user_reserve_list(Const.my_jaccount.keys()[i / 2])
                         )
            print 2

if __name__ == '__main__':
    date_apply(['2016-7-1', ])
    # reserve_plus('lyy', get_user_reserve_list('lyy'))
