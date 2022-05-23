import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

dogam= {}

for i in range(1, n+1):
    a = input().rstrip()
    dogam[i] = a
    dogam[a] = i

for j in range(m):
    q = input().rstrip()
    if q.isnumeric():
        print(dogam[int(q)])

    else:
        print(dogam[q])