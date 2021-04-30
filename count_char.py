#!/user/bin/env python
# encoding:utf-8
"""
@author:gravel_yan
@time:2021/4/2910:56

@desc: 统计一个字符串中字符出现次数
"""
message = 'It was a bright cold day in April,and the clocks were striking thirteen.'
count = {}
for char in message:
    count.setdefault(char, 0)
    count[char] += 1
print(count)
