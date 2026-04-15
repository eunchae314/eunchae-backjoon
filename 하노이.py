def h(n, s, m, e):
    if n == 1:
        print(f"{n}: {s} -> {e}")
    else:
        h(n-1, s, e, m)
        print(f"{n}: {s} -> {e}")
        h(n-1, m, s, e)

h(int(input("N: ")), 'A', 'B', 'C')