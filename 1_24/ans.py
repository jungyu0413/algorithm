import sys
sys.stdin = open("/Users/lee/Desktop/algo/1_24/input.txt", 'r')
k, n = map(int, input().split())
music=list(map(int, input().split()))
maxx = max(music)
def Count(capacity):
    cnt = 1
    sum = 0
    for x in music:
        if sum+x > capacity:
            cnt += 1
            sum = x
        else:
            sum+= x
    return cnt

lt = 1
rt = sum(music)
res = 0

while lt <= rt:
    mid = (lt+rt)//2
    if mid >= maxx and Count(mid) <= n:
        res = mid
        rt = mid-1
    else:
        lt = mid + 1
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
        









