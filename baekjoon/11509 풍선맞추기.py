# 백준 11509 풍선맞추기
# https://www.acmicpc.net/problem/11509
# 큰 방에 N개의 풍선이 떠있다.
# 풍선들은 왼쪽부터 오른쪽까지 일렬로 있다.
# 진솔이는 화살 가지고 노는 것과 사냥 연습하는 것을 좋아한다.
# 진솔이는 화살을 왼쪽에서 오른쪽으로 쏜다. 높이는 임의로 선택한다.
# 화살은 선택된 높이 H에서 풍선을 마주칠 때까지 왼쪽에서 오른쪽으로 이동한다.
# 화살이 풍선을 마주치는 순간, 풍선은 터지고 사라진다. 화살은 계속해서 가던길을 가는데 높이는 1 줄어든다.
# 그러므로 만약 화살이 높이 H에서 이동 중이었다면 풍선을 터트린 후에는 높이가 H-1이 된다.


# 최대 화살은 N개
# h가 0보다 크면 h = balloon[i] 넣고 화살 쏨 -> shoot +1 해주기
# i = 0, i ~ h 까지 for문 돌려서 balloon[i] == h-i 면 balloon[i] = 0
# sum(balloon) == 0 이면 끝
#시간초과 - 답은 나오는데 소스가 쓸데없이 지저분함
#N = int(input())
#balloon = list(map(int, input().split()))
#shoot = 0
#h = 0
# for i in range(N):
#    if balloon[i] > 0 :
#        shoot += 1
#        h = balloon[i]
#        k = 0
#        for j in range (i, N):
#            if balloon[j] == h-k :
#                balloon[j] = 0
#            k += 1
#        if sum(balloon) == 0 :
#            print(shoot)
#            break


# 새로 짜야됨
# H에서 발사된 화살은 계속 H 높이를 유지하다가 풍선을 터뜨리면 H-1이 되는 거였음
# 게임에서 처럼 오른쪽으로 이동하면서 -1되는게 아님
# 원래 답도 틀렸던거고 운이 좋아서 시간초과가 뜬 것 같다


N = int(input())
balloon = list(map(int, input().split()))
arrow = 0
h = 0

