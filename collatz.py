# Collatz序列（考拉兹猜想）

# def collatz(number):
#     if number % 2 == 0:
#         return number // 2
#     elif number % 2 == 1:
#         return 3 * number + 1
#
#
# try:
#     number = collatz(int(input("请输入一个数：")))
#     print(number)
#     while number != 1:
#         number = collatz(number)
#         print(number)
# except ValueError:
#     print("输入字符不合法！")


# 递归方式编写

def collatz(n):
    print(n)
    if n % 2 == 0:
        collatz(n // 2)
    elif n % 2 == 1 and n > 1:
        collatz(3 * n + 1)


if __name__ == '__main__':
    collatz(int(input("Enter a number：")))
