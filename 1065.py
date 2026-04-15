N = int(input())
hansu_count = 0

for i in range(1, N + 1):
    if i <= 99:
        hansu_count = hansu_count + 1
    elif i <= 999:
        num_str = str(i) 
        a = int(num_str[0])
        b = int(num_str[1])
        c = int(num_str[2])
        if (a - b) == (b - c):
            hansu_count = hansu_count + 1

print(hansu_count)