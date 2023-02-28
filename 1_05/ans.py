import sys
sys.stdin = open("/Users/jungyulee/Desktop/algo/1_05/input.txt", "rt")
n, m = map(int, input().split())
cnt = [0]*(n+m+3)
max = -2147000000
for i in range(n+1):
    for j in range(m+1):
        cnt[i+j] += 1

for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]

for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end=' ')



'''
# n면체 주사위에서 나올 수 있는 값
# 1~n
# 1~m 합의 조합

n_m = dict()
for i in range(n):
    for j in range(m):
        d_key = str(i+j)
        n_m[d_key] += 1

print(max(n_m.values))'''