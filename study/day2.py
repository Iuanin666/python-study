print("==============")
print("欢迎来到python冒险乐园！")
print("==============")

#1 询问身高

height = int(input("请输入你的身高（cm）:"))
bill = 0

#2 第一层判断 身高够不够

if height>= 120:
    print("身高符合要求，请购票。")

    #3 内部判断 根据年龄定票价

    age = int(input("请输入你的年龄："))

    if age<12:
        bill=50
        print("检测到儿童票：$50")
    elif age<=18:
        bill = 70
        print("检测到青年票：$70")
    elif age>=60:
        bill = 60
        print("检测到敬老票：$60")
    else:
        bill = 100
        print("检测到成人票：$100")

    #4 额外服务 要不要拍照

    wants_photo =input("是否需要拍照服务？（y/n）:")
    if wants_photo=="y":
        bill+=30
        print("您已添加拍照服务（+$30）")

    print(f"您的最终票价为${bill}")
else:
    print("您的身高不足120cm,您可以免费入园！")
    print("最终票价：$0")

print("祝您游玩愉快！")