n = []

for i in range(4):
    temp = []
    print("enter first row: ")
    for j in range(4):
        temp.append(int(input()))
    
    n.append(temp)

m = []
for i in range(4):
    temp = []
    for j in range(4):
        temp.append(n[j][i])
    m.append(temp)

for i in range(4):
    print(n[i])

print("enter 2 arguments: ")
row1 = int(input())

for i in range(4):
    print(m[i])

row2 = int(input())

print("Element is: ", n[row1-1][row2-1])