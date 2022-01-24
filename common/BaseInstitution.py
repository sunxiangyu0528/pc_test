import requests
import jsonpath

base_url = 'http://10.5.6.181:16630'


class GetMessage(object):

    def get_highYieldFlag(self):
        url = base_url + '/v1/fundTrends/institution/list'
        jsondata = {
            "averageRate": 5,
            "totalNetworth": 30
        }

        response = requests.post(url=url, json=jsondata)
        res = response.json()
        li = []
        for i in res["result"]:
            # print(i)
            if i["highYieldFlag"] == 1:
                li.append(i["fundInsCode"])

        print(li)
        return li

    def get_stock_code(self):


if __name__ == '__main__':
    msg = GetMessage()
    msg.get_highYieldFlag()
