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
    # 沪深300当日总市值
    sql_zsz = "SELECT sum(TOTMKTCAP)  FROM zgzb_zx.TQ_SK_FININDIC WHERE   TRADEDATE='20211213'   and  SYMBOL IN (SELECT DISTINCT (SAMPLECODE) FROM zgzb_zx.TQ_IX_COMP tic WHERE SYMBOL =000300 AND USESTATUS = 1);"
    data_zsz = db.find_all(sql_zsz)
    print(data_zsz)
    print("沪深300当日总市值", data_zsz[0]["sum(TOTMKTCAP)"])
    print(data_zsz[0]["sum(TOTMKTCAP)"])
    d = 0
    # 查到沪深300的COMPCODE
    sql2 = "SELECT  COMPCODE  FROM zgzb_zx.TQ_SK_BASICINFO WHERE SYMBOL in (SELECT DISTINCT (SAMPLECODE) FROM zgzb_zx.TQ_IX_COMP tic WHERE SYMBOL =000300 AND USESTATUS = 1) AND ISVALID=1 and SWLEVEL1CODE is not null;"
    data2 = db.find_all(sql2)
    compcode_list = []
    for b in data2:
        compcode_list.append(b["COMPCODE"])
    print("compcode_list", compcode_list)
    li = ['20210930', '20201231', '20200930']
    # compcode_list = ['10000011']
    print(len(compcode_list))
    for c in compcode_list:
        sum = 0
        sql3 = "SELECT PARENETP,REPORTTYPE   FROM zgzb_zx.TQ_FIN_PROINCSTATEMENTNEW WHERE COMPCODE = {} AND ISVALID = 1 AND ISACTPUB = 1 AND REPORTTYPE in(1, 3) and ENDDATE =20210930".format(
            c)
        data1 = db.find_all(sql=sql3)
        if len(data1) == 1:
            sql4 = "SELECT PARENETP,REPORTTYPE ,REPORTDATETYPE ,ENDDATE , COMPCODE FROM zgzb_zx.TQ_FIN_PROINCSTATEMENTNEW WHERE" \
                   " COMPCODE = {} AND ISVALID = 1 AND ISACTPUB = 1  and ENDDATE ='20210930' and REPORTTYPE !=2 and REPORTTYPE !=4 ".format(
                c)
            data4 = db.find_all(sql=sql4)
            print("COMPCODE-----", data4[0]["COMPCODE"])
            print("data4，{20210930},,,,,PARENETP", data4[0]["PARENETP"])
            data_20210930 = data4[0]["PARENETP"]
        else:
            sql4 = "SELECT PARENETP,REPORTTYPE ,REPORTDATETYPE ,ENDDATE , COMPCODE FROM zgzb_zx.TQ_FIN_PROINCSTATEMENTNEW WHERE " \
                   "COMPCODE = {} AND ISVALID = 1 AND ISACTPUB = 1 AND REPORTTYPE =3 and ENDDATE ='20210930' and REPORTTYPE !=2 and REPORTTYPE !=4 ".format(
                c)
            data4 = db.find_all(sql=sql4)
            print("COMPCODE-----", data4[0]["COMPCODE"])
            print("data4，{20210930},,,,,PARENETP", data4[0]["PARENETP"])
            data_20210930 = data4[0]["PARENETP"]

        sql5 = "SELECT PARENETP,REPORTTYPE   FROM zgzb_zx.TQ_FIN_PROINCSTATEMENTNEW WHERE COMPCODE = {} AND ISVALID = 1 AND ISACTPUB = 1 AND REPORTTYPE in(1, 3) and ENDDATE =20201231".format(
            c)
        data2 = db.find_all(sql=sql5)
        if len(data2) == 1:
            sql6 = "SELECT PARENETP,REPORTTYPE ,REPORTDATETYPE ,ENDDATE , COMPCODE FROM zgzb_zx.TQ_FIN_PROINCSTATEMENTNEW WHERE " \
                   "COMPCODE = {} AND ISVALID = 1 AND ISACTPUB = 1  and ENDDATE ='20201231' and REPORTTYPE !=2 and REPORTTYPE !=4 ".format(
                c)
            data6 = db.find_all(sql=sql6)
            print(sql6)
            print("COMPCODE-----",data6[0]["COMPCODE"])
            print("data6，{20201231},,,,,PARENETP", data6[0]["PARENETP"])
            data_20201231 = data6[0]["PARENETP"]
            # global data_20201231
        else:
            sql6 = "SELECT PARENETP,REPORTTYPE ,REPORTDATETYPE ,ENDDATE , COMPCODE FROM zgzb_zx.TQ_FIN_PROINCSTATEMENTNEW WHERE " \
                   "COMPCODE = {} AND ISVALID = 1 AND ISACTPUB = 1 AND REPORTTYPE =3 and ENDDATE ='20201231' and REPORTTYPE !=2 and REPORTTYPE !=4 ".format(
                c)
            data6 = db.find_all(sql=sql6)
            print("COMPCODE-----",data6[0]["COMPCODE"])
            print(sql6)

            print("data6，{20201231},,,,,PARENETP", data6[0]["PARENETP"])
            data_20201231 = data6[0]["PARENETP"]
            # global data_20201231

        sql7 = "SELECT PARENETP,REPORTTYPE   FROM zgzb_zx.TQ_FIN_PROINCSTATEMENTNEW WHERE COMPCODE = {} AND ISVALID = 1 AND ISACTPUB = 1 AND REPORTTYPE in(1, 3) and ENDDATE =20200930".format(
            c)
        data3 = db.find_all(sql=sql7)
        if len(data3) == 1:
            sql8 = "SELECT PARENETP,REPORTTYPE ,REPORTDATETYPE ,ENDDATE , COMPCODE FROM zgzb_zx.TQ_FIN_PROINCSTATEMENTNEW WHERE " \
                   "COMPCODE = {} AND ISVALID = 1 AND ISACTPUB = 1  and ENDDATE ='20200930' and REPORTTYPE !=2 and REPORTTYPE !=4 ".format(
                c)
            data8 = db.find_all(sql=sql8)

            print("data8，{20200930},,,,,PARENETP", data8[0]["PARENETP"])
            data_20200930 = data8[0]["PARENETP"]
        else:
            sql8 = "SELECT PARENETP,REPORTTYPE ,REPORTDATETYPE ,ENDDATE , COMPCODE FROM zgzb_zx.TQ_FIN_PROINCSTATEMENTNEW WHERE " \
                   "COMPCODE = {} AND ISVALID = 1 AND ISACTPUB = 1 AND REPORTTYPE =3 and ENDDATE ='20200930' and REPORTTYPE !=2 and REPORTTYPE !=4 ".format(c)
            data8 = db.find_all(sql=sql8)
            print("data8，{20200930},,,,,PARENETP", data8[0]["PARENETP"])
            data_20200930 = data8[0]["PARENETP"]
            # global data_20200930
        sum = data_20210930 + data_20201231 - data_20200930
        d = d + sum
        print("sum的值：", sum)
        print("d的值：", d)

print("沪深300当天PE", data_zsz[0]["sum(TOTMKTCAP)"] / d)
