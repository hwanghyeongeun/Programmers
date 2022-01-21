# 20220121 백준 10809 알파벳찾기
# https://www.acmicpc.net/problem/10809

# 알파벳 소문자로만 이루어진 단어 S가 주어진다.
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

#index는 못 찾으면 에러
#find는 못 찾으면 -1

string = str(input())
alphbet='abcdefghijklmnopqrstuvwxyz'

for i in alphbet:
    print(string.find(i), end = ' ')

