word = input()

total = 0

for ch in word:
    if ch.islower():
        total += ord(ch) - ord('a') + 1
    else:
        total += ord(ch) - ord('A') + 27

is_prime = True

if total == 1:
    is_prime = True

for i in range(2, total):
    if total % i == 0:
        is_prime = False

if is_prime:
    print("It is a prime word.")
else:
    print("It is not a prime word.")