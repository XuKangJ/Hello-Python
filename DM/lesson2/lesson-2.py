#列表
a = '中国'
b = '美国'
c = '法国'
d = '英国'
e = '意大利'
beautiful_girl = [a,b,c,d,e,d,d,]
print(beautiful_girl.count("英国"))
print(beautiful_girl[4])

#添加
f = '克罗地亚'
beautiful_girl.append(f)
print(beautiful_girl)

#删除
del beautiful_girl[2]
print(beautiful_girl)

#元组
country1 = ('瑞士','哥伦比亚','阿根廷',)
country2 = ('希腊','威尼斯','加拿大',)
country3 = (country1 + country2)
print(country3)
print(country3[3])
print(country3[1:4])

#字典
dic = {'name':'xkj','money':666,'habitation':'ShenZhen'}
print(dic)
print(dic['habitation'])
dic ['Marriage'] = 'single'
print(dic)
del dic['money']
print(dic)

