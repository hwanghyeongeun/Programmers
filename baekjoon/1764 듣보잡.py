# 20220124 1764 듣보잡
# String (문자열)
# https://www.acmicpc.net/problem/1764

N,M = map(int,input().split()) #N 듣도 M 보도

A = set()
for i in range(N):
    A.add(input())

B = set()
for i in range(M):
    B.add(input())

answer = sorted(list(A&B))
print(len(answer))

for i in range(len(answer)):
    print(answer[i])