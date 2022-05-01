inp  = []
print("Enter number of elements: ")
n = int(input())

for i in range(n):
    x = int(input())
    inp.append(x)

for i in range(n-1): #for(i = 0; i<n-1; i++)
    for j in range(n-i-1): #for(j=0; j<n-i-1; j++)
        if inp[j] > inp[j+1]:
            temp = inp[j]
            inp[j] = inp[j+1]
            inp[j+1] = temp
    
print("Sorted list: ")
for i in range(n):
    print(inp[i])