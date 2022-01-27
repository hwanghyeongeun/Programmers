# 20220127 16916 부분문자열
# String
# https://www.acmicpc.net/problem/16916

# 문자열 S의 부분 문자열이란, 문자열의 연속된 일부를 의미한다.
# 예를 들어, "aek", "joo", "ekj"는 "baekjoon"의 부분 문자열이고, "bak", "p", "oone"는 부분 문자열이 아니다.
# 문자열 S와 P가 주어졌을 때, P가 S의 부분 문자열인지 아닌지 알아보자.

# 이게 왜 골드지?

s = input()
p = input()

if p in s : print(1)
else : print(0)