import pymysql


class DB:
    def __init__(self):
        # 创建一个连接对象
        self.conn = pymysql.connect(host="rm-uf678n3wgb0j1nth2.mysql.rds.aliyuncs.com",
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
    db = DB()  # 证券代码
    sql = 'select industry_pe  from  institution.ins_industry_pe_info iimpi where industry_code =740000  and pe_type =1 and calculate_date between  "2020-12-28 "  and "2021-12-28"'
    data = db.find_all(sql=sql)
    print(data)
    li1 = []
    # 得到的而每一个Pettm存储起来
    for i in data:
        a = i["industry_pe"]
        # print(a)
        li1.append(a)
    # 从小到大排序
    li1.sort()
    print("PETTM总个数为：",li1)
    #     li1.append(i["PETTM"])
    print(len(li1))
    print(li1)
    # 单数，偶数，判断
    if len(li1) % 2 == 0:
        b = int(len(li1) / 2)
        print("中位数是",b, type(b))
        # C 轨道的值
        PETTM = (li1[b - 1] + li1[b]) / 2


        print("PETTM是（A轨道）：", PETTM * 2 - li1[0])
        print("PETTM是（B轨道）：", (PETTM * 2 - li1[0] + PETTM) / 2)
        print("PETTM是（C轨道）：", PETTM)
        print("PETTM是（D轨道）：", (li1[0] + PETTM) / 2)
        print("PETTM是（E轨道）：", li1[0])
        print("------------------------------------------------------")


    # 奇数的情况
    else:
        b = int(len(li1) / 2 - 0.5)
        print(b)
        PETTM = li1[b]


        print("PETTM是（A轨道）：", PETTM * 2 - li1[0])
        print("PETTM是（B轨道）：", (PETTM * 2 - li1[0] + PETTM) / 2)
        print("PETTM是（C轨道）：", PETTM)
        print("PETTM是（D轨道）：", (li1[0] + PETTM) / 2)
        print("PETTM是（E轨道）：", li1[0])
        print("------------------------------------------------------")
