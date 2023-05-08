import sys
sys.stdin = open("/Users/jungyulee/Desktop/algo/1_09/input.txt", "r")
n = int(input())
res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a,b,c = map(int, tmp)
    if a==b and b==c:
        money = 10000+a*1000
    elif a==b or a==c:
        money = 1000+a*100
    elif b==c:
        money = 1000+b*100
    else:
        money = c*100
    if money>res:
        res=money

print(res)





# 간단하게 하려고 했으나 오히려 TMI 느낌 
'''
num_list = []
for i in range(n):
 num_list.append(list(map(int, input().split())))
def be_max(x):
   max = 0
   for i in x:
        if i > max:
           max = i
   return max


def take_m(x):
    ch_same = 0
    max = 0
    same = 0
    for i in x:
       for j in x:
        if i == j:
            same = i
            ch_same += 1
        if i > max:
           max = i
    if ch_same == 9:
        val = 10000 + (same*1000)
    elif ch_same == 5:
        val = 1000 + (same*100)
    else:
        val = max*100

    return val

total_num = []
for i in num_list:
   total_num.append(take_m(i))
print(be_max(total_num))'''