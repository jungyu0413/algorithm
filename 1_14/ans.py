import sys
sys.stdin = open("/Users/jungyulee/Desktop/algo/1_14/input.txt", "r")

n1 = int(input())
a1 = list(map(int, input().split()))
n2 = int(input())
a2 = list(map(int, input().split()))

total = a1 + a2
re_total = []

min = 999999
for i in total:
    if i < min:
        min = i



