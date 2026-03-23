A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
scores=[A,B,C,D,E]
for i in range(5):
	if scores[i]<40:
	    scores[i]=40
total=sum(scores)
N=total//5
print(N)