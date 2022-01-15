# 20220116
# 백준 11047 동전 
# https://www.acmicpc.net/problem/11047

# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.


#이번 문제는 지난번 전자렌지랑 비슷한 문제
# for문 돌리는게 편하니까 coin 배열을 reverse해주고
# 가지고 있는 동전 금액이 k보다 작을때부터
# 몫을 구하고 돈을 빼고, 몫은 result에 계속 더해준다
# 제출 다 하고 생각난건데 for문을 끝까지 돌릴 필요 없이 money = 0 이되면 break 해도 되겠다.


n, k = map(int, input().split())
coin = []
for i in range(n):
  coin.append(int(input()))

coin.reverse()
#print(coin)

result = 0
money = 0

for i in coin:
    if i <= k:
        money = k - k//i*i
        result += k//i
        k=money

print(result)