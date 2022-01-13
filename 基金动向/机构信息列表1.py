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
    # li_comp = []
    # sql_comp = "SELECT DISTINCT code FROM wd_zx.WD_FUND_COM_INFO wfci WHERE code is not null"
    # data_comp = db.find_all(sql_comp)
    #
    # print(data_comp)
    # li3 = []
    # for i in data_comp:
    sql_zsz = "SELECT * FROM wd_zx.WD_FUND_COM_INFO wfci WHERE code ='G107138.GS'  and  enddate ='2022-01-08';"
    data_zsz = db.find_all(sql_zsz)
    print(data_zsz)
    print("股票型-基金资产净值合计", data_zsz[0]["stockfundassetstotal"])
    print("混合型-基金资金净值合计", data_zsz[0]["mixfundassetstotal"])
    # 基金资产净值合计为空情况，把值负值为0
    if data_zsz[0]["stockfundassetstotal"] == None:
        data_zsz[0]["stockfundassetstotal"] = 0
    if data_zsz[0]["mixfundassetstotal"] == None:
        data_zsz[0]["mixfundassetstotal"] = 0
    print("混合型+股票型=基金资金净值合计", data_zsz[0]["mixfundassetstotal"] + data_zsz[0]["stockfundassetstotal"])

    # 取出这个公司下面的所有基金
    sql1 = "SELECT fund_code FROM wd_zx.WD_FUND_NAV wfn WHERE  wfn.com_code ='G107138.GS' and `day` ='2022-01-07';"
    data_1 = db.find_all(sql1)
    print("data_1===============", len(data_1), data_1)

    li1 = []

    li2 = []
    sum = 0

    for i in data_1:

        print("##############################################################################")
        print(i["fund_code"][0:6])
        sql2 = "select tfbi.setup_date from fund.t_fund_base_info tfbi where beta_code like '%{}%';".format(
            i["fund_code"][0:6])

        data_2 = db_beta.find_all(sql2)
        sql3 = "SELECT fund_code,nav FROM wd_zx.WD_FUND_NAV wfn WHERE  wfn.fund_code ='{}' and `day` ='2022-01-07'".format(
            i["fund_code"])
        date3 = db.find_all(sql3)
        print("基金{}的累计单位净值是：".format(i["fund_code"]), date3[0]["nav"])
        # 当基金成立日期没值的时候，跳过这个基金
        if type(data_2) == tuple:
            continue
        print("基金{}成立日期是：".format(i["fund_code"]), data_2[0]["setup_date"])
        # 计算基金成立了多少年
        aaaaa = date_minus(data_2[0]["setup_date"], "20220108")
        # 四舍五入成立的年数
        print(aaaaa)
        bbbb =round(aaaaa,4)
        print("基金成立了多少年", bbbb)
        # 单基金平均年化收益=(累计单位净值-1)/基金成立年限
        cccc = round(float((date3[0]["nav"] - 1)) / aaaaa,2)
        print("单基金平均年化收益",cccc)
        print("单基金平均年化收益:", float((date3[0]["nav"] - 1)) / aaaaa)
        # 所有的基金相加
        # sum = sum + float((date3[0]["nav"] - 1)) / aaaaa
        sum =  sum + cccc
        print("{}公司所有基金的平均年华收益率:".format(data_zsz[0]["code"]), round(sum,2))
        li2.append(sum)
        # li2.sort()
        # print(li2)
        print("li2===========", len(li2), li2)
    print("li2sort之后的结果", li2)
    print("除以基金数量的结果",sum/len(li2))

# 得到所有基金代码
b = time.time()
print("运行时间为", b - a)
