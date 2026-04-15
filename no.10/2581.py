M = int(input())
N = int(input())
prime_list = []

for num in range(M, N + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0: 
                is_prime = False
                break
        if is_prime == True:
            prime_list.append(num)

if len(prime_list) > 0:
    print(sum(prime_list))
    print(min(prime_list))
else:
    print(-1)
