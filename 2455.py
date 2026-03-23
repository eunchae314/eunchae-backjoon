A,B=map(int,input().split())
C,D=map(int,input().split())
E,F=map(int,input().split())
G,I=map(int,input().split())

total=0
one=total-A+B
two=one-C+D
three=two-E+F
four=three-G+I

print(max(one,two,three,four))