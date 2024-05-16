import sys
sys.stdin = open('/Users/lee/Desktop/algo/1_25/input.txt')

k, n = map(int, input().split())
def Count(len):
    cnt = 1
    ep = Line[0]
    for i in range(1, k):
        if Line[i] - ep > len:
            cnt += 1
            ep = Line[i]
    return cnt

Line = []
for _ in range(k):
    Line.append(int(input()))
                
Line.sort()

lt = Line[0]
rt = Line[-1]

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid -1

print(res)