# coding=utf-8
# Author: Lyy
# Email: henryly94@gmail.com
import script

# use script.date_apply(list_gen( The_Date_Begin, The_Date_End )) to add new reserve 


months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def list_gen(begin, end):
    is_leap_year = lambda y: y % 400 == 0 or y % 4 == 0 and y % 100 != 0
    is_end = lambda y, e: y[0] == e[0] and y[1] == e[1] and y[2] == e[2]
    next_date = lambda c, e: [(c[1] == 12 and c[2] == 31) and c[0]+1 or c[0], c[2] == months[c[1]] and (c[1] == 12 and 1 or c[1]+1) or c[1], c[2] == months[c[1]] and 1 or c[2]+1]
    current_date, end_date, date_list = [int(i) for i in begin.split('-')], [int(j) for j in end.split('-')], []
    while not is_end(current_date, end_date):
        months[2] = is_leap_year(current_date[0]) and 29 or 28
        date_list.append('%d-%d-%d' % (current_date[0], current_date[1], current_date[2]))
        current_date = next_date(current_date, end_date)
    date_list.append('%d-%d-%d' % (current_date[0], current_date[1], current_date[2]))
    return date_list


if __name__ == '__main__':
    script.date_apply(list_gen('2016-10-30', '2016-10-30'))
