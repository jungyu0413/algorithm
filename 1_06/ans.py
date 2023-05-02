import sys
sys.stdin = open("/Users/jungyulee/Desktop/algo/1_06/input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))

# best solution1
def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum


max = -2147000000
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x

print(res)

# best solution2

'''
def digit_sum(x):
    sum = 0
    while x>0:
        sum += x % 10
        x /= 10
    return sum

max = -2147000000
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x

print(res)'''




# 나는 10씩 곱해주면서 나누는 값을 키웠는데, 위에서와 같이 
# 원 값을 10씩 나누면서 진행하면 더 칸편하다.
'''
ten_sum = []

def digit_sum(num):
    ten_th = 8
    val = 0
    while ten_th != -1:
        c_val = num // (10 ** ten_th)
        val += c_val
        num = num % (10 ** ten_th)
        ten_th += -1
    return val

sum_dg = list(map(digit_sum, a))

key = max(range(len(sum_dg)), key=lambda i: sum_dg[i])
print(a[key])
'''