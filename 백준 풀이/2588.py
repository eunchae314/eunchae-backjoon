A=int(input())
B=int(input())

one=B%10
ten=(B//10)%10
hundred=B//100

print(A*one)
print(A*ten)
print(A*hundred)
print(A*B)
