#
#      1      2      3

#   1 2 3   1 2 3   1 2 3

# 123 123 123 123 123 123 ....
import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
rs=[] #수열저장


def recur():

    if len(rs) == m: #트리 제일 끝
        print(" ".join(map(str,rs)))
        return

    for i in range(1, n+1):
        if i not in rs:
            rs.append(i)
            recur()
            rs.pop() #갔다 온 애들은 rs에서 빼주기.

recur()

# 만약 n=4, m=2라면 밑과 같은 형태로 진행
# rs : [1] -> [1,2] -> [1] -> [1,3] -> [1] -> [1,4]
