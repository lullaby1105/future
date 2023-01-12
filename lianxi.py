from fractions import Fraction
from string import whitespace, punctuation
# #整数
# x = 9
# print("Output #4: {0}".format(x))
# print("Output #5: {0}".format(3**4))
# print("Output #6: {0}".format(int(8.3)/int(2.7)))
# #浮点数
# print("Output #7: {0:.3f}".format(8.3/2.7))
# y = 2.5*4.8
# print("output #7: {0:.1f}".format(y))
# r = 8/float(3)
# print("Output #9:{0:.2f}".format(r))  
# print("Output #10:{0:.4f}".format(8.0/3))
# print("Output #14:{0:s}".format('I\'m enjoying learning Python.'))

# 第一章
# total_seconds = 7385
# # 方法一
# hour = total_seconds // 3600  #2,向下取整
# remain_seconds = total_seconds % 3600 #取余
# print(remain_seconds)
# minutes = remain_seconds // 60
# seconds = remain_seconds % 60
# print(hour, minutes, seconds)
# # 方法二
# # 计算商和余数
# hours, remain_seconds = divmod(total_seconds, 3600)
# minutes, seconds = divmod(remain_seconds, 60)
# # 真除法
# hour = total_seconds / 3600
# hours = round(hours,4) #保留四位小数
# # 有理分数计算
# # 创建一个Fraction对象‘
# total_seconds = Fraction(7385)
# hour = total_seconds / 3600
# hours = round(float(hours), 4)

# 重写不可变的字符串
title = "Recipe 5: Rewriting, and the Immutable String"
# 查找边界
colon_position = title.index(':')
print(colon_position) #8
# 选择字符串(切片符号)
discard_text, post_colon_text = title[:colon_position], title[colon_position+1:]
print(discard_text, post_colon_text)
# 按照指定字符串分区
pre_colon_text, _, post_colon_text = title.partition(':')

# 替换更新字符串
# post_colon_text = post_colon_text.replace(' ','_')
for character in whitespace + punctuation:
    post_colon_text = post_colon_text.replace(character, '_')
print(post_colon_text)

# 删除多余的标点符号
# 删除开头和结尾的_
post_colon_text = post_colon_text.strip('_')
print(post_colon_text)
while "__" in post_colon_text:
    post_colon_text = post_colon_text.replace('__','_')

# 判断字符串是否全为数字
is_num = 'some word'.isnumeric()
print(is_num)
is_num = '1298'.isnumeric()





