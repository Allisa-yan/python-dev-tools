# 猜数字游戏
import random


def guess_number():
    """猜数字游戏"""
    number = random.randint(1, 20)
    print(f"当前我内心所想数字在1~20之间，请猜猜是哪个呢？你总共有6次机会哦~")
    print(f'随机数为：{number}')
    i = 6
    while i > 0:
        try:
            guess_number = int(input("请输入你猜测的数字："))
            if guess_number == number:
                print("猜就对，欢迎下次再来！")
                break
            elif guess_number > 20 or guess_number < 1:
                print("不在范围内啦~")
            elif guess_number > number:
                print("猜大了")
            else:
                print("猜小了")
        except ValueError:
            print("非法输入，请重新开始！！！")
        i = i-1
        if i == 0:
            print("机会用完啦~~下次再来吧")
            break
        print(f'你还有{i}次机会哦~')


guess_number()
