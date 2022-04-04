a=[]
b=int(input("輸入陣列大小"))
c=[]
e=[]
for u in range(b):
    a.append(input("第i列").split(" "))
for i in range(b):
    for j in range(b):
        d=[]
        c.append(int(a[i][j]))
        d.append(i)
        d.append(j)
        e.append(d)
p=c.copy()
p.sort()
f=c.index(p[-1])
f1=c.index(p[-2])
f2=c.index(p[-3])
print(p)
t=int(p[-1])+int(p[-2])+int(p[-3])
print("最大值%d"%(t))
print("位置(%d,%d)(%d,%d)(%d,%d)"%(e[f][0]+1,e[f][1]+1,e[f1][0]+1,e[f1][1]+1,e[f2][0]+1,e[f2][1]+1))
