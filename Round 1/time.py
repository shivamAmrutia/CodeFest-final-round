print("input hr, min and AM/PM")
hr = int(input())
mi = int(input())
t = input()

if t == "am":
    print("time: ", hr, ":", mi)
else:
    print("time: ", (hr+12), ":", mi)
