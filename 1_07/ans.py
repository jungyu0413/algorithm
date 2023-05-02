import sys
sys.stdin = open("/Users/jungyulee/Desktop/algo/1_07/input.txt", "r")
n = int(input())

ch = [0]*(n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1

print(cnt)


# 나의 답
'''cnt = 0
num_cnt = 0
for i in range(2, n+1):
    for num in range(1, 10):
        if i % num == 0:
            num_cnt += 1
    if num_cnt < 3:
        cnt += 1
    num_cnt = 0

print(cnt)'''