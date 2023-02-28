import sys
sys.stdin = open("/Users/jungyulee/Desktop/algo/1_04/input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
min = 2147000000
ave = round(sum(a)/n) + 0.5
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    # 같은 경우 높은 점수
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1

print(ave, res)






'''
Mean = sum(a) / n
Mean_gap = 0
Mean_gap_list = []

for i in a:
    if i > Mean:
        Mean_gap_i = i - Mean
        Mean_gap_list.append(Mean_gap_i)
    else:
        Mean_gap_i = Mean - i 
        Mean_gap_list.append(Mean_gap_i)


Min = Mean_gap_list[0]

for i in range(1, len(Mean_gap_list)):
    if i < Min:
        Min = i

print(Min)'''