from common.Basedb import DB, DB_Beta

db = DB()
db_beta = DB_Beta()
# ,tso.*
sql = "SELECT tso.HOLDERANUM ,tso.COMPCODE FROM zgzb_zx.TQ_SK_OTSHOLDER tso WHERE SHHOLDERNAME = '赵建平' and ENDDATE = '20210930';"
data = db.find_all(sql)
li =[]
print(data)
for i in data:
    sql2 = "SELECT tos.SWLEVEL1NAME ,tos.SYMBOL,tos.* FROM zgzb_zx.TQ_SK_BASICINFO tos WHERE COMPCODE = {};".format(
        i["COMPCODE"])
    data2 = db.find_all(sql2)
    # print(data2)
    sql3 = "select isdk.day_k_bef ,isdk.* from institution.ins_stock_day_k isdk where stockCode like '%{}%' and tradeDate ='20220304';".format(
        data2[0]["SYMBOL"])
    data3 = db_beta.find_all(sql3)
    # print('data3', data3)
    #print(type(data3[0]["day_k_bef"]), data3[0]["day_k_bef"])
    new_dic = eval(data3[0]["day_k_bef"])
    #print("---new-dic---", type(new_dic), new_dic)
    print(
        "股票{}，公司内码{},行业{},的持股数量是{},前复权收盘价是{}".format(data2[0]["SYMBOL"], i["COMPCODE"], data2[0]["SWLEVEL1NAME"],
                                                     i["HOLDERANUM"]
                                                     , new_dic["fClose"]))
    li.append(new_dic["fClose"])
li.sort()
print(li)