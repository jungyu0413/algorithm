import sys
sys.stdin = open("/Users/jungyulee/Desktop/algo/1_14/input.txt", "r")

n1 = int(input())
a1 = list(map(int, input().split()))
n2 = int(input())
a2 = list(map(int, input().split()))

total_a = []

p1=p2=0

while p1<n1 and p2<n2:
    if a1[p1] <= a2[p2]:
        total_a.append(a1[p1])
        p1 += 1
    else:
        total_a.append(a2[p2])
        p2 += 1

if p1 < n1:
    total_a = total_a + a1[p1:]
if p2 < n2:
    total_a = total_a + a2[p2:]


print(total_a)