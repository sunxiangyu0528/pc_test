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

    # 输入证券代码
    sql = "SELECT COMPCODE ,SWLEVEL1CODE ,SWLEVEL1NAME ,a.* FROM zgzb_zx.TQ_SK_BASICINFO a WHERE SYMBOL=000711 ;"
    data = db.find_all(sql)
    print(data[0]["COMPCODE"])
    print(data[0]["SYMBOL"])
    print(data[0]["SECODE"])
    sql2 = "SELECT tss.ENDDATE,tss.ENTRYDATE ,tss.UPDATEDATE , tss.PUBLISHDATE,tss.ASKSHAMT,tss.* FROM zgzb_zx.TQ_SK_SHAREHOLDERNUM tss WHERE COMPCODE ={} order by ENDDATE  desc".format(
        data[0]["COMPCODE"])
    data2 = db.find_all(sql2)
    print("A股股东户数：", data2[0]["ASKSHAMT"], "时间是：", data2[0]["ENDDATE"])
    print("A股股东户数：", data2[1]["ASKSHAMT"], "时间是：", data2[1]["ENDDATE"])
    print("A股股东户数：", data2[2]["ASKSHAMT"], "时间是：", data2[2]["ENDDATE"])
    print("A股股东户数：", data2[4]["ASKSHAMT"], "时间是：", data2[4]["ENDDATE"])

    print("近一季度股东变化总数：", (data2[0]["ASKSHAMT"] - data2[1]["ASKSHAMT"]),
          "股东户数变动为", (data2[0]["ASKSHAMT"] - data2[1]["ASKSHAMT"]) / data2[1]["ASKSHAMT"])
    print("近半年股东变化总数：", (data2[0]["ASKSHAMT"] - data2[2]["ASKSHAMT"]),
          "股东户数变动为", (data2[0]["ASKSHAMT"] - data2[2]["ASKSHAMT"]) / data2[2]["ASKSHAMT"])
    print("近一年度股东变化总数：", (data2[0]["ASKSHAMT"] - data2[4]["ASKSHAMT"]),
          "股东户数变动为", (data2[0]["ASKSHAMT"] - data2[4]["ASKSHAMT"]) / data2[4]["ASKSHAMT"])
    # 收盘价
    sql_TCLOSE = "SELECT a.TCLOSE,a.* FROM zgzb_zx.TQ_QT_SKDAILYPRICE  a WHERE a.ENTRYDATE ='20220104' and a.SECODE ={};".format(
        data[0]["SECODE"])
    # 前复权收盘价（吴健）
    data_TCLOSE = db.find_all(sql_TCLOSE)
    # 期末价格为
    print("收盘价为：", data_TCLOSE[0]["TCLOSE"])
    sql3 = "SELECT a.wrating_targetprice ,a.rating_avgchn ,a.* FROM wd_zx.WD_SK_WSSINFO_FORYY a  WHERE windcode LIKE'%{}%' order by enddate desc;".format(
        data[0]["SYMBOL"])

    data3 = db.find_all(sql3)
    print(data3)
    # 上涨空间 ——  round(（一致目标价 – 最新收盘价）/最新收盘价,4)*100%
    print("一致预测目标价", data3[0]["wrating_targetprice"], "综合评级(中文)", data3[0]["rating_avgchn"], "上涨空间",
          ((float(data3[0]["wrating_targetprice"]) - float(data_TCLOSE[0]["TCLOSE"])) / float(
              data_TCLOSE[0]["TCLOSE"])))

    # 流通股占比
    sql4 = "SELECT a.CIRCSKAAMT ,a.ASK ,a.* FROM zgzb_zx.TQ_SK_SHAREHOLDERNUM a WHERE ENDDATE ='20210930' and COMPCODE ={}".format(
        data[0]["COMPCODE"])
    data4 = db.find_all(sql4)
    print("流通股占比", data4[0]["CIRCSKAAMT"] / data4[0]["ASK"])

    #
