# 백준 20207 달력
# 이거 좀 어려웠다
# 일단 365일 + 1개 캘린더 배열을 만들고
# 시작일부터 종료일까지 일정이 있으면 1씩 더해줌
# 캘린더의 숫자가 곧 일정이 몇개인지 알려주는거고
# 앞에서부터 0이 아닌 숫자를 만날때부터 0을 만날때까지 1씩 추가해서 가로 길이를 만들고
# 이 중에서 가장 일정이 많은 날을 높이로 해서 둘을 곱함
# 배열 끝까지 반복
# 366에 0을 넣는 이유도 이와 같음



calendar = [0] * 366

N = int(input())
plan = [list(map(int, input().split())) for _ in range(N)]


sdate = 0
edate = 0

x = 0
y = 0

result = 0

for i in range(N):
    sdate = plan[i][0]
    edate = plan[i][1]
 #   print(i, sdate, edate)
    for j in range(sdate,edate+1):
        calendar[j-1] += 1

for i in range(366):
    if calendar[i] != 0:
        x += 1
        if calendar[i] > y:
            y =calendar[i]
    if calendar[i] == 0:
        result += x*y
        x = 0
        y = 0


print(result)
