"""猜数字游戏
1. 先由电脑在一个范围内随机生成一个数字
2.在输入数字后，电脑判断与生成数字的大小
    输入的数字大，输出“数字大了，数字在0-输入数字的范围内”
    输入的数字小，输出“数字小了，数字在输入数字-最大值的范围内”
    输入数字与生成数字相等就输出“你猜对了”
    结束
"""
import random

computer = random.randint(1, 100)


i = 1
while True:

    try:
        number = int(input("请输入数字："))
    except ValueError:
        print("请输入整数，范围为1-100")
        continue
    if number <= 100:
        if number > computer:
            print(f"您输入的数字过大，范围为 0-{number}")
            i += 1
        elif number < computer:
            print(f"您输入的数字过小，范围为 {number}-100")
            i += 1
        else:
            print(f"恭喜答对了，您一共输入了{i}次，结果是{computer}")
            break


    else:
        print("您输入的数字不在1-100之间，输入错误")
        continue