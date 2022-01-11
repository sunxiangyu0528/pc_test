import pymysql


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
    sql_zsz = "SELECT SUM(TOTMKTCAP)  FROM zgzb_zx.TQ_SK_FININDIC WHERE   TRADEDATE='20211213'   and  SYMBOL IN (SELECT SYMBOL  FROM zgzb_zx.TQ_SK_BASICINFO WHERE SWLEVEL1CODE = '740000' AND SWLEVEL1NAME IS NOT NULL AND SWLEVEL1CODE IS NOT NULL AND SWLEVEL1NAME != '' AND SWLEVEL1CODE != '' AND   SWLEVEL1CODE = '740000' AND SETYPE = 101 AND ISVALID = 1 AND LISTSTATUS = 1);"
    data_zsz = db.find_all(sql_zsz)
    print("银行行业当日总市值", data_zsz[0]["SUM(TOTMKTCAP)"])
    d = 0
    sql2 = "SELECT COMPCODE FROM zgzb_zx.TQ_SK_BASICINFO WHERE SWLEVEL1CODE = '740000' AND SWLEVEL1NAME IS NOT NULL AND SWLEVEL1CODE IS NOT NULL AND SWLEVEL1NAME != '' AND SWLEVEL1CODE != '' AND SWLEVEL1CODE = '740000' AND SETYPE = 101 AND ISVALID = 1 AND LISTSTATUS = 1;  "
    data2 = db.find_all(sql2)
    compcode_list = []
    for b in data2:
        compcode_list.append(b["COMPCODE"])
    print("compcode_list", compcode_list)
    # print(data2)
    li = ['20210630', '20201231', '20200630']
    for c in compcode_list:

        sum = 0
        for i in li:

            # sql2 = "SELECT PARENETP,REPORTTYPE ,REPORTDATETYPE ,ENDDATE , COMPCODE  FROM zgzb_zx.TQ_FIN_PROINCSTATEMENTNEW WHERE COMPCODE = 80097223 AND ISVALID = 1 AND ISACTPUB = 1 AND REPORTTYPE in(1, 3) ORDER  by ENDDATE desc;"
            sql3 = "SELECT PARENETP,REPORTTYPE ,REPORTDATETYPE ,ENDDATE , COMPCODE FROM zgzb_zx.TQ_FIN_PROINCSTATEMENTNEW WHERE COMPCODE = {} AND ISVALID = 1 AND ISACTPUB = 1 AND REPORTTYPE in(1, 3) and ENDDATE ={}".format(
                c, i)
            data = db.find_all(sql=sql3)
            print(data)
            if len(data) == 1:
                sql4 = "SELECT PARENETP,REPORTTYPE ,REPORTDATETYPE ,ENDDATE , COMPCODE FROM zgzb_zx.TQ_FIN_PROINCSTATEMENTNEW WHERE COMPCODE = {} AND ISVALID = 1 AND ISACTPUB = 1 AND REPORTTYPE =1 and ENDDATE ={}".format(
                    c, i)
                data4 = db.find_all(sql=sql4)
                print("data4，{}".format(i), data4[0]["PARENETP"])
                sum = sum + data4[0]["PARENETP"]
            elif len(data) == 2:
                sql5 = "SELECT PARENETP,REPORTTYPE ,REPORTDATETYPE ,ENDDATE , COMPCODE FROM zgzb_zx.TQ_FIN_PROINCSTATEMENTNEW WHERE COMPCODE = {} AND ISVALID = 1 AND ISACTPUB = 1 AND REPORTTYPE =3 and ENDDATE ={}".format(
                    c, i)
                data5 = db.find_all(sql=sql5)
                print("data5，{}".format(i), data5[0]["PARENETP"])
                if i == "20200630":
                    sum = sum - data5[0]["PARENETP"]
                else:
                    sum = sum + data5[0]["PARENETP"]
        print("summmmmmmm", sum)
        d = d + sum
        print("dddddddddddd", d)


    print("当天PE",data_zsz[0]["SUM(TOTMKTCAP)"]/d)