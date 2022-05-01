n = int(input())

print("elements: ")
for j in range(n, 0, -1):
    ans = 1
    for i in range(2, j + 1):
        ans = ans * i
    # print(ans)
    if ((ans % 5) == 0 or (ans % 3) == 0) and (ans % 5 == 0 and ans % 3 == 0) :
        print(j)
