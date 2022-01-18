# 백준 10162 전자렌지
# https://www.acmicpc.net/problem/10162
# 3개의 시간조절용 버튼 A B C가 달린 전자레인지가 있다.
# 버튼 A, B, C에 지정된 시간은 각각 5분, 1분, 10초
# 최적의 버튼 누름 횟수 구하기. 10의 배수가 아니면 -1 출력하고 시작
# A 300 / B 60 / C 10
# 몫 // 나머지 %

time = int(input())

abc = [300,60,10]

result = []

if (time%10!=0):
    print(-1)
else:
    for i in abc:
        result.append(time//i)
        time = time - i*(time//i)
    for i in result:
        print(i,end=' ')