# 20220115 1231
# 백준 20300 서강근육맨
# https://www.acmicpc.net/problem/20300

# 근손실 배열 loss를 sort 하고
# 근손실 합 배열 losshab을 선언해서
# 총 n일 일때는 
# 일단 짝수인지 홀수인지 체크하고
# 짝수면
# 맨앞, 맨뒤 합산, 하나씩 안쪽으로 들어와서 또 합산하는 식으로 losshab을 만들고
# 홀수면 동일하게 하되
# 근손실 배열 loss의 맨 마지막을 뒤에 붙여줌
# 그리고 맥스값 출력

n = int(input())

loss = list(map(int, input().split()))
loss.sort()
losshab = []

# 짝수
if n%2 == 0:
    for i in range(n//2):
        losshab.append(loss[i]+loss[n-1-i])
else:
    for i in range(n//2):
        losshab.append(loss[i]+loss[n-2-i])
    losshab.append(max(loss))

print(max(losshab))
