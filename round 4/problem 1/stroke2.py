primary = ('Y','R','B')
friend = {'O': ('R','Y','P','A'), 'Y': (), 'R': (), 'B': (), 'P': ('R','B','G', 'A'), 'G': ('Y','B','A','O'), 'A': ('R', 'Y', 'B', 'O', 'G', 'P')}
score = {'Y': 1, 'B': 1, 'O': 2, 'P': 2, 'G': 2, 'A': 3, 'R': 1}

with open("D:\CodeFest\Final round\codefestV1.0-final-algo-master\problem 1\\test_set_1\\ts1_input.txt") as file:
    n = int(file.readline())
    for lines in range(n):
        length = int(file.readline())
        inp = file.readline().strip()
        strokes = 0
        col = []
        temp = [inp[0]]
        for i in range(1,length):
            if temp[-1] == inp[i]:
                temp.append(inp[i])
            else:
                col.append(temp)
                temp = [inp[i]]
        col.append(temp)
        
        if len(col) == 1:
            strokes = score[col[0][0]]
            print(strokes)
            continue
        for i in range(len(col)):
            
            if col[i][0] in primary:
                strokes += 1
                continue
            
            else:
                temp = score[col[i][0]]
                if i == 0:
                    for j in friend[col[i][0]]:

                        if j in friend[col[i+1][0]]:
                            temp -= 1
                            break
                    
                elif i == len(col) - 1:
                    for j in friend[col[i][0]]:
                        if j in friend[col[i-1][0]]:
                            temp -= 1
                            break
                
                else:
                    for j in friend[col[i][0]]:
                        if j in col[i-1][0]:
                            temp -= 1
                            break
                    for j in friend[col[i][0]]:
                        if j in col[i+1][0]:
                            temp -= 1
                            break
                strokes += temp
            
            # print(strokes)
        print(strokes)
        