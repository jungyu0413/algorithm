import sys
sys.stdin = open("/Users/jungyulee/Desktop/algo/1_13/input.txt", "r")


a=list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]

a.pop(0)
for x in a:
    print(x, end=' ')
'''
card = list(range(1,21))

for i in range(1, 10):
    a, b = map(int, input().split())
    if 1 < a and a < b:
        new_ch = []
        for j in range(b-a):
            new_ch.append(card[b-j-1])
        card = card[0:a-1] + new_ch + card[b:]
    elif 1 < b and a > b:
        a, b = b, a
        for j in range(b-a):
            new_ch.append(card[b-j-1])
        card = card[0:a-1] + new_ch + card[b:]
    elif 1 == a:
        for j in range(b-a):
            new_ch.append(card[b-j-1])
        card = card[a-1:b-1] + card[b:]

print(card) '''