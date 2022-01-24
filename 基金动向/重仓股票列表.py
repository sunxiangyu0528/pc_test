import pymysql
import requests


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


if __name__ == '__main__':
    db = DB()  # 证券代码
    sql = " SELECT DISTINCT fund_code FROM wd_zx.WD_FUND_STOCK_RECORD  wfsr WHERE cmp_code = 'G107081.GS'  and rpt_day ='2021-09-30';"
    data = db.find_all(sql)
    print(data)
    li = {}
    li1 = []
    for i in data:
        sql2 = "SELECT SUM(marketvalueofstockholdings) FROM wd_zx.WD_FUND_STOCK_RECORD  wfsr WHERE fund_code  = '{}'" \
               " and  rpt_day ='2021-09-30';".format(i["fund_code"])
        data2 = db.find_all(sql2)
        print(data2)
        print(i["fund_code"])
        li.update({i["fund_code"]: data2[0]["SUM(marketvalueofstockholdings)"]})
        li1.append(data2[0]["SUM(marketvalueofstockholdings)"])

    li1.sort(reverse=True)

    print(li1)
    print(li)

tu1 = (
    '011104.OF', '360001.OF', '360016.OF', '001740.OF', '360007.OF', '012758.OF', '012744.OF', '010676.OF', '002472.OF',
    '013350.OF')

