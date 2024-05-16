import sys
sys.stdin = open("/Users/lee/Desktop/algo/1_22/input.txt", 'r')
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt = 0
rt = n-1

while lt<=rt:
    mid = (lt+rt)//2
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt = mid-1
    else:
        lt = mid+1


'''
sort_idx = [0] * n
sort_list = [0] * n
for idx, num in enumerate(a):
    if num == m:
        pick_idx = idx
    cnt = 0
    for other in a:
        if num > other:
            cnt += 1
    sort_idx[idx] = cnt
    sort_list[cnt] = num

print(sort_list)
print(sort_idx[pick_idx]+1)'''






