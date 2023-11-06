import sys
sys.stdin = open("/Users/jungyulee/Desktop/algo/1_18/input.txt", 'r')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())

print(h, t, k)