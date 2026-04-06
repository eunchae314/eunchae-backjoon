N=int(input())

for i in range(N):
    scores=input()

    combo=0
    score=0

    for ch in scores:
        if ch=="O":
            combo+=1
            score+=combo

        else:
            combo=0

    print(score)