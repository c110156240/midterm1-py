a=int(input("搭了幾次電梯"))
c=1
m=0
for i in range(a):
    d=int(input("幾樓"))
    if d>c:
        m=m+20*(d-c)
        c=d
    else:
        m=m+10*(c-d)
        c=d
print(m,end="")
print("元")