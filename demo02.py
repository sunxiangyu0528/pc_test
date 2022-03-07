def func(a):
    print("这是函数func")
    print("这个是传入的参数a：", a)


li = [11, 22, 33, 44]
res = filter(func, li)
print(list(res))


def func(a):
    return a > 100


li = [11, 22, 33, 44, 111, 222, 444]
res = filter(func, li)
print(list(res))  # 结果：[111, 222, 444]
