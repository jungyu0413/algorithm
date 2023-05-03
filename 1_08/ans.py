import sys
sys.stdin = open("/Users/jungyulee/Desktop/algo/1_08/input.txt", "r")
n = int(input())
a = list(map(int, input().split()))


def reverse(x):
    res = 0
    while x>0: # 978 97 9
        t = x%10 # 8 7 9
        res = res*10+t # 8 87 879
        x = x//10 # 97 9 0
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x%i==0:
            return False
        # 나눠지는게 아무것도 없으면 True 즉, 소수
    else:
        return True


for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')






# 나의 답변 : 1은 소수에서 제외해야하며, 전체 숫자만큼 다 나누는 것이 아니라,
# 절반으로 나누기만해도 된다.
'''
print_num = []
for idx_origin, num in enumerate(a):
    str_num = str(num)
    new_num = 0
    for idx,idx_num in enumerate(str_num):
        new_num += int(idx_num) * (10**idx)
    cnt=0
    for div_num in range(2, new_num+1):
        if new_num % div_num == 0:
            cnt += 1
    if cnt < 3:
        print_num.append(new_num)

print(print_num)'''