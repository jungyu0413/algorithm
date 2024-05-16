import sys
sys.stdin = open("/Users/lee/Desktop/algo/1_20/input.txt", 'r')
a = [list(map(int, input().split())) for _ in range(9)]

def check(a):
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9:
                return False
            
    return True

if check(a):
    print('Yes')
else:
    print('No')





'''row_cnt = -1
stop_break = False
picked_st = [0, 3, 6]
picked_dx = [1, 2]
picked_dy = [0, 1, 2]

for row_num, row in enumerate(a):
    if row_num in picked_st:
        all()
    if stop_break:
        break
    row_cnt += 1
    col_list = []
    for col_num, col in enumerate(row):
        if col in col_list:
            print('No')
            stop_break = True
            break
        else:
            col_list.append(col)



if row_cnt == row_num:
    print('Yes')'''

