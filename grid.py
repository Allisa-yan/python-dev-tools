#!/user/bin/env python
# encoding:utf-8
"""
@author:gravel_yan
@time:2021/4/299:52

@desc: 打印字符图网格
"""


def print_strGrid():
    grid = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']
    ]
    for j in range(0, len(grid[0])):
        for i in range(0, len(grid)):
            print(grid[i][j], end='')
        print()


print_strGrid()
