a=input("輸入一整數序列").split(" ")
b=len(a)
d=[]
e=[]
for i in range(b):
    c=1
    for j in range(b):
        if i!=j:
            if a[i]==a[j]:
                c+=1
                d.append(c)
                e.append(a[i])
o=0
for u in range(len(d)):
    if d[u]>b/2:
        o=1
    else:
        o=0
if o==0:
    print("過半元素:no")
else:
    print("過半元素%s"%(str(e[u])))
        
