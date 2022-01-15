# 20220115
# 백준 13305 주유소
# https://www.acmicpc.net/problem/13305

# 4
# 2 3 1
# 5 2 4 1


n = int(input())
distance = list(map(int,input().split()))
cost = list(map(int,input().split()))

min = cost[0]
money = 0


for i in range(n-1):
    if cost[i] < min :
        min = cost[i]
    money += min * distance[i]

print(money)