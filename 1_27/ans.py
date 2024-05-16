import sys
sys.stdin = open('/Users/lee/Desktop/algo/1_27/input.txt')

n = int(input())

time_sc = []
for _ in range(n):
    st, et = map(int, input().split())
    time_sc.append((st, et))

time_sc.sort(key=(lambda x : (x[1], x[0])))

bf_et = 0
cnt = 0
for each_sc in time_sc:
    st, ed = each_sc
    if bf_et <= st:
        cnt += 1
        bf_et = ed
    

print(cnt)








# scd = []
# for i in range(n):
#     cnt = 1
#     scd.append(list(map(int, input().split())))

# max = 0
# bf_ed = 0
# cnt = 0
# for idx in range(n):
#     for each_scd in scd[1:]:
#         st, ed = each_scd
#         if bf_ed <= st:
#             cnt += 1
#             bf_ed = ed
#         else:
#             pass
#     if max < cnt:
#         max = cnt


# print(max)