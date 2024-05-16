import sys
sys.stdin = open("/Users/lee/Desktop/algo/1_23/input.txt", 'r')
k, n = map(int, input().split())

def Count(len):
    cnt = 0
    for x in Line:
        cnt += x//len
    return cnt

Line = []
res = 0
largest = 0
for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)

lt = 1
rt = largest
while lt <= rt:
    mid = (lt+rt) // 2
    if Count(mid)>=n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)










'''
a = [list(list(map(int, input().split()))) for _ in range(n)]
a.sort(reverse=True)
lt = 0
st_num = 0
rt = a[st_num][0]

while lt <= rt:
    mid = (lt + rt) // 2
    cnt = 0
    for val in a:
        each_cnt =  val[0] // mid
        cnt += each_cnt
    if cnt > m:
        while 
        break
    else:
        st_num += 1
        rt = a[st_num][0]'''
        









