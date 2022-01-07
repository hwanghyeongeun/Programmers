# 2022.01.07
# 백준 1913 달팽이
# 홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N2까지의 자연수를 달팽이 모양으로 N×N의 표에 채울 수 있다.
# N이 주어졌을 때, 이러한 표를 출력하는 프로그램을 작성하시오.
# 또한 N2 이하의 자연수가 하나 주어졌을 때, 그 좌표도 함께 출력하시오. 예를 들어 N=5인 경우 6의 좌표는 (4,3)이다.

#for i in range(3): print(i)


#print(n)
#print(target)

# 입력받은 숫자를 n이라고 치면 n by n 배열 만들어 0으로 초기화
# 00 에 n2을 넣고 하나씩 줄여가면서 ↓ → ↑ ← 반복하면서 채워감
# n-1번 n-2번씩 수행하고 입력값이 1이되면 끝

#n, target = map(int, input().split())

n = int(input())
target = int(input())

dir = 0 #방향

x = 0 # x좌표
y = 0 # y좌표
cx = 0 # 방향 바꾸기 전에 체크할 x좌표
cy = 0 # 방향 바꾸기 전에 체크할 y좌표

value = n*n #[0][0]에 들어갈 숫자

array = [[0]*n for i in range(n)] # n by n 배열에 0 집어 넣음

way1 = [1,0,-1,0] 
way2 = [0,1,0,-1] 


while value > 0 :
    array[x][y] = value

    #방향 바꿔도 되는지 체크
    cx = x+way1[dir%4]
    cy = y+way2[dir%4]

    if (cx<0) or (cy<0) or (cx>=n) or (cy>=n) or (array[cx][cy]!=0):
        dir += 1

    x += way1[dir%4]
    y += way2[dir%4]
    value = value - 1


#답 출력 + 위치 찾기
for i in range(n):
    for j in range(n):
        if array[i][j] == target:
            x, y = i+1, j+1
        print(array[i][j], end=' ')
    print()
print(x, y)