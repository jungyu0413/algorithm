import sys
sys.stdin = open("input.txt", "rt")
# read

n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)





'''
# my code
lt = []

for val in range(n):
    val = val + 1
    if n % val == 0:
        lt.append(val)
    else:
        pass
try:
    print(lt[k])
except:
    print(-1)
'''

