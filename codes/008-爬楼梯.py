# -*- coding:utf-8 -*-

def climbStairs(n):
    a, b = 1, 1
    i = 0
    while i < n:
        a, b = b, a+b
        i += 1
    return a


print(climbStairs(3))
print(climbStairs(4))
print(climbStairs(5))
print(climbStairs(6))