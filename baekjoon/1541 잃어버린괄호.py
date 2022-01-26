# 20220126 1541 잃어버린괄호
# Greedy
# https://www.acmicpc.net/problem/1541

# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

# - 와 + 가 있으면 +를 먼저 계산하고 - 계산해야 최소 값이 나옴
# - 로 짤라서 배열만들고 시작

cal = input().split('-')
#print(cal)
answer = 0

# 맨 앞엔 무조건 더함
for i in cal[0].split('+'):
    answer += int(i) 

# 두 번째부턴 +로 나눠서 각각 빼줌
for i in cal[1:]:
    for j in i.split('+'):
        answer -= int(j)

print(answer)

    

