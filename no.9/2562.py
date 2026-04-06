numbers=[]

for i in range(1,10):
    number=int(input())
    numbers.append(number)

a=max(numbers)
b=numbers.index(a)

print(a)
print(b+1)