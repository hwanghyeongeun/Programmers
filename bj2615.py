#2022.01.08 백준 2615 오목

#0,0부터 시작점을 잡고
#5개씩 더해서 5가 나오면 흑 승 / 10이 나오면 백 승?
#방향은 동쪽 남쪽 남서쪽 남동쪽 4개 함수로 빼고
#메인에서 함수 호출해서 돌려보고 시작점 전달

global gx, gy

#동쪽
def east(i, j):
    for i in range(19):
        for j in range(15):
            sumb = 0 #초기화
            sumw = 0 #초기화
            k = 0
            while k < 5:
                if board[i][j+k] == 1:
                    sumb += board[i][j+k]
                if board[i][j+k] == 2:
                    sumw += board[i][j+k]
                if sumb == 5:
                    gx = i
                    gy = j
                    print ("winner is black (way east)", gx, gy)
                    break
                if sumw == 10:
                    gx = i
                    gy = j
                    print ("winner is white (way east)", gx, gy)
                    break
                k += 1

#남쪽
def south(i, j):
    for i in range(15):
        for j in range(19):
            sumb = 0 #초기화
            sumw = 0 #초기화
            k = 0
            while k < 5:
                if board[i+k][j] == 1:
                    sumb += board[i+k][j]
                if board[i+k][j] == 2:
                    sumw += board[i+k][j]
                if sumb == 5:
                    gx = i
                    gy = j
                    print ("winner is black (way south)", gx, gy)
                    break
                if sumw == 10:
                    gx = i
                    gy = j
                    print ("winner is white (way south)", gx, gy)
                    break
                k += 1


#바둑판
board = []
for _ in range(19):
    ls = list(map(int,input().split()))
    board.append(ls)

print("############################################################")

#바둑판 출력
for i in range(19):
    for j in range(19):
        print(board[i][j], end=' ')
    print()


print("############################################################")

#함수 호출 부분
east(0,0)
south(0,0)