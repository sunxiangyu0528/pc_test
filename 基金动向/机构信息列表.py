import requests
import jsonpath
data={
   "averageRate":20,
   "totalNetworth":30
}
url = 'http://10.5.6.181:16630/v1/fundTrends/institution/list'
response=requests.post(url=url,json=data)
res = response.json()
print(res)

# print(jsonpath.jsonpath(res,"$..averageRate"))
li = jsonpath.jsonpath(res,"$..averageRate")
li.sort(reverse=True)
print("平均年化收益率",len(li),li)

li2 = jsonpath.jsonpath(res,"$..averageRate")
li2.sort(reverse=True)
print("平均年化收益率",len(li2),li2)