#!/user/bin/env python
# encoding:utf-8
"""
@author:gravel_yan
@time:2021/4/2913:23

@desc: 统计字典中所有值的总和
"""


def displayInventory(inventory):
    count = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        count += v
    print("总共包含多少个物品：" + str(count))


def addToInventory(inventory, dragonLoot):
    for i in range(len(dragonLoot)):
        inventory.setdefault(dragonLoot[i], 0)
        inventory[dragonLoot[i]] += 1
    return inventory


stuff = {'rope': 1, 'torch': 12, 'dagger': 34, 'arrow': 5}
dragonLoot = ['dagger', 'gold coin', 'gold coin', 'arrow']
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
