a=int(input("輸入第一行正整數為"))
b=input("第二行中的數字為").split(" ")
c=[]
for i in range(a):
    for j in range(a):
        if i!=j:
            if b[i]==b[j]:
                c.append(b[i])
            else:
               break
c.sort()
e=[]
for k in range(len(c)):
    d=0
    for o in range(len(c)):
        if c[k]==c[o]:
            d+=1
    e.append(d)
u=e.copy()
u.sort()
t=int(e.index(int(u[-1])))
print(u)
if int(u[-1])==0:
    print("每個數字剛好只出現一次")
else:
    print("最大出現的數字為"+c[t])
    print("出現次數為"+str(u[-1]))
