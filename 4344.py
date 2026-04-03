C=int(input())

for _ in range(C):
    what=list(map(int,input().split()))
    N=what[0]
    numbers=what[1:]
  
    avg=sum(numbers)/N

    count=0
    for number in numbers:
        if number>avg:
            count+=1

    percent=count/N*100
    print(f"{percent:.3f}%")