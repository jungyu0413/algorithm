import sys
sys.stdin = open('/Users/lee/Desktop/algo/1_28/input.txt', 'r')

n = int(input())

info = []
for _ in range(n):
    h, w = map(int, input().split())
    info.append((h, w))

info.sort(reverse=True)

largest = 0
cnt = 0
for x, y in info:
    if y > largest:
        largest =y
        cnt += 1

print(cnt)



'''
info.sort(key=lambda x : x[1])

cnt = 0
bf_h = 0
bf_w = 0

def Count(h, w, idx):
    cnt = 0
    for other_info in info:
        o_h, o_w = other_info
        if h > o_h or w > o_w:
            cnt += 1
        if cnt == (n-1):
            id = True
        else:
            id = False
    return id
            
cnt = 0
for idx in range(n):
    c_h, c_w = info[idx]
    if Count(c_h, c_w, idx):
        cnt += 1

print(cnt)'''