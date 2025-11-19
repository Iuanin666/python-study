# --- day1：间谍身份生成器 ---
import datetime

#1,获取当前年份
current_yeat = datetime.datetime.now().year

print("=================")
print("欢迎进入M16特工系统")
print("=================")

#2.获取用户输入

code_name = input("请输入你的特工代号：")
age_str = input("请输入你的伪装年龄：")

#3，数据类型转换

age = int(age_str)

#4.进行简单的数学运算

birth_yeat = current_yeat-age
training_years = age//2

#5 格式化输出
print("\n---正在生存档案---")
print(f"特工：{code_name}")
print(f"出生年份：{birth_yeat}(推测)")
print(f"已受训练时长:{training_years}年")
print("==================")
print("系统关闭。注意安全，"+code_name+"。")