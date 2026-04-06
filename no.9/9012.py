T = int(input())

for i in range(T):
    count = 0
    sin = input()

    for ch in sin:
        if ch == "(":
            count += 1
        elif ch == ")":
            count -= 1

        if count < 0:
            break

    if count == 0:
        print("YES")
    else:
        print("NO")