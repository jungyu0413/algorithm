import sys
sys.stdin = open("/Users/jungyulee/Desktop/algo/1_10/input.txt", "r")
n = int(input())
a = list(map(int, input().split()))
sum = 0
cnt = 0
for x in a:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)



# tmi
'''
val_list = input().split()
total = 0
ans_bool = False
bool_val = 0
for val in val_list:
    val = int(val)
    if val == 1 and ans_bool == True:
        bool_val += 1
        total += bool_val
    elif val == 1 and ans_bool == False:
        ans_bool = True
        bool_val += 1
        total += 1
    else:
        ans_bool = False
        bool_val = 0

print(total)'''



