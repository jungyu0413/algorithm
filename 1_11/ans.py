import sys
sys.stdin = open("/Users/jungyulee/Desktop/algo/1_11/input.txt", "r")
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))


# s = s[::-1]을 활용해서 더 간단하게 가능




# for 문을 더 돌아야함.
    '''
    origin = s
    resort = ''
    for j in range(len(s)):
       # print(j, len(s))
        resort += s[len(s)-j-1]
    if origin == resort:
        print('YES')
    else:
        print('NO')'''


