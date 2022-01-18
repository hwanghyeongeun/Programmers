# 백준 11508 2+1세일
# 첫 번째 줄에는 유제품의 수 N (1 ≤ N ≤ 100,000)이 주어집니다.
# 두 번째 줄부터 N개의 줄에는 각 유제품의 가격 Ci (1 ≤ Ci ≤ 100,000)가 주어집니다.
# 입력 받은 다음에 앞에서부터 3개씩 짜름 / 3으로 나눴을때 012니까 나머지 2가 아닌 애들만 합산

N = int(input())
total = 0


cost = []
for i in range(N):
    cost.append(int(input()))

cost.sort(reverse=True)

for i in range(N):
    if i%3 != 2 :
        total += cost[i]

print(total)
