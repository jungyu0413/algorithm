import sys
sys.stdin = open("/Users/jungyulee/Desktop/algo/1_16/input.txt", 'r')
n = int(input())
a=[list(map(int, input().split())) for _ in range(n)]
largest = - 2147000000
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
sum1 = sum2 = 0

for i in range(n):
    sum1 += a[i][j]
    sum2 += a[i][n-i-1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2
print(largest)











# my answer
'''line_sum = 0
sum_dict = dict()

sum_dict['cross_up'] = 0
sum_dict['cross_dn'] = 0
cross_up = 0
cross_dn = len(a)-1

for len_idx, len_num in enumerate(a):
    sum_dict[str('row_')+str(len_idx)] = 0
    for num_idx, num in enumerate(len_num):
        if len_idx == 0:
            sum_dict[str('col_')+str(num_idx)] = num
            sum_dict[str('row_')+str(len_idx)] += num  
            if num_idx == cross_up:
                sum_dict['cross_up'] += num
                cross_up += 1
            if num_idx == cross_dn:
                sum_dict['cross_dn'] += num
                cross_dn += -1

        else:
            sum_dict[str('col_')+str(num_idx)] += num
            sum_dict[str('row_')+str(len_idx)] += num   
            if num_idx == cross_up:
                sum_dict['cross_up'] += num
                cross_up += 1
            if num_idx == cross_dn:
                sum_dict['cross_dn'] += num
                cross_dn += -1

print(sum_dict)
for num in sum_dict:
    if line_sum < sum_dict[num]:
        line_sum = sum_dict[num]

print(line_sum)'''




 