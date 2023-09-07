# 记录生肖，根据年份来判断生效
chinese_zodiac="猴鸡狗猪鼠牛虎兔龙蛇马羊"
year=int(input("请输入你的出生年份:"))
print(chinese_zodiac[year % 12])
if ("狗" in chinese_zodiac):
    print('在十二生肖')


#我现在很多python的语法都忘完求了