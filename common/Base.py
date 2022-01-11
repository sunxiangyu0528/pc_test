import datetime as dt
from dateutil import parser
from dateutil import rrule


######################################## date形式天数差


def date_minus(d1, d2):
    str_1 = d1
    str_3 = d2
    # 把字符串转为 list
    str_list = list(str_1)
    str_list1 = list(str_3)
    # 在斜杠位置之前 插入要插入的字符
    str_list.insert(4, '-')
    str_list.insert(-2, '-')
    str_list1.insert(4, '-')
    str_list1.insert(-2, '-')
    # 将 list 转为 str
    d1 = "".join(str_list)
    d2 = "".join(str_list1)
    # print(d1)
    # print(d2)
    ######## 法1
    # （1）先将字符串-->时间格式date
    date1 = dt.datetime.strptime(d1, "%Y-%m-%d").date()  ##datetime.date(2018, 1, 6)
    date2 = dt.datetime.strptime(d2, "%Y-%m-%d").date()  ##datetime.date(2018, 1, 9)
    print(date1)
    print(date2)
    # （2）计算两个日期date的天数差
    Days = (date2 - date1).days
    print(Days)
    return Days / 365

if __name__ == '__main__':
    aaa = date_minus("20190101", "20201220")

    print(aaa)
