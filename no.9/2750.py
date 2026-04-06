numbers=[]

N=int(input())

for i in range(N):
    number=int(input())
    numbers.append(number)

numbers.sort()

for cha in numbers:
    print(cha)