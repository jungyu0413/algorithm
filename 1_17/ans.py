import sys
sys.stdin = open("/Users/jungyulee/Desktop/algo/1_17/input.txt", 'r')
n = int(input())
a=[list(map(int, input().split())) for _ in range(n)]


res = 0
s=e=n//2
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1

print(res)










'''
sum_apple = 0
k = 0
mid = (n-1) // 2
pick_list = []
for idx, line in enumerate(a):
    if idx == 0:
        sum_apple += line[mid]
        
    elif idx <= mid:
        k += 1
        for i in line[mid-k:mid+k+1]:
            sum_apple += i
    else:
        k += -1
        for i in line[mid-k:mid+k+1]:
            sum_apple += i

print(sum_apple)
print(10+39+30+23+11+25+50+53+15+27+29+37+30)'''


