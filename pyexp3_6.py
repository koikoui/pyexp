def inc(n):
    global s
    for i in range(0,n):
        s = s + 1
def dec(n):
    global s
    for i in range(0,n):
        s = s - 1
s = 0
inc(int(input("输入s增加的次数：")))
dec(int(input("输入s减少的次数：")))
print("s="+str(s))