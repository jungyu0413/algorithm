import sys
sys.stdin = open("/Users/jungyulee/Desktop/algo/1_15/input.txt", "r")

n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n-1):
    dn_cnt = 6
    sum_arr_up = 0
    sum_arr_dn = 0
    while i < n-1: 
        sum_arr_dn += arr[dn_cnt]
        sum_arr_up += arr[i]
        if sum_arr_up == 3:
            cnt += 1
        if sum_arr_dn == 3:
            cnt += 1
        i += 1
        dn_cnt += -1

print(int(cnt/2))