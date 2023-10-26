import sys
sys.stdin = open("/Users/jungyulee/Desktop/algo/1_15/input.txt", 'r')
n, m=map(int, input().split())
a=list(map(int, input().split()))
lt=0
rt=1
tot=a[0]
cnt=0
while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
print(cnt)



#n, m = map(int, input().split())
#arr = list(map(int, input().split()))
#cnt = 0
#for i in range(n-1):
#    dn_cnt = 6
#    sum_arr_up = 0
#    sum_arr_dn = 0
#    while i < n-1: 
#        sum_arr_dn += arr[dn_cnt]
#        sum_arr_up += arr[i]
#        if sum_arr_up == 3:
#            cnt += 1
#        if sum_arr_dn == 3:
#            cnt += 1
#        i += 1
#        dn_cnt += -1

#print(int(cnt/2))