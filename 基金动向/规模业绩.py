'''
sql测试更方便
'''
# 拟合业绩表现

import pymysql

from common.Base import date_minus

import time


class DB:
    def __init__(self):
        # 创建一个连接对象
        self.conn = pymysql.connect(host="101.132.108.94",
                                    port=3306,
                                    user="zgzb",
                                    password="aUebd32A,DlF1-SC",
                                    charset="utf8",
                                    cursorclass=pymysql.cursors.DictCursor
                                    )
        # 创建一个游标
        self.cur = self.conn.cursor()

    def find_one(self, sql):
        """获取查询出来的第一条数据"""
        # 执行查询语句
        self.conn.commit()
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data

    def find_all(self, sql):
        """获取查询出来的所有数据"""
        self.conn.commit()
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data


class DB_Beta:
    def __init__(self):
        # 创建一个连接对象
        self.conn = pymysql.connect(host="106.15.205.160",
                                    port=3306,
                                    user="beta_app_user",
                                    password="OrvjSp3VOqUPAW8K",
                                    charset="utf8",
                                    cursorclass=pymysql.cursors.DictCursor
                                    )
        # 创建一个游标
        self.cur = self.conn.cursor()

    def find_one(self, sql):
        """获取查询出来的第一条数据"""
        # 执行查询语句
        self.conn.commit()
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data

    def find_all(self, sql):
        """获取查询出来的所有数据"""
        self.conn.commit()
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data


if __name__ == '__main__':
    a = time.time()
    db = DB()  # 证券代码
    # 一周更新一次，总市值
    sql4 = "SELECT * FROM wd_zx.WD_FUND_COM_INFO wfci WHERE code ='G107138.GS'  and  enddate ='2021-09-30';"
    data4 = db.find_all(sql4)
    if data4[0]["stockfundassetstotal"] == None:
        data4[0]["stockfundassetstotal"] = 0
    if data4[0]["mixfundassetstotal"] == None:
        data4[0]["mixfundassetstotal"] = 0
    sum_total = data4[0]["stockfundassetstotal"] + data4[0]["mixfundassetstotal"]
    print("总市值是：", data4[0]["stockfundassetstotal"] + data4[0]["mixfundassetstotal"])
    # 取出这个公司下的所有基金
    sql = "SELECT wfn.fund_code FROM wd_zx.WD_FUND_NAV wfn WHERE  wfn.com_code ='G107138.GS' and `day` ='2021-09-30'"
    data = db.find_all(sql)
    print("fund_code总和为", len(data), data)
    sum_yeji = 0
    for i in data:
        print("###############################################################")
        print(i)
        # 算出每个基金的持股市值
        sql2 = "SELECT SUM(marketvalueofstockholdings)   FROM wd_zx.WD_FUND_STOCK_RECORD wfsr WHERE cmp_code ='G107138.GS'  " \
               "and rpt_day ='2021-09-30' and fund_code ='{}'".format(i["fund_code"])
        data2 = db.find_all(sql2)
        sql3 = "SELECT nav FROM wd_zx.WD_FUND_NAV wfn WHERE  wfn.com_code ='G107138.GS' and day ='2021-09-30' and fund_code ='{}'".format(
            i["fund_code"])
        print(sql3, "111111111")
        # 取出每个基金的累计净值
        data3 = db.find_all(sql3)
        print(data3, "2222222222")
        if data3 == tuple:
            print("{}基金的是累积净值没取到".format(i["fund_code"]))

        print("{}基金的是累积净值".format(i["fund_code"]), data3[0]["nav"])
        # print("--------",data2)
        sum_chigu = data2[0]["SUM(marketvalueofstockholdings)"]
        if sum_chigu == None:
            sum_chigu = 0
        print("{}基金的持股市值是".format(i["fund_code"]), sum_chigu)
        # 单个基金市值占比
        one_zhanbi = sum_chigu / sum_total
        print("单个基金市值占比", one_zhanbi)
        # 单个公司业绩
        one_yeji = one_zhanbi * data3[0]["nav"]
        print("单个公司业绩", one_yeji)
        sum_yeji = one_yeji + sum_yeji

    print("当期公司业绩",sum_yeji)