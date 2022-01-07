#2022.01.08 백준 2615 오목

#0,0부터 시작점을 잡고
#5개씩 더해서 5가 나오면 흑 승 / 10이 나오면 백 승?
#방향은 가로 세로 남서쪽 남동쪽 4개 함수로 빼고
#메인에서 함수 호출해서 돌려보고 시작점 전달


#바둑판
board = []
board.append([0]*19)
for _ in range(19):
    ls = [0] + list(map(int,input().split())) +[0]
    board.append(ls)
board.append([0]*19)

