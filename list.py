#!/usr/bin/env python
# encoding: utf-8
"""
@author: gravel_yan
@time: 2019/10/18 14:31

@desc: 将列表传递给函数，函数将返回该列表元素的字符串，并能增加元素
"""
from typing import List


def list_str(lists):
    new_str = ''
    for list in lists[:-1]:
        new_str += list + ', '
    return new_str + 'and ' + lists[-1]


fruits = ['apples', 'bananas', 'tofu', 'cats']
animals = ['cat', 'dog', 'tiger', 'pig']

print(list_str(fruits))
print(list_str(animals))
