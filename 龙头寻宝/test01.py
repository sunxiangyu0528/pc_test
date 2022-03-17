from common.Basedb import DB, DB_Beta, DB_longtou

db = DB()
db_beta = DB_Beta()
db_lt = DB_longtou()
sql = "SELECT PreClosePrice ,LimitUpPrice,NowPrice FROM present_quotation.HQ_MINUTE_V1_ALL hmva WHERE hqtime = '202110111020';"
Sum = 0
data = db_lt.find_all(sql)
for i in data:
    if i["NowPrice"] >= i["LimitUpPrice"]:
        Sum = Sum + 1
print(Sum)
