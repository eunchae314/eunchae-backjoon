school=int(input())
pc=int(input())
academy=int(input())
home=int(input())
x=(school+pc+academy+home)//60
y=(school+pc+academy+home)%60
print(x)
print(y)