is_self_num = [True] * 10001 

for i in range(1, 10001):
    num = i
    for j in str(i): 
        num = num + int(j)
    if num <= 10000:
        is_self_num[num] = False 

for i in range(1, 10001):
    if is_self_num[i] == True:
        print(i)
