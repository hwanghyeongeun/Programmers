# 2022.01.08
# 백준 16953 A→B
# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다. 
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.


# 왜 시간초과 나오는지 모르겠음 


a, b = map(int, input().split())

count = 1

while a<b:
    if b%2 == 0:
        b /= 2
    elif b%10 == 1:
        b //= 10
    count += 1
    
if a==b:
    print(count)
else:
    print('-1')
    
