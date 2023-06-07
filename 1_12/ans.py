import sys
sys.stdin = open("/Users/jungyulee/Desktop/algo/1_12/input.txt", "r")
n = input()
res = 0
for x in n:
    if x.isdecimal():
        res = res*10+int(x)
print(res)
cnt = 0
for i in range(1, res):
    if res % i == 0:
        cnt += 1
print(cnt)






'''
num = ''
for i in range(len(n)):
    try: 
        int(n[i])
        num += str(n[i])
    except:
        pass

num = int(num)
print(num)

cnt = 0
for i in range(num):
    if num % (num-i) == 0:
        cnt += 1

print(cnt) '''


