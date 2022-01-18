#백준제출

#동쪽
def east(i, j):
    global gx, gy, result
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
                    gx = i+1
                    gy = j+1
                    #print ("winner is black (way east)", gx, gy)
                    result = 1
                    break
                if sumw == 10:
                    gx = i+1
                    gy = j+1
                    #print ("winner is white (way east)", gx, gy)
                    result = 2
                    break
                k += 1

#남쪽
def south(i, j):
    global gx, gy, result
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
                    gx = i+1
                    gy = j+1
                    #print ("winner is black (way south)", gx, gy)
                    result = 1
                    break
                if sumw == 10:
                    gx = i+1
                    gy = j+1
                    #print ("winner is white (way south)", gx, gy)
                    result = 2
                    break
                k += 1

#남서쪽 * i j 거꾸로 생각해야함
def southwest(i, j):
    global gx, gy, result
    for i in range(15):
        for j in range(15):
            sumb = 0 #초기화
            sumw = 0 #초기화
            k = 0
            while k < 5:
                if board[i+k][j-k] == 1:
                    sumb += board[i+k][j-k]
                if board[i+k][j-k] == 2:
                    sumw += board[i+k][j-k]
                if sumb == 5:
                    gx = i+1+4
                    gy = j+1-4
                    #print ("winner is black (way southwest)", gx, gy)
                    result = 1
                    break
                if sumw == 10:
                    gx = i+1+4
                    gy = j+1-4
                    #print ("winner is white (way southwest)", gx, gy)
                    result = 2
                    break
                k += 1                

def southeast(i, j):
    global gx, gy, result
    for i in range(15):
        for j in range(15):
            sumb = 0 #초기화
            sumw = 0 #초기화
            k = 0
            while k < 5:
                if board[i+k][j+k] == 1:
                    sumb += board[i+k][j+k]
                if board[i+k][j-k] == 2:
                    sumw += board[i+k][j+k]
                if sumb == 5:
                    gx = i+1
                    gy = j+1
                    #print ("winner is black (way southeast)", gx, gy)
                    result = 1
                    break
                if sumw == 10:
                    gx = i+1
                    gy = j+1
                    #print ("winner is white (way southeast)", gx, gy)
                    result = 2
                    break
                k += 1



board = []
for _ in range(19):
    ls = list(map(int,input().split()))
    board.append(ls)

gx, gy, result = 0, 0, 0

east(0,0)
south(0,0)
southwest(0,4)
southeast(0,0)

print(result)

if result != 0:
    print(gx, gy)