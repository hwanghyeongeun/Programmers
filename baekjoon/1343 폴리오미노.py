# 20220129 1343 폴리오미노
# Greedy
# https://www.acmicpc.net/problem/1343

# 민식이는 다음과 같은 폴리오미노 2개를 무한개만큼 가지고 있다. AAAA와 BB
# 이제 '.'와 'X'로 이루어진 보드판이 주어졌을 때, 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다. 이때, '.'는 폴리오미노로 덮으면 안 된다.
# 폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오.

# 입력 받는 배열에 . - 이것만 보면 바로 split 치고 시작하는 버릇 고쳐야함

text = input()
text = text.replace('XXXX','AAAA')
text = text.replace('XX','BB')

if 'X' in text: print('-1')
else: print(text)

