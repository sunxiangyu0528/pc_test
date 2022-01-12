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


if __name__ == '__main__':
    pass
