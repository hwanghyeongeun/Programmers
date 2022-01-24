# 20220124 11720 숫자의 합
# String (문자열)
# https://www.acmicpc.net/problem/11720

N = int(input())
number = input()
result = 0

for i in range(N):
    result += int(number[i])

print(result)