import random

coin = random.choice(['heads', 'tails'])  # random.choice([])里面跟列表，在括号内的选项进行随机选一
print(coin)

cards = ['jack', 'queen', 'king']
random.shuffle(cards)   # random.shuffle()可以让列表中的数据随机打乱进行排列，相当于洗牌
for i in cards:
    print(i)