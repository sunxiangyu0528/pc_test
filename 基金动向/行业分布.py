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
    sql4 = "SELECT * FROM wd_zx.WD_FUND_COM_INFO wfci WHERE code ='G160072.GS'  and  enddate ='2021-09-30';"
    data4 = db.find_all(sql4)
    if data4[0]["stockfundassetstotal"]==None :
        data4[0]["stockfundassetstotal"] =0
    if data4[0]["mixfundassetstotal"] == None:
        data4[0]["mixfundassetstotal"] = 0
    sum_total = data4[0]["stockfundassetstotal"] + data4[0]["mixfundassetstotal"]
    print("总市值是：", data4[0]["stockfundassetstotal"] + data4[0]["mixfundassetstotal"])

    sql1 = "SELECT stock_code,wfsr.* FROM wd_zx.WD_FUND_STOCK_RECORD wfsr WHERE cmp_code ='G160072.GS' and rpt_day ='2021-09-30' and stock_code  not like '%HK'  "
    data1 = db.find_all(sql1)
    print(data1)
    li = []
    dic1 = {}
    sum = 0
    for i in data1:
        i_code = i["stock_code"][0:6]
        sql2 = "SELECT tsb.SWLEVEL1NAME,tsb.SWLEVEL1CODE,tsb.SYMBOL  FROM zgzb_zx.TQ_SK_BASICINFO tsb WHERE SYMBOL like '%{}%'".format(
            i_code)
        data2 = db.find_all(sql2)
        if data2[0]["SWLEVEL1NAME"] == "基础化工":
            print(data2[0]["SYMBOL"])
        #  计算农林牧渔行业净值
        if data2[0]["SWLEVEL1NAME"] == "基础化工":
            sql3 = "SELECT * FROM wd_zx.WD_FUND_STOCK_RECORD wfsr WHERE cmp_code ='G160072.GS' and rpt_day ='2021-09-30' and fund_code = '{}' and " \
                   "stock_code like '%{}%' ".format(i["fund_code"], data2[0]["SYMBOL"])
            data3 = db.find_all(sql3)
            print(sql3)
            print(data3[0]["marketvalueofstockholdings"])
            sum = sum + data3[0]["marketvalueofstockholdings"]
            print("sum-----", sum)
            print(sum)
            print("占净值比", (sum / sum_total) / 100)
