import math


def change(money, c, d):
    coins = 0
    for k in range(0, d):
        i_k = math.floor(money / c[k])
        money = money - c[k] * i_k
        coins += i_k
    return coins


print(change(77, [25, 20, 10, 5, 1], 5))


