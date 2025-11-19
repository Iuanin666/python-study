import random
difficulty_choose = int(input("输入1选择简单模式猜1- 20:\n输入2选择困难模式猜1-100:"))

print("============")
if difficulty_choose == 1 :
    number = 20
else:
    number = 100
print(f"我心里想了一个1到{number}之间的数字")
print("你能猜到它是多少吗")
print("============")

#1 生成一个随机数

secret_number = random.randint(1,number)

#2 记录你猜了多少次

count = 0

#3 开启无限循环

while True:
    count += 1

    guess_str = input("请输入你猜测的数字（输入q退出）：")

    if guess_str =="q":
        print("胆小鬼，放弃了吗？再见！")
        break
    guess = int(guess_str)

    if guess == secret_number:
        print("恭喜你猜对了！")
        print(f"你一共猜了{count}次")
        break
    elif guess > secret_number:
        print("太大了！")
    else: print("太小了")

    if count ==5:
        print("你的五次机会已经用完")
        break
    else:print(f"这是第{count}次机会")
print("游戏结束")