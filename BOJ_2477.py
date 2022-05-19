# 아이디어
# 큰 네모에서 작은 네모 빼기
# 작은 네모 넓이 구할 때 가로세로 길이는 가로/세로 제일 긴거 양 옆의 차이를 구하면 됨.

import sys
input = sys.stdin.readline

k = int(input())
hex = []

for _ in range(6):
    hex.append(list(map(int,input().rstrip().split())))

w_max, w_idx = 0, 0
h_max, h_idx = 0, 0

for i in range(len(hex)):
    # 가로
    if hex[i][0] in [1,2]:
        if w_max < hex[i][1]:
            w_max = hex[i][1]
            w_idx = i
    else:
        #세로
        if h_max < hex[i][1]:
            h_max = hex[i][1]
            h_idx = i

large_square = w_max * h_max

small_square = abs((hex[(w_idx-1)%6][1]-hex[(w_idx+1)%6][1])) * abs(hex[(h_idx-1)%6][1]-hex[(h_idx+1)%6][1])

print((large_square - small_square) * k)

#왜?
# hex[w_idx-1][1] 로 했더니 계속 런타임 에러 나서 찾아보니 hex[(w_idx-1)%6][1] 으로 했음.
# 6이 되면 인덱스가 넘어감!!
