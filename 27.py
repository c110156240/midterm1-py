c=0
while c!=1:
    a=input("輸入字串")
    if a=="end":
        c=1
    b=[]
    b1=[]
    k=len(a)  
    for i in range(k-2):
        d=0
        d=a[i]+a[i+1]+a[i+2]
        b.append(str(d))    
    t=[]
    for l in range(len(b)):
        if b[l][0]==b[l][2]:
            t.append(b[l])
        t.sort()
    print(t[1])
print("結束")