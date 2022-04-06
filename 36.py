a=int(input("幾筆資料"))
b=[]
for i in range(a):
    b1=[]
    for i in range(4):
        b1.append(int(input("前四項資料")))
    b.append(b1)
for u in range(a):
    c1=[]
    d1=[]
    for u1 in range(0,3,1):
        c=b[u][u1+1]-b[u][u1]
        d=b[u][u1+1]/b[u][u1]
        c1.append(c)
        d1.append(d)
    for p in range(len(c1)-1):
        if c1[p]==c1[p+1]:
            w=0
        elif d1[p]==d1[p+1]:
            w=1
        else:
            w=2
    if w==0:
        print(str(b[u])+str(int(c1[0])+int(b[u][-1])))
        print("此為等差數列")
    elif w==1:
        print(str(b[u])+str(int(d1[0])*int(b[u][-1])))
        print("此為等比數列")
    else:
        print("皆不是")
