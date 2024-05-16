import sys
sys.stdin = open('/Users/lee/Desktop/algo/1_29/input.txt', 'r')

n = int(input())
L = list(map(int, input().split()))
m = int(input())

L.sort(reverse=True)

for _ in range(m):
    L[0] += -1
    L[-1] += +1
    L.sort(reverse=True)

print(L[0]-L[-1])

# n = int(input())

# info = list(map(int, input().split()))

# m = int(input())

# info.sort(reverse=True)
# for _ in range(m):
#     info[info.index(max(info))] += - 1
#     info[info.index(min(info))] += 1

# print(max(info)-min(info))