A, B = map(int, input().split())

start = min(A, B)
end = max(A, B)

count = end - start + 1
total = (start + end) * count // 2

print(total)
