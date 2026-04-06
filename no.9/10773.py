numbers=[]

K=int(input())

for i in range(K):
    number=int(input())

    if number==0:
        numbers=numbers[:-1]
    else:
        numbers.append(number)

print(sum(numbers))