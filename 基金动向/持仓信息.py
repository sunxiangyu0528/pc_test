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
    db_beta = DB_Beta()
    sql = "SELECT wfsr.stock_code ,wfsr.* FROM wd_zx.WD_FUND_STOCK_RECORD wfsr WHERE cmp_code ='G107138.GS' and rpt_day ='2021-09-30' and stock_code  not like '%HK' "
    data = db.find_all(sql)
    print(data)
    li = []
    sum = 0
    for i in data:
        print(i)
        i_code = i["stock_code"][0:6]
        print(i_code)
        sql1 = "SELECT tsb.SWLEVEL1CODE ,tsb.SWLEVEL1NAME ,tsb.SYMBOL FROM zgzb_zx.TQ_SK_BASICINFO tsb WHERE SYMBOL like '%{}%';".format(
            i_code)
        data1 = db.find_all(sql1)
        print(data1)
        if data1[0]["SWLEVEL1NAME"] == "农林牧渔":
            li.append(data1[0]["SYMBOL"])
            sql2 = "SELECT wfsr.stock_code ,wfsr.* FROM wd_zx.WD_FUND_STOCK_RECORD wfsr WHERE cmp_code ='G107138.GS' and rpt_day ='2021-09-30' and stock_code like '%{}%' and fund_code='{}'".format(
                data1[0]["SYMBOL"], i["fund_code"])
            print("sql2====", sql2)
            data2 = db.find_all(sql2)
            print("data2====", data2)
            print("持股数量为：", data2[0]["hold_number"])
            sql3 = ""
            db_beta.find_all()
