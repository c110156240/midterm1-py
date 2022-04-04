a=input("輸入第一矩陣").split(" ")
b=[]
for i in range(int(a[0])):
    b.append(input("輸入").split(" "))
c=input("輸入第2矩陣").split(" ")
d=[]
for j in range(int(c[0])):
    d.append(input("輸入").split(" "))
if a==c:
    for o in range(int(a[0])):
        e=[]
        for p in range(int(a[1])): 
            e.append(int(b[o][p])+int(d[o][p]))
        print(e)
else:
    print("兩矩陣不能相加")