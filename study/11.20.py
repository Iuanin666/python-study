import time
print("火箭发射倒计时")
#1 range的用法、
for i in range(10,0,-1):#从10开始 到0结束 不包含0 每次减一
    print(f"T-minus{i}")
    time.sleep(0.5)

print("点火！发射！")
print("===========================")


print("存钱罐逻辑")

total_money=0
days = int(input("你想存几天钱？："))

#2 正序循环
#range（1，days+1）比如输入5天 就是12345

for day in range(1,days+1):
    daily_save = day*10
    total_money+= daily_save

    print(f"第{day}天，存入{daily_save}元。总额为：{total_money}")

n = int(input())
for i in range(1,n+1):
    if i % 7==0:
        print(f"{i}是幸运数字")
    elif i%2==0:
        print(f"{i}是偶数")
    else:
        print(f"{i}平平无奇")

# 循环的进阶

print("模拟电子时钟")
print("为了演示方便 只跑两个小时 每个小时3分钟")

for hour in range(0,2):
    for minute in range(0,3):
        #这里的f-string用了02d 意思是保持两位数 不够补0
        print(f"当前时间:{hour:02d}：{minute:02d}")
        time.sleep(0.5)

    print(f"{hour}点钟结束了")

print("===========================")

print("逢4必过")

for i in range(1,11):
    if i == 4:
        print("tiaoguohuaishuzhi")
        continue
    print(f"baoshu:{i}")

print("dianmingjieshu")

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}",end=" ")#yishushi mei da yin wan jia yi ge kong ge
    print("")

import random
import time
print("yongzhedouelong")
player_hp=100
monster_hp=100

print(f"nidehp:{player_hp}|elonghp:{monster_hp}")
print("zhandoukaishi")
time.sleep(1)

while player_hp>0 and monster_hp>0:
    print("\n----------------------")
    print("lun dao ni le")
    choice = input("qingxuan zhe xing dong(1 gongji 2 taopao)")
    if choice == "1":
        #sui jigongji li 10-20
        dmg=random.randint(10,20)
        monster_hp-=dmg
        print(f"nifa qi le gong ji e long shou dao {dmg}dian shanghai")

    elif choice == "2":
        print("ni shitu tao pao ")
        if random.randint(1,10)<=3:
            print("tao pao cheng gong")
            break
        else:
            print("tao pao shi bai")
    else:
        print("ni lang fei le yige huihe")
    if monster_hp<=0:
        print("gongxini jibaile e long")
        break

    time.sleep(1)

    print("elong paoxiaochongle guolai")
    enemy_dmg=random.randint(5,25)
    player_hp-=enemy_dmg
    print(f"nishoudao {enemy_dmg}dian shanghai")
    print(f"dangqianzhuangtai n i:{player_hp}HP e long:{monster_hp}HP")

    if player_hp<=0:
        print("nishule")
        break
print("game over")