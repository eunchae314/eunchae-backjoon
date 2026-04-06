N = int(input())
miters = list(map(int, input().split()))

total = 0

for i in range(N):
    for j in range(N):
        total += abs(miters[i] - miters[j])

print(total)