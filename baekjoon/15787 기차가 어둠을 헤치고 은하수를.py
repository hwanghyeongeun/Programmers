# 20220119
# 15787 기차가 어둠을 헤치고 은하수를
# https://www.acmicpc.net/problem/15787


N,M = map(int,input().split()) #N 기차번호 M명령 수

train = [[0 for _ in range(20)] for _ in range(N)]
temp = [] #비교할것

for i in range(N):
    c = list(map(int,input().split())) # command
    
    # 1 i x = i번째 기차의 x번째 자리에 사람 태우기
    if c[0] == 1:
        train[c[1]-1][c[2]-1] = 1
    # 2 i x = i번째 기차에 x번째 자리에 사람 내리기
    if c[0] == 2: 
        train[c[1]-1][c[2]-1] = 0
    # 3 i = i번째 기차에 사람들 하나씩 뒤로
    if c[0] == 3: 
        train[c[1]-1].insert(0, 0)
        train[c[1]-1].pop()
    # 4 i = i번째 기차에 사람들 하나씩 앞으로
    if c[0] == 4: 
        train[c[1]-1].append(0)
        del train[c[1]-1][0]


result = 0
for i in range(N):
    if train[i] not in temp:
        temp.append(train[i])
        result += 1

print(result) 






