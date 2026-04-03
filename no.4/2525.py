A,B=map(int,input().split())
C=int(input())
total=(A*60)+B+C
one=(total//60)%24
two=total%60
print(one,two)
