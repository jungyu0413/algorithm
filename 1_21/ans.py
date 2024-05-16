import sys
sys.stdin = open("/Users/lee/Desktop/algo/1_21/input.txt", 'r')
a = [list(map(int, input().split())) for _ in range(7)]
cnt = 0


for i in range(3):
    for j in range(7):
        tmp = a[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if a[i+k][j] != a[i+5-k-1][j]:
                break
            else:
                cnt += 1

print(cnt)

''' 
for i in range(6):
    for k in range(5):
        pick = max(k*(-2)+7, 3)
        if a[i][k:k+pick][:int(pick/2)] == a[i][k:k+pick][int(pick/2)+1:][::-1]:
            cnt += 1
        if [j[i] for j in a[k:k+pick]][:int(pick/2)] == [j[i] for j in a[k:k+pick]][int(pick/2)+1:][::-1]:
            cnt += 1

print(cnt)'''

                






