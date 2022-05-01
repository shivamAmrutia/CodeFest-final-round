d = {'a': [1,25], 'b': [2,24], 'c': [3,23], 'd': [4,22], 'e': [5,21], 'f': [6,20], 'g': [7,19], 'h': [8,18], 'i': [9,17], 'j': [10,16], 'k': [11,15], 'l': [12,14], 'm': [13,13], 'n': [14,12], 'o': [15,11], 'p': [16,10], 'q': [17,9], 'r': [18,8], 's': [19,7], 't': [20,6], 'u': [21,5], 'v': [22,4], 'w': [23,3], 'x': [24,2], 'y': [25,1], 'z': [26,0]}

s = "abcd"
f = "z"
ops = 0

inp = []
with open("D:\CodeFest\Final round\codefestV1.0-final-algo-master\problem 2\\test_set_2\\ts2_input.txt") as file:
    n = int(file.readline())
    for i in range(n):
        ops = 0
        s = file.readline().strip()
        f = file.readline().strip()
        # print(s)
        # print(f)
        for i in s:
            mi = 26
            el = f[0]
            for j in range(len(f)):
                dif = min(abs(d[f[j]][0] - d[i][0]), abs(d[f[j]][0] - d[i][1]))
                if dif < mi:
                    mi = dif
                    el = f[j]
            
            ops += mi
        out = open("D:\CodeFest\Final round\codefestV1.0-final-algo-master\problem 2\\test_set_2\output.txt", "a")

        out.write(str(ops))
        out.write('\n')
        print(ops)