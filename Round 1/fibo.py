n = int(input())
c = 0
flag = False
prev = 0
cur = 1
print("fibo series:")
while(True):
    if n <= prev:
        flag = True
        c += 1
        print(prev)
        
        if c == 5:
            break
    
    # print(prev)
    # c += 1
    # if c == 9:
    #     break
    temp = cur
    cur += prev
    prev = temp
    